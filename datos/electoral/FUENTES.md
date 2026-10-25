# Datos electorales: fuentes, controles y faltantes (elecciones nacionales 2019-2025)

Generado con `/home/claude/scripts/elec_build.py` (todo se reconstruye de una vez con `python3 -I elec_build.py /home/claude/raw /home/claude/sociopolitica/argentina.json <salida>`). La asignación de listas a fuerzas está en `/home/claude/scripts/elec_fuerzas.py`. Descargas auxiliares: `elec_dine_agg.py` (agrega por sección los CSV oficiales por mesa de la DINE) y `elec_rgob_fetch.py` (baja por sección la API de resultados.gob.ar). Todas las cifras salen de los archivos descargados en `/home/claude/raw/`. Ningún número se completó a mano ni de memoria.

## 0. Acceso a las fuentes

- **Etapa 1** (2019, generales 2021, CABA 2025): el proxy solo dejaba pasar GitHub, así que se usaron copias de los datos de la DINE publicadas en repositorios (fuentes A, B y C). Hay detalle de los repositorios revisados en el historial de este archivo.
- **Etapa 3** (25/10/2026): se habilitó `www.electoral.gob.ar` (CNE). Las provincias y el total país de los 10 archivos nacionales pasaron al escrutinio definitivo (salvo Buenos Aires en la PASO presidencial 2023); los departamentos siguen en provisorio. Ver la sección final **Escrutinio definitivo**. Lo que sigue en §0-§3 describe el estado provisorio anterior.
- **Etapa 2**: se habilitaron `datos.gob.ar`, `www.argentina.gob.ar` y `resultados.gob.ar`. Siguen bloqueados `datos.mininterior.gob.ar`, `resultados.mininterior.gob.ar` y `www.electoral.gob.ar` (CNE). Consecuencias:
  - El ZIP por mesa de la **PASO 2023** que lista el dataset de CKAN `resultados-provisionales-elecciones-20231` (`…/dine-resultados/2023-PROVISORIOS_PASO.zip`) da **404**, y la página de la DINE ya no lo enlaza. Se reemplazó por la API de resultados.gob.ar (fuente F).
  - El dataset `elecciones_legislativas_2025` (por mesa) apunta a `datos.mininterior.gob.ar`, que no es accesible. Se usó la API de resultados.gob.ar (fuente F), que publica los mismos provisorios agregados por sección.
  - El **escrutinio definitivo** por sección no está disponible en ninguna fuente accesible (el CNE está bloqueado). La DINE solo publica el definitivo 2021 por distrito, en xlsx, y se usa como control.
  - `resultados.gob.ar` corta conexiones de vez en cuando (`Connection reset`). El script reintenta hasta 8 veces y no vuelve a bajar lo que ya tiene.

## 1. Estado por elección

| Archivo | Estado | Recuento | Fuente |
|---|---|---|---|
| presidente-2019-paso.json | completo (24 provincias, 525 deptos) | provisorio por mesa; definitivo por provincia solo como control | A |
| presidente-2019-generales.json | completo (24 provincias, 525 deptos) | provisorio por mesa; definitivo por provincia solo como control | A |
| diputados-2021-paso.json | completo (24 provincias, 523 deptos; faltan Antofagasta de la Sierra y Gastre, ver §4) | provisorio por mesa; definitivo por distrito como control | D |
| diputados-2021-generales.json | completo (24 provincias, 524 deptos; falta Tapenagá, ver §4) | provisorio por mesa (cierre 14-11-2021) | B |
| senado-2021-generales.json | completo (8 provincias, 158 deptos) | provisorio por mesa | B |
| senado-2021-paso | no se construyó (no estaba pedido; los datos están en la fuente D, cargo_id 2) | — | D |
| presidente-2023-paso.json | completo (24 provincias, 525 deptos) | provisorio por sección | F |
| presidente-2023-generales.json | completo (24 provincias, 525 deptos) | provisorio por mesa | E |
| presidente-2023-balotaje.json | completo (24 provincias, 525 deptos) | provisorio por mesa | E |
| diputados-2025-generales.json | completo (24 distritos, 525 deptos). **Reemplaza al de solo CABA** | provisorio por sección | F |
| senado-2025-generales.json | completo (8 distritos: CABA, Chaco, Entre Ríos, Neuquén, Río Negro, Salta, Santiago del Estero, Tierra del Fuego; 138 deptos) | provisorio por sección | F |

**Actualización 25/10/2026:** provincia y país ya son escrutinio definitivo en los 10 archivos, salvo Buenos Aires en la PASO presidencial 2023 (`"recuento": "definitivo (provincia y país); provisorio (departamento)"`, `"recuento_departamento": "provisorio"`); ver **Escrutinio definitivo** al final. La tabla describe la fuente de los departamentos, que sigue siendo el provisorio: ninguna fuente accesible publica el definitivo por sección o por departamento.

### Fuentes

- **A.** DINE, escrutinio provisorio 2019 por mesa, reconstruido por PoliticaArgentina/data_warehouse (electorAr) a partir de los paquetes de @pmoracho:
  - https://raw.githubusercontent.com/PoliticaArgentina/data_warehouse/master/electorAr/data/escrutinios_provisorios/arg_presi_paso2019.csv
  - https://raw.githubusercontent.com/PoliticaArgentina/data_warehouse/master/electorAr/data/escrutinios_provisorios/arg_presi_gral2019.csv
  - Control: escrutinio definitivo nacional y por provincia, `…/electorAr/data/escrutinios_definitivos/{arg,caba,pba,…}_presi_{paso,gral}2019.csv` (48 archivos provinciales y 2 nacionales). Va dentro de cada JSON en `definitivo_control`.
  - Documentación de la fuente: https://github.com/PoliticaArgentina/data_warehouse/blob/master/electorAr/data_raw/escrutinios_provisorios.md
- **B.** DINE, escrutinio provisorio de las generales del 14-11-2021, archivo oficial `MESAS_ESCRUTADAS_Cierre.csv` (398 MB, todos los cargos, por mesa, con nombre de sección y electores), comprimido en RAR v5 por andresminio/forenseelectoral2021:
  - https://github.com/andresminio/forenseelectoral2021/blob/main/2%20Resultados/MESAS_ESCRUTADAS_Cierre.rar
  - Se descomprimió con `node-unrar-js` (npm), con el script `/home/claude/scripts/unrar.mjs`. Se usaron las filas de los cargos DIPUTADOS NACIONALES y SENADORES NACIONALES.
- **C.** DINE, escrutinio provisorio del 26-10-2025, solo CABA, por mesa (sin electores), publicado por Facunfer/elecciones_octubre_2025:
  - https://github.com/Facunfer/elecciones_octubre_2025/blob/main/CSV%20RESULTADOS%20-%20diputados.csv
  - https://github.com/Facunfer/elecciones_octubre_2025/blob/main/CSV%20RESULTADOS%20-%20senadores.csv
  - El repositorio no documenta de dónde salen los datos. El formato (seccion_nombre, circuito_id, mesa_id, cargo_nombre, agrupacion_nombre, votos_tipo, votos_cantidad) es el de los CSV provisorios de la DINE, y los totales coinciden con lo publicado (ver §2).
- **C (reemplazada).** La versión de 2025 con solo CABA ya no se usa: `build2025caba()` queda en el script como referencia y CABA sale ahora de la fuente F. Control: CABA Diputados en F da LLA 771.065 y FP 439.196, contra 47,36 % y 26,97 % en C. La relación entre ambas fuentes es la misma.
- **D.** DINE, escrutinio provisorio de las PASO 2021, por mesa, en el estándar de preservación de resultados electorales. Archivo `2021_PASO/ResultadosElectorales.csv`, cargo_id 3:
  - https://www.argentina.gob.ar/sites/default/files/2021-provisorios_paso.zip (enlazado en https://www.argentina.gob.ar/dine/resultados-electorales/elecciones-2021)
  - Control: escrutinio definitivo por distrito (xlsx "Consulta de Escrutinio por Zona"), https://www.argentina.gob.ar/sites/default/files/2022/07/diputados_paso_2021.rar. Va dentro del JSON en `definitivo_control`.
- **E.** DINE, escrutinio provisorio 2023 por mesa, en el mismo estándar (CKAN datos.gob.ar `resultados-provisionales-elecciones-20231`), cargo_id 1:
  - https://www.argentina.gob.ar/sites/default/files/2023_generales_1.zip (`ResultadoElectorales_2023_Generales.csv`)
  - https://www.argentina.gob.ar/sites/default/files/2023_segundavuelta.zip (`ResultadosElectorales_2023_SegundaVuelta.csv`). Trae 748 mesas marcadas `estado_final = NO ESCRUTADO`, sin votos, que no se cuentan en electores ni en mesas.
- **F.** DINE, Sistema de Publicación de Resultados Electorales: API pública `https://resultados.gob.ar/api/resultado/totalizado?año=…&recuento=Provisorio&idEleccion=…&idCargo=…&idDistrito=…&idSeccion=…`. Es la que usa la web resultados.gob.ar; el árbol de secciones sale de `…/api/menu?año=…&recuento=Provisorio&idEleccion=…`. Se bajó un JSON por sección y otro por distrito:
  - PASO 2023, presidente: idEleccion=1, idCargo=1 (554 consultas; incluye el distrito 0 = total país, que se usa solo como control).
  - Generales 2025: idEleccion=2, idCargo=3 (Diputados) e idCargo=2 (Senadores). 700 consultas.
  - Controles internos (son assert, el build falla si no se cumplen): positivos = suma de agrupaciones; positivos + blancos + nulos + recurridos + impugnados + comando = votantes; cada agrupación = suma de sus listas. La suma de secciones coincide exactamente con el total por distrito de la misma API (electores, mesas, blancos, nulos y positivos) y, en la PASO 2023, con el total país (distrito 0).
- Mapa base: `/home/claude/raw/geo/departamentos-argentina.topojson` (mgaitan/departamentos_argentina), ya convertido en `argentina.json`.

## 2. Controles de totales contra cifras publicadas

