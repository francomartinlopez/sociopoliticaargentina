# Fuentes y faltantes · datos/afinidades

Actualizado: 2026-10-25. Este archivo cubre `senadores.json`. No toca `transferencias.json` ni otros archivos de la carpeta.

## Cómo se arma `senadores.json`
- `raw/*.txt`: el voto de cada senador en cada votación. Cada archivo tiene una cabecera con fecha, tema y totales oficiales, y declara un voto por defecto (`default=`); debajo van solo las excepciones (A afirmativo, N negativo, B abstención, X ausente). `raw/2623.txt` trae la nómina completa: nombre, provincia y bloque.
- `check.py` comprueba que cada archivo cubra a los 72 senadores y que los conteos coincidan con los totales oficiales. Hoy pasan todos.
- `build_senadores.py` genera el JSON. Corre con `python3 build_senadores.py`.
- La regla es la del sitio. El voto alineado vale 1, la abstención 0,5 y el voto contrario 0; las ausencias no cuentan. La provincia toma el promedio de sus 3 senadores. Afín es 66,7 % o más; opositora, 33,3 % o menos.
- También se calcula un índice alternativo, `*_solo_disputadas`. Deja afuera las votaciones casi unánimes (el ganador con 90 % o más de los votos emitidos): Mercosur–UE y los dos bloques de pliegos judiciales votados 64-0.

## Votaciones incluidas (postura del gobierno: afirmativa en todas)
| Fecha | Tema | Totales A-N-Ab-Aus | Fuente nominal |
|---|---|---|---|
| 26/12/2025 | Presupuesto 2026 (en general) | 46-25-1-0 | Tiempo de San Juan (lista uno por uno) + Elonce (negativos y abstención): coinciden |
| 26/12/2025 | Inocencia Fiscal (en general) | 43-26-?-3 | **Parcial.** Solo se conocen los ausentes: Andrada, Uñac y Vigo (Ámbito). Ninguno cuenta para el índice |
| 11/02/2026 | Modernización laboral, media sanción | 42-30-0-0 | Acta oficial 2623 |
| 26/02/2026 | Pliego de F. Iglesias (embajador ante la UE) | 38-31-1-2 | Acta oficial 2655 |
| 26/02/2026 | Mercosur–UE | 69-3-0-0 | Acta oficial 2656 |
| 26/02/2026 | Ley de Glaciares (en general) | 40-31-1-0 | Acta oficial 2657 |
| 27/02/2026 | Régimen Penal Juvenil (en general) | 44-27-1-0 | Acta oficial 2665 |
| 27/02/2026 | Modernización laboral: aceptación de cambios (sanción) | 42-28-2-0 | Acta oficial 2678 |
| 09/04/2026 | Pliego de C. L. Crexell (embajadora en Canadá) | 45-26-0-1 | Acta oficial 2686 |
| 14/05/2026 | Prórroga de Mahiques en Casación (PE-176/25) | 58-11-0-3 | Acta oficial 2691 |
| 04/06/2026 | Pliegos judiciales O.D. 29-41 | 64-0-0-8 | Acta oficial 2764 |
| 04/06/2026 | Pliego de M. J. Sosa (TOCF 3 La Plata) | 42-22-0-8 | Acta oficial 2765 |
| 04/06/2026 | Pliegos judiciales O.D. 43-89 | 64-0-0-8 | Acta oficial 2766 |
| 06-07/08/2026 | Propiedad Privada (en general) | 37-33-0-2 | Perfil + Elonce (listas coincidentes); totales confirmados por la prensa del Senado (prensa/24146) |
| 17/09/2026 | Inocencia Fiscal II (en general) | 44-23-?-? | **Parcial.** 9 votos individuales: Chaco (Perfil), Neuquén y Río Negro (LM Neuquén) |

Las actas oficiales están en `https://www.senado.gob.ar/votaciones/detalleActa/<n>`. La lista de actas de 2026 es `https://www.senado.gob.ar/votaciones/actas`.

## Datos verificados
- **Composición:** las 72 bancas son las mismas en todas las actas, de dic. 2025 a jun. 2026, sin reemplazos. Los bloques corresponden al acta 2623 (feb. 2026).
- **Cambios de bloque informados por la prensa** (van en `bloque_nota`): Rejal pasó de Justicialista a Justicia Social Federal; Perfil presenta a Schneider como LLA, aunque en el acta figura en la UCR; Elonce lista a Juez como PRO, aunque en el acta figura en LLA.
- **Fecha de la reforma laboral:** el acta oficial dice 11/02/2026 a la 01:21. La prensa habla del 12/02 porque la votación fue de madrugada.

