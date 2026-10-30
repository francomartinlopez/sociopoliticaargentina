# Fuentes y faltantes · datos/conflictividad

Actualizado: 2026-10-30 (corte semanal). Período: 30/10/2025 a 30/10/2026.

## Archivos
- `ev.jsonl`: un hecho verificado por línea. Es el archivo que se edita.
- `build_hechos.py`: valida las claves de provincia, las categorías y el período, asigna coordenadas de ciudad y genera `hechos.json`. Corre con `python3 build_hechos.py`.
- `hechos.json`: lo que lee el sitio, con `meta`, `hechos` y `piquetes`.

## Criterios
- **Cifras:** cada número sale de la nota citada en `fuentes`. Cuando las fuentes difieren se carga la cifra más completa y las demás quedan en `nota`. Ejemplo: en la marcha del 11/02/2026 hay 71 detenidos según la ministra Monteoliva, 37 según Diario de Cuyo y 15 según Jorge Macri.
- **null:** ninguna fuente dio el dato. No se completó nada por estimación propia.
- **Personas:** casi ninguna crónica trae cifras de asistentes. Las que hay: 24M en CABA, 100.000 según el gobierno; 24M en Córdoba, más de 200.000 según la Mesa de DD.HH.; 24M en Mar del Plata, 100.000 según 0223; fuerzas federales, unas 200 personas; Marcha de la Bronca en Mendoza, más de 5.000 según La Izquierda Diario. Segunda tanda: cuarta marcha universitaria en CABA, 120.000 según el cálculo de La Nación; Córdoba, más de 120.000 según la Facultad de Artes de la UNC; Ni Una Menos en Rosario, 65.000 según Rosario3; parazo en Rawson, más de 6.000 (15.000 en la provincia) según El Cohete a la Luna; AMSAFE en Santa Fe, más de 10.000 según el gremio; Glaciares en Mendoza (04/02), más de 3.000 según FARCO.
- **procesados:** solo imputaciones o cargos informados en la nota, y la nota aclara si es un anuncio del gobierno o una imputación judicial.
- **Coordenadas:** centro de la ciudad. Los paros nacionales se ubican en CABA.
- **Fuentes partidarias o militantes:** tres hechos se apoyan en La Izquierda Diario, medio del PTS (dos en Santa Cruz y la réplica de Mendoza del 19/09); en la Marcha de la Bronca de CABA es una de las dos fuentes. En la segunda tanda se usaron FARCO (agencia de radios comunitarias), El Cohete a la Luna, el sitio de ATE y la Facultad de Artes de la UNC como fuentes de parte; Indymedia sirvió solo de pista y no se cita. Va aclarado en cada nota.
- **Cifras de parte:** las cifras que dan sindicatos u organizadores van en `personas_max` (o en las dos puntas si son la única) y la nota dice quién las dio. Las adhesiones a paros, sindicales u oficiales, van en nota.
- **Crónicas previas:** algunos paros provinciales se cargaron con una nota del mismo día o de la víspera, cuando no se encontró crónica posterior. Va aclarado en nota.
- **Fechas deducidas:** cuando la nota dice «este martes» o «la madrugada del viernes», la fecha se calculó con el calendario y la nota lo aclara. Los acampes y tomas largas se fechan por su inicio o, si no se sabe, por la primera crónica que los informa.

## Cobertura lograda
143 hechos (91 nuevos en la segunda tanda): 64 manifestaciones pacíficas, 28 con incidentes, 25 paros, 12 conflictos policiales o penitenciarios, 6 motines, 5 tomas y 3 atentados. 63 tienen dos fuentes o más. 106 están fuera de CABA (37 en CABA).

