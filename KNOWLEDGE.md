---
name: bootcamp-data-science
description: "Bootcamp de Data Science de Borja y su proyecto EDA individual sobre Formula 1: idea elegida, hipótesis, clasificación de estados, análisis completado, decisiones tomadas y entregables. Documento autocontenido para retomar el proyecto o pasarlo a otra IA."
---

# Bootcamp de Data Science — Proyecto EDA sobre Fórmula 1

Documento de estado del proyecto, autocontenido: incluye contexto completo, decisiones tomadas con su justificación, análisis realizados, resultados obtenidos y siguientes pasos. Permite retomar el proyecto sin información previa.

**Protocolo de sincronización (3 nov 2026):** este archivo es la fuente de verdad central del proyecto. Cualquier avance, decisión o resultado — venga de conversaciones con Vibe (Le Chat) o de trabajo con las IAs del editor (VS Code) — debe quedar reflejado aquí. Al retomar el proyecto: leer primero este archivo; al terminar una sesión de trabajo: actualizarlo con lo nuevo.

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
  - **H2 (1990–2023):** los accidentes, no los fallos, dominan ya los abandonos. **✅ COMPLETADA - NO CONFIRMADA**
  - **H3 (temporada 2023):** "Los accidentes de 2023 no se repartieron al azar: se concentran en pocos equipos, y esa concentración se relaciona con la zona de salida (mitad de parrilla hacia atrás)." **✅ COMPLETADA - NO CONFIRMADA**
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
  - `hipotesis 2.ipynb`: análisis completo de H2. **✅ COMPLETADO**
  - `hipotesis 3.ipynb`: análisis completo de H3 (33 accidentes analizados). **✅ COMPLETADO Y REPRODUCIBLE** (Restart & Run All verificado)
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

## 6. Análisis completado: H2

### Hipótesis H2
**Enunciado:** "Los accidentes, no los fallos, dominan ya los abandonos (1990-2023)"

**Criterio de aceptación definido (celda 1 de `hipotesis 2.ipynb`):**
> H2 se confirma si:
> 1. La proporción `Accident / (Accident + Mechanical issue)` supera el 50% en la media de 2020-2023
> 2. Esto ocurre en **al menos 3 de las 4 temporadas** (2020, 2021, 2022, 2023)
> 3. Esa proporción media es superior a la de 1990-1999

**Metodología aplicada:**
1. Carga de `results_90_23.csv` y `races_90_23.csv`
2. Merge con año y filtro de coches que salieron (excluir DNQ, DNPQ, 107% Rule, Withdrew)
3. Cálculo de cuota: `Accident / (Accident + Mechanical issue)` por año
4. Análisis de sensibilidad: reclasificación temporal de statusId 22 (Suspension) como Accident
5. Visualización: gráficos de líneas con datos anuales y media móvil (5 años), incluida la media móvil de la cuota A/(A+M) con umbral del 50%

**Resultados obtenidos:**

| Década | Cuota A/(A+M) | Accidentes | Mecánicos |
|--------|----------------|-------------|-----------|
| 1990-1999 | 37.09% | 17.8% | 30.2% |
| 2000-2009 | 40.48% | 11.7% | 18.9% |
| 2010-2019 | 42.45% | 7.6% | 10.5% |
| 2020-2023 | **52.60%** | 7.6% | 7.0% |

| Temporada | Cuota A/(A+M) | ¿Supera 50%? |
|-----------|----------------|--------------|
| 2020 | 48.1% | ❌ NO |
| 2021 | 57.4% | ✅ SÍ |
| 2022 | 47.9% | ❌ NO |
| 2023 | 56.9% | ✅ SÍ |

**Verificación de criterios:**
- ✅ **Criterio 1:** Media 2020-2023 (52.60%) > 50%
- ❌ **Criterio 2:** Solo 2 de 4 temporadas superan el 50% (2021 y 2023)
- ✅ **Criterio 3:** 52.60% > 37.09% (media 1990-1999)

**Análisis de sensibilidad (Suspension como Accident):**
- Media 1990-1999: 40.24%; media 2020-2023: **54.33%**; temporadas > 50%: **2/4** (sigue sin cumplirse la consistencia anual)
- Rol metodológico: es la COTA MÁXIMA favorable a los accidentes; al no salvar H2 ni siquiera este escenario, los escenarios intermedios quedan descartados por diseño