## Excluidas y por qué
- **Votaciones en particular, mociones y trámites:** la moción de Recalde para volver a comisión (acta 2677), la habilitación sobre tablas y las designaciones internas. Las mociones de orden no son votaciones «en general».
- **Tratados técnicos y leyes sin postura oficial clara:** Austria, Francia y Singapur/Suiza/San Marino; armas de fuego (acta 2693, 14/05/2026); EAAF; reglamento; golpe de 1976. Ascensos de las FF.AA. y Autoridad de la Competencia (actas 2684 y 2685): no se abrieron.
- **Pliegos del 16/07/2026 (29) y del 27/08/2026 (66 o 67):** sin acta oficial publicada ni lista nominal de prensa.
- **Transferencia de la justicia de menores a CABA y reforma de biocombustibles (17/09/2026):** solo hay totales (44-21 para la transferencia), sin nominal y sin postura oficial confirmada.
- **DNU y vetos desde dic. 2025:** no se encontró ninguna votación del Senado sobre DNU ni vetos en el período (ver `datos/congreso/FUENTES.md`).

## Faltantes
- El sitio del Senado no publica actas posteriores al 04/06/2026, y las de 2025 no tienen URL accesible: la herramienta solo abre URL que aparecen en buscadores o páginas, y la shell recibe 403 de senado.gob.ar. Cuando se publiquen, completar Inocencia Fiscal, Inocencia Fiscal II, los pliegos de julio y agosto y cualquier sesión de sep.–oct. 2026.
- Inocencia Fiscal II: Letra P cita un tuit con 43-23 y el resto de los medios da 44-23.
- Inocencia Fiscal (dic. 2025): Ámbito ubica a Uñac en La Rioja, pero es senador por San Juan.

---

# transferencias.json

Actualizado: 2026-10-25. Esta sección cubre `transferencias.json`; lo de arriba (senadores) queda igual. Montos en millones de pesos corrientes. Cada bloque del JSON lleva `f`, `url` y `fecha`.

## Qué está completo
- **ATN por provincia, oct-2025 a sep-2026 (24 jurisdicciones), mes por mes.** Fuentes:
  - oct-2025: La Nación, 03/11/2025.
  - nov-2025: 0, según La Unión, 19/12/2025.
  - dic-2025: Chequeado, 18/12, y Primera Edición, 06/01/2026. El total de 76.000 coincide con El Destape.
  - ene-may-2026, en bloque: Infobae, 07/06/2026, con datos de Interior y del informe de JGM.
  - jun-2026: 0, derivado del acumulado de Politikon.
  - jul-2026: El Esquiú.
  - ago-2026: 0, según Noticias Chaco.
  - sep-2026: BAE Negocios, 16/10/2026.

  El acumulado ene-sep 2026 cierra exacto con Politikon Chaco (151.000 a agosto + 33.000 en septiembre = 184.000) y con los parciales de CEPA (corte al 14/09) y de la OPC (Misiones 25.000, Corrientes 19.000, Catamarca 18.500, Jujuy 13.500). Total de los 12 meses: 273.000.
- **Gasto total ejecutado 2025 por provincia:** Ministerio de Economía, Subsecretaría de Coordinación Fiscal Provincial, ejecución provisoria APNF del IV trimestre 2025 (argentina.gob.ar, archivo .xls, datos al 12/06/2026). Se incluye también el I semestre 2026 como referencia.
- **Población:** Censo 2022, resultados definitivos (suma 45.892.285, el total definitivo del INDEC). Tomada de Argentina en Datos y cruzada en 9 jurisdicciones con Infobae (21/11/2023).
- **Indicadores calculados:** ATN de 12 meses / gasto 2025 (%) y ATN por habitante.

## Qué falta
- **TNA (transferencias no automáticas corrientes + capital) por provincia, 12 meses: null en las 24.** No se pudo abrir ninguna fuente con la tabla completa:
  - repositorio DGSIAF/Presupuesto Abierto (dgsiaf-repo.mecon.gob.ar y presupuestoabierto.gob.ar, 403 desde la shell);
  - PDF de la OPC (`opc.gob.ar/download/52956`, error del sitio);
  - politikonchaco.com y PDF de zubancordoba.com (fuera de la lista permitida);
  - informes de Fundación Encuentro (los datos por provincia están en gráficos-imagen y el PDF está en Google Drive, bloqueado);
  - índice de informes de JGM (Google Sheets, bloqueado).

  La prensa publica solo las 3 primeras provincias de cada mes. Lo verificado quedó en `tna.datos_parciales`: montos mensuales de jun-sep 2026 para algunas provincias, participaciones ene-ago 2026 y componentes ene-sep 2026 de la OPC (cajas previsionales, infraestructura hídrica, subsidios eléctricos).