Por provincia: CABA 37 · Buenos Aires 16 · Córdoba 10 · Mendoza 9 · Santa Cruz 7 · Río Negro 6 · Santa Fe 6 · Neuquén 6 · Catamarca 6 · Salta 5 · Chubut 5 · La Pampa 4 · Jujuy 4 · Tucumán 4 · San Juan 3 · Misiones 3 · Entre Ríos 3 · Chaco 2 · Tierra del Fuego 2 · Corrientes 2 · Santiago del Estero 1 · Formosa 1 · La Rioja 1 · San Luis 0.

Primera tanda (51 hechos, más la fila del paro de AMSAFE del 02/03, que estaba en `ev.jsonl` pero no en `hechos.json`):
- **Reforma laboral:** 9/12/2025 (paro de ATE y cortes), 15/12 (ataque a Seivara), 18/12 (CGT y ATE), 4/02/2026, 11/02, 18/02 (toma de FATE), 19/02 (paro general, Congreso y Acceso Oeste), 27/02 y 4/03 (desalojo de FATE).
- **Otras movilizaciones nacionales:** 24M (50 años del golpe) en 5 ciudades, Ni Una Menos, CGT del 30/04, 22/07, San Cayetano, endeudamiento (20/08), Marcha de la Bronca (19/09) y la quinta Marcha Federal Universitaria (15/10).
- **Conflictos policiales:** Rosario (feb.), retirados bonaerenses (feb.), Jujuy (mar.), fuerzas federales (abr.) y acampe de Santa Cruz (may.–jul.).
- **Cárceles y comisarías:** Alcaidía de Salta (26/10/2025), Penal 2 de General Roca (24/11/2025), Comisaría 3 de Balvanera (25/05/2026) y Alcaidía 1 de CABA (22/10/2026).

Segunda tanda (búsqueda provincia por provincia):
- **Paros docentes y estatales provinciales:** UEPC (02/03 y 09/03) y gremios estatales cordobeses contra la reforma previsional (29/12, 12/01, 04/02); primer paro docente bonaerense contra Kicillof (02/03), FUDB (01/10) y FEB (22/10); UnTER (02/03, 05/05 con gas en los puentes, 24/09 por el IPROSS); ATE-ATEN contra el acuerdo de GNL (24/06) y ATE Salud (13/10) en Neuquén; «faltazo», parazo y represión en Vialidad (abr.) y autoconvocados (may.) en Chubut; SUTEF por tiempo indeterminado desde el 03/08 en Tierra del Fuego; AGMER (27/08 y 30/09); CEDEMS y bases de ADEP (27–29/07); Formosa y La Rioja (27/07); FTEL-MPL en Misiones (11/08); UTELPa (04/12/2025 y 02/02/2026); Chaco (03/02 y 25/02); San Juan (11/03 y 26/03); Catamarca (02/03 y 04/03); Corrientes (28/03 y 25/05); Santa Cruz (Legislatura 12/03, Las Heras 15/04 con dos dirigentes detenidos, toma del CPE 15/04, petroleros 22/10).
- **Minería, Glaciares y agua:** caravana contra San Jorge (09/12/2025) y represión con 17 detenidos (11/12) en Mendoza; marchas por la Ley de Glaciares en Mendoza (04/02, 9 detenidos; 27/02; 09/04, 8 detenidos), Córdoba (27/02) y Congreso (08/04, 8 detenidos); Fiambalá (07/10) y Andalgalá (13/10); No a la Mina en Esquel (04/03); corte por agua en El Cruce, Salta (27/06).
- **Jubilados:** Congreso 17/12/2025, 18/03 (3 detenidos) y 15/07 (agresión al padre Paco Olveira); Concordia 23/09 (3 detenidos).
- **Policías y penitenciarios:** Catamarca (27/02 y 14/07), Cipolletti (07/03), exonerados en Posadas (desde 06/04), SPF en Santa Rosa (23/04 y 27/05) y SPB en La Plata (29/05).
- **Cárceles:** Comisaría 6ª de Santiago del Estero (21/07) e instituto de menores de Benjamín Paz, Tucumán (25/05).
- **Cortes y piquetes:** Volver al Trabajo en Puente Pueyrredón (07/04); Tartagal (18/09, un detenido); RN 81 en Salta (desde 29/09); viales en Añelo (11/06).
- **Tomas:** Aires del Sur en Río Grande (24/02) y frigorífico Ecocarnes en San Fernando (23/10).
- **Atentados:** molotov contra el Sindicato de Dragado y Balizamiento en Rosario (08/05).
- **Réplicas de jornadas nacionales:** cuarta Marcha Federal Universitaria (12/05: CABA, 120.000 según La Nación, y Córdoba, Rosario, Mendoza, Mar del Plata, Neuquén y Posadas); paro general del 19/02 (Tucumán, Córdoba, Neuquén, Mendoza); 24M (Rosario, La Plata, Tucumán, Salta, Jujuy, Bahía Blanca); Ni Una Menos (Rosario, 65.000 según Rosario3, y Córdoba); quinta marcha universitaria en Tucumán (15/10).
- **Correcciones:** al paro de AMSAFE del 02/03 se le sumó la cifra sindical de más de 10.000 manifestantes; al motín de Balvanera, la versión de El Cronista (7 afectados y sin fugas).
- **Piquetes:** totales anuales de Diagnóstico Político (2023: 8.239 · 2024: 5.996 · 2025: 3.893) y el top 5 provincial de 2025. **No hay serie mensual**: no se encontró ninguna publicada para el período.

