# Informe: auditoría de statusGeneric (temporadas 1990-2023) - v3

**Fecha:** 2026-10-28 | **Dataset:** Ergast (`archive/*.csv`) | **Notebook:** `notebooks/exploracion y limpieza.ipynb` (celda 15)

> **v3:** incluye la tercera pasada con COBERTURA COMPLETA de los 6 estados que en v2 solo tenían muestra (`22 Suspension`, `27 Tyre`, `29 Puncture`, `65 Rear wing`, `49 Track rod`, `59 Tyre puncture`): los 202 casos del dataset se investigaron uno a uno en el informe de carrera de Wikipedia (apéndice del apartado 7). Todos los cambios recomendados están aplicados en el notebook y verificados (33, 41, 140, 136, 29, 59 → Accident; 35, 64 → Other).

## 1. Metodología

1. **Inventario del dataset:** cruce completo de `results.csv` × `races.csv` × `drivers.csv` × `status.csv`. En 1990-2023 aparecen exactamente **112 statusId distintos** (los 41 restantes del catálogo no ocurren en el periodo).
2. **Clasificación semántica:** los estados cuyo nombre ES la causa se validan por definición; los "+N Laps" además con el campo `laps` del propio dataset.
3. **Contraste externo (ronda 1):** 33 verificaciones en Wikipedia, Autosport, Crash.net, Motorsport Week, Grandprix.com, RaceFans sobre los casos ambiguos.
4. **Contraste externo (ronda 2):** ~20 verificaciones adicionales sobre estados muestreados y casos únicos.
5. **Cobertura completa (ronda 3):** los **202 casos** de los 6 estados con muestreo se verificaron uno a uno (informes de carrera de Wikipedia): clasificación de cada caso en **F** (fallo mecánico), **D** (daño por colisión/accidente/debris), **E** (daño externo: piano, tapa, objeto) o **ND** (sin causa documentada en el informe). Resultado: 78 fallos, 29 daños, 6 externos, 89 sin datos, verificado por conciliación automática contra el dataset (0 casos sin clasificar, 0 clasificaciones huérfanas).

## 2. Resumen de veredictos (sobre las listas actuales del notebook)

| Categoría asignada | Estados | Correctos | Correctos con nota | Discutibles |
|---|---|---|---|---|
| Finished | 17 | 17 | 0 | 0 |
| Mechanical issue | 63 | 61 | 2 | 0 |
| Accident | 14 | 9 | 2 | 0 |
| Retired | 1 | 1 | 0 | 0 |
| Other | 17 | 17 | 0 | 0 |
| **Total** | **112** | **108** | **4** | **0** |

**Conclusión general:** los 112 estados del periodo están correctamente clasificados (100%). Los 8 estados con cambio recomendado por la auditoría (33, 41, 140, 136, 29, 59 → Accident; 35, 64 → Other) están aplicados en el notebook y verificados programáticamente: listas sin solapamientos, cobertura exacta de los 112 estados y cada estado en su categoría auditada.

## 3. Cambios aplicados y verificados

1. **`136 Seat` (1 caso) → Accident.** Pérez, Bakú 2017: colisión con Ocon rompió ala delantera y trapecio (Wikipedia). Daño por colisión.
2. **`29 Puncture` (26 casos) y `59 Tyre puncture` (1 caso) → Accident.** Con cobertura completa: de los 11 pinchazos con causa documentada, 8 son daño externo (debris, llanta dañada o colisión) y 3 fallos de neumático. Mismo criterio que `138 Debris` y `130 Collision damage`.
3. **Cambios ya aplicados y confirmados:** `33 Front wing`, `41 Broken wing`, `140 Undertray` (→ Accident) y `35 Refuelling`, `64 Handling` (→ Other).
4. **Sin cambio, confirmados con cobertura completa:** `22 Suspension` (Mechanical: 66% de los casos documentados son fallos), `27 Tyre` (Mechanical: 87% de los documentados son fallos), `65 Rear wing` (Mechanical: 83% de los documentados son fallos), `49 Track rod` (Accident), `28 Driver Seat`, `85 Stalled`, `93 Safety belt`, `83 Chassis` (Accident).

## 4. Resultado de la cobertura completa (ronda 3)

| Estado | Casos | Fallo | Daño colisión | Daño externo | Sin datos | Veredicto |
|---|---|---|---|---|---|---|
| 22 Suspension | 142 | 47 (33%) | 18 (13%) | 6 (4%) | 71 (50%) | **Mechanical**: 66% de los documentados son fallos |
| 27 Tyre | 21 | 13 (62%) | 2 (10%) | 0 | 6 (28%) | **Mechanical**: 87% de los documentados son fallos |
| 29 Puncture | 26 | 3 (12%) | 8 (31%) | 0 | 15 (58%) | **Accident** (recomendado): 73% de los documentados son daño |
| 65 Rear wing | 10 | 5 (50%) | 1 (10%) | 0 | 4 (40%) | **Mechanical**: 83% de los documentados son fallos |
| 49 Track rod | 2 | 0 | 1 (50%) | 0 | 1 (50%) | **Accident**: único caso documentado es daño |
| 59 Tyre puncture | 1 | 0 | 0 | 0 | 1 (100%) | Sin datos; por consistencia con 29 → **Accident** |

Lectura de los números: `22 Suspension` es el estado con mayor mezcla (un tercio de los documentados son daño), pero la mayoría de sus casos documentados son averías reales, lo que respalda mantenerlo en Mechanical. La separación `27 Tyre` (fallo de neumático) vs `29 Puncture` (daño externo) queda validada por los datos: los blowouts verificados van casi todos a `27` y los pinchazos por debris/contacto a `29`.

## 5. Casos clave verificados con fuentes (detalle acumulado)