- **Totales nacionales de TNA (Politikon Chaco, etapa pagado):** jun 48.300, jul 98.611, ago 68.288, sep 159.975; ene-sep 966.463 (la serie suma exacto).
- **La Pampa:** la DNAP la excluye de la ejecución 2025 y 2026. Se usa el total de erogaciones de la Ley 3603 (presupuesto 2025, Adm. Central y Org. Descentralizados), que no es 1:1 con la APNF ejecutada del resto.

## Advertencias y discrepancias
- **Politikon incluye los ATN dentro de las TNA.** Para el indicador del sitio («no automáticas + ATN»), no sumarlos dos veces.
- **Tucumán:** la OPC (vía El Ancasti y Conclusión) habla de ATN -91% real en ene-sep 2026; Politikon no registra ATN para Tucumán en 2026. Se usa Politikon (0). Conviene revisarlo con el PDF de la OPC.
- **Chubut, dic-2025 (9.500):** solo en Primera Edición/Politikon. Las notas del 18-19/12 listan seis provincias porque el giro fue posterior.
- **ATN 2025:** 207.500 según Politikon/BAE; 209.000 según el informe de JGM (Infobae).
- **CABA:** en las TNA recibe montos grandes por la cautelar de la Corte por coparticipación (47% de las discrecionales de 2025). No son ATN.
- Montos nominales sin deflactar. El denominador (gasto 2025) no coincide con el período de las transferencias. Santiago del Estero informa su ejecución en etapa compromiso.

## Para completar
Bajar de Presupuesto Abierto el crédito pagado de las transferencias a gobiernos provinciales (inciso 5, corrientes y de capital) por provincia, de oct-2025 a sep-2026, o el anexo por provincia del informe de la OPC con datos a septiembre 2026. Con eso se llena `tna.total_12m_millones` y se calculan `discrecionales_pct_presupuesto` y `discrecionales_por_habitante_pesos`.

---

# Gobernadores

Actualizado: 2026-10-25. Esta sección cubre `gobernadores.json`; lo anterior (senadores y transferencias) queda igual. Cada hecho del JSON lleva su URL. El script que lo generó quedó fuera del repositorio; el JSON es el dato.

## Regla (lectura propia, también en `meta.regla`)
- **afin:** aliado electoral de LLA en 2025 (lista conjunta o acuerdo explícito), o respaldo público a la agenda del gobierno sin oponerse a sus leyes clave.
- **neutral:** acompaña algunas iniciativas y rechaza otras. Incluye a los dialoguistas, a los miembros de Provincias Unidas y a los peronistas que negocian votos.
- **opositora:** confronta abiertamente (Fuerza Patria o kirchnerismo, o quien encabeza la oposición), o sus legisladores votan en contra de todas las leyes clave.

Resultado: 6 afines, 12 neutrales y 6 opositoras.

## Fuentes principales
- **Pacto de Mayo (09/07/2024):** Los Andes (08/07/2024) y Bloomberg Línea. Firmaron 17 gobernadores y Jorge Macri. Faltaron Kicillof, Quintela, Melella, Insfrán, Ziliotto y Vidal; Vidal no fue por el clima y mandó un representante.
- **Reunión de Milei con 20 gobernadores (30/10/2025):** La Voz de San Justo. No fueron convocados Kicillof, Insfrán, Quintela ni Melella.
- **Alianzas de 2025:**
  - Escrutinio provisorio de la DINE (resultados.gob.ar, ya cargado en `datos/electoral/diputados-2025-generales.json`).
  - Los cuatro gobernadores aliados de LLA (Zdero, Frigerio, Cornejo y Poggi): El Economista, 24/04/2026.
  - Acuerdos de cada distrito: Letra P (Entre Ríos, Chaco), Sitio Andino y Los Andes (Mendoza), Canal 26 (CABA) y LPO (San Luis: sin lista propia y voto anunciado a LLA).
  - Provincias Unidas: Ámbito y Noticias NQN.
- **Votos de los senadores:** salen de `senadores.json` (Presupuesto 2026, actas 2623 y 2678 de la reforma laboral, Propiedad Privada) y llevan las mismas fuentes que allí.
- **2026:**
  - La Nación: Nueva York (11/03) y Provincias Unidas (29/09).
  - Perfil: comitiva a París (28/09), PASO (05/10) y sesión del DNU 70/23 (15/10).
  - El Economista: sesión del DNU 70/23 (15/10).
  - C5N: reuniones con Santilli (16/09).
  - Letra P: «acuerdómetro» (07/10).
  - BA Times: mapa de alianzas para 2027 (19/05).