| Elección | Este dataset | Cifra publicada | Resultado |
|---|---|---|---|
| Presidente 2019 Generales | FdT 48,29 % / JxC 40,22 % de los afirmativos (provisorio, 100.078 mesas) | Definitivo: Fernández 48,24 %, Macri 40,28 % (La Nación, El Litoral, Minuto Uno). El definitivo de data_warehouse da exactamente 48,24 / 40,28 | OK (diferencia provisorio-definitivo ≤ 0,06 pp). Por provincia y fuerza, provisorio/definitivo queda entre 0,979 y 1,000 |
| Presidente 2019 PASO | FdT 47,69 % / JxC 31,87 % de los válidos (afirmativos + blancos) | Chequeado: FdT 47,65 % provisorio y 47,78 % definitivo; JxC 32,08 % provisorio y 31,79 % definitivo. Definitivo de data_warehouse: 47,79 / 31,80 | OK (≤ 0,21 pp contra ambos). Por provincia, provisorio/definitivo queda entre 0,909 y 1,001 una vez corregido el código de TDF (§3) |
| Diputados 2021 Generales (total país) | JxC 9.735.745 votos (41,89 %); FdT 7.801.865 (33,57 %) de los afirmativos | Chequeado: provisorio 41,9 % / 33,5 %. FdT 2019 (11.606.411) menos 3.804.546 = 7.801.865 | OK. JxC: Chequeado da "644 mil votos menos que en 2019" (10.397.134), es decir unos 9,75 M; aquí la diferencia sale de 661.389 votos (el número publicado está redondeado y podría venir del definitivo). Letra P, con 96,32 % de mesas: JxC 42,10 %, FdT 33,36 %, FIT 5,93 %, liberales 3,9 % (963.870 votos). Aquí FIT da 5,14 % y AL 4,67 % (1.085.550 votos): la diferencia viene del corte parcial de Letra P y de qué listas suma como "liberales" |
| Senado 2021, Santa Fe (control provincial) | JxC 40,33 %, FdT 32,20 %, FAP 12,50 % | Conclusión, con 97,39 % de mesas: 40,35 / 32,17 / 12,47 | OK |
| Diputados 2025, CABA | LLA 47,36 %, FP 26,97 % | Chequeado: LLA 47,35 % (47,42 % en otro párrafo), FP 27 %, con 94,76 % de mesas | OK |
| Senado 2025, CABA | LLA 50,33 %, FP 30,64 % | Chequeado: LLA 50,4 %, FP 30,5 % (La Capital: "Bullrich cosechó el 50 %") | OK |
| Presidente 2023 Generales | UxP 36,69 % / LLA 29,99 % / JxC 23,84 % / HxNP 6,79 % / FIT 2,70 % de los afirmativos (provisorio, 104.520 mesas; UxP 9.645.983, LLA 7.884.336) | Referencia: Massa ~36,8, Milei ~30,0, Bullrich ~23,8, Schiaretti ~6,8, Bregman ~2,7 (el definitivo da Massa 36,78) | OK (Massa 0,1 pp por debajo: diferencia provisorio-definitivo) |
| Presidente 2023 Balotaje | LLA 55,69 % / UxP 44,31 % de los afirmativos (14.476.462 / 11.516.142; 103.772 mesas) | Definitivo: 55,65 / 44,35 | OK (0,04 pp; el provisorio oficial publicado fue 55,69 / 44,31) |
| Presidente 2023 PASO | Sobre válidos (afirmativos + blancos): LLA 30,04 %, JxC 28,28 %, UxP 27,27 %, HxNP 3,83 %, FIT 2,65 %. Sobre afirmativos: 31,57 / 29,72 / 28,66 | Provisorio oficial: 30,04 / 28,27 / 27,27 (es el mismo `votosPorcentaje` que da la API getResultados de la DINE para el total país) | OK |
| Diputados 2021 PASO (total país) | JxC 39,86 %, FdT 31,03 %, FIT 4,38 % de los válidos (99.428 mesas, 21.286.049 afirmativos) | Definitivo DINE por distrito: 21.765.879 afirmativos en total | OK: el provisorio cubre el 97,8 % de los afirmativos del definitivo. Por distrito, provisorio/definitivo va de 0,965 a 0,997, salvo Catamarca (0,906, por la sección faltante, §4) |
| Diputados 2025 Generales (total país) | LLA 9.341.798 (40,66 % de los afirmativos); FP 7.637.537 (33,24 %); PU 1.574.551 (6,85 %). Sobre válidos: 39,51 / 32,30 / 6,66 | Referencia del pedido: LLA ~40,7, FP ~31,7. Chequeado (99,3 % de los votos): LLA 9.341.798 (40,6 %), "Fuerza Patria y fuerzas aliadas" 7.635.619 (33 %), con el Frente Cívico de Santiago como aliado; PU 1.701.877 (7,4 %) | LLA: OK, coincide al voto. FP: coincide con Chequeado (diferencia de 1.918 votos). Sin el Frente Cívico por Santiago (284.387) da 32,00 %, y sin él ni Chubut "Frente Unidos Podemos" da 31,62 %. El ~31,7 de referencia parece excluir esos aliados. Se mantuvo el criterio de 2021 (Frente Cívico → FP, `duda=False`). PU: aquí 0,55 pp menos. Chequeado suma frentes provinciales que acá quedaron en PROV (posiblemente "Por San Juan" de Orrego, 132.286 votos; ver §5) |
| Senado 2025 (8 distritos) | LLA 42,03 %, FP 34,61 % de los afirmativos | — (no hay total nacional comparable) | Controlado contra los totales por distrito de la API (sin diferencias) |

En todos los archivos, `fuerzas` cuenta votos afirmativos. Los porcentajes de presidente se calculan sobre afirmativos; los de legislativos se publican sobre válidos (afirmativos + blancos).

## 3. Observaciones sobre los datos

- **Departamentos: escrutinio provisorio** (provincia y país pasaron al definitivo; ver la sección final). Los provisorios no incluyen las mesas que no se transmitieron. Por eso `electores` es el padrón de las mesas incluidas, no el padrón total. Ejemplo: 2019 Generales suma 33.824.771 electores en 100.078 mesas; el definitivo publica 34.229.969. `mesas` informa cuántas mesas se agregaron en cada unidad.
- **2019:** la fuente no trae recurridos, impugnados ni votantes, así que `votantes` = afirmativos + blancos + nulos y `otros` = null.
- **2019, códigos de partido:** los códigos de columna de los CSV provisorios no coinciden con `electorAr/data/listas/listas_presi_*2019.csv`. En ese archivo 00002 y 00008 están invertidos (FIT y MAS), y el de generales usa otra numeración. Se identificaron comparando provincia por provincia contra el definitivo: 00005=FdT, 00009=JxC, 00001=CF, 00002=FIT, 00010=NOS, 00004=Unite/Espert, 00008=MAS, 00011=Frente Patriota, 00051=MAV, 00050=Partido Autonomista. **En Tierra del Fuego, en la PASO, 00002 y 00008 vienen al revés** (provisorio 876/3.039 contra definitivo FIT 3.058 / MAS 883). Se corrigió con `PRESI2019_OVERRIDE`.
- **2019, nombres faltantes:** algunas filas traen `depto = "NA"`: Catamarca 014 y 016, Chaco 006. Se resolvieron por código de sección usando el nombre que tiene ese mismo código en el archivo DINE 2021 (Antofagasta de la Sierra, Santa María, Presidencia de la Plaza). Está listado en `geo/crosswalk.json` → `nombres_por_codigo_2019_NA`.
- **2021:** `otros` = recurridos + impugnados + comando. "comando" son los votos del Comando Electoral que informa la DINE. Cada campo también va por separado.
- **2025 (fuente F):** trae electores (padrón de las mesas escrutadas), así que ya se puede calcular la participación (67,43 % en Diputados). `cobertura` lista los distritos.
- **CSV DINE por mesa (D, E): padrón duplicado.** En 2021, cada mesa aparece también con `padron_tipo = COMANDO`, que repite `mesa_electores`. La primera agregación de `elec_dine_agg.py` lo contaba dos veces (68 M de electores en Diputados). Se corrigió: cada mesa (distrito, sección, circuito, mesa, tipo de mesa) se cuenta una sola vez, sea cual sea el `padron_tipo`. Los votos de tipo COMANDO se siguen sumando en `comando`.
- **PASO (2021 y 2023):** `fuerzas` = votos de la agrupación (suma de sus listas internas). El detalle por lista interna va en `listas_internas`, a nivel país y por distrito: por ejemplo, en 2023, JxC "B- LA FUERZA DEL CAMBIO" (Bullrich) 8.044.932 contra "A- EL CAMBIO DE NUESTRAS VIDAS" (Rodríguez Larreta) 5.351.126, y UxP "A- CELESTE Y BLANCA" (Massa) contra "B- JUSTA Y SOBERANA" (Grabois). Ojo: estas cifras de listas internas suman a nivel distrito; los totales nacionales de la PASO 2023 son los de `pais`.
- **2023, `otros`:** recurridos + impugnados + comando, igual que en 2021.
- Claves extra en los JSON, además del esquema pedido: `recuento`, `notas`, `cobertura` (2025), `positivos`, `mesas`, `recurridos`/`impugnados`/`comando` (cuando existen), `sin_poligono` (votos de secciones sin polígono en el mapa), `listas` (votos por lista oficial dentro de cada fuerza) y `definitivo_control` (2019).

## 4. Crosswalk (código de resultados → id del mapa)

Archivo completo: `geo/crosswalk.json`, con una fila por fuente (`2019`, `2021`, `dine2021paso`, `dine2023`, `rgob2023paso`, `rgob2025`), provincia, código de sección y nombre de la fuente, el `map_id` y la regla aplicada (3.165 filas). Los nombres se comparan en mayúsculas y sin tildes. No hay coincidencias aproximadas: todo lo que no coincide literalmente está en esta tabla. **Control independiente** (se ejecuta en cada build): dentro de cada época de codificación, cada código de sección de la DINE apunta al mismo id del mapa en todas las fuentes, aunque los nombres sean distintos. Resultado: 0 inconsistencias. **La DINE renumeró las secciones de Santa Fe desde 2023**: hasta 2021 el código 1 era Belgrano, el 9 La Capital, etc. (orden alfabético); desde 2023 el 1 es La Capital, el 2 Las Colonias, etc. Los nombres coinciden en todas las fuentes, así que la asignación a polígonos es correcta. Por eso el control compara 2019-2021 y 2023-2025 por separado.

Reglas que no son de igualdad literal:

- **CABA:** "COMUNA 0N" pasa a "COMUNA N" (comunas 1 a 9), en todas las fuentes.
- **Alias explícitos** (provincia | nombre en la fuente → nombre en el mapa | fuente):