## Faltantes y por qué
- **Tope de búsquedas:** la segunda tanda también agotó las 200 búsquedas web del turno. Quedaron sin relevar San Luis (ningún hecho), Santiago del Estero (solo un motín) y, con poca profundidad, Tucumán, Formosa, La Rioja, Chaco y Misiones.
- **Sesgo geográfico:** bajó de 31 de 51 (61 %) a 37 de 143 (26 %) en CABA, pero las provincias chicas siguen subrepresentadas, en parte porque sus medios aparecen poco en el buscador.
- **Marchas de jubilados de los miércoles:** hay 8 en CABA y una en Concordia. Faltan muchas semanas y casi todas las réplicas provinciales (Mendoza, Catamarca, Rosario y otras tienen rondas semanales).
- **Saqueos y conflictos militares:** no se encontró ningún caso. Lo más cercano a lo militar sigue siendo el paro de ATE del personal civil de Defensa (27/08/2026), que no se cargó.
- **Motines:** fuera de los seis cargados, las búsquedas devolvieron sobre todo peleas entre internos o hechos de 2016–2025.
- **Convocatorias sin crónica posterior (no cargadas):** las réplicas provinciales del 07/04 por Volver al Trabajo; el paro del FTEL del 05–06/08 y el del 26–27/08 en Misiones; la caravana docente del 28/05 y la marcha del 19/03 en Chaco; el paro de AMP «de un martes» de septiembre en La Rioja; ADOSAC del 22–24/04 y 05–07/05; SUTEF del 08–09/04; ATECH Regional Sur del 23/04; UnTER del 16–17/04 con corte en la Ruta 151 (solo Indymedia). También siguen pendientes la UTA en el interior (11/02), el cabildo del Garrahan (04/02), Glaciares en Bariloche (26/02) y la marcha de fuerzas federales de agosto.
- **Fuentes sin abrir:** algunas notas se citan solo como referencia en `nota` porque la página no cargó (MendoVoz 27/02, El Día sobre el SPB, Diario Ahora de Corrientes, San Fernando Nuestro).
- **Excluidos a propósito:** los disturbios por los festejos y la derrota de la Selección (07/07 y 20/07/2026, también en Córdoba), porque no son conflictos sociopolíticos; los ataques a locales partidarios con solo pintadas (LLA Rosario, 15/10).
- **Heridos civiles:** casi ninguna fuente da cifras de manifestantes heridos; las cargadas suelen ser de efectivos. Va aclarado en nota.
- **Fechas aproximadas:** la protesta policial de Jujuy (noche del 9 al 10/03), el motín de Salta, los hechos de La Izquierda Diario y, en la segunda tanda, todos los que llevan «fecha deducida» en nota. La toma de Aires del Sur, los cortes de Salta y el paro de UnTER por el IPROSS (24/09) tienen fecha aproximada.