- **Gobernadores en funciones verificados:**
  - Corrientes: Juan Pablo Valdés, electo el 31/08/2025 (Diario de Cuyo).
  - Santiago del Estero: Elías Suárez, electo el 26/10/2025 con más del 70% (La Nación); asumió el 10/12/2025 (Letra P).

## Casos dudosos (detalle en `meta.casos_dudosos`)
- **Afín por apoyo explícito, no por alianza de 2025:** San Juan (Orrego).
- **Neutrales cerca de afín:** Salta, Neuquén, Chubut, Jujuy y Corrientes.
- **Opositoras que podrían leerse neutrales:** Santiago del Estero (el gobernador tiene un tono moderado; la categoría se apoya sobre todo en el voto de sus senadores), La Pampa y Tierra del Fuego (dialogan con Santilli en 2026).
- **CABA:** afín por la lista conjunta de 2025, con tensión política por 2027.

## Discrepancias y faltantes
- **Formosa y La Rioja:** no se encontró un hecho con fuente posterior a junio de 2026. `ultima_novedad` es el último encontrado.
- **Comitiva a París:** las notas son previas al viaje (30/09–02/10/2026) y no se verificó quiénes viajaron finalmente. Perfil daba como dudosa la presencia de Llaryora.
- **Senadores de Santa Cruz (Movere):** la vinculación con Vidal se toma de La Nación (11/03/2026). Votaron en contra de la reforma laboral y de Propiedad Privada.
- **Tierra del Fuego:** la reunión Melella–Santilli prevista para el 17/09/2026 no está confirmada.
- **Sesión del DNU 70/23 (15/10/2026):** El Economista y Perfil difieren en algunos nombres. Para Misiones y Salta, ninguna de las dos aclara si los presentes sumaban al quórum opositor; Perfil dice que Biella y Outes «dieron quórum».
- **Partidos:** el nombre del partido de Poggi (Avanzar San Luis) no se verificó con una fuente específica. Letra P menciona el frente «Ahora San Luis» para mayo de 2025.

---

# transferencias.json · TNA por provincia (Presupuesto Abierto)

Actualizado: 2026-10-25. Esta sección completa los campos `tna` e `indicadores.discrecionales_*` de `transferencias.json` y reemplaza los apartados «Qué falta → TNA» y «Para completar» de la sección anterior, que quedan como registro. No se tocó ningún dato de ATN, presupuesto ni población.

## Fuente y método
- **Presupuesto Abierto** (Ministerio de Economía), visualización «¿Dónde se gasta?»: https://www.presupuestoabierto.gob.ar/sici/visualizacion-donde-se-gasta. Los datos se bajaron del endpoint público que usa la página, `POST https://www.presupuestoabierto.gob.ar/sici/rest-api/visualizaciones/donde-se-gasta/{ejercicio}/filter`, con el cuerpo `[{"column":"codigoInciso","value":5},{"column":"codigoPrincipal","value":7|8},{"column":"codigoParcial","value":1..9}]`. Devuelve crédito inicial, vigente, comprometido, devengado y **pagado** por ubicación geográfica. Las respuestas crudas, con la consulta incluida, están en `/home/claude/raw/presupuestoabierto/q/`.
- **TNA a la provincia** = crédito pagado de las partidas 5.7.1 a 5.7.5 (corrientes) y 5.8.1 a 5.8.5 (capital): Administración Pública Provincial, empresas públicas provinciales e instituciones de enseñanza provinciales. Las parciales 2 y 5 no tuvieron movimientos. Se **excluyen los municipios** (5.7.6 a 5.7.9 y 5.8.6 a 5.8.9): 17.244 millones en 2025 y 11.249 millones en 2026.
- **ATN:** mismo endpoint, filtrado por servicio 325 (Ministerio del Interior), programa 19 y actividad 21 «Aportes del Tesoro Nacional (ATN)». Los ATN están **dentro** de las TNA (partida 5.7.1), así que `discrecionales_*` ya los incluye y no se suman dos veces. El campo `tna.sin_atn_*` da el resto.
- **Período.** La fuente accesible solo da acumulados por ejercicio, sin apertura mensual. La base mensual (`credito-mensual-AAAA.zip` en dgsiaf-repo.mecon.gob.ar) sigue con 403, y la API `/api/v1/credito` pide un token personal que no se tramitó. Por eso:
  - `tna.total_12m_millones` = **año calendario 2025** (ejercicio cerrado, actualizado el 05/07/2026): son los últimos 12 meses completos por provincia;
  - `tna.acumulado_2026_millones` = del **1/1 al 23/10/2026** (última actualización del ejercicio 2026).
  
  La ventana oct-2025 a sep-2026 de los ATN no se puede armar para las TNA.