**Auditoría `Retired` (statusId 31) — censo completo (informe `informe_retired_statusId31.md`, nov 2026):**
- 67/67 casos verificados con fuentes externas, 0 sin datos: **46 F (68.7%), 16 D (23.9%), 5 O (7.5%)**
- **Cero casos 1990-2004**: la etiqueta solo existe desde ~2005 (cambio administrativo del cronometraje FIA: retiradas en boxes pasan a anunciarse como "Retired" en vez de con su avería específica) → la comparación histórica del criterio 3 queda intacta
- Impacto en la ventana crítica 2020-2023 (7 casos: 3 F, 1 D, 3 O): con el mapeo F→Mechanical, D→Accident, O→fuera del reparto, entran +1 accidente y +3 mecánicos → la cuota moderna baja ligeramente (~51-52%, estimado) → **la sensibilidad Retired REFUERZA la no-confirmación**
- Conclusión: el veredicto de H2 es robusto ante los 4 escenarios de clasificación (base, Suspension→Accident, Retired mapeado, combinado). La exclusión de `Retired` en el análisis base era ligeramente favorable a H2 (68.7% de los casos eran mecánicos), y aun así H2 no se confirmó
- ⚠️ Pendiente: ejecutar en VS Code la sensibilidad exacta con el mapeo del informe; los O quedan fuera del reparto (decisión declarada)

**Conclusión final:** **H2 NO SE CONFIRMA ❌**

El criterio 2 (3 de 4 temporadas con cuota > 50%) no se cumple porque 2020 (48.1%) y 2022 (47.9%) están ligeramente por debajo del umbral, a pesar de que la media de la década sí supera el 50%.

**Terminología oficial (revisión 2-3 nov 2026):** el término correcto es **"no se confirma"**, no "se refuta": con los datos no cabe afirmar ni que los accidentes dominan ni que no dominan. Con n≈240 abandonos con causa en 2020-2023, una cuota de 52.6% frente a un empate 50/50 da p≈0.56 (estimado con conteos aproximados; pendiente test binomial exacto) → **paridad estadística**. Formulación oficial:
> "H2 no se confirma: los datos de 2020-2023 muestran paridad entre accidentes y fallos mecánicos (52.6% vs 47.4%), con una tendencia estructural al alza desde los 90 (37%). La afirmación 'los accidentes dominan ya' no está soportada; la correcta es 'los accidentes alcanzaron y rozan el dominio, pero no lo consolidan'."

⚠️ Pendiente en el notebook: la celda de conclusión aún dice "H2 se REFUTA con los datos actuales" — sustituir por la formulación oficial.

**Media móvil de la cuota (análisis complementario, 2 nov 2026):**
- La cuota suavizada (ventana de 5 años) cruza el 50% solo **dos veces** en 34 años: **2012** (51.3%, transitorio: volvió a caer hasta ~38% en 2018) y **2023** (51.5%)
- El pico de 2008-2009 (59.3%/54.7% anual) nunca superó el 50% suavizado (máx. 49.1% en 2009)
- **Interpretación:** el cambio es real pero reciente y con retrocesos; el cruce de 2023 es una observación de frontera (incluye 2019, solo 4 temporadas modernas) — confirmarlo requiere datos futuros
- Decisiones declaradas: ventana de 5 años por consistencia con H1; la serie suavizada empieza en 1994 (NaN 1990-93 por `min_periods`); la MM5 describe, no dictamina — nunca se usa para re-evaluar el criterio a posteriori
- Blindaje opcional: MM5 con ventanas 3 y 7 (confirmar que 2012 es transitorio en todas y que 2023 solo cruza con ventana 5)

**Cierre metodológico (revisión punto por punto de H2, 2-3 nov 2026):**
- El enunciado admite dos lecturas — (a) dominio por temporada, (b) dominio en conjunto — y el criterio exige ambas a la vez más el ancla histórica: hipótesis deliberadamente "dura" (si el fenómeno es real, debe verse claro, no con diferencia mínima)
- La ventana 2020-2023 se fijó a priori como "las últimas 4 temporadas" (evita grados de libertad del investigador / cherry-picking); 2020 es temporada COVID atípica pero no se excluye post-hoc
- El criterio de consistencia anual exige mayoría de TEMPORADAS (3/4), no mayoría del total — añade consistencia año a año que la media no tiene
- La métrica es la media de cuotas anuales (cada año pesa igual); la cuota calculada desde series de tasas es equivalente a conteos (el denominador común se cancela). Pendiente calcular la cuota agregada de la ventana como robustez
- Con todo ello, la no-confirmación es robusta ante ambas lecturas del enunciado

