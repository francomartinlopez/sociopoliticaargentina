# Fuentes y faltantes · datos/congreso

Actualizado: 2026-10-30. Cada número de `votaciones.json` y `ejecutivo.json` lleva su URL al lado. Este archivo resume de dónde salió todo y qué falta.

## Fuentes usadas

**Oficiales**
- Senado, prensa: https://www.senado.gob.ar/prensa/23921/noticias (74 pliegos, 04/06/2026) · https://www.senado.gob.ar/prensa/24088/noticias (29 pliegos, 16/07/2026)
- HCDN, actas de votación: https://votaciones.diputados.gob.ar/pdf/acta/5672. La herramienta bloqueó el resto del sitio, así que no se pudieron leer otras actas.
- **Base Infoleg de Normativa Nacional** (Ministerio de Justicia, datos.jus.gob.ar, dataset d9a963ea-8b1d-4ca3-9dd9-07a4773e8c23, recurso bf0ec116-ad4e-4572-a476-e57167a84403, act. 05/10/2026): de ahí sale la serie mensual de DNU firmados. Detalle en la sección «DNU firmados por mes» más abajo.
- argentina.gob.ar/normativa (`/normativa/nacional/norma-<id>/texto`): textos completos de los decretos, usados para validar la clasificación de Infoleg. El Boletín Oficial y servicios.infoleg.gob.ar siguen bloqueados.

**Observatorios y verificadores**
- ODCL, Universidad Austral: informes de sep. 2024 y oct. 2025 y comunicado de feb. 2026, con conteos anuales de DNU, la lista de DNU rechazados y las leyes vetadas e insistidas en 2025.
- Chequeado: ranking de DNU (base SAIJ, act. 30/09/2025), lista de vetos (act. 12/09/2025), ranking de vetos (act. 15/09/2025) y notas de sesiones.
- ACIJ, «De la excepción a la regla» (DNU 2011–2024), consultado a través de Hoy Día (07/10/2025). No se encontró el PDF original.
- Dir. de Información Parlamentaria de HCDN (vía La Nación, 30/08/2024) y Noticias Argentinas (24/08/2025): vetos e insistencias históricas.

**Prensa (cruce de al menos dos medios por votación cuando fue posible)**
La Capital, Los Andes, El Economista, Ámbito, Chequeado, Noticias NQN, Diario de Cuyo, Tiempo de San Juan, BAE Negocios, Canal 26, C5N, La Nación, Infobae, La Gaceta, Palabras del Derecho, Al Día Argentina (Microjuris), El Ancasti, Memo, Bloomberg Línea, iProfesional, Parlamentario, Diario Panorama, Primera Edición, ANBariloche, Aire de Santa Fe, A24, MDZ, Hoy Día, Tiempo Argentino y otros. Las URL exactas están en cada registro.

## Correcciones al index.html actual
1. **Propiedad Privada:** Diputados la aprobó el 21/10/2026 con 124-119-6, con cambios (restituye la Ley de Tierras Rurales 26.737), y vuelve al Senado. La nota «Diputados todavía no la trató» quedó vieja.
2. **DNU rechazados por ambas cámaras:** no es solo el 656/2024. El **DNU 340/2025** (marina mercante y huelga) también cayó: Diputados lo rechazó el 06/08/2025 y el Senado el 21/08/2025, con 55 votos por el rechazo.
3. **Financiamiento universitario 2024:** la insistencia en Diputados fue 160-84-5 en las dos fuentes, no 160-85.
4. **Propiedad Privada en el Senado:** las notas fechan la sesión el jueves 6/8/2026, no el 7/8; las crónicas se publicaron en la madrugada del 7.

