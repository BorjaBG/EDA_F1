"""Funciones analíticas y de contraste de hipótesis (H1–H4) para el EDA F1."""

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

from .config import DECADAS_ANALISIS, PUNTOS_F1_2023


def mapear_puntos_posicion(posiciones: pd.Series) -> pd.Series:
    """Convierte posiciones de carrera en puntos oficiales FIA de GP 2023.

    Args:
        posiciones: Serie con posiciones finales o estimadas (1..20 o ``'\\N'``).

    Returns:
        Serie numérica de tipo ``float`` con los puntos correspondientes (0.0 fuera del top-10).
    """
    pos_num = pd.to_numeric(posiciones, errors="coerce")
    return pos_num.map(PUNTOS_F1_2023).fillna(0.0)


def calcular_tasas_anuales(df_hist: pd.DataFrame) -> pd.DataFrame:
    """Calcula el porcentaje anual de cada categoría de ``statusGeneric``.

    Args:
        df_hist: DataFrame histórico ya filtrado con columnas ``year`` y ``statusGeneric``.

    Returns:
        Tabla cruzada normalizada por año (en porcentaje sobre coches que salieron).
    """
    return (
        pd.crosstab(
            index=df_hist["year"],
            columns=df_hist["statusGeneric"],
            normalize="index",
        )
        * 100
    )


def evaluar_h1(df_hist: pd.DataFrame) -> dict:
    """Evalúa H1: caída histórica de la tasa de abandono mecánico (1990–2023).

    Args:
        df_hist: DataFrame de resultados históricos con columna ``year`` y ``statusGeneric``.

    Returns:
        Diccionario con tasas anuales, media móvil a 5 años, medias por década,
        porcentaje de reducción y veredicto booleano ``confirmada``.
    """
    tasas = calcular_tasas_anuales(df_hist)
    serie_mec = tasas["Mechanical issue"]

    medias_decada = {
        f"{ini}-{fin}": float(serie_mec.loc[ini:fin].mean())
        for ini, fin in DECADAS_ANALISIS
    }
    tasa_1990s = medias_decada["1990-1999"]
    tasa_2020s = medias_decada["2020-2023"]
    reduccion_pct = (1 - (tasa_2020s / tasa_1990s)) * 100

    return {
        "tasas": tasas,
        "serie_mecanicos": serie_mec,
        "media_movil_5y": serie_mec.rolling(window=5).mean(),
        "medias_decada": medias_decada,
        "tasa_1990s": tasa_1990s,
        "tasa_2020s": tasa_2020s,
        "reduccion_pct": float(reduccion_pct),
        "confirmada": bool(tasa_2020s < (tasa_1990s / 3)),
    }


def evaluar_h2(df_hist: pd.DataFrame) -> dict:
    """Evalúa H2: dominancia relativa de accidentes frente a fallos mecánicos.

    Args:
        df_hist: DataFrame histórico con columnas ``year`` y ``statusGeneric``.

    Returns:
        Diccionario con series anuales, cuota ``A/(A+M)``, medias por década,
        recuento de temporadas 2020–2023 > 50%, desglose de criterios y veredicto.
    """
    tasas = calcular_tasas_anuales(df_hist)
    acc = tasas["Accident"]
    mec = tasas["Mechanical issue"]
    # Nota: acc/(acc+mec) == count_acc/(count_acc+count_mec) al compartir denominador anual
    cuota_acc = acc / (acc + mec)

    medias_cuota = {
        f"{ini}-{fin}": float(cuota_acc.loc[ini:fin].mean())
        for ini, fin in DECADAS_ANALISIS
    }
    cuotas_2020s = cuota_acc.loc[[2020, 2021, 2022, 2023]]
    temporadas_sobre_50 = int((cuotas_2020s > 0.5).sum())

    c1 = medias_cuota["2020-2023"] > 0.5
    c2 = temporadas_sobre_50 >= 3
    c3 = medias_cuota["2020-2023"] > medias_cuota["1990-1999"]

    return {
        "serie_accidentes": acc,
        "serie_mecanicos": mec,
        "cuota_accidentes": cuota_acc,
        "medias_cuota": medias_cuota,
        "cuotas_2020s": cuotas_2020s,
        "temporadas_sobre_50": temporadas_sobre_50,
        "criterios": {"c1": bool(c1), "c2": bool(c2), "c3": bool(c3)},
        "confirmada": bool(c1 and c2 and c3),
    }


