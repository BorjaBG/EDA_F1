---
name: bootcamp-data-science
description: "Bootcamp de Data Science de Borja y su proyecto EDA individual sobre Formula 1: idea elegida, hipótesis, clasificación de estados, análisis completado, decisiones tomadas y entregables. Documento autocontenido para retomar el proyecto o pasarlo a otra IA."
---

# Bootcamp de Data Science — Proyecto EDA sobre Fórmula 1

Documento de estado del proyecto, autocontenido: incluye contexto completo, decisiones tomadas con su justificación, análisis realizados, resultados obtenidos y siguientes pasos. Permite retomar el proyecto sin información previa.

## 1. Contexto general

- **Autor:** Borja Bueno Garaigordobil. Hace un bootcamp de Data Science.
- **Encargo:** proyecto **individual** — un EDA (análisis exploratorio de datos) sobre temática libre, resolviendo un problema real con hipótesis formuladas **antes** del análisis y verificadas después.
- **Entregables y evaluación:**
  - Presentación (60%): máx. 15 min, público NO técnico, sin código, con hilo narrativo (~30% caso de uso / ~50% análisis / ~20% conclusiones y plan de acción). Formato slides (PowerPoint/Prezi), no notebooks ni PDF.
  - Memoria (30%): máx. 10 páginas; documentar fuentes, técnicas y dificultades.
  - Código (10%): repo GitHub con README breve; estructura `src/data`, `src/notebooks`, `src/utils`, `src/main.ipynb`; valoran limpieza y documentación.
- **Guía del centro (5 fases del EDA):** business case → data understanding → data cleaning → analysis (uni/bi/multivariante) → resultados (contraste de hipótesis + plan de acción + comunicación).

## 2. Proyecto elegido: "¿Cuánto cuesta no ver la bandera a cuadros?"

EDA sobre el coste de los abandonos en F1 ("el coste de romperse"): fiabilidad mecánica + accidentes.

- **Caso de negocio:** F1 reparte premios según la posición en el campeonato de constructores (fondo ~1.266 M$ en 2024; cada posición vale ~£7M menos que la anterior); cada abandono cuesta puntos que equivalen a millones. Además, dañar coches consume presupuesto dentro del tope presupuestario (destruir un monoplaza ~6 M$). Anécdotas narrativas: Williams sin chasis de repuesto tras los accidentes de Albon (2024); Sargeant y Ocon con 7 DNFs cada uno en 2023; Williams 11 DNFs en 2023.
- **Diseño macro → micro:** una única pregunta de negocio con hipótesis a dos escalas:
  - **H1 (1990–2023):** la tasa de abandono mecánico ha caído de forma sostenida. **✅ COMPLETADA Y CONFIRMADA**
  - **H2 (1990–2023):** los accidentes (no los fallos) dominan ya los abandonos. **⏳ EN PROGRESO - RESULTADOS PRELIMINARES**
  - **H3 (temporada 2023):** los abandonos se concentran en pocos equipos/pilotos, no al azar. **⏳ PENDIENTE**
  - **H4 (temporada 2023):** los accidentes costaron más puntos que los fallos mecánicos. **⏳ PENDIENTE**
- **Por qué dos escalas:** una sola temporada no permite análisis por circuito (n=1 por circuito) ni tendencias; el histórico completo exige normalizar sistemas de puntuación. El foco de temporada da frescura y el contexto histórico permite decir si 2023 es anómala (referencias externas: tasa de no-finalización no técnica 27% en 1992 vs 7% en 2023; fiabilidad moderna ~95%).
- **Foco de temporada:** 2023 (alternativa considerada: 2024).
- **Ideas descartadas durante la exploración** (por si se reabren): pole→victoria, ¿piloto o coche?, estrategia de boxes, reglamento 2022 y adelantamientos, efecto GP en casa, lluvia, sprints, punto de vuelta rápida (2019-2024, eliminado en 2025).

## 3. Datos

- **Fuente en uso:** CSVs derivados de Ergast (`archive/*.csv`), desde Kaggle ("Formula 1 Race Data"). Tablas: `results`, `status`, `races`, `constructors`, `drivers`.
- **Datos limpiados guardados:** En `data/` (generados desde `exploracion y limpieza.ipynb`):
  - `races_23.csv`: 22 carreras de 2023
  - `races_90_23.csv`: 617 carreras (1990-2023)
  - `results_23.csv`: 440 resultados de 2023 con `statusGeneric`
  - `results_90_23.csv`: ~13,850 resultados (1990-2023) con `statusGeneric`
  - `status.csv`: tabla de status con columna `statusGeneric`
  - `constructors_23.csv`: constructores de 2023
  - `drivers_23.csv`: pilotos de 2023