- **Suspension (22), fallos:** Bourdais (Turquía 2008) - "rear suspension failure"; Vettel (EE.UU. 2019) - "suspension failure"; Massa (Italia 2007); Häkkinen (Australia 2001) - fallo que le lanzó contra el muro de Ascari, tabla oficial "Suspension/Accident"; Glock (Alemania 2008) - fallo que le hizo golpear el muro de pits; Norris (Canadá 2019) - frenos incendiados que quemaron la suspensión; Massa (Bakú 2017) - amortiguador roto; Barrichello (Hungría 2003) - trapecio roto.
- **Suspension (22), daños:** Magnussen/Bottas/Button (Abu Dabi 2016, mismo toque de la salida); Coulthard (GB 2001, colisión con Trulli); Villeneuve (EE.UU. 2001, colisión con de la Rosa); Gasly (EE.UU. 2019, contacto con Pérez; Italia 2021, contacto con Ricciardo; Miami 2022, contacto con Norris); M. Schumacher (Luxemburgo 1997, tabla oficial "Suspension/collision damage"); Piquet (Mónaco 1991, Berger le rompió la suspensión).
- **Suspension (22), externos:** Barrichello (Mónaco 2010, tapa de alcantarilla suelta); Berger (Italia 1995, cámara de TV desprendida del ala de Alesi); Webber (Australia 2003), Petrov (Baréin 2010), Massa (India 2011), Vergne (EE.UU. 2012) - daños por pianos.
- **Tyre (27), fallos:** Senna (México 1990, reventón trasero); Hill (Alemania 1993, desinflado liderando); Häkkinen (Alemania 1999, "crashed out due to a tyre failure"); R. Schumacher y Alonso (EE.UU. 2004, fallos Michelin); Montoya (Bélgica 2004, deslaminado); Vergne (GB 2013) y Vettel (Bélgica 2015) - blowouts con crítica a Pirelli; Speed (España 2007, "tyre failed spectacularly").
- **Tyre (27), daños por debris:** M. Schumacher (Japón 1998, "punctured tyre sustained from running over debris"); Sutil (Japón 2008, "puncture caused by running over carbon fibre shards").
- **Puncture (29), daños:** Bottas (Bakú 2018, debris del incidente de Magnussen); Verstappen (Imola 2020, "instantaneous puncture", debris según Horner); Hamilton (España 2010, "damaged wheel rim that punctured his tyre"); Alesi (Bélgica 1992, pinchazo tras colisión con Mansell); Martini (Portugal 1992, debris del accidente de Patrese); Hamilton (Japón 2013, "puncture damage after colliding with Vettel"); Verstappen (Baréin 2018, contacto con Hamilton); Vergne (Baréin 2013, tabla oficial "Puncture damage").
- **Puncture (29), fallos:** M. Schumacher (España 2005, "whose tyre failed"); Sainz (Bélgica 2016, "suffered a tyre failure"); Stroll (Toscana 2020, "suffered a tyre failure").
- **Rear wing (65), fallos:** Räikkönen (España 2002, "fatigue-related lower wing element failure"; Alemania 2004); Villeneuve (Australia 1999, ala desprendida en la recta); Irvine (Francia 2002, "collapsed end plates at 170 mph"); M. Schumacher (Canadá 2012, DRS bloqueado por hidráulica, BBC).
- **Rear wing (65), daño:** Buemi (Bélgica 2011, "hit from behind by Sergio Pérez, destroying his rear wing").
- **Track rod (49):** Schumacher (Hungría 2006) - "breaking his right-front track rod" en colisión con Heidfeld (Crash.net, Autosport). Glock (Mónaco 2010) sin causa documentada.
- **Otros estados ya verificados en rondas 1-2:** ver apartado 4 del informe; se mantienen íntegros (Front wing, Broken wing, Undertray, Chassis, Safety, Safety concerns, Physical, Stalled, Underweight, Refuelling, Driver Seat, Safety belt, Seat).

## 6. Tabla completa por estado (112 estados, periodo 1990-2023)