**Material para presentación:**
"Aunque la cuota de accidentes ha crecido de 37% a 53%, no domina de forma sostenida en los últimos 4 años. El cambio es real, pero aún no es definitivo."

**Visualizaciones generadas:**
- Celda 8: Gráfico de barras por década (cuota A/(A+M))
- Celda 12: Gráfico de líneas con tasas absolutas anuales + media móvil de 5 años
- Celda 13: Gráfico de la cuota A/(A+M) — cuota anual (scatter), media móvil de 5 años y umbral del 50% marcado

## 7. Análisis completado: H3 ✅

### Hipótesis H3
**Enunciado:** "Los accidentes de 2023 no se repartieron al azar: se concentran en pocos equipos, y esa concentración se relaciona con la zona de salida (mitad de parrilla hacia atrás)."

**Criterio de aceptación definido (3 nov 2026, A PRIORI):**
> H3 se confirma si:
> 1. Top-3 equipos acumulan ≥ 50% de los accidentes (el azar daría ~30% con 10 equipos).
> 2. Chi-cuadrado de bondad (p < 0.05): Los accidentes NO se reparten al azar.
> 3. Gradiente: Tasa de la mitad trasera (11-20) ≥ 1.5× la de la delantera (1-10).
> **H3 se confirma solo si los 3 criterios se cumplen simultáneamente.**

**Metodología aplicada:**
1. Datos: `results_23.csv` con `statusGeneric == 'Accident'` (33 accidentes en 2023).
2. Merge con `constructors_23.csv` para obtener el equipo de cada piloto.
3. Zonas de parrilla: Cuartos (1-5, 6-10, 11-15, 16-20); ~110 salidas por zona en 2023.
4. Chi-cuadrado: Comparación de accidentes observados vs. esperados (proporcional a salidas por equipo).
5. Gradiente: Tasa trasera / tasa delantera.

**Notas metodológicas y revisión (Vibe, 3 nov 2026):**
- **Marco conceptual:** H3 es una "radiografía" del accidente de 2023: quién se accidenta, desde dónde sale, y si el "quién" es real o solo el eco del "dónde" (variable de confusión: los equipos peores clasifican atrás).
- **Ángulo exploratorio declarado a priori (cruce equipo×zona):** comparar la zona habitual del equipo (su media de clasificación 2023) con la posición concreta del día del accidente. Si dentro de una misma zona todos los equipos se accidentan parecido → manda la parrilla; si hay equipos que destacan controlando la zona → manda el equipo. ✅ **Implementado en el notebook** (heatmap de contingencia + gráfico de barras apiladas por equipo/zona); con n=33 en casillas 10×zonas es puramente descriptivo (no confirma ni tumba H3, como se declaró a priori).
- **Salidas desde pit lane (`grid=0`):** en 2023 hay 5 casos; el notebook los cuenta en la mitad trasera. ✅ **Declarado en el notebook** (celda de markdown después del cálculo del top-3): decisión razonable (pit lane = último, ya que los coches salen después de que el resto haya recibido la señal de inicio).
- **Bins de zonas + pit lane (corregido y verificado, 3 nov 2026):** definición única `grid.replace(0, 20)` + `bins=[1,6,11,16,21]`, `right=False`, aplicada a accidentes (celda de zona) y a salidas (celda del gradiente). El fix reasignó 1 accidente con `grid=0` de la Zona 1 a la Zona 4 y corrigió los denominadores → **el gradiente pasó de 1.30 a 1.52 y el criterio 3 pasa a CUMPLE**. ⚠️ Fragilidad declarada: con n=33, 1.52 está en el filo del umbral 1.5 — un solo accidente reclasificado voltea el criterio (si ese accidente de pit lane contara como delantera: ~1.34). El 1.30 anterior era un artefacto (pit lane caía en la Zona 1 con los bins antiguos).
- **Numeración de criterios:** ✅ **Unificada** en el notebook (1=top-3, 2=chi-cuadrado, 3=gradiente).