- **Período de análisis:** 1990–2023 (137 statusId distintos en el dataset completo, 112 statusId diferentes aparecen en los datos del usuario para este período).
- **Cuidado:** la API Ergast cerró a finales de 2024 — no usar la API; los CSVs del dataset siguen siendo válidos. Sucesores si se necesita API: Jolpica-F1 (sucesora directa), OpenF1 (telemetría, JSON/CSV), FastF1 (librería Python).
- **Notebooks:**
  - `exploracion y limpieza.ipynb`: limpieza inicial y creación de `statusGeneric`. **✅ COMPLETADO**
  - `hipotesis 1.ipynb`: análisis completo de H1. **✅ COMPLETADO**
  - `hipotesis 2.ipynb`: análisis en progreso de H2. **⏳ EN PROGRESO**
- **Trampas de calidad conocidas:** el sistema de puntuación cambió (9-6-4 → 10-6-4 → 25-18-15 desde 2010) → normalizar a "proporción de puntos posibles" o restringir; el campo `laps` permite validar "+N Laps"; regla del 90%: hay pilotos retirados que figuran como clasificados.

## 4. Clasificación de estados (COMPLETADA y auditada)

Variable creada: `statusGeneric` con 5 categorías aplicadas a todos los statusId que aparecen en los datos del usuario (1990-2023).

### Listas finales aplicadas (celda 15 de `exploracion y limpieza.ipynb`)

| statusGeneric | Nº estados | Casos principales | StatusIds destacados |
| --- | --- | --- | --- |
| **Finished** | 17 | `Finished` y todos los `+N Laps` | 1, 11, 12, 13, 14, 17, 18, 19, 45, 50, 55, 58, 88, 111, 128 |
| **Mechanical issue** | 63 | Componentes/sistemas explícitos | 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 34, 36, 37, 38, 39, 40, 42, 43, 44, 46, 47, 48, 60, 61, 63, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 79, 80, 84, 85, 86, 87, 91, 93, 94, 95, 98, 99, 101, 102, 103, 106, 108, 109, 110, 121, 126, 129, 131, 132, 135 |
| **Accident** | 14 | Accident, Collision, Spun off, daños | 3, 4, 20, 29, 33, 41, 49, 59, 83, 130, 136, 137, 138, 140 |
| **Retired** | 1 | Estado genérico sin causa | 31 |
| **Other** | 17 | Administrativos y condición del piloto | 2, 35, 54, 62, 64, 68, 73, 77, 78, 81, 82, 89, 90, 92, 96, 97, 139 |

### Cambios clave aplicados tras auditoría
**De Mechanical issue a Accident:**
- `29: Puncture` → Accident (73% de los casos documentados son daño por debris/colisión)
- `59: Tyre puncture` → Accident (por consistencia con 29)
- `33: Front wing` → Accident (daño por contacto, ej: Pérez Bakú 2017)
- `41: Broken wing` → Accident (daño por contacto)
- `136: Seat` → Accident (Pérez Bakú 2017, daño por colisión con Ocon)
- `140: Undertray` → Accident (daño por contacto, ej: Alonso USA 2023)

**De Mechanical issue a Other:**
- `35: Refuelling` → Other (problema administrativo, ej: Albers Francia 2007)
- `64: Handling` → Other (problema de configuración, no fallo mecánico)

**Mantenidos en Mechanical issue con nota de ambigüedad:**
- `22: Suspension` (142 casos: ~34% de los documentados son daño, ~50% sin causa)
- `27: Tyre` (21 casos: 87% de los documentados son blowouts/fallos reales)
- `65: Rear wing` (10 casos: 83% fallos estructurales verificados)

**Metodología de la auditoría:**
- 3 rondas de verificación
- 112 statusId auditados (todos los que aparecen en los datos del usuario para 1990-2023)
- 202 casos verificados individualmente (de los 6 estados más ambiguos)
- Fuentes externas: Wikipedia (informes de carrera), Autosport, Crash.net, Motorsport Week, Grandprix.com, RaceFans, BBC
- Conciliación automática: 0 statusId sin clasificar en los datos del usuario

