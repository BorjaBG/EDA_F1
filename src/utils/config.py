"""Configuración y constantes globales del proyecto EDA F1."""

from pathlib import Path

# Rutas del proyecto resueltas de forma robusta respecto a src/
SRC_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = SRC_DIR.parent
DATA_DIR = SRC_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
DOCS_DIR = PROJECT_ROOT / "docs"
PRESENTACION_IMG_DIR = PROJECT_ROOT / "presentacion" / "img"

# Paleta oficial F1 Broadcast Dark Mode
BG_COLOR = "#15151E"      # Fondo negro carbón oficial F1
AX_COLOR = "#1A1A24"      # Fondo interior de ejes
ROJO_F1 = "#E10600"       # Accidentes / riesgo / tendencia protagonista
AZUL_MEC = "#4CC9F0"      # Fallos mecánicos (alto contraste en modo oscuro)
NEGRO_F1 = "#15151E"      # Contraste / referencia oscura
PLATA_F1 = "#B0B0C0"      # Textos secundarios / barras neutras
GRIS_F1 = "#9CA3AF"       # Datos crudos anuales / categoría neutra
BLANCO_F1 = "#FFFFFF"     # Texto principal y acentos
GRID_COLOR = "#2E2E3E"    # Rejilla sutil

PALETA_F1 = {
    "Accident": ROJO_F1,
    "Mechanical issue": AZUL_MEC,
    "Finished": GRIS_F1,
    "Retired": "#FFB703",
    "Other": "#6C757D",
}

# statusId excluidos en todos los análisis de tasas (coches que NO tomaron la salida)
# 81: Did not qualify, 97: Did not prequalify, 77: 107% Rule, 54: Withdrew
NON_STARTER_STATUS_IDS = [81, 97, 77, 54]

# Periodos definidos a priori para comparativas históricas (H1 y H2)
DECADAS_ANALISIS = [
    (1990, 1999),
    (2000, 2009),
    (2010, 2019),
    (2020, 2023),
]

# Sistema de puntuación oficial de Fórmula 1 en carreras de GP (temporada 2023)
PUNTOS_F1_2023 = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}

# Tipo de cambio de referencia usado para homogeneizar cifras económicas de 2023
TIPO_CAMBIO_EUR_USD = 0.92