| Provincia | Nombre en la fuente | Regla | Fuente |
|---|---|---|---|
| BUENOS AIRES | CORONEL ROSALES / CORONEL DE MARINA L. ROSALES | → CORONEL DE MARINA LEONARDO ROSALES | 2019 / 2021 |
| BUENOS AIRES | GENERAL MADARIAGA | → GENERAL JUAN MADARIAGA | 2019 |
| BUENOS AIRES | GONZALES CHAVES | → ADOLFO GONZALES CHAVES | 2019 |
| BUENOS AIRES | JOSE C. PAZ | → JOSE C PAZ | 2019, 2021 |
| BUENOS AIRES | LEANDRO N. ALEM | → LEANDRO N ALEM | 2019, 2021 |
| BUENOS AIRES | NUEVE DE JULIO | → 9 DE JULIO | 2019 |
| CHACO | FRAY JUSTO STA. MARIA DE ORO | → FRAY JUSTO SANTA MARIA DE ORO | 2019 |
| CHACO | LIBERTADOR GRAL. SAN MARTIN | → LIBERTADOR GENERAL SAN MARTIN | 2019 |
| CHACO | MAYOR L. J. FONTANA | → MAYOR LUIS J. FONTANA | 2019 |
| CHACO | PRIMERO DE MAYO / 1º DE MAYO | → 1° DE MAYO | 2019 / 2021 (º se normaliza a °) |
| CHUBUT | F. AMEGHINO | → FLORENTINO AMEGHINO | 2019 |
| CHUBUT | PASO DE LOS INDIOS | → PASO DE INDIOS | 2019 |
| CHUBUT | RIO SENGER | → RIO SENGUER | 2019 |
| CORDOBA | ROQUE SAENZ PENA | → PRESIDENTE ROQUE SAENZ PENA | 2019 |
| JUJUY | GENERAL BELGRANO / DR. MANUEL BELGRANO | → DOCTOR MANUEL BELGRANO | 2019 / 2021 |
| LA PAMPA | CHICAL-CO | → CHICAL CO | 2019 |
| LA RIOJA | ANGEL VICENTE PENALOZA | → GENERAL ANGEL V. PENALOZA | 2019, 2021 |
| LA RIOJA | FELIPE VARELA | → CORONEL FELIPE VARELA | 2019 |
| LA RIOJA | JUAN FACUNDO QUIROGA / GENERAL JUAN FACUNDO QUIROGA | → GENERAL JUAN F. QUIROGA | 2019 / 2021 |
| LA RIOJA | GENERAL ORTIZ DE OCAMPO | → GENERAL OCAMPO | 2019, 2021 |
| MENDOZA | LUJAN | → LUJAN DE CUYO | 2019 |
| MISIONES | CONCEPCION DE LA SIERRA | → CONCEPCION | 2019 |
| MISIONES | EL DORADO | → ELDORADO | 2019 |
| RIO NEGRO | NUEVE DE JULIO | → 9 DE JULIO | 2019 |
| RIO NEGRO | SAN ANTONIO OESTE | → SAN ANTONIO | 2019 |
| SALTA | SAN MARTIN | → GENERAL JOSE DE SAN MARTIN | 2019 |
| SAN JUAN | NUEVE DE JULIO | → 9 DE JULIO | 2019 |
| SAN LUIS | PEDERNERA / PRINGLES / PUEYRREDON / SAN MARTIN | → GENERAL PEDERNERA / CORONEL PRINGLES / JUAN MARTIN DE PUEYRREDON / LIBERTADOR GENERAL SAN MARTIN | 2019 |
| SANTA FE | NUEVE DE JULIO | → 9 DE JULIO | 2019 |
| SANTA FE | VILLA CONSTITUCION | → CONSTITUCION (mismo código 2019/2021) | 2021 |
| SANTIAGO DEL ESTERO | JUAN F. IBARRA | → JUAN F IBARRA | 2019, 2021 |
| SANTIAGO DEL ESTERO | TABOADA | → GENERAL TABOADA | 2019 |
| TUCUMAN | ALBERDI / JUAN B. ALBERDI | → JUAN BAUTISTA ALBERDI | 2019 / 2025 |
| varios | nombres abreviados de la API 2025 | 22 alias explícitos en `ALIAS` (p. ej. CHACO "PCIA. DE LA PLAZA" → PRESIDENCIA DE LA PLAZA, "CMDTE. FERNANDEZ" → COMANDANTE FERNANDEZ; MISIONES "L.N.ALEM" → LEANDRO N. ALEM; SAN LUIS "DUPUY" → GOBERNADOR DUPUY; BUENOS AIRES "GENERAL LAMADRID" → GENERAL LA MADRID, "VEINTICINCO DE MAYO" → 25 DE MAYO; RIO NEGRO "GENERAL CONESA" → CONESA; LA RIOJA "GRAL. ORTIZ DE OCAMPO" → GENERAL OCAMPO). Cada uno verificado: el mismo código de sección apunta a ese polígono en el CSV DINE 2023 | 2025 |

- **Unidades que se agregan a otro polígono**, porque el mapa conserva límites anteriores a su creación:
  - BUENOS AIRES | LEZAMA → se suma a CHASCOMUS. Partido creado en 2009 a partir de Chascomús. El valor de Chascomús en el mapa incluye a Lezama.
  - TIERRA DEL FUEGO | TOLHUIN → se suma a RIO GRANDE. Departamento creado en 2017 a partir de Río Grande.
- **Unidades de resultados sin polígono:** TIERRA DEL FUEGO | ANTARTIDA ARGENTINA (bases antárticas; el mapa excluye la Antártida). Cuenta en provincia y país y va en `sin_poligono`. Votantes: 161 (PASO 2019), 163 (generales 2019), 128 (diputados 2021).
- **Polígonos del mapa sin resultados:**
  - TIERRA DEL FUEGO | Islas Malvinas (id 489), en todas las elecciones: no tiene electores.
  - CHACO | Tapenagá (id 315), solo en diputados 2021 generales: el archivo provisorio de cierre no trae ninguna mesa de la sección 009. Sí aparece en 2019 y en la PASO 2021. Es un hueco de la fuente; no se completó.
  - CATAMARCA | Antofagasta de la Sierra (id 344, sección 014) y CHUBUT | Gastre (id 375, sección 004), solo en diputados 2021 PASO: el CSV provisorio oficial no trae ninguna mesa de esas secciones. Es un hueco de la fuente.
  - Votantes en la sección ANTARTIDA ARGENTINA (sin polígono): 165 (PASO 2021), 200 (PASO 2023), 201 (generales 2023), 196 (balotaje 2023) y 176 (2025).
- Unidades de resultados sin match: ninguna.

## 5. Fuerzas y bloques (`fuerzas.json`)

Cada fuerza tiene nombre, color, bloque, motivo y la lista exacta de listas oficiales (año, cargo, provincia, nombre) que agrupa. Se reutilizan los ids de `index.html` (`LLA, JXC, UXP, FDT, FP, HXNP, PU, CF, FIT, NOS, DES, AL, PROV, OTR`). **Ids nuevos**, que `index.html` todavía no define en `F`: `OJXC` (partidos de JxC con lista propia, der), `OPJ` (peronismo por fuera del frente, izq), `OIZ` (otras izquierdas, izq), `ODE` (otras derechas, der), `VCV` (Randazzo/Vamos con Vos, cen), `HPC` (Hacemos por Córdoba 2021, cen), `MPN`, `JSRN`, `FRC` (Misiones), `SER` (Santa Cruz) y `FAP` (Santa Fe), todos cen. Se separaron en lugar de meterlos en `OTR`, porque `OTR` es "cen" en `index.html` y habría puesto en el centro a listas de izquierda o de derecha.

**Etapa 2: no se crearon ids nuevos.** 2023 usa `UXP, LLA, JXC, HXNP, FIT` (más `OPJ` para Guillermo Moreno, `OIZ` para MAS, PO y MIJD, `ODE` para Biondini, UCeDé y Liber.ar, y `OTR` para MAV, Libres del Sur y Proyecto Joven). 2025 usa `LLA, FP, PU, FIT` y los ids de la etapa 1. Las tablas son `L2021P` (PASO 2021: hereda `L2021` y agrega las listas que solo compitieron en la PASO), `L2023` y `L2025N` (24 distritos, con clave (distrito, agrupación)). Reglas 2025: toda lista de LLA, sola o en alianza con PRO, UCR u oficialismos provinciales (Chaco, Mendoza, Entre Ríos, PBA, etc.) → LLA. La boleta peronista de cada provincia que integró Fuerza Patria → FP, aunque use un nombre local: Fuerza Entre Ríos, Frente de la Victoria (Formosa), Frente Defendemos La Pampa, Federales Defendamos La Rioja, Fuerza Justicialista Mendoza, Fuerza San Juan, Frente Justicialista (San Luis), Fuerza Santacruceña, Frente Tucumán Primero. Los frentes de los gobernadores fundadores de Provincias Unidas → PU: Vamos Corrientes, Despierta Chubut, Frente Jujuy Crece, además de las listas "Provincias Unidas" y "Ciudadanos Unidos" (CABA). PRO, UCR y CC-ARI con lista propia → OJXC. Peronistas por fuera de FP (Natalia de la Sota en Córdoba, Melella en TDF, Partido de la Victoria en Salta) → OPJ. Los frentes de gobernadores sin alineación nacional formal (La Neuquinidad, Primero los Salteños, Por San Juan, Por Santa Cruz) → PROV. `fuerzas.json` se regeneró con todas las listas.

Decisiones a revisar (marcadas como duda en `elec_fuerzas.py`; la lista completa de las que se usaron, con su nota, sale en `/tmp/elec_resumen.json` → `dudas`, 165 entradas):

- **2025, para controlar primero:** Santiago del Estero "FRENTE CÍVICO POR SANTIAGO" → FP (sin él, FP nacional baja de 33,24 % a 32,00 %) y "FRENTE FUERZA PATRIA PERONISTA" → FP. Chubut "FRENTE UNIDOS PODEMOS" → FP (se asume que fue la boleta peronista). San Juan "POR SAN JUAN" (Orrego) y Santa Cruz "POR SANTA CRUZ" (Vidal) → PROV: si Chequeado los suma a PU, eso explicaría su 7,4 %. "HACEMOS" (San Juan) y "HACEMOS POR SANTIAGO" → PU. Neuquén "LA NEUQUINIDAD" (Figueroa) → PROV. Córdoba "DEFENDAMOS CÓRDOBA" → OPJ. TDF "DEFENDAMOS TIERRA DEL FUEGO" → OPJ. Listas liberales menores por fuera de LLA (Partido Libertario, Fuerza Libertaria, Liber.ar, Unión Liberal, Frente Libertario Demócrata, Republicanos Unidos, Unite) → ODE. Proyecto Sur, PTP y Frente Amplio por la Soberanía → OIZ. Muchas listas chicas sin alineación verificada → OTR/PROV.
- **PASO 2021:** Celeste Provida → ODE. FORJA (Córdoba) y Frente Grande (Tucumán) → OPJ. Partido Demócrata (Córdoba), Conservador Popular (PBA) y Frente Estamos con Vos (Formosa) → PROV. Varias listas bonaerenses chicas → OTR.
- **2023:** Frente Liber.ar → ODE, Proyecto Joven → OTR. Libres del Sur va a OTR en la boleta presidencial (en 2021 había ido a PROV en las listas provinciales; ambos son "cen").

Decisiones de la etapa 1:

- 2021 La Rioja "VAMOS LA RIOJA" → JXC (se asume que fue el frente de JxC; verificar).
- 2021 Santiago del Estero "FRENTE CIVICO POR SANTIAGO" → FDT. No es una duda de datos: la cifra oficial nacional del FdT, 7.801.865, solo cuadra si se lo incluye. Tampoco hubo otra lista del FdT en la provincia.
- 2021 San Luis "FUERZA SAN LUIS" → FDT (PJ puntano con la boleta del FdT). "UNIDOS POR SAN LUIS" → JXC.
- 2021 Tucumán "FUERZA REPUBLICANA" (Bussi) → PROV/cen: es un partido provincial de derecha, pero sin alianza nacional en 2021, así que la regla del proyecto lo manda al centro.
- 2021 Santa Fe "SOMOS FUTURO" y "SOBERANIA POPULAR" → OIZ; "PODEMOS" y "PRIMERO SANTA FE" → PROV. La alineación no está verificada.
- 2021 Salta "FRENTE SI + PRS" y "UNIDOS POR SALTA", Mendoza "VAMOS ! MENDOCINOS", Misiones "LIBERTAD, VALORES Y CAMBIO", Chaco "FRENTE INTEGRADOR", Santiago del Estero "FRENTE PATRIOTICO LABORISTA", Tucumán "FRENTE AMPLIO POR TUCUMÁN", Entre Ríos "CONSERVADOR POPULAR" → PROV/cen, sin verificar.
- 2021 TDF "REPUBLICANOS UNIDOS" → OJXC. 2021 Santiago del Estero "FRENTE RENOVADOR" → OPJ. 2021 La Rioja UCeDé → ODE.
- Socialismo y Libres del Sur (2021) → PROV/cen: centroizquierda no peronista ni trotskista. La regla de izquierda se aplicó solo al peronismo, al FIT y a los partidos de izquierda radical.
- 2025 CABA "CIUDADANOS UNIDOS" (Lousteau) → PU. "ALIANZA POTENCIA" → ODE. "HAGAMOS FUTURO" → OTR. UCeDé → ODE.
- 2019: "Unite por la Libertad y la Dignidad" (Espert) se cargó con el id `DES` de `index.html` (nombre "Despertar (Unite por la Libertad y la Dignidad)"). MAS → OIZ, Frente Patriota → ODE, MAV → OTR, Partido Autonomista → PROV.
- 2021 libertarios (`AL`): Avanza Libertad (PBA), La Libertad Avanza (CABA y Córdoba), Unite (Santa Fe y Santiago del Estero). "+ VALORES" (PBA, Hotton) → ODE.