- **Indicadores** (en %, como `atn_pct_gasto`):
  - `discrecionales_pct_presupuesto` = TNA 2025 / gasto total ejecutado 2025 × 100. Numerador y denominador son del mismo año.
  - `discrecionales_por_habitante_pesos` = TNA 2025 / población del Censo 2022.
  - `discrecionales_2026_acum_*`: TNA del 1/1 al 23/10/2026 sobre el mismo gasto 2025 y por habitante. Es una referencia, no está anualizado.
  - La Pampa usa el gasto presupuestado 2025 (Ley 3603), igual que en el indicador de ATN.

## Cruces
- **Total 2025:** 2.490.134 millones contra 2.492.543 de Politikon Chaco (BAE Negocios, 05/01/2026). Diferencia: -0,10 %.
- **ATN 2025:** 207.500, igual que Politikon y BAE. El informe de JGM citado por Infobae da 209.000.
- **CABA 2025:** 47,1 % del total, en línea con el 47 % que informa Politikon.
- **ATN 2026:** 184.000 al 23/10, igual que Politikon ene-sep. Coincide en las 24 jurisdicciones con `atn.acumulado_2026_ene_sep_millones`: no hubo ATN entre el 1 y el 23 de octubre. El ATN 2025 de cada provincia también cubre lo cargado para oct-dic 2025.
- **Total 2026:** 1.010.883 al 23/10, contra 966.463 de Politikon a septiembre. La diferencia (44.420) serían los pagos de octubre, pero no se puede verificar.
- **Participaciones 2026** (Presupuesto Abierto al 23/10, contra Politikon ene-ago, que es otro período):

  | Jurisdicción | Presupuesto Abierto | Politikon |
  |---|---|---|
  | Buenos Aires | 20,1 % | 20,4 % |
  | CABA | 9,6 % | 11,7 % |
  | Entre Ríos | 7,4 % | 8,4 % |
  | Córdoba | 6,1 % | 6,8 % |
  | Santa Fe | 6,5 % | 6,6 % |
  | Río Negro | 0,6 % | 0,4 % |
  | Tierra del Fuego | 0,5 % | 0,4 % |
  | La Rioja | 0,3 % | 0,3 % |

  El orden y las magnitudes coinciden.
- **OPC / CEPA:** no se consiguió un total nacional de TNA de la OPC con la misma definición: su -49 % real incluye municipios. Los componentes de la OPC (cajas previsionales, infraestructura hídrica, subsidios eléctricos) siguen en `tna.datos_parciales`.

## Advertencias
- **Montos nominales** en millones de pesos corrientes, sin deflactar.
- **Períodos distintos.** Los ATN de 12 meses (oct-2025 a sep-2026) y las TNA de 2025 no cubren el mismo período: no se pueden sumar ni comparar directamente. El indicador `atn_pct_gasto` sigue igual.
- **CABA 2025** (1,17 billones, 8,5 % de su gasto): son casi todos pagos por la cautelar de coparticipación de la Corte Suprema, no un giro discrecional en sentido estricto. En 2026 baja al 9,6 % del total.
- **«No automática» no quiere decir «arbitraria».** Incluye financiamiento de cajas previsionales no transferidas (ANSES, subparcial 3003: 170.167 millones en 2026), educación y obras con destino fijado por convenio. Por eso La Pampa salta a 57.434 millones en 2026: la OPC registra 45.000 de caja previsional.
- **Ubicación geográfica:** es la que imputa el SIDIF. En estas partidas, Interprovincial, Nacional y No clasificado dieron 0.
- **Denominadores:** Santiago del Estero informa su gasto en etapa compromiso; La Pampa, presupuestado.

## Scripts
`/home/claude/scripts/pa_fetch.py` (descarga), `pa_summary.py` (resumen) y `tna_update.py` (escritura en el JSON).

---