## 5. Análisis completado: H1 ✅

### Hipótesis H1
**Enunciado:** "La tasa de abandono mecánico ha caído de forma sostenida (1990-2023)"

**Criterio de aceptación definido (celda 1 de `hipotesis 1.ipynb`):**
> H1 se confirma si la tasa media de los 2020s es menos de un tercio de la de los 1990s

**Metodología aplicada:**
1. Excluidos del denominador: statusId 81 (DNQ), 97 (DNPQ), 77 (107% Rule), 54 (Withdrew) → coches que no salieron a pista
2. Cálculo: `(statusGeneric == 'Mechanical issue').mean() * 100` por año
3. Filtro: solo coches que salieron efectivamente

**Resultados obtenidos:**
- Tasa media años 90 (1990-1999): **30.2%**
- Tasa media años 2020 (2020-2023): **7%**
- Diferencia absoluta: **23 puntos porcentuales**
- Diferencia relativa: **77% de reducción**
- Umbral de aceptación (1/3 de 30.2%): **10.07%**

**Conclusión:** 7% < 10.07% → **H1 se CONFIRMA ✅**

**Visualización:** Gráfico con puntos anuales + media móvil de 5 años (celdas 6, 8, 9, 10 de `hipotesis 1.ipynb`) muestra tendencia claramente decreciente.

## 6. Análisis en progreso: H2 ⏳

### Hipótesis H2
**Enunciado:** "Los accidentes, no los fallos, dominan ya los abandonos (1990-2023)"

**Criterio de aceptación definido (celda 1 de `hipotesis 2.ipynb`):**
> H2 se confirma si en 2020-2023 los accidentes superan a los fallos mecánicos como causa de abandono, **y** esta proporción es mayor que en 1990-1999

**Metodología aplicada:**
1. Carga de `results_90_23.csv` y `races_90_23.csv`
2. Merge con año y filtro de coches que salieron (excluir DNQ, DNPQ, 107% Rule, Withdrew)
3. Cálculo de proporciones por año usando `pd.crosstab()` con normalización por fila
4. Extracción de series: `Accident` y `Mechanical issue`

**Resultados preliminares:**
- **1990-1999:** Accidentes 17.8% | Mecánicos 30.2%
- **2000-2009:** Accidentes 11.7% | Mecánicos 18.9%
- **2010-2019:** Accidentes 7.6% | Mecánicos 10.5%
- **2020-2023:** Accidentes 7.6% | Mecánicos 7.0%

**Análisis de resultados:**
- ✅ En 2020-2023, los accidentes (7.6%) **superan ligeramente** a los mecánicos (7.0%)
- ❌ Sin embargo, la proporción de accidentes en 2020-2023 (7.6%) es **menor** que en 1990-1999 (17.8%)
- **Conclusión preliminar:** Según el criterio actual, **H2 NO se confirmaría** (el segundo requisito no se cumple)

**Nota:** El criterio podría ajustarse. Por ejemplo, si se usa solo "accidentes superan a mecánicos en 2020-2023", entonces **H2 se confirmaría** (7.6% > 7.0%).

## 7. Estado actual y siguientes pasos

### ✅ Completo
- Limpieza de datos y creación de `statusGeneric`
- Auditoria exhaustiva de la clasificación de estados
- Análisis y validación de H1
- Datos limpiados guardados en `data/`
- Análisis preliminar de H2 con resultados numéricos

### ⏳ Pendiente
- **H2 (1990-2023):** Decidir criterio de aceptación final y concluir análisis
- **H3 (temporada 2023):** Analizar concentración de abandonos por equipo/piloto
- **H4 (temporada 2023):** Calcular puntos perdidos por tipo de abandono
- **Estructura final del repo:** Crear estructura `src/data`, `src/notebooks`, `src/utils`, `src/main.ipynb` según exigencias del centro
- **Memoria:** Documentar el proceso de auditoría de estados y los resultados de H1 y H2

### 📊 Próximos pasos inmediatos
1. **H2:** Decidir si ajustar el criterio de aceptación o mantener el actual
2. Redactar conclusión formal de H2 en `hipotesis 2.ipynb`
3. Crear notebook `hipotesis 3.ipynb` para H3

