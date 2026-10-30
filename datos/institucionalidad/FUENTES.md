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