## Discrepancias registradas (detalle en el campo `discrepancias`)
- Paquete fiscal en Diputados (28/06/2024): Chequeado da 144-108-3 en general; Diario Panorama da 136-116-3, que según Chequeado corresponde a Ganancias.
- Emergencia en discapacidad en Diputados: 148-71-3 (El Ancasti, Memo), 143 (ANBariloche) o 149 (Los Andes).
- Emergencia en discapacidad en el Senado: 56-0 (BAE, Microjuris) o 55 (Noticias NQN).
- Garrahan en el Senado (sanción): 62-8 (C5N, Blog del Contador, Primera Edición) o 60-8 (Ámbito).
- Insistencia universitaria en Diputados (2025): 174-67-2 (El Economista, epígrafe de Los Andes) o 175 (cuerpo de la nota de Los Andes).
- Mercosur–UE en el Senado: 69-3. Forbes suma 3 abstenciones, lo que da 75 votos para 72 bancas: es imposible.
- Bloque de pliegos del 27/08/2026: 66 (Infobae, La Gaceta) o 67 votos (Palabras del Derecho).
- Número del DNU de la SIDE: 656/2024. Algunos medios escribieron 256 o 565 por error.
- Senado 656/2024: Palabras del Derecho invierte las etiquetas; tres medios coinciden en 49 por el rechazo y 11 a favor del decreto.
- DNU de A. Fernández: 177 (Chequeado) o 179 (ODCL). Vetos de A. Fernández: 13 (Chequeado) o 12 (DIP-HCDN). DNU de CFK en 2007–2015: 78 (Chequeado) u 81 (ODCL). DNU de Macri: 71, aunque Chequeado escribe 78 en un párrafo.
- Fecha de publicación del veto 534/2025: 04/08/2025 (Chequeado) o 06/08/2025 (Microjuris).

## Faltantes
- **DNU firmados en oct. 2026:** quedan fuera del corte de la Base Infoleg (último BO cargado: 30/09/2026). El DNU 1157/2026 es de ese mes.
- **Total de DNU de 2026:** no hay un conteo publicado para cruzarlo. La Base Infoleg, ya validada, da 29 entre enero y septiembre (por fecha de firma).
- **DNU validados o rechazados:** solo están los casos documentados (70/2023, 656/2024, 179/2025 y 340/2025). No hay un conteo exhaustivo de la Bicameral ni de las cámaras; puede haber otras validaciones de una sola cámara que no se encontraron.
- **Votos de Diputados sobre el DNU 340/2025:** no se publicaron. Del Senado solo se conocen los 55 votos por el rechazo.
- **Senado y DNU 179/2025 (FMI):** no se encontró votación.
- **Vetos de 2026:** no se encontró ninguno, pero tampoco una fuente que confirme cero; por eso van como null.
- **Insistencia del ATN en Diputados:** no se encontró votación. El ODCL lo cuenta como no insistido.
- **Bahía Blanca:** la insistencia del Senado (10/07/2025, 51 afirmativos) tiene una sola fuente.
- **Pliegos de sep. y oct. 2026:** no se encontraron sesiones. Tampoco el detalle de los 7 pliegos que faltan para llegar a los 177 que informa La Gaceta (74 + 29 + 67 = 170).
- **Abstenciones sin publicar:** Senado en Ley Bases (12/06/2024) y paquete fiscal (13/06/2024); Penal Juvenil en Diputados (0 implícito por el conteo de ausentes); Mercosur–UE y Propiedad Privada en el Senado.
- **Ausentes:** solo se cargaron donde una fuente los publica.
- **Eliminación de las PASO 2027:** no se votó. Al 21/10/2026 sigue en el Senado sin dictamen.