## 8. Hilo narrativo de la presentación (borrador)

"F1 reparte ~1.200M$ según una tabla de puntos → cada bandera a cuadros que no ves es un cheque que no cobras → históricamente los coches se rompían; hoy casi nunca → entonces ¿quién quema dinero ahora y por qué? → en 2023 lo pagaron unos pocos equipos/pilotos, sobre todo por accidentes → plan de acción: inversión en fiabilidad vs formación/sanciones". 

Empezar con empatía (afición del autor por la F1). Cerrar con números de impacto. Sin código ni jerga; la correlación se explica como "cuando uno sube, ¿sube el otro?".

**Resultados para incluir:**
- H1: "La tasa de abandono mecánico se redujo de 30.2% en los 90 a solo 7% en la actualidad, una mejora del 77% que confirma que los coches son mucho más fiables"
- H2: "Aunque los accidentes superan ligeramente a los fallos mecánicos en 2020-2023 (7.6% vs 7.0%), su proporción ha disminuido respecto a los años 90, lo que sugiere que ambos tipos de abandonos han caído drásticamente"

## 9. Estructura actual del repositorio

```
EDA_F1/
├── archive/              # Datos originales de Kaggle
│   ├── races.csv
│   ├── results.csv
│   ├── status.csv
│   ├── constructors.csv
│   └── drivers.csv
│
├── data/                 # Datos limpiados (generados por exploracion y limpieza.ipynb)
│   ├── races_23.csv
│   ├── races_90_23.csv
│   ├── results_23.csv
│   ├── results_90_23.csv
│   ├── status.csv
│   ├── constructors_23.csv
│   └── drivers_23.csv
│
├── notebooks/
│   ├── exploracion y limpieza.ipynb  # ✅ COMPLETADO: limpieza + statusGeneric
│   ├── hipotesis 1.ipynb             # ✅ COMPLETADO: análisis H1
│   └── hipotesis 2.ipynb             # ⏳ EN PROGRESO: análisis H2
│
└── KNOWLEDGE.md          # Este documento
```

## 10. Decisiones tomadas y documentadas

### Clasificación de estados
- ✅ Todos los statusId que aparecen en los datos del usuario (1990-2023) están clasificados en `statusGeneric`
- ✅ Auditoria completa con verificación externa de casos ambiguos
- ✅ Cambios aplicados: 7 statusId movidos de Mechanical a Accident, 2 movidos de Mechanical a Other

### Análisis H1
- ✅ Criterio de aceptación definido A PRIORI
- ✅ Población de análisis: excluidos DNQ, DNPQ, 107% Rule, Withdrew
- ✅ Métrica: tasa de abandono mecánico = (abandonos mecánicos / coches que salieron) × 100
- ✅ Resultado: H1 se CONFIRMA

### Análisis H2 (en progreso)
- ✅ Criterio de aceptación definido A PRIORI
- ✅ Metodología: proporción de statusGeneric por año usando crosstab
- ⏳ Conclusión pendiente: decidir si ajustar criterio o mantener el actual

### Datos
- ✅ Datos originales de Ergast en `archive/`
- ✅ Datos limpiados con `statusGeneric` en `data/`
- ✅ Notebooks separados por fase: limpieza vs análisis

## 11. Preferencias de trabajo

- Temática elegida por afición a la Fórmula 1.
- El usuario avanza por pasos y decide él el alcance.
- Ha realizado la limpieza y auditoría de estados con rigor metodológico.
- Idioma de trabajo: español.
- Estilo: prefiera explicaciones claras y código comentado.

## 12. Material para la memoria

- **Anexo de auditoría:** El proceso de clasificación de `statusGeneric` documentado en este KNOWLEDGE.md (sección 4) puede usarse directamente como anexo de la memoria.
- **Resultados H1:** Los números exactos (30.2% → 7%, 77% de reducción) y el gráfico con media móvil son material directo para la sección de resultados.
- **Resultados H2:** Los números de evolución (17.8%→7.6% accidentes, 30.2%→7.0% mecánicos) muestran que ambos tipos de abandonos han caído drásticamente.
- **Fuentes:** Ergast/Kaggle, Wikipedia, Autosport, Crash.net, Motorsport Week, Grandprix.com, RaceFans, BBC (para la auditoría de estados).