# Corte del 30/10/2026
- **Senadores:** la reforma de Salud Mental (29/10/2026, 42-21-0, postura del gobierno afirmativa) no entra al índice porque no se publicó lista nominal. Diario Nuevo Día deduce los votos de Santa Cruz por pertenencia de bloque, no por votos informados: no se usa. Cargar cuando haya acta o lista de prensa.
- **Transferencias:** Presupuesto Abierto, consultado el 30/10/2026, sigue dando 184.000 millones de ATN pagados en 2026: no hubo giros de ATN en octubre hasta la última actualización de la fuente. Octubre no se carga hasta cerrar el mes.
- **Gobernadores:** no se encontraron hechos de la semana que cambien alguna categoría. Weretilneck (Río Negro) apoyó eliminar las PASO, según el título de El Destape (29/10), pero la nota no abrió.

---

## Corte del 06/11/2026 · Gobernadores
`gobernadores.json` tiene ahora `meta.actualizado` 2026-11-06. Hechos del 30/10 al 06/11/2026, más dos de septiembre que estaban pendientes de confirmación (Tierra del Fuego).

### Cambio de categoría (lectura propia)
- **Tierra del Fuego (Melella): de opositora a neutral.** Se confirmó la reunión con Santilli del 17/09/2026 (Diario Prensa, 17/09; Letra P, 18/09). Allí anunció que acompañará «en general» el Presupuesto 2027, con cambios en discapacidad y universidades, y el proyecto sobre Malvinas. Sigue en contra de eliminar las PASO. El 26/09 firmó con la Nación un anticipo financiero de hasta $45.000 millones (Letra P, 29/09; LPO, 16/10). Eso encaja en el criterio de neutral: acompaña algunas iniciativas y rechaza otras. La categoría anterior quedó en `categoria_anterior`.
- **Nuevo conteo:** 6 afines, 13 neutrales y 5 opositoras.

### Hechos cargados (sin cambio de categoría)
- **Río Negro (Weretilneck), 29/10:** adelantará las elecciones provinciales de 2027 y respaldó eliminar las PASO (Ámbito y Neuquén Post, 29/10). Sigue neutral: compitió contra LLA en 2025 y critica la apertura comercial. Se agregó a `casos_dudosos`.
- **Tucumán (Jaldo):** sigue rechazando la suspensión de las PASO (Los Andes, 02/11; Filo.news, 01/11).
- **Mendoza (Cornejo):** no definió el voto de sus senadores sobre las PASO y busca garantías sobre Petri (Los Andes, 02/11). La frase «peor es elegir mal» (29/10) se toma de una columna de Memo (30/10). Sigue afín.
- **Salta (Sáenz) y Misiones (Passalacqua):** condicionan su apoyo a las PASO (Los Andes, 02/11; Filo.news, 01/11).
- **Santa Fe (Pullaro):** Los Andes lo ubica a favor de suspender las PASO (02/11).
- **Buenos Aires (Kicillof):** el 30/10 la Corte aceptó la demanda por el fondo del transporte del interior y le dio 60 días a la Nación (El Tribuno e InfoRegión).
- **La Rioja (Quintela):** cruce con Milei por el RIGI (28/10; La Red 88.3 y Acero y Roca). Se cierra el faltante «sin hecho posterior a junio».
- **Catamarca (Jalil):** recibió a Milei en la inauguración de Rio Tinto (28/10; mismas fuentes).
- **Formosa (Insfrán):** discursos del 17/10 y del 04/11 contra Milei (El Destape). Se cierra el faltante «sin hecho posterior a junio».

### Pendientes
- **Formosa:** los dos hechos tienen una sola fuente (El Destape). Falta una segunda.
- **Mendoza:** la interpretación de Memo (Cornejo ofrecería votos por las PASO a cambio de que LLA no lleve candidato propio) es del columnista y no se cargó.
- **Senadores de Tierra del Fuego:** que el diputado Tita no diera quórum el 15/10 a cambio de los anticipos sale de fuentes sin nombre (LPO). Se usa solo para el dato del anticipo.
- **El Intransigente (29/10, Weretilneck)** y la nota de El Destape del corte anterior no abrieron. Se usaron Ámbito y Neuquén Post.

## Corte del 13/11/2026 · Gobernadores
`gobernadores.json` tiene ahora `meta.actualizado` 2026-11-13. Hechos del 07/11 al 13/11/2026 (WebSearch + WebFetch).

### Cambios de categoría
- **Ninguno.** Conteo sin cambios: 6 afines, 13 neutrales y 5 opositoras.

