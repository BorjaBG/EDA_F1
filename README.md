# ¿Cuánto cuesta no ver la bandera a cuadros? — EDA Fórmula 1

Análisis Exploratorio de Datos (EDA) sobre el impacto deportivo y financiero de los abandonos (**DNFs**) en la Fórmula 1 entre **1990 y 2023**, comparando **roturas mecánicas** frente a **accidentes**.

---

## Caso de Negocio

En la Fórmula 1 moderna, el campeonato de constructores reparte una bolsa de premios superior a **1.100 M€** donde cada posición perdida supone entre **7 y 11 M€** menos de ingresos, mientras que los equipos operan bajo un límite presupuestario (_Cost Cap_) de **~125 M€**. Cada abandono no solo impide sumar puntos: cuando ocurre por accidente, consume presupuesto directo en reparaciones de chasis y recambios.

**Pregunta central:** _¿Cuánto cuesta no ver la bandera a cuadros y qué causa pesa más hoy: la fiabilidad mecánica o el accidente?_

---

## Resumen de Hipótesis y Resultados

Todas las hipótesis y criterios de aceptación fueron definidos _a priori_ antes de ejecutar el análisis estadístico:

| Hipótesis |  Periodo  | Enfoque                                      | Resultado clave                                                                                  |     Veredicto      |
| :-------- | :-------: | :------------------------------------------- | :----------------------------------------------------------------------------------------------- | :----------------: |
| **H1**    | 1990–2023 | Evolución de fallos mecánicos                | Caída del **30.2% → 7.0%** (**-77%**)                                                            |   **CONFIRMADA**   |
| **H2**    | 1990–2023 | ¿Dominan los accidentes sobre la mecánica?   | Cuota A/(A+M) **52.6%**, pero solo **2/4** años > 50% (paridad **7.6% vs 7.0%**)                 | **NO SE CONFIRMA** |
| **H3**    |   2023    | Concentración por equipos y zona de parrilla | Top-3 **48.5%**, Chi² _p_ = **0.9661** (media 3.3/equipo), gradiente trasera/delantera **1.52×** | **NO SE CONFIRMA** |
| **H4**    |   2023    | Coste en puntos: accidentes vs. averías      | **65 vs 28 pts** contrafactuales (ratio **2.32×**; sensibilidad **1.42×**)                       |   **CONFIRMADA**   |

### Capa deportiva y económica (Temporada 2023)

- **Duelos decididos por abandonos:** Ferrari perdió el subcampeonato frente a Mercedes por **11 puntos** (~10 M€ en premios) tras la rotura de Leclerc en Baréin (+15 pts); Aston Martin y McLaren empataron a **266 puntos** en carreras de GP (Aston Martin superaba a McLaren en el contrafactual de rendimiento).
- **Factura de taller:** Las reparaciones de la parrilla rondaron los **~37 M€** (41,1 M\$ / 37,8 M€ según estimaciones de _Sports Illustrated_), lideradas por Logan Sargeant (**3,99 M€** / 4,33 M\$) y Williams (**6,55 M€**).

---

## Estructura del Repositorio

```text
EDA_F1/
├── src/
│   ├── main.ipynb                       # Cuaderno ejecutivo maestro (orquesta utils/ y resume H1–H4)
│   ├── data/
│   │   ├── README.md                    # Documentación del esquema de datos (CSVs excluidos de Git)
│   │   └── raw/                         # CSVs originales de Kaggle/Ergast (uso local)
│   ├── notebooks/
│   │   ├── 00_exploracion_y_limpieza.ipynb  # Limpieza, filtro histórico y clasificación statusGeneric
│   │   ├── 01_hipotesis_1.ipynb             # Contraste detallado de H1
│   │   ├── 02_hipotesis_2.ipynb             # Contraste y sensibilidad (Suspension) de H2
│   │   ├── 03_hipotesis_3.ipynb             # Contraste de H3 (equipos, Chi² y zonas de parrilla)
│   │   └── 04_hipotesis_4.ipynb             # Contraste de H4 (contrafactuales A y B + Retired)
│   └── utils/
│       ├── __init__.py                  # API pública del paquete auxiliar
│       ├── config.py                    # Rutas, paleta F1 Dark Mode, exclusiones y tabla de puntos
│       ├── data_loader.py               # Carga unificada de datasets históricos y 2023
│       ├── plotting.py                  # Contexto visual F1 Broadcast y umbral_criterio()
│       └── analysis.py                  # Métricas y evaluación reproducible de H1–H4
├── docs/
│   ├── informe_statusGeneric.md         # Auditoría completa de los 112 statusId (1990–2023)
│   └── informe_retired_statusId31.md    # Auditoría caso a caso de los 67 estados "Retired"
├── presentacion/
│   ├── index.html                       # Presentación web interactiva (10 diapositivas, F1 Broadcast)
│   └── img/                             # Gráficas finales exportadas y recursos visuales
├── KNOWLEDGE.md                         # Registro técnico y trazabilidad de decisiones del proyecto
├── requirements.txt                     # Dependencias Python del proyecto
└── README.md
```

---

## Fuentes de Datos

1. **Formula 1 World Championship (1950–2024) — Kaggle / Ergast:** Resultados oficiales de carrera, parrillas, tiempos vuelta a vuelta (`lap_times.csv`), escuderías, pilotos y catálogo de estados (`status.csv`).
2. **Auditoría documental externa:** Contrastes históricos en Wikipedia, Autosport, StatsF1, RaceFans y BBC para resolver estados ambiguos y clasificar los 67 casos etiquetados genéricamente como `Retired` (`statusId = 31`).
3. **Estimación de daños 2023:** Informe de costes por piloto recopilado a partir de datos de _Sports Illustrated_ / _Formula Data Analysis_ (`damage_cost_2023.csv`).

---

## Cómo Reproducir el Análisis

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Preparar los datos:**
   - Descarga los CSV originales del dataset **Formula 1 World Championship (Ergast)** en Kaggle y colócalos en `src/data/raw/` (detalle en [`src/data/README.md`](src/data/README.md)).
   - Ejecuta [`src/notebooks/00_exploracion_y_limpieza.ipynb`](src/notebooks/00_exploracion_y_limpieza.ipynb) para generar los conjuntos limpios en `src/data/`.
3. **Ejecutar el análisis:**
   - Para la visión ejecutiva completa, abre y ejecuta [`src/main.ipynb`](src/main.ipynb).
   - Para el desarrollo estadístico paso a paso y análisis de sensibilidad, abre los cuadernos en `src/notebooks/`.

---