## Corte del 30/10/2026
- **Período móvil:** `build_hechos.py` ahora recibe la fecha de corte (`python3 build_hechos.py 2026-10-30`) y toma los 12 meses anteriores. Sale del mapa el motín de la Alcaidía de Salta (26/10/2025), que queda en `ev.jsonl` como historial. Las rutas del script pasaron a ser relativas a la carpeta.
- **Puntos del mapa:** `puntos.json` lo genera ahora el mismo script. Las ciudades ya proyectadas con `geo.mjs` conservan su punto exacto (`puntos_ref.json`, tabla lat,lon → x,y). Las ciudades nuevas (Esquina, Chascomús, Pampa del Indio, San Vicente de Misiones y San Luis) se proyectan con un polinomio de grado 3 ajustado sobre las 45 ya proyectadas: error máximo de 0,08 px en el ajuste y de 0,16 px en validación cruzada (dejando una afuera). Se revisó que los 143 hechos anteriores mantienen exactamente sus coordenadas.
- **25 hechos nuevos (168 en total):**
  - Semana del 25 al 30/10: marcha de jubilados al Congreso con un cruce entre el diputado Pietragalla Corti y la Policía de la Ciudad (28/10, El Destape); paro universitario de CONADU Histórica, AGD-UBA, FAGDUT y FATUN (28/10, Infobae y Hoy Día) y de COAD en la UNR (28/10, El Cronista); marchas por la docente rural Nancy Godoy en Corrientes (26/10) y Esquina (28/10, «cientos de personas» según Infobae); paro nacional de CTERA por su femicidio (29/10, Diario Popular, Cadena 3 y El Argentino Diario) con marchas en Posadas, Chascomús y Concordia.
  - Provincias con pocos hechos (búsqueda hacia atrás): San Luis pasa de 0 a 4 (27/02, 01/04 con represión frente a la Legislatura según ATE, 01/07 y 08/10); Santiago del Estero, Formosa y La Rioja suman las marchas universitarias del 12/05 y el 15/10; Chaco, el paro docente del 02/03 y el corte frustrado en Pampa del Indio (29/04); Misiones, los cortes yerbateros (20/04), el tractorazo (05/09) y la marcha universitaria de Posadas (15/10); Tierra del Fuego, el paro de la UOM en Mirgor (10/08) y el acampe del SUTEF (21/04).
- **Fuentes de parte o con advertencia:** Agenfor es la agencia oficial del gobierno de Formosa; InfoGremiales es un medio sindical; el relato de San Luis del 01/04 es de ATE (las «decenas de heridos» no tienen número y quedaron en null). Varias crónicas se leyeron en réplicas de Examedia.
- **Pendientes de esta semana (sin crónica o sin acceso):** marcha de ATEP, SADOP y APEMyS en Tucumán (29/10; GN Noticias no abrió); paro del SUTEF por Nancy Godoy en Tierra del Fuego (fechas contradictorias); movilización de AMSAFE y SADOP en Rosario (29/10; Conclusión no abrió); paro provincial de SUTECO en Corrientes (29/10); paro de la FUDB en Buenos Aires (30/10, solo convocatoria); paro de las dos CTA de «fines de octubre» (sin fecha confirmada ni crónica); adhesión de Docentes Autoconvocados en Formosa (sin fecha). La protesta de FeTERA en Atucha se habría pasado a noviembre.
- **Cobertura:** Santiago del Estero, Formosa, La Rioja y San Juan siguen con 3 hechos; Tucumán, San Luis, Chaco, Corrientes y Tierra del Fuego con 4.