- **Limitación declarada a priori:** con n=33 y esperados ~3.3 accidentes por equipo, el chi-cuadrado tiene poca potencia y sus esperados < 5 (aproximación al límite); debe llegar a la memoria. Nota: el chi-cuadrado aplicado evalúa tasas por equipo, no solo conteos.

**Resultados obtenidos:**
- **Top-3 equipos**: Alpine F1 Team (6 accidentes, 18.2%), Williams (6 accidentes, 18.2%), Haas F1 Team (4 accidentes, 12.1%) → **48.5%** (❌ NO CUMPLE criterio 1: 48.5% < 50%).
- **Chi-cuadrado**: p-value = **0.9661** (❌ NO CUMPLE criterio 2: p >> 0.05; distribución estadísticamente indistinguible del azar).
- **Gradiente**: **1.52** (trasera: 20/221 salidas = 9.05% vs delantera: 13/219 = 5.94%) (✅ **CUMPLE** criterio 3: 1.52 ≥ 1.5).

**Conclusión final:** **H3 NO SE CONFIRMA ❌** (exige 3/3; caen los criterios 1 y 2, pero el criterio 3 SÍ se cumple: gradiente 1.52 ≥ 1.5).

**Material para presentación:**
> *"Los accidentes de 2023 fueron democráticos entre equipos (top-3 = 48.5%, p=0.9661: indistinguible del azar), pero no respecto a la parrilla: la mitad trasera sufrió un 52% más de accidentes (gradiente 1.52). Al no cumplirse los 3 criterios a la vez, H3 no se confirma — aunque sí emerge un gradiente de parrilla."*

**Visualizaciones generadas:**
- Gráfico de barras por equipo (con anotación del top-3: 48.5%).
- Gráfico de tarta por zona de parrilla.
- Gráfico de comparación delantera vs. trasera (con umbral del 1.5× marcado).
- **Cruce exploratorio:** heatmap de contingencia zona habitual vs. zona real + gráfico de barras apiladas por equipo/zona.

## 8. Estado actual y siguientes pasos

### ✅ Completo
- Limpieza de datos y creación de `statusGeneric`
- Auditoria exhaustiva de la clasificación de estados
- Análisis y validación de H1
- Análisis y validación de H2
- Análisis y validación de H3 (notebook `hipotesis 3.ipynb` con 33 accidentes analizados)
- Datos limpiados guardados en `data/`
- Criterios formales definidos y verificados para H1, H2 y H3

### ⏳ Pendiente
- **H4 (temporada 2023):** Calcular puntos perdidos por tipo de abandono
- **Cálculos en VS Code (en cola):** sensibilidad Retired exacta con el mapeo del informe; cuota agregada 2020-2023; conteos exactos A y M 2020-2023 para test binomial exacto; opcional MM5 ventanas 3/7; cuota 2020 a 4 decimales en escenario Suspension
- **Cambios de notebook pendientes (repo):** `hipotesis 2.ipynb`: sustituir "H2 se REFUTA" por la formulación oficial "no se confirma"; añadir print de la serie MM5 (celda 13) + comentario NaN 1990-93; comentario de equivalencia cuota tasas↔conteos (celda 7). `hipotesis 3.ipynb`: ✅ bins corregidos y pit lane unificado (verificado: gradiente 1.52, criterio 3 CUMPLE), numeración unificada, pit lane declarado, cruce exploratorio añadido (heatmap + gráfico de barras apiladas); ✅ `labels` definido en la celda de zona antes de su primer uso y notebook re-ejecutado de arriba abajo sin errores (commit 8c777ab; verificado en remoto: 13/219, 20/221, gradiente 1.52, criterio 3 CUMPLE) → **H3 CERRADA** (3 nov 2026)
- **Subir `informe_retired_statusId31.md` al repo** (p. ej. `docs/`) y referenciarlo
- **Estructura final del repo:** Crear estructura `src/data`, `src/notebooks`, `src/utils`, `src/main.ipynb` según exigencias del centro
- **README:** Redactar (actualmente solo contiene el título "# EDA_F1")
- **Memoria:** Documentar proceso, resultados y dificultades

### 📊 Próximos pasos inmediatos
1. **H4:** Crear notebook `hipotesis 4.ipynb` y calcular impacto económico de accidentes vs mecánicos en 2023
2. **Repo:** Redactar README y migrar a estructura `src/` exigida por el centro

## 9. Hilo narrativo de la presentación (borrador)