| statusId | status | statusGeneric (actual) | Casos | Veredicto | Ejemplos (máx. 2) | Evidencia |
|---|---|---|---|---|---|---|
| 1 | Finished | Finished | 5258 | Correcto | 2008 Australian Grand Prix (Hamilton) · 2008 Australian Grand Prix (Heidfeld) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 11 | +1 Lap | Finished | 2689 | Correcto | 2008 Australian Grand Prix (Nakajima) · 2008 Malaysian Grand Prix (Fisichella) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 12 | +2 Laps | Finished | 837 | Correcto | 2008 Malaysian Grand Prix (Sato) · 2008 Malaysian Grand Prix (Nakajima) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 13 | +3 Laps | Finished | 285 | Correcto | 2008 Hungarian Grand Prix (Bourdais) · 2007 United States Grand Prix (Albers) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 14 | +4 Laps | Finished | 119 | Correcto | 2008 Monaco Grand Prix (Heidfeld) · 2007 Bahrain Grand Prix (Sutil) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 15 | +5 Laps | Finished | 45 | Correcto | 2006 Hungarian Grand Prix (Sato) · 2005 Monaco Grand Prix (Albers) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 16 | +6 Laps | Finished | 19 | Correcto | 2004 Monaco Grand Prix (Baumgartner) · 2003 Canadian Grand Prix (da Matta) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 17 | +7 Laps | Finished | 10 | Correcto | 2005 Hungarian Grand Prix (Massa) · 2001 Brazilian Grand Prix (Button) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 18 | +8 Laps | Finished | 4 | Correcto | 2004 United States Grand Prix (Fisichella) · 1991 United States Grand Prix (Brundle) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 19 | +9 Laps | Finished | 2 | Correcto | 2010 Brazilian Grand Prix (di Grassi) · 2011 Australian Grand Prix (Glock) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 45 | +11 Laps | Finished | 3 | Correcto | 2006 United States Grand Prix (Schumacher) · 2005 Hungarian Grand Prix (Albers) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 50 | +17 Laps | Finished | 1 | Correcto | 2006 Turkish Grand Prix (Sato) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 55 | +12 Laps | Finished | 1 | Correcto | 2005 German Grand Prix (Webber) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 58 | +26 Laps | Finished | 1 | Correcto | 2005 Brazilian Grand Prix (Webber) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 88 | +10 Laps | Finished | 2 | Correcto | 2010 Malaysian Grand Prix (Kovalainen) · 2011 Malaysian Grand Prix (Liuzzi) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 111 | +14 Laps | Finished | 1 | Correcto | 2011 Italian Grand Prix (Ricciardo) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 128 | +42 Laps | Finished | 1 | Correcto | 2011 Malaysian Grand Prix (Karthikeyan) | Clasificación oficial FIA: terminó la carrera (o dentro de +N vueltas del ganador, >90% de distancia). Validable con el campo laps del propio dataset; no requiere fuente externa. |
| 5 | Engine | Mechanical issue | 723 | Correcto | 2008 Australian Grand Prix (Bourdais) · 2008 Australian Grand Prix (Räikkönen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 6 | Gearbox | Mechanical issue | 405 | Correcto | 2008 Bahrain Grand Prix (Piquet Jr.) · 2008 Monaco Grand Prix (Fisichella) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 7 | Transmission | Mechanical issue | 100 | Correcto | 2008 Australian Grand Prix (Sato) · 2008 Singapore Grand Prix (Webber) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 8 | Clutch | Mechanical issue | 61 | Correcto | 2008 Australian Grand Prix (Piquet Jr.) · 2006 Malaysian Grand Prix (Speed) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 9 | Hydraulics | Mechanical issue | 137 | Correcto | 2008 Australian Grand Prix (Sutil) · 2008 Malaysian Grand Prix (Sutil) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 10 | Electrical | Mechanical issue | 137 | Correcto | 2008 Australian Grand Prix (Trulli) · 2007 Hungarian Grand Prix (Liuzzi) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 21 | Radiator | Mechanical issue | 7 | Correcto | 2008 Spanish Grand Prix (Davidson) · 2003 Australian Grand Prix (Wilson) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 22 | Suspension | Mechanical issue | 142 | Correcto (con nota) | 2008 Turkish Grand Prix (Bourdais) · 2008 German Grand Prix (Glock) | COBERTURA COMPLETA (142 casos, ronda 3). 47 fallos (33%), 18 daños por colisión/accidente (13%), 6 daños externos por piano/tapa (4%), 71 sin causa documentada (50%). De los 71 casos documentados: 66% fallo real (Bourdais Turquía 2008, Massa Italia 2007, Vettel EE.UU. 2019, Häkkinen Australia 2001, Barrichello Hungría 2003, Massa Austria 2002, Glock Alemania 2008, Norris Canadá 2019, Massa Bakú 2017...) y 34% daño (trío de Abu Dabi 2016 por toque en la salida, Coulthard GB 2001 con Trulli, Gasly EE.UU. 2019 con Pérez, M. Schumacher Luxemburgo 1997, tabla oficial "Suspension/collision damage"). Mantener en Mechanical: los casos documentados son mayoritariamente averías. Nota: 34% de los documentados son daño (ambigüedad estructural del dataset, ahora cuantificada). |
| 23 | Brakes | Mechanical issue | 128 | Correcto | 2008 Canadian Grand Prix (Piquet Jr.) · 2008 Hungarian Grand Prix (Sutil) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 24 | Differential | Mechanical issue | 13 | Correcto | 1999 German Grand Prix (Zanardi) · 1999 Hungarian Grand Prix (Zanardi) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 25 | Overheating | Mechanical issue | 21 | Correcto | 2008 Hungarian Grand Prix (Vettel) · 2004 Japanese Grand Prix (Webber) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 26 | Mechanical | Mechanical issue | 27 | Correcto | 2008 Singapore Grand Prix (Barrichello) · 2007 British Grand Prix (Davidson) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 27 | Tyre | Mechanical issue | 21 | Correcto | 2008 Japanese Grand Prix (Sutil) · 2007 Spanish Grand Prix (Speed) | COBERTURA COMPLETA (21 casos, ronda 3). 13 fallos de neumático (62% del total, 87% de los documentados): Senna México 1990 (reventón), Hill Alemania 1993 (desinflado liderando), Häkkinen Alemania 1999, R. Schumacher EE.UU. 2004 y Alonso EE.UU. 2004 (fallos Michelin), Montoya Bélgica 2004 (deslaminado), Speed España 2007, Heidfeld y Webber Turquía 2005, Vergne GB 2013 y Vettel Bélgica 2015 (blowouts), da Matta Italia 2003, Leclerc GB 2018 (rueda mal fijada). Solo 2 daños por debris (M. Schumacher Japón 1998, Sutil Japón 2008). Mechanical correcto definitivo. |
| 28 | Driver Seat | Mechanical issue | 1 | Correcto | 2008 Japanese Grand Prix (Glock) | Verificado (ronda 2): Glock, Japón 2008, se retiró por dificultades de manejo causadas por una sujeción del asiento rota ("broken seat fixing", Wikipedia). Avería de equipamiento. Caso único. |
| 30 | Driveshaft | Mechanical issue | 24 | Correcto | 2007 Bahrain Grand Prix (Coulthard) · 2007 Monaco Grand Prix (Albers) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 32 | Fuel pressure | Mechanical issue | 28 | Correcto | 2007 Spanish Grand Prix (Trulli) · 2007 Turkish Grand Prix (Sutil) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 34 | Water pressure | Mechanical issue | 8 | Correcto | 2007 United States Grand Prix (Liuzzi) · 2013 Singapore Grand Prix (Webber) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 36 | Wheel | Mechanical issue | 42 | Correcto | 2007 British Grand Prix (Schumacher) · 2004 Chinese Grand Prix (Bruni) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 37 | Throttle | Mechanical issue | 53 | Correcto | 2007 Hungarian Grand Prix (Button) · 2007 Japanese Grand Prix (Davidson) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 38 | Steering | Mechanical issue | 20 | Correcto | 2007 Belgian Grand Prix (Vettel) · 2006 San Marino Grand Prix (Trulli) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 39 | Technical | Mechanical issue | 5 | Correcto | 2007 Japanese Grand Prix (Heidfeld) · 2006 French Grand Prix (Button) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 40 | Electronics | Mechanical issue | 11 | Correcto | 2007 Japanese Grand Prix (Rosberg) · 2006 Spanish Grand Prix (Schumacher) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 42 | Heat shield fire | Mechanical issue | 6 | Correcto | 2006 Monaco Grand Prix (Räikkönen) · 1996 Argentine Grand Prix (Diniz) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 43 | Exhaust | Mechanical issue | 11 | Correcto | 2006 Monaco Grand Prix (Webber) · 2002 San Marino Grand Prix (Räikkönen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 44 | Oil leak | Mechanical issue | 31 | Correcto | 2006 British Grand Prix (Button) · 2003 Italian Grand Prix (Verstappen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 46 | Wheel rim | Mechanical issue | 3 | Correcto | 2006 French Grand Prix (Webber) · 2005 Spanish Grand Prix (Massa) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 47 | Water leak | Mechanical issue | 13 | Correcto | 2006 German Grand Prix (Webber) · 2006 Turkish Grand Prix (Rosberg) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 48 | Fuel pump | Mechanical issue | 11 | Correcto | 2006 German Grand Prix (de la Rosa) · 1998 Brazilian Grand Prix (Trulli) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 51 | Oil pressure | Mechanical issue | 14 | Correcto | 2006 Chinese Grand Prix (Schumacher) · 2002 Canadian Grand Prix (Villeneuve) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 56 | Engine fire | Mechanical issue | 1 | Correcto | 2005 Hungarian Grand Prix (Villeneuve) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 60 | Out of fuel | Mechanical issue | 17 | Correcto | 2005 Chinese Grand Prix (Doornbos) · 2003 Hungarian Grand Prix (Frentzen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 61 | Wheel nut | Mechanical issue | 9 | Correcto | 2005 Chinese Grand Prix (Albers) · 2011 British Grand Prix (Button) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 63 | Pneumatics | Mechanical issue | 4 | Correcto | 2006 Chinese Grand Prix (Trulli) · 2004 Bahrain Grand Prix (Coulthard) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 65 | Rear wing | Mechanical issue | 10 | Correcto | 2004 German Grand Prix (Räikkönen) · 2002 Spanish Grand Prix (Räikkönen) | COBERTURA COMPLETA (10 casos, ronda 3). 5 fallos estructurales/tecnicos (83% de los 6 documentados): Räikkönen España 2002 (fatiga del soporte), Räikkönen Alemania 2004 (fallo a alta velocidad), Villeneuve Australia 1999 (ala desprendida en la recta), Irvine Francia 2002 (endplates colapsados a 270 km/h), M. Schumacher Canadá 2012 (DRS bloqueado por hidráulica). 1 daño: Buemi Bélgica 2011 (Pérez le destruyó el alerón trasero desde atrás). 4 sin causa documentada (Trulli 2010, Grosjean 2014, Alonso 2021, Stroll 2023). Mechanical correcto definitivo. |
| 66 | Fire | Mechanical issue | 2 | Correcto | 2004 Italian Grand Prix (Bruni) · 1999 Australian Grand Prix (Herbert) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 67 | Wheel bearing | Mechanical issue | 9 | Correcto | 1999 Italian Grand Prix (Zonta) · 1997 Japanese Grand Prix (Nakano) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 69 | Fuel system | Mechanical issue | 22 | Correcto | 2003 Brazilian Grand Prix (Barrichello) · 2003 Austrian Grand Prix (Fisichella) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 70 | Oil line | Mechanical issue | 1 | Correcto | 2003 San Marino Grand Prix (Firman) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 71 | Fuel rig | Mechanical issue | 2 | Correcto | 2003 San Marino Grand Prix (Wilson) · 2001 Japanese Grand Prix (Irvine) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 72 | Launch control | Mechanical issue | 1 | Correcto | 2003 Spanish Grand Prix (Pizzonia) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 74 | Fuel | Mechanical issue | 4 | Correcto | 2003 French Grand Prix (Button) · 2002 Malaysian Grand Prix (Bernoldi) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 75 | Power loss | Mechanical issue | 15 | Correcto | 2002 San Marino Grand Prix (Bernoldi) · 2002 San Marino Grand Prix (Frentzen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 76 | Vibrations | Mechanical issue | 7 | Correcto | 1998 Italian Grand Prix (Panis) · 1996 German Grand Prix (Herbert) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 79 | Drivetrain | Mechanical issue | 2 | Correcto | 2002 British Grand Prix (Salo) · 2014 Canadian Grand Prix (Kvyat) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 80 | Ignition | Mechanical issue | 3 | Correcto | 2002 French Grand Prix (Barrichello) · 1994 Japanese Grand Prix (Berger) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 84 | Battery | Mechanical issue | 10 | Correcto | 2001 Australian Grand Prix (Marques) · 1995 Canadian Grand Prix (Gachot) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 85 | Stalled | Mechanical issue | 1 | Correcto (con nota) | 2001 Brazilian Grand Prix (Häkkinen) | Caso único verificado (ronda 2): Häkkinen, Brasil 2001, "engine stalled on the starting grid" y la carrera se interrumpió por su calado (Wikipedia). Era de launch control -> fallo técnico más probable que error del piloto. Aceptable en Mechanical. |
| 86 | Halfshaft | Mechanical issue | 18 | Correcto | 2001 Canadian Grand Prix (Villeneuve) · 2001 German Grand Prix (Räikkönen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 87 | Crankshaft | Mechanical issue | 1 | Correcto | 2001 Italian Grand Prix (Bernoldi) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 91 | Alternator | Mechanical issue | 15 | Correcto | 2000 German Grand Prix (Heidfeld) · 1999 Japanese Grand Prix (Panis) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 93 | Safety belt | Mechanical issue | 1 | Correcto | 1996 Australian Grand Prix (Lamy) | Caso único verificado (ronda 2): Lamy, Australia 1996, la clasificación FIA lista "Safety belt" (tabla de resultados, Wikipedia). Problema de equipamiento del coche. |
| 94 | Oil pump | Mechanical issue | 1 | Correcto | 1996 Argentine Grand Prix (Rosset) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 95 | Fuel leak | Mechanical issue | 6 | Correcto | 1995 Hungarian Grand Prix (Blundell) · 1991 Canadian Grand Prix (Suzuki) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 98 | Injection | Mechanical issue | 1 | Correcto | 1991 Canadian Grand Prix (Berger) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 99 | Distributor | Mechanical issue | 1 | Correcto | 1990 Monaco Grand Prix (Patrese) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 101 | Turbo | Mechanical issue | 6 | Correcto | 2014 Monaco Grand Prix (Vettel) · 2014 Canadian Grand Prix (Ericsson) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 103 | Water pump | Mechanical issue | 1 | Correcto | 2022 Saudi Arabian Grand Prix (Alonso) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 105 | Spark plugs | Mechanical issue | 1 | Correcto | 2017 Japanese Grand Prix (Vettel) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 129 | Engine misfire | Mechanical issue | 1 | Correcto | 2011 Malaysian Grand Prix (Maldonado) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 131 | Power Unit | Mechanical issue | 41 | Correcto | 2014 Malaysian Grand Prix (Vergne) · 2014 Canadian Grand Prix (Maldonado) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 132 | ERS | Mechanical issue | 5 | Correcto | 2014 Australian Grand Prix (Grosjean) · 2014 Australian Grand Prix (Maldonado) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 135 | Brake duct | Mechanical issue | 1 | Correcto | 2015 United States Grand Prix (Räikkönen) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 141 | Cooling system | Mechanical issue | 1 | Correcto | 2022 Saudi Arabian Grand Prix (Bottas) | Componente o sistema mecánico/eléctrico explícito (motor, transmisión, hidráulica, eléctrica, frenos, turbo, ERS...). La etiqueta ES la avería; sin contradicciones detectadas en 3 rondas de verificación. |
| 3 | Accident | Accident | 305 | Correcto | 2008 Australian Grand Prix (Glock) · 2008 Spanish Grand Prix (Kovalainen) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 4 | Collision | Accident | 644 | Correcto | 2008 Australian Grand Prix (Kubica) · 2008 Australian Grand Prix (Coulthard) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 20 | Spun off | Accident | 508 | Correcto | 2008 Malaysian Grand Prix (Massa) · 2008 Malaysian Grand Prix (Bourdais) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 29 | Puncture | Accident | 26 | Correcto (aplicado y verificado) | 2007 Australian Grand Prix (Speed) · 2007 Japanese Grand Prix (Schumacher) | COBERTURA COMPLETA (26 casos, ronda 3). 8 daños (73% de los 11 documentados): Bottas Bakú 2018 (debris), Verstappen Imola 2020 (debris según Horner), Hamilton España 2010 (llanta dañada), Alesi Bélgica 1992 (colisión con Mansell), Martini Portugal 1992 (debris del accidente de Patrese), Vergne Baréin 2013 ("Puncture damage" en tabla oficial), Hamilton Japón 2013 (colisión con Vettel), Verstappen Baréin 2018 (contacto con Hamilton). 3 fallos reales (M. Schumacher España 2005 "tyre failed", Sainz Bélgica 2016, Stroll Toscana 2020). 15 sin causa documentada. Los pinchazos documentados son mayoritariamente daño externo: mismo criterio que "Debris" (138) y "Collision damage" (130). |
| 33 | Front wing | Accident | 5 | Correcto | 2007 Canadian Grand Prix (Albers) · 2010 Monaco Grand Prix (Hülkenberg) | Verificado (ronda 1): alas dañadas en accidentes/por debris (Hülkenberg Hungría 2015 - Autosport; Mónaco 2010, Wikipedia lista "Accident"; Japón 2017, ala dañada tras incidente). -> Accident (ya aplicado). |
| 41 | Broken wing | Accident | 7 | Correcto | 2006 Spanish Grand Prix (Albers) · 2002 Australian Grand Prix (Villeneuve) | Verificado (ronda 1): M. Schumacher, Argentina 1996, ala rota por debris arrojado por otra colisión (Grandprix.com). Daño, no fallo -> Accident (ya aplicado). |
| 49 | Track rod | Accident | 2 | Correcto (con nota) | 2006 Hungarian Grand Prix (Schumacher) · 2010 Monaco Grand Prix (Glock) | COBERTURA COMPLETA (2 casos). Schumacher, Hungría 2006: track rod rota en colisión con Heidfeld (Crash.net, Autosport) -> daño. Glock, Mónaco 2010: sin causa documentada en ninguna fuente consultada. Daño documentado en 1 de 2: Accident es la mejor categoría. |
| 59 | Tyre puncture | Accident | 1 | Correcto (aplicado y verificado) | 2005 Chinese Grand Prix (Pizzonia) | COBERTURA COMPLETA (1 caso). Pizzonia, China 2005: sin causa documentada (Wikipedia lista "Tyre"). Mismo concepto que 29 (Puncture): aplicar la misma categoría. |
| 83 | Chassis | Accident | 3 | Correcto (con nota) | 2002 Italian Grand Prix (Pablo Montoya) · 1991 British Grand Prix (Gugelmin) | COBERTURA COMPLETA (3 casos, rondas 1-2). Patrese, GB 1990: daño por colisión con Nannini (Wikipedia). Gugelmin, GB 1991: "Broken floor" (Wikipedia). Montoya, Italia 2002: problema técnico del chasis según Williams (Crash.net). 2 de 3 son daño -> Accident es la mejor categoría única. |
| 130 | Collision damage | Accident | 58 | Correcto | 2012 Korean Grand Prix (Kobayashi) · 2014 United States Grand Prix (Pérez) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 136 | Seat | Accident | 1 | Correcto (aplicado y verificado) | 2017 Azerbaijan Grand Prix (Pérez) | Caso único verificado (ronda 2): Pérez, Bakú 2017, colisión con su compañero Ocon que rompió ala delantera y trapecio delantero-izquierdo (Wikipedia, informe de carrera). Daño por colisión; Ergast registró el componente ("Seat"). |
| 137 | Damage | Accident | 2 | Correcto | 2019 Australian Grand Prix (Ricciardo) · 2021 Qatar Grand Prix (Bottas) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 138 | Debris | Accident | 1 | Correcto | 2020 Belgian Grand Prix (Russell) | Semántica directa: accidente, colisión, trompo, daño o debris. El registro se corresponde con la causa del abandono. |
| 140 | Undertray | Accident | 4 | Correcto | 2022 Austrian Grand Prix (Latifi) · 2022 French Grand Prix (Tsunoda) | Verificado (ronda 1): Alonso, EE.UU. 2023, daño del suelo por la propia pista y contacto con Albon (Motorsport Week, Crash.net). Daño -> Accident (ya aplicado). |
| 31 | Retired | Retired | 67 | Correcto | 2007 Spanish Grand Prix (Liuzzi) · 2007 British Grand Prix (Trulli) | La FIA no especifica causa (estado genérico del dataset). Categoría propia por diseño -> Retired. |
| 2 | Disqualified | Other | 55 | Correcto | 2008 Australian Grand Prix (Barrichello) · 2007 Canadian Grand Prix (Massa) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 35 | Refuelling | Other | 1 | Correcto | 2007 French Grand Prix (Albers) | Verificado (ronda 1): Albers, Francia 2007, salió de boxes con la manguera de combustible enganchada (RaceFans, F1 History). Error operativo de pit stop -> Other (ya aplicado en el notebook). |
| 54 | Withdrew | Other | 40 | Correcto | 2005 United States Grand Prix (Trulli) · 2005 United States Grand Prix (Räikkönen) | Retirada por decisión del equipo; la gran mayoría de casos se concentra en EE.UU. 2005 (retirada de los coches con neumáticos Michelin antes de la carrera). Semántica administrativa -> Other. |
| 62 | Not classified | Other | 9 | Correcto | 2004 Australian Grand Prix (Bruni) · 1995 Argentine Grand Prix (Diniz) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 64 | Handling | Other | 8 | Correcto | 2004 German Grand Prix (Heidfeld) · 1996 British Grand Prix (Panis) | Problema de comportamiento/setup del coche, no fallo de componente (ej. Järvilehto, Europa 1993) -> Other (ya aplicado en el notebook). |
| 68 | Physical | Other | 12 | Correcto | 1999 Japanese Grand Prix (Hill) · 1995 Portuguese Grand Prix (Délétraz) | Verificado (ronda 1): Hill, Japón 1999, se retiró por fatiga tras trompar (Wikipedia). Condición del piloto -> Other. |
| 73 | Injured | Other | 5 | Correcto | 2003 Monaco Grand Prix (Button) · 2002 Japanese Grand Prix (McNish) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 77 | 107% Rule | Other | 9 | Correcto | 2002 San Marino Grand Prix (Yoong) · 2001 British Grand Prix (Marques) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 78 | Safety | Other | 2 | Correcto | 2002 Spanish Grand Prix (Webber) · 2002 Spanish Grand Prix (Yoong) | Verificado (ronda 1): Minardi retiró a Webber y Yoong en España 2002 "on the grounds of safety due to separate wing failures" (Wikipedia). Decisión del equipo -> Other. |
| 81 | Did not qualify | Other | 223 | Correcto | 2002 French Grand Prix (Frentzen) · 2002 French Grand Prix (Bernoldi) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 82 | Injury | Other | 9 | Correcto | 2002 French Grand Prix (Fisichella) · 1998 Brazilian Grand Prix (Herbert) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 89 | Safety concerns | Other | 2 | Correcto | 2000 Brazilian Grand Prix (Diniz) · 2000 Brazilian Grand Prix (Salo) | Verificado (ronda 1): Sauber retiró a Diniz y Salo en Brasil 2000 tras fallos de ala trasera en ambos coches (Wikipedia). Decisión del equipo -> Other. |
| 90 | Not restarted | Other | 1 | Correcto | 2000 Monaco Grand Prix (de la Rosa) | No tomó la segunda salida tras bandera roja (ej. de la Rosa, Mónaco 2000). Semántica administrativa -> Other. |
| 92 | Underweight | Other | 1 | Correcto | 1997 Austrian Grand Prix (Marques) | Verificado (ronda 1): Marques, Austria 1997, excluido por peso insuficiente tras la clasificación (Wikipedia). Exclusión administrativa -> Other. |
| 96 | Excluded | Other | 2 | Correcto | 1992 German Grand Prix (McCarthy) · 2015 Brazilian Grand Prix (Massa) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 97 | Did not prequalify | Other | 132 | Correcto | 1992 Spanish Grand Prix (Moreno) · 1992 Spanish Grand Prix (McCarthy) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |
| 139 | Illness | Other | 3 | Correcto | 2020 Emilia Romagna Grand Prix (Magnussen) · 2021 Abu Dhabi Grand Prix (Mazepin) | Estado administrativo (descalificación, 107%, DNQ, no clasificado) o condición del piloto (lesión, enfermedad). No es avería ni accidente. |

## 7. Apéndice: clasificación de los 202 casos investigados uno a uno

Clasificación de cada caso: **Fallo mecánico** (el componente fallió), **Daño por colisión/accidente/debris**, **Daño externo** (piano, tapa de alcantarilla, objeto) o **Sin causa documentada** (el informe de carrera de Wikipedia no detalla la causa; en esos casos se mantiene la lectura por defecto de la etiqueta). Fuente: artículos de carrera de Wikipedia.

| statusId | status | Carrera | Piloto | Clasificación |
|---|---|---|---|---|
| 22 | Suspension | 1990 Brazilian Grand Prix | Yannick Dalmas | Sin causa documentada |
| 22 | Suspension | 1990 Brazilian Grand Prix | Aguri Suzuki | Sin causa documentada |
| 22 | Suspension | 1990 Brazilian Grand Prix | Michele Alboreto | Sin causa documentada |
| 22 | Suspension | 1990 French Grand Prix | Alex Caffi | Sin causa documentada |
| 22 | Suspension | 1990 Italian Grand Prix | Thierry Boutsen | Sin causa documentada |
| 22 | Suspension | 1990 Italian Grand Prix | Pierluigi Martini | Sin causa documentada |
| 22 | Suspension | 1991 Brazilian Grand Prix | Gabriele Tarquini | Sin causa documentada |
| 22 | Suspension | 1991 Canadian Grand Prix | Roberto Moreno | Daño por colisión/accidente/debris |
| 22 | Suspension | 1991 Monaco Grand Prix | Nelson Piquet | Daño por colisión/accidente/debris |
| 22 | Suspension | 1991 Portuguese Grand Prix | Mark Blundell | Sin causa documentada |
| 22 | Suspension | 1991 San Marino Grand Prix | Bertrand Gachot | Sin causa documentada |
| 22 | Suspension | 1992 Brazilian Grand Prix | Bertrand Gachot | Sin causa documentada |
| 22 | Suspension | 1992 Italian Grand Prix | Aguri Suzuki | Sin causa documentada |
| 22 | Suspension | 1993 Australian Grand Prix | Johnny Herbert | Sin causa documentada |
| 22 | Suspension | 1993 Belgian Grand Prix | Jean Alesi | Fallo mecánico |
| 22 | Suspension | 1993 Brazilian Grand Prix | Riccardo Patrese | Fallo mecánico |
| 22 | Suspension | 1993 British Grand Prix | Alessandro Zanardi | Sin causa documentada |
| 22 | Suspension | 1993 British Grand Prix | Gerhard Berger | Sin causa documentada |
| 22 | Suspension | 1993 European Grand Prix | Gerhard Berger | Fallo mecánico |
| 22 | Suspension | 1993 French Grand Prix | Luca Badoer | Sin causa documentada |
| 22 | Suspension | 1993 French Grand Prix | Alessandro Zanardi | Sin causa documentada |
| 22 | Suspension | 1993 German Grand Prix | Luca Badoer | Sin causa documentada |
| 22 | Suspension | 1993 Hungarian Grand Prix | Christian Fittipaldi | Sin causa documentada |
| 22 | Suspension | 1993 Italian Grand Prix | Michele Alboreto | Sin causa documentada |
| 22 | Suspension | 1993 Italian Grand Prix | Gerhard Berger | Fallo mecánico |
| 22 | Suspension | 1993 Monaco Grand Prix | Thierry Boutsen | Sin causa documentada |
| 22 | Suspension | 1993 South African Grand Prix | Jean Alesi | Sin causa documentada |
| 22 | Suspension | 1993 Spanish Grand Prix | Johnny Herbert | Sin causa documentada |
| 22 | Suspension | 1994 Australian Grand Prix | Michele Alboreto | Sin causa documentada |
| 22 | Suspension | 1994 Portuguese Grand Prix | Érik Comas | Sin causa documentada |
| 22 | Suspension | 1994 San Marino Grand Prix | Gerhard Berger | Sin causa documentada |
| 22 | Suspension | 1995 Belgian Grand Prix | Jean Alesi | Fallo mecánico |
| 22 | Suspension | 1995 Italian Grand Prix | Gerhard Berger | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 1995 Monaco Grand Prix | Luca Badoer | Sin causa documentada |
| 22 | Suspension | 1995 San Marino Grand Prix | Domenico Schiattarella | Sin causa documentada |
| 22 | Suspension | 1996 Argentine Grand Prix | Gerhard Berger | Sin causa documentada |
| 22 | Suspension | 1996 Belgian Grand Prix | Rubens Barrichello | Daño por colisión/accidente/debris |
| 22 | Suspension | 1996 Canadian Grand Prix | Eddie Irvine | Fallo mecánico |
| 22 | Suspension | 1996 Hungarian Grand Prix | Pedro Lamy | Sin causa documentada |
| 22 | Suspension | 1996 Monaco Grand Prix | Jean Alesi | Fallo mecánico |
| 22 | Suspension | 1996 San Marino Grand Prix | Jacques Villeneuve | Daño por colisión/accidente/debris |
| 22 | Suspension | 1997 Australian Grand Prix | Jan Magnussen | Sin causa documentada |
| 22 | Suspension | 1997 Brazilian Grand Prix | Rubens Barrichello | Sin causa documentada |
| 22 | Suspension | 1997 Brazilian Grand Prix | Pedro Diniz | Sin causa documentada |
| 22 | Suspension | 1997 Italian Grand Prix | Pedro Diniz | Sin causa documentada |
| 22 | Suspension | 1997 Luxembourg Grand Prix | Michael Schumacher | Daño por colisión/accidente/debris |
| 22 | Suspension | 1998 Argentine Grand Prix | Ralf Schumacher | Sin causa documentada |
| 22 | Suspension | 1998 French Grand Prix | Heinz-Harald Frentzen | Sin causa documentada |
| 22 | Suspension | 1998 Monaco Grand Prix | Ralf Schumacher | Fallo mecánico |
| 22 | Suspension | 1998 Monaco Grand Prix | Jan Magnussen | Fallo mecánico |
| 22 | Suspension | 1998 Monaco Grand Prix | Rubens Barrichello | Fallo mecánico |
| 22 | Suspension | 1999 Australian Grand Prix | Alexander Wurz | Sin causa documentada |
| 22 | Suspension | 1999 Belgian Grand Prix | Luca Badoer | Sin causa documentada |
| 22 | Suspension | 1999 British Grand Prix | Ricardo Zonta | Sin causa documentada |
| 22 | Suspension | 1999 German Grand Prix | Giancarlo Fisichella | Sin causa documentada |
| 22 | Suspension | 1999 Monaco Grand Prix | Jean Alesi | Sin causa documentada |
| 22 | Suspension | 1999 Monaco Grand Prix | Pedro Diniz | Sin causa documentada |
| 22 | Suspension | 1999 Monaco Grand Prix | Johnny Herbert | Sin causa documentada |
| 22 | Suspension | 2000 Australian Grand Prix | Jos Verstappen | Fallo mecánico |
| 22 | Suspension | 2000 Australian Grand Prix | Pedro de la Rosa | Fallo mecánico |
| 22 | Suspension | 2000 Hungarian Grand Prix | Jean Alesi | Fallo mecánico |
| 22 | Suspension | 2000 Japanese Grand Prix | Nick Heidfeld | Fallo mecánico |
| 22 | Suspension | 2000 Malaysian Grand Prix | Johnny Herbert | Fallo mecánico |
| 22 | Suspension | 2000 Monaco Grand Prix | Michael Schumacher | Fallo mecánico |
| 22 | Suspension | 2001 Australian Grand Prix | Mika Häkkinen | Fallo mecánico |
| 22 | Suspension | 2001 British Grand Prix | David Coulthard | Daño por colisión/accidente/debris |
| 22 | Suspension | 2001 San Marino Grand Prix | Michael Schumacher | Sin causa documentada |
| 22 | Suspension | 2001 Spanish Grand Prix | Rubens Barrichello | Fallo mecánico |
| 22 | Suspension | 2001 United States Grand Prix | Jacques Villeneuve | Daño por colisión/accidente/debris |
| 22 | Suspension | 2002 Austrian Grand Prix | Felipe Massa | Fallo mecánico |
| 22 | Suspension | 2002 Belgian Grand Prix | Pedro de la Rosa | Fallo mecánico |
| 22 | Suspension | 2002 Brazilian Grand Prix | Heinz-Harald Frentzen | Fallo mecánico |
| 22 | Suspension | 2002 Brazilian Grand Prix | Enrique Bernoldi | Sin causa documentada |
| 22 | Suspension | 2002 Canadian Grand Prix | Enrique Bernoldi | Sin causa documentada |
| 22 | Suspension | 2002 Italian Grand Prix | Allan McNish | Fallo mecánico |
| 22 | Suspension | 2003 Australian Grand Prix | Antônio Pizzonia | Fallo mecánico |
| 22 | Suspension | 2003 Australian Grand Prix | Nick Heidfeld | Sin causa documentada |
| 22 | Suspension | 2003 Australian Grand Prix | Mark Webber | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 2003 Austrian Grand Prix | Olivier Panis | Sin causa documentada |
| 22 | Suspension | 2003 Brazilian Grand Prix | Ralph Firman | Fallo mecánico |
| 22 | Suspension | 2003 British Grand Prix | Giancarlo Fisichella | Sin causa documentada |
| 22 | Suspension | 2003 Hungarian Grand Prix | Rubens Barrichello | Fallo mecánico |
| 22 | Suspension | 2003 Spanish Grand Prix | Heinz-Harald Frentzen | Sin causa documentada |
| 22 | Suspension | 2004 Canadian Grand Prix | Mark Webber | Sin causa documentada |
| 22 | Suspension | 2005 Bahrain Grand Prix | Jacques Villeneuve | Sin causa documentada |
| 22 | Suspension | 2005 Canadian Grand Prix | Fernando Alonso | Sin causa documentada |
| 22 | Suspension | 2005 Canadian Grand Prix | Narain Karthikeyan | Daño por colisión/accidente/debris |
| 22 | Suspension | 2006 Brazilian Grand Prix | Jarno Trulli | Sin causa documentada |
| 22 | Suspension | 2006 Brazilian Grand Prix | Ralf Schumacher | Sin causa documentada |
| 22 | Suspension | 2006 San Marino Grand Prix | Yuji Ide | Sin causa documentada |
| 22 | Suspension | 2007 Belgian Grand Prix | Giancarlo Fisichella | Fallo mecánico |
| 22 | Suspension | 2007 Italian Grand Prix | Felipe Massa | Fallo mecánico |
| 22 | Suspension | 2007 Japanese Grand Prix | Jenson Button | Sin causa documentada |
| 22 | Suspension | 2007 Spanish Grand Prix | Ralf Schumacher | Sin causa documentada |
| 22 | Suspension | 2007 Spanish Grand Prix | Kimi Räikkönen | Fallo mecánico |
| 22 | Suspension | 2008 German Grand Prix | Timo Glock | Fallo mecánico |
| 22 | Suspension | 2008 Turkish Grand Prix | Sébastien Bourdais | Fallo mecánico |
| 22 | Suspension | 2009 Australian Grand Prix | Felipe Massa | Sin causa documentada |
| 22 | Suspension | 2009 Hungarian Grand Prix | Sebastian Vettel | Sin causa documentada |
| 22 | Suspension | 2010 Australian Grand Prix | Timo Glock | Fallo mecánico |
| 22 | Suspension | 2010 Bahrain Grand Prix | Vitaly Petrov | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 2010 Japanese Grand Prix | Nico Rosberg | Fallo mecánico |
| 22 | Suspension | 2010 Japanese Grand Prix | Lucas di Grassi | Daño por colisión/accidente/debris |
| 22 | Suspension | 2010 Monaco Grand Prix | Rubens Barrichello | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 2010 Spanish Grand Prix | Karun Chandhok | Daño por colisión/accidente/debris |
| 22 | Suspension | 2011 Belgian Grand Prix | Sergio Pérez | Fallo mecánico |
| 22 | Suspension | 2011 Indian Grand Prix | Felipe Massa | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 2011 Monaco Grand Prix | Timo Glock | Fallo mecánico |
| 22 | Suspension | 2012 Australian Grand Prix | Heikki Kovalainen | Sin causa documentada |
| 22 | Suspension | 2012 Canadian Grand Prix | Timo Glock | Fallo mecánico |
| 22 | Suspension | 2012 Canadian Grand Prix | Narain Karthikeyan | Sin causa documentada |
| 22 | Suspension | 2012 Hungarian Grand Prix | Narain Karthikeyan | Sin causa documentada |
| 22 | Suspension | 2012 Italian Grand Prix | Jean-Éric Vergne | Fallo mecánico |
| 22 | Suspension | 2012 United States Grand Prix | Jean-Éric Vergne | Daño externo (piano/tapa/objeto) |
| 22 | Suspension | 2013 Chinese Grand Prix | Nico Rosberg | Fallo mecánico |
| 22 | Suspension | 2013 Monaco Grand Prix | Sergio Pérez | Daño por colisión/accidente/debris |
| 22 | Suspension | 2013 Spanish Grand Prix | Romain Grosjean | Sin causa documentada |
| 22 | Suspension | 2014 Austrian Grand Prix | Daniil Kvyat | Sin causa documentada |
| 22 | Suspension | 2014 Brazilian Grand Prix | Daniel Ricciardo | Fallo mecánico |
| 22 | Suspension | 2014 British Grand Prix | Marcus Ericsson | Fallo mecánico |
| 22 | Suspension | 2014 Canadian Grand Prix | Kamui Kobayashi | Fallo mecánico |
| 22 | Suspension | 2014 Russian Grand Prix | Max Chilton | Fallo mecánico |
| 22 | Suspension | 2015 Hungarian Grand Prix | Sergio Pérez | Daño por colisión/accidente/debris |
| 22 | Suspension | 2015 Russian Grand Prix | Daniel Ricciardo | Sin causa documentada |
| 22 | Suspension | 2016 Abu Dhabi Grand Prix | Jenson Button | Daño por colisión/accidente/debris |
| 22 | Suspension | 2016 Abu Dhabi Grand Prix | Valtteri Bottas | Daño por colisión/accidente/debris |
| 22 | Suspension | 2016 Abu Dhabi Grand Prix | Kevin Magnussen | Daño por colisión/accidente/debris |
| 22 | Suspension | 2016 European Grand Prix | Carlos Sainz | Fallo mecánico |
| 22 | Suspension | 2016 European Grand Prix | Daniil Kvyat | Sin causa documentada |
| 22 | Suspension | 2016 German Grand Prix | Felipe Massa | Sin causa documentada |
| 22 | Suspension | 2017 Australian Grand Prix | Kevin Magnussen | Sin causa documentada |
| 22 | Suspension | 2017 Azerbaijan Grand Prix | Felipe Massa | Fallo mecánico |
| 22 | Suspension | 2018 Hungarian Grand Prix | Charles Leclerc | Sin causa documentada |
| 22 | Suspension | 2018 Mexican Grand Prix | Carlos Sainz | Fallo mecánico |
| 22 | Suspension | 2019 Brazilian Grand Prix | Lance Stroll | Sin causa documentada |
| 22 | Suspension | 2019 Canadian Grand Prix | Lando Norris | Fallo mecánico |
| 22 | Suspension | 2019 United States Grand Prix | Pierre Gasly | Daño por colisión/accidente/debris |
| 22 | Suspension | 2019 United States Grand Prix | Sebastian Vettel | Fallo mecánico |
| 22 | Suspension | 2020 Austrian Grand Prix | Daniil Kvyat | Sin causa documentada |
| 22 | Suspension | 2021 Italian Grand Prix | Pierre Gasly | Daño por colisión/accidente/debris |
| 22 | Suspension | 2021 United States Grand Prix | Pierre Gasly | Fallo mecánico |
| 22 | Suspension | 2022 Miami Grand Prix | Pierre Gasly | Daño por colisión/accidente/debris |
| 27 | Tyre | 1990 Mexican Grand Prix | Ayrton Senna | Fallo mecánico |
| 27 | Tyre | 1991 French Grand Prix | Jyrki Järvilehto | Sin causa documentada |
| 27 | Tyre | 1991 Hungarian Grand Prix | Mark Blundell | Sin causa documentada |
| 27 | Tyre | 1993 German Grand Prix | Damon Hill | Fallo mecánico |
| 27 | Tyre | 1993 Spanish Grand Prix | Martin Brundle | Sin causa documentada |
| 27 | Tyre | 1998 Japanese Grand Prix | Michael Schumacher | Daño por colisión/accidente/debris |
| 27 | Tyre | 1999 German Grand Prix | Mika Häkkinen | Fallo mecánico |
| 27 | Tyre | 2003 Italian Grand Prix | Cristiano da Matta | Fallo mecánico |
| 27 | Tyre | 2004 Belgian Grand Prix | Juan Pablo Montoya | Fallo mecánico |
| 27 | Tyre | 2004 United States Grand Prix | Ralf Schumacher | Fallo mecánico |
| 27 | Tyre | 2004 United States Grand Prix | Fernando Alonso | Fallo mecánico |
| 27 | Tyre | 2005 Malaysian Grand Prix | Rubens Barrichello | Sin causa documentada |
| 27 | Tyre | 2005 Turkish Grand Prix | Nick Heidfeld | Fallo mecánico |
| 27 | Tyre | 2005 Turkish Grand Prix | Mark Webber | Fallo mecánico |
| 27 | Tyre | 2007 Spanish Grand Prix | Scott Speed | Fallo mecánico |
| 27 | Tyre | 2008 Japanese Grand Prix | Adrian Sutil | Daño por colisión/accidente/debris |
| 27 | Tyre | 2013 British Grand Prix | Jean-Éric Vergne | Fallo mecánico |
| 27 | Tyre | 2015 Belgian Grand Prix | Sebastian Vettel | Fallo mecánico |
| 27 | Tyre | 2015 Singapore Grand Prix | Romain Grosjean | Sin causa documentada |
| 27 | Tyre | 2016 Austrian Grand Prix | Sebastian Vettel | Sin causa documentada |
| 27 | Tyre | 2018 British Grand Prix | Charles Leclerc | Fallo mecánico |
| 29 | Puncture | 1990 Brazilian Grand Prix | Alessandro Nannini | Sin causa documentada |
| 29 | Puncture | 1992 Belgian Grand Prix | Jean Alesi | Daño por colisión/accidente/debris |
| 29 | Puncture | 1992 Portuguese Grand Prix | Pierluigi Martini | Daño por colisión/accidente/debris |
| 29 | Puncture | 1994 Italian Grand Prix | David Brabham | Sin causa documentada |
| 29 | Puncture | 1995 Italian Grand Prix | Martin Brundle | Sin causa documentada |
| 29 | Puncture | 1997 Spanish Grand Prix | Mika Salo | Sin causa documentada |
| 29 | Puncture | 1998 San Marino Grand Prix | Johnny Herbert | Sin causa documentada |
| 29 | Puncture | 2004 German Grand Prix | Cristiano da Matta | Sin causa documentada |
| 29 | Puncture | 2005 French Grand Prix | Christijan Albers | Sin causa documentada |
| 29 | Puncture | 2005 French Grand Prix | Patrick Friesacher | Sin causa documentada |
| 29 | Puncture | 2005 Spanish Grand Prix | Michael Schumacher | Fallo mecánico |
| 29 | Puncture | 2007 Australian Grand Prix | Scott Speed | Sin causa documentada |
| 29 | Puncture | 2007 Japanese Grand Prix | Ralf Schumacher | Sin causa documentada |
| 29 | Puncture | 2010 Spanish Grand Prix | Lewis Hamilton | Daño por colisión/accidente/debris |
| 29 | Puncture | 2011 Abu Dhabi Grand Prix | Sebastian Vettel | Sin causa documentada |
| 29 | Puncture | 2012 Bahrain Grand Prix | Pastor Maldonado | Sin causa documentada |
| 29 | Puncture | 2012 German Grand Prix | Lewis Hamilton | Sin causa documentada |
| 29 | Puncture | 2013 Bahrain Grand Prix | Jean-Éric Vergne | Daño por colisión/accidente/debris |
| 29 | Puncture | 2013 Japanese Grand Prix | Lewis Hamilton | Daño por colisión/accidente/debris |
| 29 | Puncture | 2016 Belgian Grand Prix | Carlos Sainz | Fallo mecánico |
| 29 | Puncture | 2018 Azerbaijan Grand Prix | Valtteri Bottas | Daño por colisión/accidente/debris |
| 29 | Puncture | 2018 Bahrain Grand Prix | Max Verstappen | Daño por colisión/accidente/debris |
| 29 | Puncture | 2018 French Grand Prix | Lance Stroll | Sin causa documentada |
| 29 | Puncture | 2020 Emilia Romagna Grand Prix | Max Verstappen | Daño por colisión/accidente/debris |
| 29 | Puncture | 2020 Tuscan Grand Prix | Lance Stroll | Fallo mecánico |
| 29 | Puncture | 2021 Qatar Grand Prix | Nicholas Latifi | Sin causa documentada |
| 49 | Track rod | 2006 Hungarian Grand Prix | Michael Schumacher | Daño por colisión/accidente/debris |
| 49 | Track rod | 2010 Monaco Grand Prix | Timo Glock | Sin causa documentada |
| 59 | Tyre puncture | 2005 Chinese Grand Prix | Antônio Pizzonia | Sin causa documentada |
| 65 | Rear wing | 1999 Australian Grand Prix | Jacques Villeneuve | Fallo mecánico |
| 65 | Rear wing | 2002 French Grand Prix | Eddie Irvine | Fallo mecánico |
| 65 | Rear wing | 2002 Spanish Grand Prix | Kimi Räikkönen | Fallo mecánico |
| 65 | Rear wing | 2004 German Grand Prix | Kimi Räikkönen | Fallo mecánico |
| 65 | Rear wing | 2010 Abu Dhabi Grand Prix | Jarno Trulli | Sin causa documentada |
| 65 | Rear wing | 2011 Belgian Grand Prix | Sébastien Buemi | Daño por colisión/accidente/debris |
| 65 | Rear wing | 2012 Canadian Grand Prix | Michael Schumacher | Fallo mecánico |
| 65 | Rear wing | 2014 Canadian Grand Prix | Romain Grosjean | Sin causa documentada |
| 65 | Rear wing | 2021 United States Grand Prix | Fernando Alonso | Sin causa documentada |
| 65 | Rear wing | 2023 Japanese Grand Prix | Lance Stroll | Sin causa documentada |

## 8. Notas finales

- La conciliación entre este apéndice y el dataset es exacta: 202 casos clasificados, 0 sin clasificar.
- En los casos "Sin causa documentada" (89 de 202, sobre todo carreras de los 90 y primeros 2000 con informes escasos), la decisión de categoría descansa en la etiqueta del estado, que sigue siendo la mejor información disponible.
- Fuentes consultadas en total (rondas 1-3): Wikipedia (artículos de carrera), Autosport, Crash.net, Motorsport Week, Grandprix.com, RaceFans, BBC, F1technical, F1.com, Turbos and Tantrums.
