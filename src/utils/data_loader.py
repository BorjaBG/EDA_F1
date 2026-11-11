"""Funciones de carga y preparación de datasets limpios para el EDA F1."""

from pathlib import Path
import pandas as pd

from .config import DATA_DIR, NON_STARTER_STATUS_IDS


def filtrar_coches_que_salieron(df: pd.DataFrame) -> pd.DataFrame:
    """Excluye participaciones sin salida oficial en parrilla.

    Descarta los registros correspondientes a DNQ, DNPQ, 107% Rule y Withdrew
    definidos en ``NON_STARTER_STATUS_IDS``.

    Args:
        df: DataFrame de resultados con la columna ``statusId``.

    Returns:
        Copia del DataFrame filtrada únicamente con monoplazas que tomaron la salida.
    """
    return df[~df["statusId"].isin(NON_STARTER_STATUS_IDS)].copy()


def cargar_datos_historicos(
    data_dir: Path = DATA_DIR,
    excluir_no_salieron: bool = True,
) -> pd.DataFrame:
    """Carga los resultados históricos (1990–2023) con el año y nombre de GP.

    Args:
        data_dir: Directorio que contiene ``results_90_23.csv`` y ``races_90_23.csv``.
        excluir_no_salieron: Si es ``True``, excluye los coches que no tomaron la salida.

    Returns:
        DataFrame combinado con los resultados históricos y las columnas ``year`` y ``name``.
    """
    results = pd.read_csv(data_dir / "results_90_23.csv")
    races = pd.read_csv(data_dir / "races_90_23.csv")

    if excluir_no_salieron:
        results = filtrar_coches_que_salieron(results)

    return results.merge(races[["raceId", "year", "name"]], on="raceId", how="left")


def cargar_datos_2023(
    data_dir: Path = DATA_DIR,
    excluir_no_salieron: bool = False,
) -> dict[str, pd.DataFrame]:
    """Carga todas las tablas limpias de la temporada 2023 en un diccionario.

    Args:
        data_dir: Directorio raíz de los archivos CSV procesados.
        excluir_no_salieron: Si es ``True``, aplica ``filtrar_coches_que_salieron`` a ``results_23``.

    Returns:
        Diccionario con claves ``results``, ``races``, ``constructors``, ``drivers``,
        ``lap_times``, ``damage_cost`` y ``status``.
    """
    results_23 = pd.read_csv(data_dir / "results_23.csv")
    if excluir_no_salieron:
        results_23 = filtrar_coches_que_salieron(results_23)

    return {
        "results": results_23,
        "races": pd.read_csv(data_dir / "races_23.csv"),
        "constructors": pd.read_csv(data_dir / "constructors_23.csv"),
        "drivers": pd.read_csv(data_dir / "drivers_23.csv"),
        "lap_times": pd.read_csv(data_dir / "lap_times_23.csv"),
        "damage_cost": pd.read_csv(data_dir / "damage_cost_2023.csv"),
        "status": pd.read_csv(data_dir / "status.csv"),
    }