"F1 reparte ~1.200M$ según una tabla de puntos → cada bandera a cuadros que no ves es un cheque que no cobras → históricamente los coches se rompían; hoy casi nunca → entonces ¿quién quema dinero ahora y por qué? → pero en 2023 el accidente fue democrático: se repartió entre los equipos de forma estadísticamente indistinguible del azar, aunque la mitad trasera de la parrilla sufrió un 52% más (gradiente 1.52, en el filo del umbral) → plan de acción: gestionar el riesgo deportivo (parrilla trasera) más que invertir en fiabilidad". 

Empezar con empatía (afición del autor por la F1). Cerrar con números de impacto. Sin código ni jerga; la correlación se explica como "cuando uno sube, ¿sube el otro?".

**Resultados para incluir:**
- **H1:** "La tasa de abandono mecánico se redujo de 30.2% en los 90 a solo 7% en la actualidad, una mejora del 77% que confirma que los coches son mucho más fiables"
- **H2:** "Aunque la cuota de accidentes ha crecido de 37% a 53%, no domina de forma sostenida en los últimos 4 años. El cambio de tendencia es real pero aún no es definitivo."
- **H3:** "Los accidentes de 2023 fueron democráticos entre equipos (top-3 = 48.5%, p=0.9661: indistinguible del azar), pero la mitad trasera sufrió un 52% más (gradiente 1.52). H3 no se confirma porque exige los 3 criterios a la vez."
- **H4:** (pendiente) "Los accidentes costaron Z millones más que los fallos mecánicos en 2023"

## 10. Estructura actual del repositorio

```
EDA_F1/
├── archive/              # Datos originales de Kaggle
│   ├── races.csv
│   ├── results.csv
│   ├── status.csv
│   ├── constructors.csv
│   └── drivers.csv
│
├── data/                 # Datos limpiados (generados desde exploracion y limpieza.ipynb)
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
│   ├── hipotesis 2.ipynb             # ✅ COMPLETADO: análisis H2
│   └── hipotesis 3.ipynb             # ✅ COMPLETADO: análisis H3 (33 accidentes en 2023)
│
└── KNOWLEDGE.md          # Este documento
```

**Repo remoto (GitHub):** github.com/BorjaBG/EDA_F1 (acceso concedido a la IA vía GitHub App, 2 nov 2026; con permiso de ESCRITURA). Estado remoto: `.gitignore`, `KNOWLEDGE.md`, `README.md` (vacío) y `notebooks/` con los 4 notebooks. Los CSVs no se suben (correcto: el enunciado prohíbe archivos pesados).

## 11. Decisiones tomadas y documentadas

### Clasificación de estados
- ✅ Todos los statusId que aparecen en los datos del usuario (1990-2023) están clasificados en `statusGeneric`
- ✅ Auditoria completa con verificación externa de casos ambiguos
- ✅ Cambios aplicados: 7 statusId movidos de Mechanical a Accident, 2 movidos de Mechanical a Other

### Análisis H1
- ✅ Criterio de aceptación definido A PRIORI
- ✅ Población de análisis: excluidos DNQ, DNPQ, 107% Rule, Withdrew
- ✅ Métrica: tasa de abandono mecánico = (abandonos mecánicos / coches que salieron) × 100
- ✅ Resultado: **H1 se CONFIRMA**

### Análisis H2
- ✅ Criterio de aceptación definido A PRIORI (3 condiciones con cuota A/(A+M))
- ✅ Metodología: proporción de statusGeneric por año usando cuota `Accident / (Accident + Mechanical)`
- ✅ Sensibilidad aplicada: reclasificación de Suspension (statusId 22) como Accident (cota máxima pro-accidentes)
- ✅ Nueva sensibilidad (nov 2026): censo documental de `Retired` (67/67 casos, informe `informe_retired_statusId31.md`) con mapeo F→Mechanical, D→Accident, O→fuera; refuerza la no-confirmación
- ✅ Veredicto robusto ante los 4 escenarios de clasificación (base, Suspension→Accident, Retired mapeado, combinado)
- ✅ Visualización: gráficos de líneas, barras y media móvil
- ✅ Resultado: **H2 NO SE CONFIRMA** (criterio 2 no se cumple: solo 2/4 temporadas > 50%)