### Hechos cargados
- **Relevamiento de El Cronista sobre las PASO (12/11):** nueve gobernadores apoyan en público eliminarlas (Jalil, Figueroa, Zdero, Valdés, Torres, Orrego, Frigerio, Sadir y Pullaro); Vidal y Llaryora estarían «dispuestos a acompañar»; Cornejo, Sáenz y Passalacqua condicionan su apoyo y Jaldo lo rechaza. La cuenta oficial llega justo a 37 votos en el Senado. Se cargó como hecho en Catamarca, Chaco, Corrientes, San Juan, Jujuy, Santa Fe, Santa Cruz, Córdoba, Neuquén, Entre Ríos y Chubut. Es una sola fuente y es un relevamiento periodístico, no declaraciones de cada gobernador. Mendoza, Salta, Misiones y Tucumán no se tocaron: ya tenían la misma posición con fecha 02/11.
- **Neuquén (Figueroa), 09/11:** convocó por Decreto 1860/2026 a elecciones provinciales el 14/02/2027. Nadia Márquez (LLA) descartó un acuerdo y anticipó candidato propio; según Infobae (13/11), en LLA «no cayó bien». Fuentes: Ámbito (09/11), Letra P (09/11) e Infobae (13/11). Sigue neutral; se actualizó `casos_dudosos`.
- **PRO (Jorge Macri, Frigerio, Torres), 12/11:** Ritondo dijo que el bloque PRO acompañará la reforma política, pero que su postura depende de esos tres gobernadores (El Cronista, 12/11). El principio de acuerdo PRO–LLA por el Presupuesto 2027 incluye la coparticipación y un crédito de la CAF para la Ciudad y la baja del IVA del huevo que impulsó Frigerio (El Cronista, Perfil y Parlamentario, 12/11).
- **Río Negro (Weretilneck), 10/11:** acotó la elección provincial a la segunda quincena de mayo o junio de 2027 y repitió su apoyo a eliminar las PASO (Diario Río Negro, 10/11; Noti-Río, 12/11).

### Pendientes
- **Formosa:** sigue faltando una segunda fuente para los hechos del 17/10 y el 04/11; la búsqueda de la semana no la encontró.
- **Ritondo y los gobernadores del PRO:** la frase sale solo de El Cronista (12/11).
- **Sin novedades con fuente en la semana:** Buenos Aires, La Pampa, La Rioja, Formosa, Santiago del Estero, Tierra del Fuego, San Luis, Mendoza, Misiones, Salta y Tucumán. Kicillof, Insfrán y Quintela coincidieron en la recepción al papa León XIV (08/11, Infobae), pero no se cargó porque no es un hecho de la relación con la Nación.
- **MDZ (12/11, reacción del Senado a la presión por las PASO)** no abrió (error del sitio). Varias notas que el buscador mostraba como de noviembre de 2026 eran en realidad de 2024 (El Ancasti sobre Kicillof y Quintela; El Cronista sobre Jorge Macri) y se descartaron.