## DNU firmados por mes (Base Infoleg) · agregado 2026-10-25
- **Fuente:** Base Infoleg de Normativa Nacional (ZIP del 05/10/2026; CSV generado el 01/10/2026). **Corte:** último Boletín Oficial cargado el 30/09/2026 y última fecha de sanción el 29/09/2026. Septiembre está completo: 294 decretos cargados ese mes. Octubre de 2026 queda en null.
- **Criterio:** `tipo_norma = "Decreto"` y `clase_norma = "DNU"` (la base no tiene un tipo «Decreto de Necesidad y Urgencia»: el marcador va en `clase_norma`), firmados desde el 10/12/2023. Se cuenta por **mes de firma** (`fecha_sancion`) → `serie_mensual[].dnu_firmados`. La misma lista contada por mes de publicación en el BO está en `dnu_publicados_mensual`.
- **Validación con el texto completo** (argentina.gob.ar/normativa): se leyeron los 116 DNU marcados y los 3.229 decretos no marcados del período. Se buscó la fórmula «en acuerdo general de ministros decreta», la invocación del art. 99 inc. 3 y la cita de la Ley 26.122. Correcciones:
  - **se excluye el 44/2026** (nomenclatura del Mercosur): Infoleg lo marca DNU, pero se dicta por el art. 99 inc. 1 y el art. 664 del Código Aduanero, sin acuerdo de ministros;
  - **se agregan el 493/2025** (marco regulatorio de agua potable de AySA), **el 521/2025** (ejercicios militares) y **el 867/2026** (modificación del Presupuesto 2026): son DNU con la fórmula completa, pero Infoleg no los marca;
  - el 302/2024 es DNU aunque el texto escribe «MNISTROS»;
  - el 254/2024 lleva acuerdo de ministros, pero es una promulgación parcial (art. 80 CN): no se cuenta;
  - el 28/2023 figura con sanción el 13/11/2023, cosa imposible por la numeración (la serie 2023 se reinició el 10/12). Se cuenta en dic. 2023 por su publicación del 13/12.
- **Casos de control:** 70/2023, 656/2024, 179/2025, 340/2025 y 681/2026 son DNU. El 681/2025 no lo es: es la promulgación de la Ley 27.793.
- **Totales por año de firma:** 2023 (desde el 10/12): 7 · 2024: 47 · 2025: 35 · 2026 (ene–sep): 29. **Por año de publicación:** 7 · 47 · 33 · 31. La diferencia entre los dos criterios son el 941 y el 942/2025, firmados el 31/12/2025 y publicados el 02/01/2026.
- **Cruce con el ODCL (U. Austral):** coincide en 2023 (7), 2024 (47) y 2025 (35); en los cortes acumulados del 10/09/2024 (39), el 23/09/2024 (42) y el 08/07/2025 (76); y en el detalle de dic. 2025 a feb. 2026 (2, 8 y 1). Sin las correcciones, Infoleg daba 33 en 2025 y 9 en ene. 2026.
- **Cruce con Chequeado (base SAIJ):** la lista suma 48 al 12/11/2024, contra 46 de Chequeado, y 83 al 30/09/2025, contra 82. No se identificaron las normas que explican la diferencia.
- **En `ejecutivo.json`:** `serie_mensual[].dnu_firmados` y `dnu_firmados_detalle`, `meta.dnu_firmados_fuente`, `meta.granularidad.dnu_firmados`, `dnu_publicados_mensual` y `dnu_lista` (número, fecha de firma, fecha del BO, título, tema y URL de cada uno). El resto de los campos no se tocó.
- **Scripts:** `/home/claude/scripts/dnu_extract.py`, `dnu_scan_texts.py`, `dnu_verify.py`, `dnu_update.py` y `dnu_cum.py`.

## Corte del 30/10/2026
- **Nueva votación:** reforma de la Ley de Salud Mental (proyecto del Ejecutivo), media sanción del Senado el 29/10/2026 (votada en la madrugada del 30) con 42-21-0. Fuentes: Parlamentario (0 abstenciones), El Intransigente, Información Regional y Desarrollo Zonal. No hay lista nominal ni ausentes publicados. En la misma sesión se aprobaron el RIIR, el mercado voluntario de carbono y otros proyectos, sin votos publicados (no se cargan).
- **PASO 2027:** sigue sin dictamen en el Senado; el Gobierno postergó la comisión por falta de votos y el bloque PRO se opone (El Liberal, 18/10; La Nación, 30/10).
- **Presupuesto 2027:** el dictamen previsto para el 28/10 en Diputados no se firmó porque el PRO no acompañó; se habla del 18 o el 25/11 para la sesión (El Cronista, La Nación). No hubo votación.
- **DNU de octubre:** la Base Infoleg no se actualizó desde el 05/10/2026 (consultado el 30/10 en la API de datos.jus.gob.ar), así que octubre sigue en null. Se registró por prensa el DNU 1286/2026 (IOSFA/OSFA, BO 28/10/2026; Infobae y El Cronista) en `serie_mensual[2026-10].dnu_conocidos_prensa`, sin conteo exhaustivo.
- **Vetos 2026:** no se encontró ninguno nuevo.