def evaluar_h3(results_23: pd.DataFrame, constructors_23: pd.DataFrame) -> dict:
    """Evalúa H3: concentración de accidentes por equipo y gradiente de parrilla en 2023.

    Args:
        results_23: Resultados de la temporada 2023 (440 participaciones).
        constructors_23: Catálogo de escuderías de 2023 con ``constructorId`` y ``name``.

    Returns:
        Diccionario con distribución por equipo, porcentaje Top-3, p-value del test
        Chi-cuadrado de bondad de ajuste, tasas por mitad de parrilla, gradiente y veredicto.
    """
    df = results_23.merge(
        constructors_23[["constructorId", "name"]],
        on="constructorId",
        how="left",
    ).copy()

    # Salidas desde pit lane (grid == 0) asignadas a la mitad trasera según criterio a priori
    df["grid_corr"] = df["grid"].replace(0, 20)
    df["mitad_parrilla"] = np.where(df["grid_corr"] <= 10, "Delantera (P1-P10)", "Trasera (P11-P20)")

    accidentes = df[df["statusGeneric"] == "Accident"]
    acc_por_equipo = accidentes["name"].value_counts()
    salidas_por_equipo = df["name"].value_counts()
    acc_obs = acc_por_equipo.reindex(salidas_por_equipo.index, fill_value=0)
    acc_esp = (salidas_por_equipo / salidas_por_equipo.sum()) * acc_obs.sum()

    # Criterio 1: Top-3 equipos >= 50%
    top3_pct = float((acc_por_equipo.head(3).sum() / len(accidentes)) * 100)
    c1 = top3_pct >= 50.0

    # Criterio 2: Test Chi-cuadrado de bondad de ajuste (p < 0.05)
    _, p_value, _, _ = chi2_contingency(
        pd.DataFrame({"Observados": acc_obs, "Esperados": acc_esp}).T
    )
    c2 = float(p_value) < 0.05

    # Criterio 3: Gradiente mitad trasera vs delantera >= 1.5x
    tabla_mitad = (
        df.assign(es_acc=df["statusGeneric"] == "Accident")
        .groupby("mitad_parrilla")
        .agg(salidas=("es_acc", "count"), accidentes=("es_acc", "sum"))
    )
    tabla_mitad["tasa_pct"] = (tabla_mitad["accidentes"] / tabla_mitad["salidas"]) * 100
    tasa_del = float(tabla_mitad.loc["Delantera (P1-P10)", "tasa_pct"])
    tasa_tras = float(tabla_mitad.loc["Trasera (P11-P20)", "tasa_pct"])
    gradiente = tasa_tras / tasa_del
    c3 = gradiente >= 1.5

    return {
        "total_accidentes": int(len(accidentes)),
        "accidentes_por_equipo": acc_por_equipo,
        "media_por_equipo": float(acc_obs.mean()),
        "top3_pct": top3_pct,
        "p_value_chi2": float(p_value),
        "tabla_mitad": tabla_mitad,
        "tasa_delantera_pct": tasa_del,
        "tasa_trasera_pct": tasa_tras,
        "gradiente_parrilla": float(gradiente),
        "criterios": {"c1": bool(c1), "c2": bool(c2), "c3": bool(c3)},
        "confirmada": bool(c1 and c2 and c3),
    }