## Corte del 06/11/2026 · transferencias
- **Fuente:** Presupuesto Abierto, consultado el 06/11/2026. Según `rest-api/ejercicio/allForVisualizaciones`, el ejercicio 2026 se actualizó el 04/11/2026: octubre ya está cerrado en la fuente. Consultas reproducidas a mano con el mismo endpoint `donde-se-gasta/2026/filter` (los scripts de `/home/claude/scripts` no estaban); respuestas crudas en el scratchpad de la sesión, no en el repo.
- **ATN de octubre 2026 = 0 pagado en las 24 jurisdicciones.** Presupuesto Abierto da 197.500 millones pagados en 2026: 184.000 a septiembre más 13.500 (Chaco 4.000, Corrientes 3.500, Entre Ríos 3.000, Misiones 3.000). [Economis, 03/11/2026](https://economis.com.ar/?p=501235) informa que en octubre no hubo ATN pagados y que esos 13.500 se devengaron el 30/10 y se pagan en noviembre. Las dos fuentes cierran provincia por provincia. Los 13.500 quedan como nota en cada provincia y se cargan en nov-2026.
- **Ventana de 12 meses:** pasa a nov-2025 a oct-2026. Sale oct-2025 (13.000: Chaco 2.000, Entre Ríos 3.000, Neuquén 3.000, San Juan 2.000, Tucumán 3.000). Total: 273.000 → 260.000. Se recalcularon `atn_pct_gasto` y `atn_por_habitante_pesos` con los mismos denominadores.
- **TNA 2026:** se actualizó el acumulado al 04/11/2026: 1.097.403 millones (antes 1.010.883 al 23/10). Municipios excluidos: 14.664. Se recalcularon `participacion_2026_pct` y `discrecionales_2026_acum_*`. TNA 2025 e indicadores `discrecionales_*` sin cambios.
- **TNA nacional de octubre:** 89.259 millones pagados (-70,2 % real interanual), según Economis, que no nombra la fuente de la serie. Se cargó en `tna_mensual_2026_millones`. El acumulado ene-oct (1.055.722) es suma propia.
- **Pendientes:** confirmar el TNA de octubre con Politikon Chaco u otra fuente; cargar los 13.500 de ATN en nov-2026 cuando cierre el mes; la apertura mensual de las TNA sigue sin poder bajarse (dgsiaf-repo con 403, API con token).

## Corte del 06/11/2026 · senadores
- **Sin cambios en `senadores.json`:** no hubo votaciones en el Senado entre el 30/10 y el 06/11/2026; Parlamentario (06/11) llama «última sesión» a la del 29/10. La reforma de Salud Mental (29/10, 42-21-0) sigue sin lista nominal: elDiarioAR solo informa los bloques (a favor: LLA, PRO, UCR, Movimiento por Misiones, Primero los Salteños, Despierta Chubut, Provincias Unidas y Movere; en contra: Justicialismo, Independencia y Convicción Federal). Los votos no se deducen por bloque, así que no se incorpora. No se corrió `build_senadores.py` y el JSON no se tocó.
- **Pendientes:** acta o lista nominal de Salud Mental (senado.gob.ar sigue con 403 desde la shell, 06/11/2026); siguen los faltantes de arriba (Inocencia Fiscal I y II, pliegos de julio y agosto).

## Corte del 13/11/2026 · transferencias
- **Fuente:** Presupuesto Abierto, consultado el 13/11/2026. El ejercicio 2026 se actualizó el 11/11/2026 (`rest-api/ejercicio/allForVisualizaciones`). El ATN pagado de 2026 sigue en 197.500 millones: no hubo giros de ATN después de los 13.500 de comienzos de noviembre.
- **Distribución de los 13.500 (pagados a comienzos de noviembre):** Chaco 4.000, Corrientes 3.500, Entre Ríos 3.000 y Misiones 3.000. La confirman Politikon Chaco con datos de la DNAP ([Diario Río Negro/NA, 04/11](https://www.rionegro.com.ar/economia/cuatro-provincias-recibieron-atn-en-el-inicio-de-noviembre-como-se-distribuye-el-reparto-en-2026-4784202/); [El Argentino Diario, 05/11](https://elargentinodiario.com.ar/politica/05/11/2026/atn-noviembre-corrientes-chaco-entre-rios-misiones-politikon/)) y Nadin Argañaraz sobre Presupuesto Abierto ([Economis, 04/11](https://economis.com.ar/nacion-reactivo-los-atn-en-noviembre-y-giro-9-500-millones-a-misiones-corrientes-y-entre-rios/)). Coincide provincia por provincia con Presupuesto Abierto. Economis titula «9.500 millones a tres provincias» porque deja afuera a Chaco en el título; el cuerpo da los cuatro montos.
- **Cómo se cargó:** en cada provincia, `atn.nov_2026_parcial_millones` (valor al 11/11, con fuentes; 0 en las otras 20) y `atn.acumulado_2026_al_11_11_millones`; en el total nacional, `totales_nacionales.atn_2026_nov_parcial_millones`; en `meta`, `control_2026_11_13` y `actualizado` = 2026-11-13. **No cambian** la ventana de 12 meses (nov-2025 a oct-2026), `total_12m_millones` ni los indicadores: noviembre no cerró.
- **Pendientes:** al cierre de noviembre, pasar el mes a `por_mes_millones["2026-11"]` y mover la ventana a dic-2025 a nov-2026 (sale nov-2025, que es 0 en las 24; el total quedaría en 273.500 si no hay más giros), y recalcular `atn_pct_gasto` y `atn_por_habitante_pesos`. Siguen pendientes la confirmación del TNA de octubre con Politikon y la apertura mensual de las TNA.

## Corte del 13/11/2026 · senadores
- **Sin cambios en `senadores.json`:** no hubo sesiones en el recinto del Senado entre el 07 y el 13/11/2026. Noticias Argentinas (12/11) ubica la próxima sesión, con la ley de Discapacidad, el jueves de la semana siguiente; Infobae (12/11) y Perfil (13/11) no registran sesiones en la semana. No se corrió `build_senadores.py`.
- **Pendientes:** sigue sin lista nominal la reforma de Salud Mental (29/10, 42-21-0); la búsqueda de la semana no encontró ninguna lista uno por uno y senado.gob.ar sigue con 403 desde la shell (13/11/2026). Siguen los faltantes de arriba.