### Análisis H3
- ✅ Enunciado reformulado y criterio de aceptación definidos A PRIORI (3 nov 2026, ver sección 7)
- ✅ Metodología: Zonas de parrilla (cuartos), chi-cuadrado de bondad, gradiente trasera/delantera
- ✅ Resultado: **H3 NO SE CONFIRMA** (criterios 1 y 2 caen: top-3=48.5%<50%, p=0.9661>>0.05; criterio 3 CUMPLE: gradiente=1.52≥1.5, trasera 9.05% vs delantera 5.94%)

### Datos
- ✅ Datos originales de Ergast en `archive/`
- ✅ Datos limpiados con `statusGeneric` en `data/`
- ✅ Notebooks separados por fase: limpieza vs análisis

## 12. Preferencias de trabajo

- Temática elegida por afición a la Fórmula 1.
- El usuario avanza por pasos y decide él el alcance.
- Ha realizado la limpieza y auditoría de estados con rigor metodológico.
- Idioma de trabajo: español.
- Estilo: prefiera explicaciones claras y código comentado.
- Protocolo de conocimiento: el KNOWLEDGE.md del repo EDA_F1 es la fuente de verdad central; sincronizarlo al terminar cada sesión. La GitHub App tiene permiso de escritura desde el 2 nov 2026 (Vibe puede hacer push directamente).

## 13. Material para la memoria

- **Anexo de auditoría:** El proceso de clasificación de `statusGeneric` documentado en este KNOWLEDGE.md (sección 4) puede usarse directamente como anexo de la memoria.
- **Resultados H1:** Los números exactos (30.2% → 7%, 77% de reducción) y el gráfico con media móvil son material directo para la sección de resultados.
- **Resultados H2:**
  - La clarificación de la métrica (sección 6, Análisis H2) documenta una decisión metodológica con justificación
  - Resultados finales: Tabla con tasas por década y cuotas por temporada
  - El análisis de sensibilidad (statusId 22, cota máxima) y la auditoría de `Retired` (67/67 casos, 0 sin datos) como anexos de robustez — ambos refuerzan la no-confirmación
  - Media móvil de la cuota: cruces transitorios 2012/2023; el cambio es real pero reciente y con retrocesos
  - Cierre metodológico: las dos lecturas del enunciado + paridad estadística (p≈0.56) — por qué "no se confirma" y no "se refuta"; media de cuotas anuales vs cuota agregada (decisión declarada); clasificación caso a caso vs componente físico (alerón de Grosjean 2013: F estructural sin contacto, frente a Front wing/Broken wing = Accident por contacto): la categoría depende de la causa verificada, no de la pieza
  - Conclusión: "Aunque la cuota de accidentes ha crecido, no domina de forma sostenida"
- **Resultados H3:**
  - Tabla con desglose por equipo/zona y valores numéricos exactos: top-3 equipos (Alpine, Williams, Haas) = 48.5%, chi-cuadrado p=0.9661, gradiente trasera/delantera = 1.52 (20/221 vs 13/219).
  - Análisis de los 3 criterios: top-3 no llega al 50% y p-value muy superior a 0.05 (distribución indistinguible del azar); el gradiente SÍ supera el umbral (1.52 ≥ 1.5) — H3 no se confirma porque exige los 3 a la vez. Declarar la fragilidad: con n=33, un solo accidente reclasificado voltea el criterio 3.
  - Conclusión: "Los accidentes de 2023 no muestran concentración estadísticamente significativa (p=0.9661) ni top-3 dominante (48.5%), pero sí un gradiente de parrilla: la mitad trasera sufrió un 52% más (gradiente 1.52, en el filo del umbral)."
  - Limitaciones y decisiones a documentar: chi-cuadrado con n=33 y esperados ~3.3 por equipo (poca potencia, aproximación al límite — declarado a priori); salidas desde pit lane (5 casos) asignadas a la mitad trasera (`replace(0,20)`, unificado en accidentes y salidas); corrección de los bins de zonas y su efecto en el criterio 3 (1.30→1.52); cruce exploratorio equipo×zona (ya en el notebook: equipos de zona habitual 1 se accidentan en Z1-Z2; zona habitual 3 concentra 13/15 en Z3-Z4 → descriptivamente, manda la parrilla)
- **Fuentes:** Ergast/Kaggle, Wikipedia, Autosport, Crash.net, Motorsport Week, Grandprix.com, RaceFans, BBC (para la auditoría de estados).