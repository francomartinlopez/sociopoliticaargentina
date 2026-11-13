# Institucionalidad: fuentes

Consulta: 25/10/2026; corte semanal del 30/10/2026. Archivos: `designaciones.json`, `incumplimientos.json`, `corrupcion.json` y `transparencia.json`. No había archivos previos en esta carpeta.

## Reutilización
- **Datos de `datos/justicia/estado.json`:** vacantes (298, 29,7 %), Corte (3 de 5), Procurador interino (Casal) y pliegos de 2026 (218 enviados, 129 aprobados, 2 rechazados). No se recalcularon; `designaciones.json` los referencia.
- **Datos de `datos/congreso/ejecutivo.json`:** fechas de veto e insistencia de las leyes 27.793, 27.795 y 27.796, y el rechazo del DNU 656/2024.
- **Datos de `datos/afinidades`:** el acta 2691, sobre el nuevo acuerdo de Carlos Mahiques.

## Fuentes oficiales consultadas
Argentina.gob.ar/normativa (Infoleg), leído desde la terminal:
- Ley 27.795 ([norma-419006](https://www.argentina.gob.ar/normativa/nacional/norma-419006)) y Decreto 759/2025 ([norma-419007](https://www.argentina.gob.ar/normativa/nacional/norma-419007)): "Promúlgase … sin perjuicio de lo dispuesto por el artículo 5° de la Ley N° 24.629".
- Ley 27.796 ([ley-27796-419008](https://www.argentina.gob.ar/normativa/nacional/ley-27796-419008)) y Decreto 760/2025 ([norma-419009](https://www.argentina.gob.ar/normativa/nacional/norma-419009)), con los considerandos de costo fiscal ($196.270 millones) y déficit de Salud ($102.400 millones).
- Resolución 542/2026 de Salud ([norma-425270](https://www.argentina.gob.ar/normativa/nacional/norma-425270)), sobre residencias.
- El Boletín Oficial (boletinoficial.gob.ar) no se pudo abrir: robots.txt. El Decreto 681/2025 se tomó de Palabras del Derecho (22/09/2025).

## Hallazgos principales
- **$LIBRA:** el 23/10/2026 el juez Martínez de Giorgi sobreseyó a Javier y Karina Milei y a otros nueve investigados, a pedido del fiscal Taiano y sin indagatorias. Fuentes: [Ámbito](https://www.ambito.com/politica/el-celular-mauricio-novelli-un-supuesto-acuerdo-y-los-millones-cripto-las-pruebas-que-no-alcanzaron-la-causa-libra-n6337466) y [El Heraldo](https://www.elheraldo.com.ar/noticias/judiciales/la-justicia-sobreseyo-al-presidente-javier-milei-y-a-su-hermana-karina-en-la-causa-libra). Antes se había apartado a las querellas (03/07/2026), decisión que la Cámara confirmó el 04/09/2026 ([Infobae](https://www.infobae.com/judiciales/2026/09/04/confirmaron-la-decision-de-apartar-a-las-querellas-en-la-causa-libra/)).
- **ANDIS:** 19 procesados el 09/02/2026, confirmados por la Cámara Federal el 22/09/2026.
- **Adorni:** el expediente está en etapa de justificación patrimonial (juez Lijo, fiscal Pollicita), sin indagatoria. Presentó su descargo el 21/09/2026 y el fiscal pidió nuevas medidas el 28/09/2026.
- **Espert:** citado a indagatoria el 23/06/2026 (juez Mirabelli, San Isidro).
- **Ley 27.795:** el 06/10/2026 el juzgado declaró inconstitucional el Decreto 759/2025 y ordenó cumplir la ley de inmediato. La Corte ya había dejado firme la cautelar el 25/06/2026.
- **Informes del jefe de Gabinete:** 7 presentados desde dic. 2023 (Posse 1, Francos 5, Adorni 1, Santilli 0). Ningún jefe de Gabinete fue al Senado desde el 26/06/2025.

## Criterios
- **Etapa judicial:** se toma la etapa más alta alcanzada y se aclara en `etapa_nota`. En $LIBRA, "imputación" significa que el fiscal impulsó la acción nombrando al Presidente; no hubo indagatorias. En el caso Adorni se deja "denuncia", porque las fuentes no informan una imputación formal ni una indagatoria.
- **Respuesta oficial:** cita breve o paráfrasis marcada como tal.
- **Responsabilidad de la AGN y la Defensoría del Pueblo:** la AGN la designó Diputados y la Defensoría depende del Congreso. Se marcan como responsabilidad del Congreso, no del Ejecutivo.

## Discrepancias
- **ANDIS:** Buenos Aires Times dice que la Cámara "ordenó el juicio"; Perfil habla de confirmación de procesamientos. Se usa "procesamiento".
- **Juzgados:** el de ANDIS figura como Juzgado Federal N° 11 en las fuentes, con Casanello y luego Lijo como subrogante. Para $LIBRA no se confirmó el número del juzgado de Martínez de Giorgi.
- **Renuncia de García-Mansilla:** la carta fue del 14/04/2025 según Diario Judicial; el Decreto 276/2025 fija la vigencia desde el 07/04/2025.

## Faltantes
- **AAIP:** la tasa de pedidos denegados y la serie posterior a abril de 2025 no se pudieron calcular, porque el proxy rechazó `descarga.aaip.gob.ar`. Tampoco se verificó quién dirige hoy la AAIP.
- **Decretos y estadísticas:** no hay conteo publicado de decretos secretos o reservados, ni relevamiento de estadísticas discontinuadas.
- **Ley 27.793:** no se sabe si el fallo de Campana quedó firme ni cómo están los aranceles en 2026.
- **Ley 27.796:** no se encontró resolución del amparo del Garrahan, ni si la emergencia de un año se considera vencida.
- **Sentencia del 06/10/2026 (Ley 27.795):** no se sabe si el Estado la apeló.
- **Amparo del PRO sobre la AGN:** no se encontró resolución.
- **Espert:** falta la fecha de la indagatoria y si declaró.
- **Sobreseimiento de $LIBRA:** pendiente de las quejas ante Casación.

## Corte del 30/10/2026
- **$LIBRA:** el sobreseimiento del 23/10 no está firme. Lo apelaron las querellas apartadas (27/10; El Destape, Revista Quórum) y la PIA pidió reabrir la causa y apeló en subsidio ante la Sala I de la Cámara Federal (Infobae, 30/10). Según Infobae, el fiscal Taiano no apeló. Misiones Online tituló que «la Fiscalía Anticorrupción apeló», pero la nota no abrió: se toma la versión de Infobae.
- **ANDIS:** el 29/10 trascendió un informe de Gendarmería sobre los audios de Spagnuolo. Infobae y MDZ titulan que «no son auténticos»; Página/12, Rosario3 y La Capital, que «no pudo determinar» su autenticidad, y según La Capital todavía no hay informe firmado en el expediente. Se carga la versión prudente. La etapa (procesamiento confirmado) no cambia.
- **Espert:** pasa de imputación a **procesamiento**: el 22/10/2026 Mirabelli lo procesó por presunto lavado, con prohibición de salir del país y embargo de $1.000 millones (MDZ, Canal 26, Tiempo de San Juan). Apeló el 27/10 ante la Cámara Federal de San Martín. En la indagatoria del 07/07/2026 no respondió preguntas y presentó un escrito. Este dato era anterior al corte del 25/10 y se había pasado por alto.
- **Ley 27.795:** el Estado apeló la sentencia del 06/10; el juez concedió el recurso con efecto suspensivo y mantuvo la cautelar (iProfesional, 09/10/2026). Se cierra ese faltante.
- **Informes del jefe de Gabinete:** Santilli acordó presentar su primer informe en el Senado el 25/11/2026 (Infobae, 29/10). No cambia el conteo hasta que ocurra.
- **Sin cambios:** designaciones (el Senado solo dio ingreso a nuevas postulaciones judiciales el 29/10, sin votación).

## Corte del 06/11/2026
Búsqueda del 30/10 al 06/11/2026.
- **$LIBRA (etapa: imputación; estado: sobreseimiento no firme):** el 04/11 la Sala II de Casación (Slokar y Ledesma; Yacobucci en disidencia) hizo lugar a la queja de los damnificados apartados y concedió el recurso de casación contra su apartamiento ([El Destape](https://www.eldestapeweb.com/politica/reves-milei-libra-camara-casacion-acepto-queja-victimas-allana-camino-reincorporarlas-querellantes-2026114144934), [LPO](https://www.lapoliticaonline.com/judiciales/reves-para-milei-casa/)). LPO dice que «readmitió a dos damnificados»; El Destape, que el fondo sigue pendiente: se usa la versión de El Destape. El pedido de reapertura de la PIA lo resuelve Daniel Rafecas, que subroga el Juzgado N° 8 durante la licencia de Martínez de Giorgi ([La Nación](https://www.lanacion.com.ar/politica/milei-impulsa-el-ascenso-del-juez-rafecas-y-se-podria-abrir-una-nueva-vacante-en-comodoro-py-nid03112026/), [La Capital MdP](https://www.lacapitalmdp.com/libra-una-fiscalia-especializada-apelo-el-sobreseimiento-de-milei-y-busca-reabrir-la-causa/)).
- **ANDIS (etapa: procesamiento; en trámite):** al 04/11 el peritaje de Gendarmería todavía no estaba en el expediente ([Examedia/NA](https://examedia.com.ar/portada/post/88179238)). Desde el 03/11 Lijo toma 39 indagatorias, sobre todo a directivos de Suizo Argentina. Los fiscales pidieron el 16/10 indagar a Spagnuolo por ese tramo y el juez aún no lo ordenó ([El Destape](https://eldestapeweb.com/politica/andis-comenzo-nueva-tanda-39-indagatorias-hechos-corrupcion-discapacidad-numero-2-kovalivker-202611320414)).
- **Adorni (etapa: denuncia; en trámite):** el 06/11 Pollicita dictaminó que no hay elementos para sostener el enriquecimiento ilícito durante la función y pidió pasar la causa al fuero Penal Económico por posible evasión. No es un archivo ni un sobreseimiento: decide Lijo ([elDiarioAR](https://www.eldiarioar.com/politica/fiscal-pollicita-no-encontro-elementos-suficientes-acusar-enriquecimiento-ilicito-manuel-adorni_1_13644790.html), [El Esquiú](https://elesquiu.com/politica/2026/11/6/la-causa-contra-adorni-podria-cambiar-de-fuero-tras-el-dictamen-del-fiscal-pollicita-602464.html), [La Capital](https://www.lacapital.com.ar/politica/segun-el-fiscal-pollicita-no-hay-elementos-suficientes-sostener-que-adorni-se-enriquecio-ilicitamente-n10290858.html)).
- **Espert (etapa: procesamiento; en trámite):** sin novedades en el período.
- **Causa agregada: Reidel / Nucleoeléctrica (etapa: imputación, 08/05/2026; en trámite).** Faltaba en el archivo ([La Nación](https://www.lanacion.com.ar/politica/imputaron-a-demian-reidel-por-los-gastos-con-la-tarjeta-corporativa-de-nucleoelectrica-nid08052026/), [Infobae](https://www.infobae.com/judiciales/2026/05/08/demian-reidel-rechazo-las-acusaciones-en-un-descargo-espontaneo-ante-la-justicia/)).
- **Designaciones:** el 03/11 se envió al Senado el pliego de Rafecas para la Cámara Nacional de Casación en lo Criminal y Correccional ([iProfesional](https://www.iprofesional.com/legales/468250-ascenso-daniel-rafecas-disputa-comodoro-py-tablero-judicial)), dentro de una tanda de 27 a 30 pliegos. Acuerdos fijó audiencias para 64 postulantes el 17, 18 y 27/11 ([Parlamentario](https://www.parlamentario.com/2026/11/06/antes-que-culminen-las-ordinarias-acuerdos-analizara-los-pliegos-de-mas-de-60-candidatos/)). Corte Suprema y Procurador: sin pliegos; La Nación (06/11) recoge versiones de que Mahiques aspira a la Procuración, sin confirmación oficial.
- **Incumplimientos:** el 05/11 el Senado dictaminó la ley de discapacidad que reemplaza la emergencia de la Ley 27.793 (vence el 31/12) y va al recinto el 19/11 ([El Argentino Diario](https://elargentinodiario.com.ar/politica/05/11/2026/ley-discapacidad-senado-dictamen-19-noviembre/)). Se cierra el faltante de la Ley 27.796: la emergencia venció el 21/10/2026 y la prórroga no logró quórum en Diputados (Gestión Sindical, Examedia, Parlamentario). Santilli no concurrió al Congreso en el período, así que el conteo del art. 101 no cambia.
- **Transparencia:** se cargó la presentación de FOPEA ante el Relator de la ONU (26/10).

### Pendientes
- **Fuentes bloqueadas:** `monitoreo.fopea.org/comunicados/` no respondió al pedido de permiso. elintransigente.com y conclusion.com.ar fallaron al abrir.
- **Sin resolver:** Casación sobre las querellas de $LIBRA y el juzgado sobre la PIA; informe firmado de Gendarmería (ANDIS); Cámara de San Martín (Espert); decisión de Lijo sobre la competencia (Adorni); actividad de la causa Reidel posterior a mayo.
- **Causas sin cargar:** créditos del Banco Nación a funcionarios, porque no se verificó su estado actual.
- **Transparencia:** AAIP, ya que el sitio oficial sigue mostrando a Beatriz de Anchorena y no hay confirmación reciente; tasa de denegaciones (descarga.aaip.gob.ar); publicación de las declaraciones juradas 2025.
- **Leyes:** amparo del Garrahan; apelación de la Ley 27.795 ante la Cámara.

## Corte del 13/11/2026
Búsqueda del 07/11 al 13/11/2026.
- **$LIBRA (etapa: imputación; estado: sobreseimiento no firme):** el 12/11 se conoció que Taiano dictaminó contra el pedido de la PIA de reabrir la causa y de asumir la investigación. Mantiene su pedido de sobreseimiento ([iProfesional](https://www.iprofesional.com/legales/468937-taiano-rechazo-reabrir-la-causa-libra-y-cuestiono-el-pedido-de-la-pia), [Examedia/NA](https://examedia.com.ar/portada/post/88225537)). Había sido Rafecas, como subrogante, quien le corrió vista ([Cholila Online](https://cholilaonline.ar/2026/11/escandalo-libra-definiran-si-reabren-la-causa-contra-los-milei.html)). Decide ahora Martínez de Giorgi; la PIA apeló en subsidio ante la Cámara Federal. Según Examedia, Casación podría hacer la audiencia sobre las querellas antes de fin de año y resolver en 2027. Tiempo Argentino (07/11) menciona que la Sala I rechazó un pedido de las querellas de volver a la causa, pero no da la fecha: no se carga.
- **ANDIS (etapa: procesamiento; en trámite):** el 12/11 se conoció la pericia final de Gendarmería. Concluye que «no fue posible establecer» si las voces son de Spagnuolo y detecta rasgos «compatibles con un proceso de regrabación» y «posibles operaciones de edición». No concluye que los audios sean falsos. La firmaron tres peritos oficiales y nueve de parte; cinco de la fiscalía y la Datip lo hicieron en disidencia ([La Nación vía Examedia](https://examedia.com.ar/portada/post/88228973)). Hay una sola fuente con este detalle. Diario Panorama (29/10) ya había anticipado conclusiones similares. Continúan las indagatorias del tramo Suizo Argentina.
- **Adorni (etapa: denuncia; en trámite):** Lijo no resolvió la incompetencia. MDZ y [Perfil](https://noticias.perfil.com/noticias/politica/caso-adorni-el-juez-lijo-toma-distancia-del-fiscal-y-analiza-pedir-mas-pruebas.phtml) informan, con fuentes cercanas al juez, que evalúa pedir más pruebas. Se carga como trascendido. La nota de MDZ no abrió (error del sitio).
- **Espert y Reidel:** sin novedades en el período.
- **Excluida:** la causa por la salida de Flávio Bolsonaro (Capuchetti, fiscal Ochoa) investiga presunto encubrimiento, no corrupción, y no tiene imputados ([Radio Rafaela, 05/11](https://radiorafaela.com.ar/nacionales/la-fiscalia-investiga-si-el-gobierno-utilizo-fondos-publicos-en-la-fuga-de-flavio-bolsonaro)). No se carga en `corrupcion.json`.
- **Designaciones:**
  - Casal sigue interino ([Diario Judicial, 11/11](https://www.diariojudicial.com/news-104860-casal-abre-el-libro-de-pases)).
  - Corte: sin pliegos.
  - Acuerdos confirmó las audiencias del 17, 18 y 27/11 (Parlamentario 12/11, Infobae 10/11). La presidencia de la comisión sigue en disputa.
  - Última tanda de pliegos: Palabras del Derecho dice 27, con 28 entradas en su lista; Parlamentario, unos 30.
- **Antecedentes que faltaban:**
  - Decreto 467/2026 (16/06/2026), que modificó el 222/2003 y eliminó la etapa de observaciones ciudadanas ([Chequeado](https://chequeado.com/nota/el-gobierno-modifico-el-decreto-para-nombrar-jueces-de-la-corte-y-elimino-instancias-de-participacion-ciudadana), [Ámbito](https://www.ambito.com/politica/por-decreto-el-gobierno-javier-milei-oficializo-nuevos-requisitos-designar-jueces-la-corte-suprema-n6289071)).
  - Designación de Gabriela Zangaro en la OA (Decreto 194/2026; Palabras del Derecho y Canal 26, que habla de «resolución»).
  - Suspensión, el 28/04/2026, de la Bicameral del Defensor del Pueblo (Ámbito).
  - Sesión del Senado del 16/07/2026 con 29 a 36 pliegos (ver `datos/justicia/FUENTES.md`).
- **Incumplimientos:** sin cambios de estado. No hubo resolución de la Cámara sobre la Ley 27.795 ni sobre el amparo del Garrahan. La ley de discapacidad sigue prevista para el recinto el 19/11. Santilli no concurrió al Congreso, así que el conteo del art. 101 no cambia.
- **Transparencia:**
  - AAIP: Beatriz de Anchorena firma como titular la Res. AAIP 104/2026 ([Boletín Oficial, 21/05/2026](https://www.boletinoficial.gob.ar/detalleAviso/primera/342206/20260521)). Esta vez el Boletín Oficial sí abrió.
  - DDJJ 2025: presentadas a fines de agosto (iProfesional 31/08, Chequeado 01/09). Presti no la había presentado al 01/09.

### Pendientes
- **Sin resolver:**
  - $LIBRA: decisión de Martínez de Giorgi sobre la reapertura; fondo de Casación; apelación de Marchetto.
  - ANDIS: incorporación formal de la pericia, con segunda fuente.
  - Espert: Cámara de San Martín.
  - Adorni: decisión de Lijo.
  - Reidel: actividad posterior a mayo.
- **Causas sin cargar:** créditos del Banco Nación (hoy en el juzgado de Capuchetti) y Francisco Adorni (IOSFA y enriquecimiento ilícito), porque no se verificó su etapa actual.
- **Transparencia:** tasa de denegaciones de la AAIP (descarga.aaip.gob.ar sigue sin probarse); DDJJ de Presti; titular de la SIGEN.
- **Fuentes que fallaron:** conclusion.com.ar y mdzol.com dieron error al abrir. eldestapeweb.com entró en un bucle de redirección.