def evaluar_h4(
    results_23: pd.DataFrame,
    lap_times_23: pd.DataFrame,
) -> dict:
    """Evalúa H4: coste contrafactual en puntos (Accident vs Mechanical issue) en 2023.

    Calcula el Contrafactual A (posición en la última vuelta completada, con fallback
    a parrilla si ``laps == 0``) y el Contrafactual B (rendimiento medio del piloto en
    carreras terminadas, con fallback a media de equipo si terminó menos de 3 GPs).

    Args:
        results_23: Resultados de la temporada 2023 con ``statusGeneric``.
        lap_times_23: Tiempos y posiciones vuelta a vuelta de las 22 carreras de 2023.

    Returns:
        Diccionario con tablas y totales de puntos perdidos en Contrafactual A y B,
        ratios, conteos de abandonos, criterios evaluados y veredicto final.
    """
    abandonos = results_23[
        results_23["statusGeneric"].isin(["Accident", "Mechanical issue"])
    ].copy()

    # Contrafactual A: posición en última vuelta completada; fallback a grid si laps == 0
    ultima_vuelta = (
        lap_times_23.groupby(["raceId", "driverId"])["lap"]
        .max()
        .reset_index()
        .merge(
            lap_times_23[["raceId", "driverId", "lap", "position"]],
            on=["raceId", "driverId", "lap"],
            how="left",
        )
        .rename(columns={"position": "pos_ultima_vuelta"})
    )

    ab = abandonos.merge(
        ultima_vuelta[["raceId", "driverId", "pos_ultima_vuelta"]],
        on=["raceId", "driverId"],
        how="left",
    )
    ab["pos_estimada_A"] = ab["pos_ultima_vuelta"].fillna(ab["grid"])
    ab["puntos_A"] = mapear_puntos_posicion(ab["pos_estimada_A"])

    res_A = ab.groupby("statusGeneric")["puntos_A"].agg(["sum", "count", "mean"])
    pts_A_acc = float(res_A.loc["Accident", "sum"])
    pts_A_mec = float(res_A.loc["Mechanical issue", "sum"])
    ratio_A = pts_A_acc / pts_A_mec

    # Contrafactual B: rendimiento medio del piloto en carreras terminadas (fallback equipo si <3)
    terminados = results_23[results_23["statusGeneric"] == "Finished"].copy()
    terminados["puntos_reales"] = mapear_puntos_posicion(terminados["position"])

    media_piloto = terminados.groupby("driverId")["puntos_reales"].mean()
    conteo_piloto = terminados.groupby("driverId").size()
    media_equipo = terminados.groupby("constructorId")["puntos_reales"].mean()
    driver_team = results_23.drop_duplicates(["driverId", "constructorId"]).set_index("driverId")["constructorId"]

    media_final = media_piloto.copy()
    for drv in media_final.index:
        if conteo_piloto[drv] < 3 and drv in driver_team.index:
            media_final[drv] = media_equipo[driver_team[drv]]

    ab["puntos_B"] = ab["driverId"].map(media_final)
    res_B = ab.groupby("statusGeneric")["puntos_B"].agg(["sum", "count", "mean"])
    pts_B_acc = float(res_B.loc["Accident", "sum"])
    pts_B_mec = float(res_B.loc["Mechanical issue", "sum"])

    c1 = pts_A_acc > pts_A_mec
    c2 = ratio_A >= 1.5
    return {
        "tabla_A": res_A,
        "puntos_A_accident": pts_A_acc,
        "puntos_A_mecanico": pts_A_mec,
        "ratio_A": float(ratio_A),
        "tabla_B": res_B,
        "puntos_B_accident": pts_B_acc,
        "puntos_B_mecanico": pts_B_mec,
        "ratio_B": float(pts_B_acc / pts_B_mec),
        "conteo_accidentes": int(res_A.loc["Accident", "count"]),
        "conteo_mecanicos": int(res_A.loc["Mechanical issue", "count"]),
        "criterios": {"c1": bool(c1), "c2": bool(c2)},
        "confirmada": bool(c1 and c2),
    }
