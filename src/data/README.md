# Datos del Proyecto (`src/data/`)

Por tamaño y buenas prácticas de control de versiones, los archivos `.csv` están excluidos de Git mediante `.gitignore`. Este directorio contiene tanto los datos originales en `raw/` como los conjuntos limpios generados por [`00_exploracion_y_limpieza.ipynb`](../notebooks/00_exploracion_y_limpieza.ipynb).

> **Descarga directa de los CSVs del proyecto:** todos los archivos CSV necesarios están disponibles en [esta carpeta de Google Drive](https://drive.google.com/drive/folders/1FNLgKU6Nc4e3q0OKzD77TV9CnBllzs7g?usp=sharing).

---

## 1. Datos originales (`src/data/raw/`)

Proceden del dataset público **Formula 1 World Championship (1950 - 2024)** en Kaggle (derivado de la base histórica de **Ergast**).

Para reproducir la limpieza desde cero, descarga el dataset de Kaggle y coloca los CSV originales dentro de `src/data/raw/` (especialmente: `races.csv`, `results.csv`, `status.csv`, `constructors.csv`, `drivers.csv` y `lap_times.csv`).

---

## 2. Datos limpios y procesados (`src/data/`)

Generados al ejecutar [`src/notebooks/00_exploracion_y_limpieza.ipynb`](../notebooks/00_exploracion_y_limpieza.ipynb):

| Archivo | Descripción | Registros |
| :--- | :--- | :---: |
| `status.csv` | Catálogo de estados (`statusId`) enriquecido con la clasificación auditada `statusGeneric` (`Finished`, `Accident`, `Mechanical issue`, `Retired`, `Other`) | 139 |
| `races_90_23.csv` | Carreras oficiales del periodo histórico 1990–2023 | 617 |
| `races_23.csv` | Grandes Premios de la temporada 2023 | 22 |
| `results_90_23.csv` | Resultados individuales de 1990–2023 con `statusGeneric` integrado | 13.850 |
| `results_23.csv` | Resultados individuales de la temporada 2023 con `statusGeneric` integrado | 440 |
| `constructors_23.csv` | Escuderías participantes en 2023 | 10 |
| `drivers_23.csv` | Pilotos participantes en 2023 | 22 |
| `lap_times_23.csv` | Tiempos y posiciones vuelta a vuelta de las 22 carreras de 2023 | 24.386 |
| `damage_cost_2023.csv` | Estimación periodística de costes de reparación por daños en 2023 por piloto (fuente: *Sports Illustrated* / *Formula Data Analysis*, USD y EUR) | 20 |