## 6. Archivos descargados

- `/home/claude/raw/polar_dw/`: provisorios 2019 por mesa, listas 2019 y definitivos 2019 (en `def2019/`).
- `/home/claude/raw/forense2021/`: RAR original y `x/MESAS_ESCRUTADAS_Cierre.csv`.
- `/home/claude/raw/facunfer2025/`: CSV de CABA 2025.
- `/home/claude/raw/pa_dw/repo`: clon parcial (sin blobs) de data_warehouse, usado para inspeccionar el árbol y los PR.
- `/home/claude/raw/probe/`: clones parciales de los repositorios revisados en §0, solo para inspección.
- `/home/claude/raw/infra_datos/`: inspección, sin uso en la salida.
- `/home/claude/raw/dine/`: ZIP oficiales de la DINE (`2021-provisorios_paso.zip`, `2021-provisorios_generales.zip`, `2023_generales_1.zip`, `2023_segundavuelta.zip`), RAR de definitivos 2021 por distrito (`def_*.rar` y su contenido en `x_def_*`), y agregados por sección `agg2_*.json` (salida de `elec_dine_agg.py` corregido). `2023-PROVISORIOS_PASO.zip` es la página 404 que devolvió el servidor, no un ZIP. `agg_*.json` es la primera agregación, con el padrón duplicado: no se usa.
- `/home/claude/raw/rgob/`: menús y JSON por sección de la API de resultados.gob.ar (`2023_1_1/`, `2025_2_2/`, `2025_2_3/`).
- `/home/claude/raw/dine2025/`: intento fallido de bajar el dataset por mesa 2025 (datos.mininterior.gob.ar no resuelve).

## 7. Intendentes (`intendentes.json`)

Generado con `python3 -I /home/claude/scripts/intend/build_intendentes.py /home/claude/scripts/intend /home/claude/raw /home/claude/sociopolitica/argentina.json <salida>`. Los datos cargados a mano están en `nombres_ba.py` (nombres de candidatos bonaerenses y controles del definitivo) y `nonba.py` (resto del país), cada uno con su URL. Los agregados de la DINE salen de `intend_dine.py`. Ningún dato se completó de memoria. Lo que no se encontró queda en `null` y figura en `meta`.

**Cobertura:** 82 ciudades (42 partidos bonaerenses y 40 del resto del país). 70 tienen la última elección y 58 también la anterior. Quedan 12 ciudades sin resultados (`meta.pendientes_sin_resultados`): Río Cuarto, Resistencia, Corrientes, Paraná, Concordia, Santiago del Estero, Bariloche, General Roca, Comodoro Rivadavia, Trelew, Puerto Madryn y La Rioja. Motivo: se agotó el cupo de búsquedas web de la sesión (200). Otras 12 ciudades tienen la última elección pero no la anterior (`meta.sin_eleccion_anterior`).

### Población (Censo 2022)
- **Buenos Aires:** cuadro de la SCBA "Población, superficie y densidad por partido 2022" (fuente que cita: INDEC - DPE, definitivos). Se leyó con WebFetch porque `scba.gov.ar` está bloqueado para la shell. https://www.scba.gov.ar/planificacion/poblacion%20sup%20dens%20x%20partido%202022%20departamental.pdf. Control: General Pueyrredon 667.082 coincide con La Capital MdP. telencuestas da 1.840.868 para La Matanza contra 1.841.247 de la SCBA, es decir, diferencias de unos cientos de personas entre publicaciones.
- **Resto del país:** si el municipio coincide con un departamento (Mendoza, San Juan, Córdoba Capital, San Miguel de Tucumán, Catamarca Capital, La Rioja Capital), se usa la población del departamento según telencuestas.com (INDEC). Para las localidades se usaron los datos de INDEC por localidad publicados en julio de 2024, tomados de la prensa: Rosario, Santa Fe y Rafaela (Rafaela Noticias / El Litoral); Neuquén, Bariloche, General Roca y Cipolletti (Diario Río Negro); Comodoro, Trelew y Puerto Madryn (Diario Jornada). Río Gallegos, Concordia y Villa Mercedes salen de fichas de Wikipedia. Cuando no se encontró la cifra municipal, se usó la del departamento que contiene a la ciudad y se marcó con `poblacion_ambito`: Salta, Jujuy, Formosa, Santa Rosa, Posadas, San Luis, Río Cuarto, Resistencia, Corrientes, Paraná y Santiago del Estero. **Santa Rosa (departamento: 119.622) está por verificar.**
- `infra.datos.gob.ar`, `indec.gob.ar`, `censo.gob.ar` y `apis.datos.gob.ar` (Georef) están bloqueados.
- Quedan sin incluir, por verificar, los casos en que el departamento supera 100.000 habitantes pero el municipio no se pudo medir (`meta.no_incluidas_por_verificar`): Yerba Buena, Tafí Viejo, La Banda, Gualeguaychú, Goya, Oberá, Orán, Tartagal, Sáenz Peña, etc. Excluidas por estar debajo de 100.000: Villa María (96.061), Río Grande (departamento: 99.241), Villa Gobernador Gálvez (92.137) y Ushuaia.

