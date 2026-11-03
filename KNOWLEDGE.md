---
name: bootcamp-data-science
description: "Bootcamp de Data Science de Borja y su proyecto EDA individual sobre Formula 1: idea elegida, hipótesis, clasificación de estados, análisis completado, decisiones tomadas y entregables. Documento autocontenido para retomar el proyecto o pasarlo a otra IA."
---

# Bootcamp de Data Science — Proyecto EDA sobre Fórmula 1

Documento de estado del proyecto, autocontenido: incluye contexto completo, decisiones tomadas con su justificación, análisis realizados, resultados obtenidos y siguientes pasos. Permite retomar el proyecto sin información previa.

**Protocolo de sincronización (3 nov 2026):** este archivo es la fuente de verdad central del proyecto. Cualquier avance, decisión o resultado debe quedar reflejado aquí.

## 1. Contexto general

- **Autor:** Borja Bueno Garaigordobil.
- **Encargo:** proyecto **individual** — un EDA sobre temática libre, resolviendo un problema real con hipótesis formuladas **antes** del análisis.
- **Entregables:**
  - Presentación (60%): 15 min, público NO técnico, slides (PowerPoint/Prezi).
  - Memoria (30%): máx. 10 páginas.
  - Código (10%): repo GitHub con estructura `src/data`, `src/notebooks`, `src/utils`, `src/main.ipynb`.
- **Guía del centro:** business case → data understanding → data cleaning → analysis → resultados.

## 2. Proyecto elegido: "¿Cuánto cuesta no ver la bandera a cuadros?"

- **Caso de negocio:** F1 reparte ~1.266M$ en premios (cada posición vale ~£7M menos). Abandonos = pérdida de puntos = millones.
- **Hipótesis:**
  - **H1 (1990–2023):** Tasa de abandono mecánico ha caído. **✅ CONFIRMADA**
  - **H2 (1990–2023):** Accidentes dominan los abandonos. **✅ NO CONFIRMADA**
  - **H3 (2023):** Accidentes se concentran en pocos equipos/zonas. **✅ COMPLETADA - NO CONFIRMADA**
  - **H4 (2023):** Accidentes costaron más puntos que fallos mecánicos. **⏳ PENDIENTE**

## 3. Datos

- **Fuente:** CSVs de Ergast/Kaggle (`archive/`).
- **Datos limpiados:** `data/results_23.csv`, `results_90_23.csv` (con `statusGeneric`).
- **Notebooks:** `exploracion y limpieza.ipynb`, `hipotesis 1.ipynb`, `hipotesis 2.ipynb`, **`hipotesis 3.ipynb`** ✅.

## 4. Clasificación de estados

- **`statusGeneric`:** 5 categorías (Finished, Mechanical, Accident, Retired, Other).
- **Auditoría:** 112 statusId auditados, 202 casos verificados.

## 5. Análisis H1 ✅

- **Criterio:** Tasa media 2020s < 1/3 de los 90s.
- **Resultado:** 7% < 10.07% → **CONFIRMADA**.

## 6. Análisis H2 ✅

- **Criterio:** Cuota A/(A+M) > 50% en 2020-2023 + 3/4 temporadas > 50% + > 1990s.
- **Resultado:** Solo 2/4 temporadas > 50% → **NO CONFIRMADA**.

## 6bis. Análisis H3 ✅

### Hipótesis H3
**Enunciado:** *"Los accidentes de 2023 no se repartieron al azar: se concentran en pocos equipos, y esa concentración se relaciona con la zona de salida (mitad de parrilla hacia atrás)."*

**Criterios (A PRIORI, 3 nov 2026):**
1. Top-3 equipos acumulan ≥ 50% de los accidentes.
2. Chi-cuadrado (p < 0.05): Los accidentes NO se reparten al azar.
3. Gradiente: Tasa de la mitad trasera (11-20) ≥ 1.5× la de la delantera (1-10).
**→ H3 se confirma solo si los 3 criterios se cumplen.**

**Metodología:**
- Datos: `results_23.csv` con `statusGeneric == 'Accident'` (33 accidentes).
- Zonas de parrilla: Cuartos (1-5, 6-10, 11-15, 16-20).
- Chi-cuadrado: Observados vs. esperados (proporcional a salidas).
- Gradiente: Tasa trasera / tasa delantera.

**Resultados:**
- **Top-3 equipos:** Alpine (18.2%), Williams (18.2%), Haas (12.1%) → **48.5%** (❌ Criterio 1).
- **Chi-cuadrado:** p-value = **0.9661** (❌ Criterio 2).
- **Gradiente:** **1.30** (❌ Criterio 3).

**Conclusión:** **H3 NO SE CONFIRMA ❌** (ninguno de los 3 criterios se cumple).

**Material para presentación:**
> *"Aunque los equipos de la mitad trasera de la parrilla tienen un 30% más de accidentes, la distribución por equipos es estadísticamente similar al azar (p=0.9661), y el top-3 solo acumula el 48.5% de los accidentes."*

**Visualizaciones:**
- Gráfico de barras por equipo (con anotación del top-3: 48.5%).
- Gráfico de tarta por zona de parrilla.
- Gráfico de comparación delantera vs. trasera (con umbral del 1.5×).

## 7. Estado actual

### ✅ Completo
- Limpieza de datos y `statusGeneric`.
- Auditoría de estados.
- Análisis y validación de **H1, H2, H3**.
- Datos limpiados en `data/`.
- Criterios formales definidos y verificados para **H1, H2, H3**.

### ⏳ Pendiente
- **H4:** Calcular puntos perdidos por tipo de abandono en 2023.
- Estructura final del repo (`src/`).
- README y memoria.

## 8. Hilo narrativo

**Resultados para incluir:**
- **H1:** "Tasa de abandono mecánico: 30.2% (90s) → 7% (actualidad). Mejora del 77%."
- **H2:** "Cuota de accidentes: 37% → 53%. No domina sostenidamente."
- **H3:** **"Accidentes en 2023: top-3 suma 48.5%, p=0.9661, gradiente=1.30. No hay concentración significativa."**
- **H4:** (pendiente).

## 9. Estructura del repositorio

```
EDA_F1/
├── archive/              # Datos originales
├── data/                 # Datos limpiados (con statusGeneric)
├── notebooks/
│   ├── exploracion y limpieza.ipynb  # ✅
│   ├── hipotesis 1.ipynb             # ✅
│   ├── hipotesis 2.ipynb             # ✅
│   └── hipotesis 3.ipynb             # ✅ NUEVO
└── KNOWLEDGE.md          # Este documento
```

## 10. Decisiones documentadas

### Análisis H3
- ✅ Enunciado y criterios definidos A PRIORI (3 nov 2026).
- ✅ Metodología: Zonas de parrilla, chi-cuadrado, gradiente.
- ✅ Resultado: **NO SE CONFIRMA** (ningún criterio cumplido).

## 11. Preferencias de trabajo

- Protocolo: `KNOWLEDGE.md` es la fuente de verdad central.

## 12. Material para la memoria

- **Resultados H3:**
  - Desglose por equipo/zona (top-3: 48.5%, p=0.9661, gradiente=1.30).
  - Análisis de los 3 criterios y por qué no se confirman.
  - Conclusión: *"No hay concentración estadística ni relación clara con la zona de salida."*
- **Fuentes:** Ergast/Kaggle, Wikipedia, Autosport, etc.