### Resultados
- **Provincia de Buenos Aires (2019 y 2023):** escrutinio provisorio por mesa de la DINE, cargo INTENDENTE, agregado por sección (partido), con todas las listas, electores, votantes, blancos y nulos. Fuentes: https://www.argentina.gob.ar/sites/default/files/2019-provisorios_generales.zip (`2019_Generales/ResultadosElectorales.csv`) y la fuente E (`2023_generales_1.zip`). Salida intermedia: `/home/claude/raw/dine2019/intend_2019.json` y `/home/claude/raw/dine/intend_2023.json`. El % es sobre votos positivos.
  - Control con el definitivo (`definitivo_control`): para 2019, la Junta Electoral PBA (https://www.juntaelectoral.gba.gov.ar/resultados/poranio/2019.pdf), en 21 partidos (el texto que se pudo extraer del PDF llega hasta la Segunda Sección). El provisorio cubre entre 93 % y 98 % de los votos del definitivo, con el mismo orden de llegada en todos los casos. Para 2023: Bahía Blanca (La Nueva) y General Pueyrredon (La Capital MdP).
  - Ganadores 2023: nombre según La Tecla (los 135 electos), confirmado por Infobae, Radio 10, Perfil, El Cronista, El Día o La Nueva. El partido ganador sale de la DINE. Tandil, General Rodríguez, Luján y Necochea solo tienen a La Tecla como fuente nominal; el partido coincide con la DINE. Ganadores 2019: Ámbito (los 135), confirmado por la Junta Electoral (definitivo), A24 o LetraP ("reelecto"). **San Nicolás 2019:** Ámbito escribe "Miguel Passaglia". Se cargó "Manuel Passaglia": LetraP dice que el intendente fue reelecto y LPO (2023) lo nombra como intendente en ejercicio. Moreno 2019 figura como "Melina Mariel Fernández", según la Junta.
  - Candidatos que no ganaron: se cargó el nombre solo cuando aparece en la prensa citada (`nombres_fuentes`). Los demás quedan en `null`, sobre todo en 2019 y en las listas chicas.
- **Catamarca (capital) y Río Gallegos, 2023:** elección municipal simultánea con la nacional. Los datos salen de la DINE por mesa, sin nombres de candidatos. Río Gallegos se armó con los circuitos 01800 a 01850 de Güer Aike: allí la lista "Juntos por Río Gallegos" junta el 100 % de sus votos de la sección. Los circuitos 00021 y 0021B tienen la lista "Juntos por 28" y pertenecen a otra localidad. Salida: `/home/claude/raw/dine/intend_2023_rgallegos.json`.
- **Informes DINE de elecciones provinciales 2023** (PDF en www.argentina.gob.ar, en `/home/claude/raw/reportes/`): dan el ganador, el partido, los votos y el % de cada municipio. Con ellos se cargaron, solo con el ganador y la marca `verificacion_ganador`: Salta, San Salvador de Jujuy, Formosa, Neuquén (definitivo), Santa Rosa, Posadas (votos del sublema), Cipolletti (sin nombre), San Luis y Villa Mercedes (lemas). También sirvieron como segunda fuente en San Juan y Tucumán. Se probaron URLs equivalentes para Mendoza, Chaco, Entre Ríos, Santa Fe, Chubut, Santiago del Estero, La Rioja y Catamarca, sin éxito.
- **Mendoza:** Mendoza Post para 2023 (resultados oficiales con votos, blancos, nulos, votantes y electores; % sobre votos emitidos) y Los Andes para Maipú y San Rafael. Para 2019, Vía País, Diario Uno, Los Andes, MDZ, El Economista y Wikipedia, con listas parciales. San Rafael y San Martín 2019 no tienen porcentajes.
- **San Juan 2023:** sistema SIPAD, parecido a los lemas. Los % salen de La Mecha con escrutinio **parcial** (29-41 % de mesas). El ganador está confirmado por La Nación, El Economista y la DINE (`ganador_dine`). 2019: Diario de Cuyo (98 % de mesas) y El Economista para la Capital. En Rawson, Rivadavia y Chimbas 2019 la fuerza del ganador queda en `null`, porque ninguna fuente la nombra.
- **Córdoba:** 2023 de Cadena 3 (definitivo) y Sitio Andino; 2019 de BAE Negocios. **Rosario, Santa Fe y Rafaela:** La Capital, La Nación, El Economista, Aire de Santa Fe y LetraP. En Rosario 2023 las fuentes solo informan a los dos primeros.
- **San Miguel de Tucumán 2023:** informe DINE (Chahla, 44,18 %, con 84,83 % de mesas) y Minuto Uno (segunda: Beatriz Ávila). 2019 queda pendiente.

### Fuerzas
Se siguen las reglas de `fuerzas.json` (detalle en `meta.reglas_fuerzas`). Se sugieren dos ids nuevos en `fuerzas_sugeridas`: `LUM` (La Unión Mendocina, der) y `UPCSF` (Unidos para Cambiar Santa Fe, cen; la alternativa es JXC). Decisiones a revisar: Encuentro Marplatense → UXP (La Capital MdP: alianza de UxP y Acción Marplatense); CRECER (Othacehé, Merlo) → OPJ; Frente Libertario Demócrata y Jubilados (Mendoza) → LLA; Frente Vamos Salta (Sáenz) → PROV; Ciudad Futura 2019 → OIZ; UCR de De Loredo en Córdoba 2019 → OJXC; Partido Verde de Mendoza → PROV.

### Coordenadas
`lat`/`lon` es el centroide esférico del departamento o partido, calculado a partir de `/home/claude/raw/geo/departamentos-argentina.topojson` (`centroides.mjs`). Si el municipio no coincide con un departamento, el centroide es aproximado y el campo `latlon_fuente` lo indica. En departamentos grandes, como Las Heras o Luján de Cuyo, el centroide queda lejos de la ciudad. Georef, que tiene los centroides municipales, está bloqueado.

## 8. Gobernador (`gobernador.json`)

Generado con `/home/claude/scripts/elec_gob.py` (`python3 -I elec_gob.py /home/claude/raw /home/claude/sociopolitica/argentina.json /home/claude/sociopolitica/datos/electoral`). Usa la cabecera de `elec_build.py` para el crosswalk: mismos alias y reglas, sin coincidencias aproximadas. El script es idempotente: también reescribe en `fuerzas.json` las listas `"<año> gobernador …"`. **Si se vuelve a correr `elec_build.py`, que regenera `fuerzas.json` desde `elec_fuerzas.py`, hay que correr después `elec_gob.py`**, porque las fuerzas nuevas de abajo no están en `elec_fuerzas.py`. Esquema: `provincias[PROV].{ultima,anterior}`. Detalle de campos en `meta.esquema` y cobertura en `meta.cobertura`. Ninguna cifra se completó a mano ni de memoria. Donde no hubo fuente, `totales` = null.

### Fuentes

- **G1. Definitivos 2019 por provincia**: Atlas Electoral de Andy Tow, compilado por PoliticaArgentina/data_warehouse (`electorAr/data/escrutinios_definitivos/{prov}_gober_{gral,paso}2019.csv`), bajados a `/home/claude/raw/gob/dw/`. Son 22 distritos (todos menos Corrientes y Santiago del Estero) y 9 PASO (CABA, PBA, Catamarca, Chubut, Entre Ríos, Mendoza, Salta, Santa Fe y San Juan). La fuente no trae votantes: se calculan como positivos + blancos + nulos (+ recurridos). Tampoco trae fecha, salvo en las tres elecciones simultáneas con la nacional.
- **G2. DINE, provisorio por mesa, cargo 4**. Son los mismos ZIP del estándar de preservación, agregados por sección con `elec_dine_agg.py`:
  - `2019-provisorios_generales.zip` y `2019-provisorios_paso.zip` (bajados en esta etapa a `/home/claude/raw/gob/dine/`): Gobernador de PBA y Catamarca y Jefe de Gobierno de CABA, del 27-10-2019 y del 11-08-2019. Se usan **solo para la apertura por departamento**. Los totales de la provincia salen de G1, y el provisorio va en `departamento_fuente.totales_provisorios`.
  - `2023_generales_1.zip`: PBA, Catamarca y CABA, 22-10-2023.
  - `MESAS_ESCRUTADAS_Cierre.csv` (fuente B, cargo GOBERNADOR): Santiago del Estero, 14-11-2021 (`agg_2021_gral_gob_sde.json`).
- **G3. API resultados.gob.ar, PASO 2023, idCargo=4** (`elec_rgob_fetch_skip.py`, 161 consultas, en `/home/claude/raw/gob/rgob/2023_1_4/`): PASO de PBA y de Catamarca, y la elección de gobernador de **Santa Cruz** del 13-08-2023 (ley de lemas, publicada dentro de la PASO). **Ojo**: para las secciones de PBA que no están en la Sección Primera, la API responde 408 "No se encontró la seccion" si no se le pasa `idSeccionProvincial`. La variante `_skip` lo pasa y además no aborta ante un fallo. Controles: la suma de secciones coincide con el total del distrito (positivos y electores), y cada agrupación es igual a la suma de sus listas.
- **G4. Informes "<Provincia> 2023 - Elecciones provinciales" del Observatorio Electoral (DINE)**, en `https://www.argentina.gob.ar/sites/default/files/2023/MM/<prov>_2023_-_elecciones_provinciales[_0].pdf`, bajados a `/home/claude/raw/gob/dinepdf/`. Hay informe con tabla de gobernador para 11 provincias: Jujuy, Salta, TDF, La Pampa, Misiones, Neuquén y Río Negro (definitivos), y Córdoba, Formosa, San Luis y Tucumán (provisorios, con 88,9 % a 98,6 % de mesas). Las tablas se transcribieron en `PDF_2023` y el script controla con `assert` que la suma cierre con el total del informe. Erratas del informe, corregidas y documentadas en `notas`: Formosa da 677.794 para Carbajal, cuando es 67.794 (así cierra con los positivos y con el 20,24 %), y Salta da "válidos 710.962" cuando es 710.684 (así cierra con el total). No hay informe con gobernador para Chaco, Chubut, Entre Ríos, La Rioja, Mendoza, Santa Fe ni San Juan. El de San Juan es de junio y solo trae legislativas, porque la elección de gobernador se postergó al 2 de julio. Tampoco hay informes 2025, ni de Corrientes 2021.

### Cobertura

| Provincia | Última | Depto | PASO | Anterior | Depto | PASO |
|---|---|---|---|---|---|---|
| Buenos Aires | 2023 G2 prov. | sí (134) | sí, G3 con deptos | 2019 G1 def. | sí (G2 prov.) | sí, con deptos |
| CABA | 2023 G2 prov. | sí (15) | no (la organizó la Ciudad) | 2019 G1 def. | sí | sí, con deptos |
| Catamarca | 2023 G2 prov. | sí (16) | sí, G3 con deptos | 2019 G1 def. | 15/16 (falta Antofagasta de la Sierra) | sí, 14/16 deptos |
| Santa Cruz | 2023 G3 prov. (lemas) | sí (7) | — | 2019 G1 def. (lemas) | no | — |
| Santiago del Estero | **2025: sin cifras** | — | — | 2021 G2 prov. | sí (27) | — |
| Córdoba, Formosa, San Luis, Tucumán | 2023 G4 prov. | no | — | 2019 G1 def. | no | — |
| Jujuy, Salta, TDF, La Pampa, Misiones, Neuquén, Río Negro | 2023 G4 def. | no | — | 2019 G1 def. | no | Salta: sí |
| Chaco, Chubut, Entre Ríos, La Rioja, Mendoza, Santa Fe, San Juan | **2023: sin cifras**, solo ganador y `pct_prensa` | no | — | 2019 G1 def. | no | sí en Chubut, ER, Mendoza, SF, SJ |
| Corrientes | **2025: sin cifras** | — | — | **2021: sin cifras** | — | — |

Elecciones sin cifras: `totales` = null. Cuando la prensa lo da, `ganador` y `pct_prensa` (porcentajes de El Cronista o de un informe parcial de la ReFEE en el repositorio de la UCA) permiten pintar la provincia. Esto ocurre en 7 de las 9; Corrientes 2021/2025 y Santiago del Estero 2025 no tienen ni ganador. Motivo: los tribunales electorales provinciales, Wikipedia y andytow.com no están en la lista de dominios permitidos, y el cupo de búsquedas web de la corrida se agotó antes de encontrar fuentes alternativas (espejos en GitHub, etc.). **Pendientes**: Chaco, Chubut, Entre Ríos, La Rioja, Mendoza, Santa Fe y San Juan 2023; Corrientes 2021 y 2025; Santiago del Estero 2025. También faltan las PASO provinciales de Chaco 2019, La Pampa 2019 (17-02-2019, según el informe G4) y 2023, Mendoza 2023 (11-06), Santa Fe 2023, Entre Ríos 2023 y CABA 2023. Balotaje: en ninguna de las elecciones cubiertas hay segunda vuelta en las fuentes (`balotaje` = null en todos los casos).

### Controles

- **Ganador contra prensa (2023)**: El Cronista ("cuántas provincias ganó JxC y UxP, el mapa electoral 2023"). Los porcentajes coinciden, en general a la centésima, en Jujuy, Salta, TDF, La Pampa, Misiones, Neuquén (36,94 / 34,40 sobre afirmativos), Río Negro, Córdoba (42,76 / 39,76 sobre válidos) y Formosa. Con diferencias de provisorio contra definitivo: San Luis (53,25 contra 53,31), PBA (44,89 contra 45,08), CABA (49,61 contra 49,56) y Catamarca (54,09 contra 53,80; el artículo trae tres cifras distintas). La diferencia más grande es **Tucumán**: 58,02 % (provisorio al 88,9 %) contra 56,31 % en la prensa; está anotada en `control_prensa`. En Santa Cruz, SER da 46,49 % y UxP 43,83 %, contra 46 % y 44 % en la prensa. El script falla si el ganador no coincide con el de la prensa o si la diferencia supera 2 pp.
- **2019**: en PBA, CABA y Catamarca el ganador del provisorio DINE por sección coincide con el del definitivo G1. **Para las demás provincias de 2019 y para Santiago del Estero 2021 no se pudo hacer el control de prensa** (búsqueda agotada). Santiago del Estero 2021 sí es coherente con diputados nacionales 2021 en la misma provincia: Frente Cívico 62,1 % en gobernador contra 63,5 % en diputados.
- Departamentos sin mesas en la fuente (`departamento_faltantes`): Catamarca 2019, Antofagasta de la Sierra (generales y PASO) y Santa María (PASO). Lezama se suma a Chascomús, igual que en las nacionales.

### Fuerzas (cambios en `fuerzas.json`)

- **Ids nuevos**, todos `cen`: `COM` (Comunidad / La Neuquinidad, Rolando Figueroa), `GSA` (frentes de Gustavo Sáenz, "Sáenz Gobernador" 2019 y "Gustavo Gobernador" 2023), `CHF` (Chubut al Frente, Arcioni 2019) y `FORJA` (Melella 2019, que compitió contra el PJ/FdT de Bertone).
- **Se reutilizan** `HPC` (Hacemos por Córdoba 2019 y Hacemos Unidos por Córdoba 2023), `MPN`, `JSRN` (incluye la alianza con UNE en 2023), `FRC`, `SER` (lema "Por Santa Cruz" 2023) y `FAP` (Frente Progresista santafesino 2019). Se amplió el `motivo` de HPC, SER y FAP.
- **Frentes provinciales asignados a la fuerza nacional**: Cambia Jujuy, Cambia Mendoza, Vamos Tucumán, Córdoba Cambia, Chaco Somos Todos, Cambiemos en cada provincia, Frente Amplio Formoseño, San Luis Unido / Cambia SL (Poggi) y Nueva Santa Cruz → JXC. Creer Entre Ríos, Frente Chaqueño, Elegí Mendoza, FREJUPA, PJ de Formosa, Frente Justicialista de Jujuy, Frente Patriótico Chubutense, Frente Todos (San Juan), Frente Juntos (Santa Fe), Frente Unidad Justicialista (San Luis) y Frente Cívico por Santiago 2021 → FDT, y sus equivalentes de 2023 → UXP.
- **Decisiones a revisar** (también en las `notas` de cada elección):
  - TDF 2019: la fuente solo trae las fórmulas ("Melella - Urquiza" → FORJA, "Bertone - Arcando" → FDT). TDF 2023: "Frente Unidos Hacemos Futuro" (Melella) → UXP; PRO y Republicanos Unidos, que compitieron por fuera de "JxC Tierra del Fuego" → OJXC.
  - Misiones 2019 y 2023: Lenguaza → FDT/UXP. Río Negro 2023: "Vamos con Todos" (Horne) → UXP. Salta 2023: "Avancemos" (Estrada) → UXP.
  - Córdoba 2023: "Creo en Córdoba de Todos" → OPJ. Formosa 2023: "Libertad, Trabajo y Progreso" (Paoltroni) → ODE.
  - Partido Obrero con lista propia (Misiones, Formosa, Chaco "Del Obrero", Chubut "Del Obrero") → FIT; Política Obrera → OIZ.
  - Peronismo disidente → OPJ: Comunidad Organizada (La Pampa), Juntos por la Gente (San Luis 2019), Hacemos Tucumán (Alperovich), Juntos por Jujuy (Snopek), Frente Grande (Salta).
  - Fuerza Republicana (Tucumán), Olmedo Gobernador (Salta 2019), Frente Integrador (Chaco 2019) y Santa Cruz Somos Todos → PROV. En Chubut 2023 (sin cifras), Luque (oficialismo) → PROV. En Mendoza 2023 (sin cifras), De Marchi → PROV.
  - **Incoherencias con la sección 7 (intendentes)**, a unificar: allí se sugieren `LUM` (La Unión Mendocina, der) y `UPCSF` (Unidos para Cambiar Santa Fe), y el frente de Sáenz va a PROV. Aquí Sáenz → GSA, De Marchi → PROV y Pullaro → JXC.

## 9. Legislaturas provinciales (`legislaturas.json`)

Generado con `python3 /home/claude/scripts/leg/build.py [salida]` (por defecto escribe `datos/electoral/legislaturas.json`). Hay un módulo por provincia (`/home/claude/scripts/leg/p_*.py`) con los datos cargados y la fuente de cada cifra; `common.py` tiene las ayudas (lectura de la API, cruce con los ids de departamento de `argentina.json`). Los datos que se extrajeron con scripts de PDF o de la API están en `salta_data.json` (`gen_salta.py`), `pba25.json` (`gen_pba.py`) y `api_data.json` (`gen_api.py`). Las descargas están en `/home/claude/raw/leg/` (`pdf/`: informes DINE; `20*_*/`: JSON de resultados.gob.ar; `dine2019_html/`: páginas DINE 2019). La API se baja con `python3 -I /home/claude/scripts/leg_rgob_fetch.py <dir> <año> <idEleccion> <idCargo,...> [<idDistrito,...>]`. La salida es determinista y el build avisa si las bancas de una elección no suman las bancas en juego o si una composición no suma el total de la cámara. Ningún número se completó de memoria: lo que falta queda en `null` y se explica en `notas`.

### Fuentes

- **L1. DINE, "Elecciones provinciales 2019"** (escrutinio definitivo por provincia): `https://www.argentina.gob.ar/interior/observatorioelectoral/analisis-politico-electoral/<provincia>`. Se usó para las elecciones de 2019 de Chubut, Córdoba, Entre Ríos (diputados), La Pampa, Neuquén, Río Negro, San Juan, Santa Cruz, Santa Fe (diputados) y Tierra del Fuego.
- **L2. DINE, informes "Elecciones provinciales 2023"** (PDF, `https://www.argentina.gob.ar/sites/default/files/2023/MM/<provincia>_2023_-_elecciones_provinciales*.pdf`, enlazados desde `/interior/observatorioelectoral/datos-electorales/<provincia>`): Córdoba, Corrientes, Formosa, Jujuy, La Pampa, La Rioja, Misiones, Neuquén, Río Negro, Salta, San Juan, San Luis, Tierra del Fuego y Tucumán. Cada uno dice si cita el provisorio o el definitivo; se copió en `recuento`.
- **L3. DINE, "Informes post electorales 2025"** (escrutinio provisorio; índice en `https://www.argentina.gob.ar/node/478074`): Buenos Aires, CABA, Catamarca, Chaco, Corrientes, Formosa, Jujuy, La Rioja, Mendoza, Misiones, Salta, San Luis y Santiago del Estero.
- **L4. DINE, "Elecciones 2025: bancas en juego por bloques legislativos nacionales y provinciales"**, `https://www.argentina.gob.ar/sites/default/files/2025/09/bancas_en_juego_2025_nacional_y_provincial.pdf`. Por provincia da, por bloque, las bancas en juego en 2025 (electas en 2021) y el total. Con eso se armaron composiciones y, donde no había otra fuente, las bancas de 2021 o 2023 (ver "Cálculos y derivaciones").
- **L5. DINE, API de resultados.gob.ar** (provisorio): las categorías provinciales que se contaron junto con la nacional. Generales 2023: diputados de la Ciudad, senadores y diputados bonaerenses (con `idSeccionProvincial` para cada sección electoral) y legisladores de Catamarca. PASO 2023 (13-08-2023): diputados de Santa Cruz, cuya general provincial fue ese día. Generales 2021: diputados de Santiago del Estero. Las secciones suman exactamente el total de distrito de la misma API.
- **L6. Prensa y otros**: La Voz del Interior (escrutinio oficial de Córdoba 2023), LetraP y Hoy Día (bancas de Córdoba 2023), La Nación (bancas departamentales de Córdoba 2019), informe de la UCA sobre Chubut 2023 (bancas, electores) y Wikipedia "2023 Chubut provincial elections" (votos por lista de Chubut 2023, que cita datosoficiales.juschubut.gov.ar; no hubo segunda fuente para esos votos). Las URL están en cada elección.
- No accesibles: los tribunales electorales provinciales (Santa Fe, Entre Ríos, Tucumán, Córdoba, Chubut, Junta Electoral PBA), que la DINE enlaza para el detalle por departamento. El cupo de búsquedas web de la corrida se agotó antes de terminar: las elecciones sin datos quedaron así por eso.

### Cobertura

`V` = votos por fuerza; `B` = bancas obtenidas; `C` = composición resultante; `D` = detalle por departamento (cantidad con id del mapa).

| Distrito | Última | Anterior |
|---|---|---|
| Buenos Aires | 2025 (L3) Dip y Sen: V B C, por sección | 2023 (L5) Dip y Sen: V por sección, D 77 y 57; B no; C por bloque (L4) |
| Catamarca | 2025 (L3) Dip V B C; Sen B C, D 8 (falta Antofagasta de la Sierra) | 2023 (L5) Dip V B C D 16; Sen V B C D 8 |
| Chaco | 2025 (L3) V B C | 2023: sin votos; B y C por bloque (L4) |
| Chubut | 2023 V B C (votos de Wikipedia) | 2019 (L1) V B C |
| CABA | 2025 (L3) V B C | 2023 (L5) V C D 15; B calculadas (D'Hondt) |
| Córdoba | 2023 V B C, D 26 (solo las dos primeras fuerzas, provisorio) | 2019 (L1) V B C |
| Corrientes | 2025 (L3) Dip y Sen V B C | 2023 (L2) Dip y Sen V B C |
| Entre Ríos | 2023: **sin datos** | 2019 (L1) Dip V B C; Sen **sin datos** |
| Formosa | 2025 (L3) V B C | 2023 (L2) V B C |
| Jujuy | 2025 (L3) V B C | 2023 (L2) V B C |
| La Pampa | 2023 (L2) V B C | 2019 (L1) V B C |
| La Rioja | 2025 (L3) V B C, D 7, por departamento | 2023 (L2) B C, D 11; sin votos |
| Mendoza | 2025 (L3) Dip V B C; Sen B C (sin votos de la Cuarta sección) | 2023: sin votos ni bancas; C por bloque (L4) |
| Misiones | 2025 (L3) V B C | 2023 (L2) V B C |
| Neuquén | 2023 (L2) V B C | 2019 (L1) V B C |
| Río Negro | 2023 (L2) V B C | 2019 (L1) V B C |
| Salta | 2025 (L3) Dip V B C D 11; Sen B C D 12 | 2023 (L2) Dip V B D 15; Sen V B D 11; C no |
| San Juan | 2023 (L2) V B C, D 19 (ganador de la banca) | 2019 (L1) V B C |
| San Luis | 2025 (L3) Dip B C (V sin Gobernador Dupuy), D 5; Sen V B C D 4 | 2023 (L2) Dip y Sen V B C, D 4 y 5 |
| Santa Cruz | 2023 (L5) V, D 7; **sin bancas ni composición** | 2019 (L1) V B C |
| Santa Fe | 2023: **sin datos** | 2019 (L1) Dip V B C; Sen **sin datos** |
| Santiago del Estero | 2025 (L3) V B C | 2021 (L5 y L4) V B C D 27 |
| Tierra del Fuego | 2023 (L2) V B C | 2019 (L1) V B C |
| Tucumán | 2023 (L2) V B C, por sección | 2019: **sin datos** |

Recuento: todo 2025 y las elecciones de L5 son escrutinio provisorio; las de L1 son definitivas; las de L2 dicen en cada caso cuál citan.

### Ciclos

Renovación total cada 4 años: Chubut, Córdoba, Entre Ríos, La Pampa, Neuquén, Río Negro, San Juan, Santa Cruz, Santa Fe, Santiago del Estero (2021 y 2025), Tierra del Fuego y Tucumán; para ellas, las dos últimas son 2023 y 2019, salvo Santiago del Estero. Renovación por mitades cada 2 años (2025 y 2023): Buenos Aires, Catamarca, Chaco, CABA, Formosa, Jujuy, La Rioja, Mendoza, Misiones, Salta y San Luis. Corrientes: Diputados por mitades y Senado por tercios (mandato de 6 años). Por secciones o departamentos: Buenos Aires (8 secciones, cada una elige diputados o senadores en años alternos), Mendoza (4 secciones), Tucumán (3 secciones), Salta, San Luis y La Rioja (departamentos), y los senados de Catamarca, Salta, San Luis, Entre Ríos y Santa Fe (uno por departamento). En esos casos `por_seccion` = true, `secciones` trae el detalle y `fuerzas` es la suma de las secciones que votaron.

### Composición resultante

- Renovación total: suma de las bancas obtenidas.
- Renovación parcial: bancas obtenidas en la última elección más las de la anterior (los mandatos que siguen), según la fuerza por la que fue electo cada legislador. Es lo que hace el build cuando no hay otra indicación.
- Donde faltan las bancas de una de las dos elecciones (Buenos Aires, Mendoza, Chaco 2023, Formosa 2023, Misiones 2023) o la cámara renueva por tercios (Senado de Corrientes), la composición sale de los bloques de L4 o de L2/L3. Esos son bloques legislativos vigentes, que pueden haber cambiado después de la elección; `composicion_metodo` lo aclara en cada caso. `sin_clasificar` agrupa los bloques cuyo origen no consta (por ejemplo "Unión, Renovación y Fe" en Diputados bonaerenses); `sin_datos`, la banca de Antofagasta de la Sierra (Catamarca 2025).

### Cálculos y derivaciones (revisar si aparece la fuente oficial)

- **CABA 2023**: bancas calculadas por D'Hondt sobre el provisorio (JxC 15, UxP 10, LLA 4, FIT 1). La última banca se define por 55 votos entre UxP y JxC. Control: L4 da 10 bancas de UxP y 1 del PTS-FIT electas en 2023.
- **Catamarca 2023, Diputados**: UxP 11, LLA 5, JxC 4, a partir de L4 (bancas que siguen por bloque). Coincide con un D'Hondt sobre el provisorio. Senado: UxP ganó los 8 departamentos (L5), lo que coincide con L4.
- **Santiago del Estero 2021**: bancas de L4 (bancas en juego en 2025 = las 40 de 2021: Frente Cívico 16, Frente Justicialista 12, JxC 5, Frente Renovador y Progresista 4, Frente Patriótico Laborista 3).
- **Chaco 2023**: bancas por bloque de L4 (JxC 8, PJ 6, Frente Grande 1, PTP 1), sin votos.
- **Santa Fe 2019**: la DINE deja en blanco las bancas de Frente Social y Popular e Igualdad y Participación (2 y 2). Se calcularon por D'Hondt sobre las 22 bancas de minoría; el cálculo reproduce las bancas que la DINE sí da a las demás listas.
- **Salta 2023**: en el PDF, la tabla de General José de San Martín no tiene encabezado. Se identificó por descarte y por su tamaño.
- **Errores de las fuentes**: la DINE repite la tabla de diputados en la de senadores de la Cuarta sección de Mendoza 2025, y la de General Belgrano en la de Gobernador Dupuy (San Luis 2025). En esos casos se cargaron solo las bancas. Río Negro 2019: "7.85" se leyó como 7.850 (coincide con el 2,03 %).

### Fechas

Las de 2019 (L1), 2025 (L3), las elecciones de L5 y las de Córdoba, Chubut, Corrientes, San Juan, Tucumán y Mendoza 2023 están en las fuentes. Para La Pampa, Neuquén, Río Negro, Tierra del Fuego, Jujuy, Formosa, Misiones, La Rioja, Salta, San Luis, Chaco, Santa Fe y Entre Ríos 2023 la fecha no figura en las fuentes citadas: `fecha_verificada` = false.

### Fuerzas

Se siguen los ids de `fuerzas.json` (incluidos los agregados por la tarea de Gobernador: `COM`, `GSA`, `CHF`, `FORJA`), por lo que `fuerzas_sugeridas` queda vacío. El frente peronista principal va a `FDT` (2019 y 2021), `UXP` (2023) o `FP` (2025). Criterios a revisar:
- Frentes de gobernadores en 2025: Vamos Corrientes y Frente Jujuy Crece → `PU`, como en fuerzas.json para 2025, aunque en 2023 los mismos espacios (ECO + Vamos Corrientes, Cambia Jujuy) van a `JXC`. Chaco Puede + LLA y LLA + Cambia Mendoza → `LLA`. Ahora San Luis (Poggi, mayo de 2025, separado de LLA) → `OJXC`.
- Otros frentes provinciales: oficialismo de Sáenz → `GSA` (en 2023 incluye al PJ salteño, que integró "Gustavo Gobernador"); Comunidad y Desarrollo Ciudadano (Figueroa) → `COM`; Chubut al Frente → `CHF`; Forja (Melella) → `FORJA` en 2019 y 2023; UNE (Río Negro 2023) → `JSRN`; Por Santa Cruz → `SER`; Frente Progresista santafesino → `FAP`.
- Frente Cívico por Santiago → `FP` (2025) y `FDT` (2021), como en fuerzas.json; el PJ santiagueño, aliado, → `OPJ`. ECO (Colombi, Corrientes 2025) → `PROV`.
- Tucumán 2023: las listas "acople" sin bancas cuya alineación no consta quedan en `OTR` con `acople_verificado` = false; los votos de UXP y JXC están subestimados.
- La Unión Mendocina (De Marchi) cuenta como `cen` en las composiciones de Mendoza. Las secciones 7 y 8 no coinciden en este punto (`LUM` der contra PROV).

### Pendientes

Entre Ríos 2023 (ambas cámaras) y Senado 2019; Santa Fe 2023 (ambas cámaras) y Senado 2019; Tucumán 2019; Mendoza 2023 (votos y bancas por lista); Chaco 2023 (votos); Santa Cruz 2023 (bancas); Salta 2023 (composición); Buenos Aires 2023 (bancas por lista y sección). También faltan los votos de Chubut 2023 en una segunda fuente y el definitivo de todas las elecciones de 2025.


## Unificación de códigos de fuerzas (25/10/2026)

- Unidos para Cambiar Santa Fe (Pullaro, 2023): JXC en gobernador, intendentes y legislaturas.
- La Unión Mendocina (De Marchi, 2023): centro en los tres archivos (en intendentes se conserva el id LUM, con bloque centro).
- Frentes de Gustavo Sáenz (Salta): GSA en gobernador; en intendentes y legislaturas quedan como PROV. Ambos son centro, así que la vista por afinidad no cambia.


## Escrutinio definitivo (25/10/2026)

Los 10 archivos nacionales (`presidente-2019-paso`, `presidente-2019-generales`, `presidente-2023-paso`, `presidente-2023-generales`, `presidente-2023-balotaje`, `diputados-2021-paso`, `diputados-2021-generales`, `diputados-2025-generales`, `senado-2021-generales`, `senado-2025-generales`) tienen ahora **provincia y país con el escrutinio definitivo** y **departamento con el provisorio**. Cada JSON lleva `"recuento": "definitivo (provincia y país); provisorio (departamento)"`, `"recuento_departamento": "provisorio"`, `fuente_departamento`/`url_departamento` (la fuente provisoria anterior) y `pais_provisorio` (el total país anterior, para comparar). La suma de departamentos ya **no** coincide con la provincia: los departamentos siguen siendo los del provisorio.

Copias de los archivos anteriores (provisorio puro), de `fuerzas.json` y de este FUENTES.md: `/home/claude/work/electoral_provisorio/`. `fuerzas.json` **no se regeneró ni se tocó** (sigue idéntico a la copia; se mantienen la unificación de códigos y el nombre "Fuerza Patria y aliados").

### Dónde se buscó un definitivo por sección (no existe en ninguna fuente accesible)

- **CNE** (`www.electoral.gob.ar`, accesible desde esta etapa): páginas de cada elección (`/nuevo/paginas/btn/elecc2019.php`, `elecc2021.php`, `elecc2023.php`, `elecc2025.php`) y de actas (`escrutinio2021.php`, `actas_esc_pri_2021.php`, `/nuevo/paginas/pdf/actas_escrutinio/2023/PASO/actas.php`, `actas_esc_generales2023.php`, `actas_esc_segvta2023.php`, `actas2025.php`), publicaciones y "Estadísticas" (solo participación, padrón y alianzas). Lo único con resultados son las **actas de escrutinio definitivo de cada Junta Electoral Nacional**, en PDF, **por distrito** (sin detalle por sección; varias son escaneos).
- **DINE** (`www.argentina.gob.ar/dine/resultados-electorales/elecciones-AAAA`): 2019, xlsx de definitivo por distrito (presidente generales; total país PASO y generales); 2021, rar con xlsx "Consulta de Escrutinio por Zona" por distrito (diputados y senadores, PASO y generales); 2023 y 2025, ningún definitivo.
- **datos.gob.ar** (CKAN): solo datasets de resultados provisorios (`resultados-provisionales-elecciones-*`, `elecciones_legislativas_2025`). Búsquedas "escrutinio definitivo" y "definitivo": 0 resultados.
- **resultados.gob.ar**: la API solo acepta `recuento=Provisorio` (con `recuento=Definitivo` responde "Error al obtener el resultados" o una lista vacía; el JS de la web tiene `recuento:"Provisorio"` fijo).

Por eso, en los 10 archivos, el definitivo cubre provincia y país y el departamento sigue provisorio.

### Fuentes y método por archivo

| Archivo | Provincia y país (definitivo) | Fuente del definitivo | Departamento |
|---|---|---|---|
| presidente-2019-paso | 24 distritos | Votos por provincia de PoliticaArgentina/data_warehouse (`electorAr/data/escrutinios_definitivos/*_presi_paso2019.csv`, ya descargados en `raw/polar_dw/def2019/`), **controlados contra las actas CNE** ("2019 - Actas escrutinio PASO.zip"): `control_actas_cne` en el JSON | provisorio |
| presidente-2019-generales | 24 distritos | DINE, `p.v._definitivo_x_distrito_grales_2019.xlsx` (incluye exterior, privados de libertad y comando; coincide con las actas CNE) | provisorio |
| diputados-2021-paso | 24 distritos | DINE, `diputados_paso_2021.rar` (xlsx por distrito) | provisorio |
| diputados-2021-generales | 24 distritos | DINE, `diputados_generales_2021.rar` | provisorio |
| senado-2021-generales | 8 distritos | DINE, `senadores_generales_2021.rar` | provisorio |
| presidente-2023-paso | 23 distritos definitivos; **Buenos Aires sigue provisoria** | Actas CNE de las PASO 2023 | provisorio |
| presidente-2023-generales | 24 distritos | Actas CNE de las generales 2023 | provisorio |
| presidente-2023-balotaje | 24 distritos + residentes en el exterior + privados de libertad (`fuera_de_distrito`) | Actas CNE de la segunda vuelta + planillas RERE y REPL de la CNE | provisorio |
| diputados-2025-generales | 24 distritos | Actas CNE 2025 | provisorio |
| senado-2025-generales | 8 distritos | Actas CNE 2025 | provisorio |

Scripts (en `/home/claude/scripts/cne/`; todos con `python3 -I`):
- `fetch_actas.py`: baja las actas listadas en las páginas de la CNE a `/home/claude/raw/cne/<elección>/`.
- `totext.py`: texto de cada acta (capa de texto si es limpia; si no, OCR con tesseract a 300 dpi) en `/home/claude/raw/cne/txt/`.
- `parse_actas.py`: extrae por categoría emitidos/afirmativos/blancos/recurridos/impugnados/nulos y las líneas "nombre votos" (`/home/claude/work/cne_parse/*.json`).
- `def_2019.py`, `def_2021.py`, `def_2023.py <paso|generales|balotaje> <parsed> --write`, `def_2025.py <parsed> --write`: arman los JSON. `def_common.py`: utilidades (emparejamiento de listas, unidades, escritura).
- `transc_2023_paso.py`, `transc_2023_generales.py`, `transc_2023_balotaje.py`, `transc_2025.py`: **transcripción revisada** de los distritos donde la extracción automática no cerraba (tablas en imagen, OCR defectuoso, nombres y números en líneas distintas). Cada valor se leyó de la capa de texto o de la imagen de la página (renderizada con pdftoppm) y se controló con las sumas del propio acta. Cada distrito trae en el JSON (`transcripcion`) el archivo, si salió de la extracción automática o de la transcripción, y una nota.
- `check_presi.py`, `xcheck_2019.py`, `xcheck_json.py`: controles.

Regla de uso de un distrito extraído automáticamente: la suma de las listas tiene que ser igual a "votos afirmativos" del acta y afirmativos + blancos + nulos (+ recurridos + impugnados) igual a "total de votos emitidos". Si no, se transcribe a mano.

**Asignación a fuerzas (sin cambios):** cada lista del definitivo se emparejó con su lista del provisorio del mismo distrito y toma su fuerza (la de `fuerzas.json`). El emparejamiento es por nombre (igual, sin prefijos "ALIANZA"/"PARTIDO", o por similitud) y además exige votos compatibles (provisorio/definitivo entre 0,80 y 1,25 en 2021; entre 0,85 y 1,15 en 2025). Los emparejamientos que no son por nombre idéntico quedan listados (2025: `emparejamientos_listas` en el JSON; 2021: ejemplos como "CO.PE.BO." → "CORRIENTE DE PENSAMIENTO BONAERENSE", "AZA.JUNTOS" → "JUNTOS", "UNITE P/LA LIB. Y LA DIGN." → "UNITE POR LA LIBERTAD Y LA DIGNIDAD"). En 2019 y 2023 presidenciales las agrupaciones son nacionales y el emparejamiento es directo (en la PASO 2023, por lista interna: "Celeste y Blanca" y "Justa y Soberana" → Unión por la Patria, etc.). No quedó ninguna lista del definitivo sin pareja ni ningún id nuevo. `listas` del JSON conserva los nombres del provisorio con los votos definitivos. En las PASO, `listas_internas` sigue siendo el provisorio (`"listas_internas_recuento": "provisorio"`).

**Campos de provincia:** `electores` y `mesas` son los del párrafo PRIMERO del acta (o de la planilla anexa); `votantes` = total de votos emitidos del acta; `positivos` = suma de las listas; `recurridos`/`impugnados` cuando el acta los informa (si no, `otros` = null). Sin `comando`: el definitivo no lo separa.

### Controles contra cifras oficiales (total país definitivo)

| Archivo | Definitivo (este dataset) | Referencia | Resultado |
|---|---|---|---|
| Presidente 2019 generales | FdT 12.946.037 (48,24 %), JxC 10.811.586 (40,28 %) de los afirmativos | 48,24 / 40,28 | OK, exacto |
| Presidente 2019 PASO | FdT 47,79 %, JxC 31,80 % de los válidos (12.205.938 / 8.121.689) | Chequeado: 47,78 / 31,79 definitivo | OK (≤ 0,01 pp). El xlsx "total país" de la DINE da FdT 12.205.085 y JxC 8.121.596 (diferencias de 853 y 93 votos, que no se pueden atribuir a una provincia: ese xlsx no desagrega por distrito) |
| Presidente 2023 generales | UxP 9.853.492 (36,78 %), LLA 8.034.990 (29,99 %), JxC 6.379.023 (23,81 %), HxNP 1.802.068 (6,73 %), FIT 722.061 (2,70 %) | 36,78 / 29,99 / 23,83 | Massa y Milei OK. Bullrich da **23,81 %**, no 23,83: 6.379.023 / 26.791.634 afirmativos. No se forzó la cifra; 23,83-23,84 es el valor del provisorio |
| Presidente 2023 balotaje | LLA 14.596.752 (55,65 %), UxP 11.631.822 (44,35 %) con exterior y privados de libertad; solo los 24 distritos: 14.554.560 / 11.598.720 (`pais_solo_distritos`) | 55,65 / 44,35 | OK. Los 24 distritos suman exactamente las cifras definitivas que se publicaron (14.554.560 / 11.598.720). Residentes en el exterior (UxP 12.833 / LLA 37.413) y privados de libertad (20.269 / 4.779) los escrutó la CNE como distrito único y van en `fuera_de_distrito`; con ellos el porcentaje sigue siendo 55,65 / 44,35 |
| Presidente 2023 PASO | Sobre válidos: LLA 29,97, JxC 28,10, UxP 27,19 (Buenos Aires provisoria) | Provisorio oficial 30,04 / 28,27 / 27,27 | Sin definitivo nacional publicado para comparar; ver la salvedad de Buenos Aires |
| Diputados 2021 generales | JxC 40,48 %, FdT 32,64 % de los válidos; 23.602.493 afirmativos | — | Sumas por distrito = TOTALES del xlsx DINE en los 24 distritos; Chaco controlado contra el acta CNE: idéntico |
| Diputados 2021 PASO | JxC 39,68 %, FdT 31,12 % de los válidos; 21.765.879 afirmativos | Mismo total que el control de §2 | OK |
| Senado 2021 | JxC 45,22 %, FdT 26,63 % de los válidos (8 distritos) | — | Sumas = TOTALES del xlsx |
| Diputados 2025 | LLA 9.437.860 (40,66 % de los afirmativos; 39,46 % de los válidos), FP 7.739.305 (33,34 % / 32,36 %), PU 1.587.890 (6,84 % / 6,64 %) | Provisorio: LLA 9.341.798, FP 7.637.537 | Mismo orden y diferencias de 0,1 pp como máximo |
| Senado 2025 | LLA 42,01 %, FP 34,65 % de los afirmativos (8 distritos) | — | — |

Controles internos (en todos): suma de fuerzas = positivos en cada provincia; listas = fuerzas; departamentos idénticos a la copia provisoria; ningún id de fuerza nuevo; `fuerzas.json` sin cambios. Electores definitivos contra provisorios: provisorio/definitivo entre 0,90 y 1,02 en todos los distritos (sirvió para descartar errores de OCR como "300.057 0" en La Pampa o "13194930" en Tucumán). Controles cruzados con las actas CNE de las cifras que vienen de xlsx/csv (buscando la cifra literal en el texto u OCR del acta): 2019 PASO, la mayoría de las cifras aparece tal cual (las que faltan son tablas que el OCR no leyó; Tucumán se verificó contra la imagen y coincide en las 10 listas). 2021 generales (`xcheck_json.py`): 159 de 182 cifras encontradas; las faltantes son tablas escaneadas que el OCR no leyó (Córdoba, Neuquén, San Juan, Tucumán). 2021 PASO: 173 de 236; además de las tablas escaneadas, faltan los totales de agrupaciones con varias listas internas, porque el acta solo da las listas (ejemplo verificado: Chaco, JxC 138.457 + 93.455 + 18.662 = 250.574, igual que la DINE). 2019 generales: en Catamarca el acta CNE confirma blancos 23.100 y nulos 1.841, que son las cifras de la DINE; el definitivo de data_warehouse que estaba en `definitivo_control` traía 40.180 / 1.074, que son los de otra categoría. En Neuquén el acta CNE (1.ª versión) aún no incluía a los residentes en el exterior (FdT 194.158); la DINE sí los incluye (194.205), y con ella cierra el total oficial 12.946.037.

### Inconsistencias de las propias actas (no se corrigió ninguna cifra)

Cuando la suma de listas no coincide con "votos afirmativos" del acta, se usan los votos por lista. Casi siempre ese "afirmativos" incluye los blancos o los nulos, y la suma de listas + blancos + nulos da exactamente los emitidos. Cada caso queda en `controles_definitivo` y en la nota de `transcripcion`:
- PASO 2023: Corrientes ("afirmativos 635.243"; las listas suman 613.873 = emitidos − blancos − nulos), Jujuy ("436.554" = 414.080 + blancos; las listas suman 414.078, 2 menos), Río Negro (incluye nulos), Santa Fe (incluye blancos), Chaco (las listas suman 5 votos menos que el afirmativos del acta, que sí cierra con emitidos).
- Generales 2023: Corrientes (incluye blancos), San Juan (incluye nulos).
- Balotaje 2023: Corrientes y Santa Fe (incluyen blancos), San Juan (incluye nulos).
- Diputados 2025: Corrientes y Santa Fe (incluyen blancos).
- **Electores:** Corrientes 2025 dice "sobre un total de 651.679 electores … el 59,99 %", y las dos cifras no son compatibles. San Luis (PASO, generales y balotaje 2023 y 2025) no informa electores. En 2023 se usó el padrón de la CNE (`total_electores_2023.zip`, nota en el JSON). En 2025 (Corrientes y San Luis) `electores` queda con el provisorio y la provincia lleva `"electores_recuento": "provisorio"`.
- **Buenos Aires, PASO 2023:** el acta presidencial de la Junta bonaerense solo trae emitidos 9.315.160, afirmativos 8.576.307, blancos 656.356 y nulos 82.497, sin desagregar por agrupación ni lista. La provincia queda con el provisorio (`"recuento": "provisorio (…)"` dentro de su entrada) y el total país de la PASO 2023 mezcla 23 distritos definitivos con Buenos Aires provisoria (lo dice `recuento` del archivo). `pais.mesas` es null porque el acta de San Luis no informa mesas.

### Diferencias con el provisorio (total país)

| Archivo | Afirmativos provisorio → definitivo | Principales fuerzas: definitivo (provisorio) | Provisorio/definitivo de afirmativos por provincia |
|---|---|---|---|
| presidente-2019-paso | 24.292.208 → 24.660.382 | FdT 49,50 (49,40), JxC 32,93 (33,01), CF 8,44 (8,45) % afirm. | 0,964 (Buenos Aires) a 1,000 |
| presidente-2019-generales | 26.742.165 → 26.838.336 | FdT 48,24 (48,29), JxC 40,28 (40,22) | 0,986 (TDF) a 0,999 |
| presidente-2023-paso | 22.539.543 → 22.923.187 | LLA 31,65 (31,57), JxC 29,67 (29,72), UxP 28,72 (28,66) | 0,926 (Salta) a 1,000 (Buenos Aires, que sigue provisoria) |
| presidente-2023-generales | 26.291.718 → 26.791.634 | UxP 36,78 (36,69), LLA 29,99 (29,99), JxC 23,81 (23,84), HxNP 6,73 (6,79) | 0,949 (San Juan) a 0,996 |
| presidente-2023-balotaje | 25.992.604 → 26.228.574 | LLA 55,65 (55,69), UxP 44,35 (44,31) | 0,975 (Jujuy) a 0,999 |
| diputados-2021-paso | 21.286.049 → 21.765.879 | JxC 39,68 (39,86), FdT 31,12 (31,03) % válidos | 0,906 (Catamarca) a 0,997 |
| diputados-2021-generales | 23.238.621 → 23.602.493 | JxC 40,48 (40,64), FdT 32,64 (32,57) | 0,939 (Formosa) a 0,999 |
| senado-2021-generales | 6.959.726 → 7.018.937 | JxC 45,22 (45,36), FdT 26,63 (26,66) | 0,975 (Corrientes) a 0,996 |
| diputados-2025-generales | 22.977.871 → 23.212.615 | LLA 39,46 (39,51), FP 32,36 (32,30), PU 6,64 (6,66) | 0,970 (Salta) a 0,997 |
| senado-2025-generales | 5.218.954 → 5.286.932 | LLA 40,87 (40,92), FP 33,71 (33,69) | 0,971 (Salta) a 0,995 |

El definitivo agrega las mesas que el provisorio no transmitió, los votos recurridos e impugnados ya resueltos y, en las generales, los de residentes en el exterior y privados de libertad. Por eso tiene siempre más afirmativos y más electores. Algunas listas chicas cambian más del 5 % por distrito (quedan en `controles_definitivo`; por ejemplo Unión Liberal en Buenos Aires 2025, 43.339 en el provisorio y 38.796 en el acta, verificado contra la imagen).

### Archivos descargados (etapa 3)

- `/home/claude/raw/cne/`: páginas HTML de la CNE; actas en `2019/` (zips y su contenido en `x_paso/`, `x_gen/`), `2021_paso/`, `2021_generales/`, `2023_paso/`, `2023_generales/`, `2023_balotaje/` (con `RERE.pdf` y `REPL.pdf`), `2025_generales/`; textos/OCR en `txt/`; xlsx DINE 2019 en `dine_def2019/`; padrón CNE 2023 en `padron/`; páginas DINE en `dine_pages/`; JS de resultados.gob.ar en `rgob_js/`.
- Imágenes de páginas usadas para transcribir: `/home/claude/work/cne_img/`. Extracciones intermedias: `/home/claude/work/cne_parse/`.
