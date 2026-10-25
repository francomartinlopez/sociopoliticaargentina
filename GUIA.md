# Guía de actualización — Monitor Sociopolítico Argentino

El sitio es estático: `index.html` (estructura, mapas y gráficos), `argentina.json` (mapa base de provincias y departamentos, no se toca) y la carpeta `datos/` (todos los datos). **Para actualizar se cambian solo los archivos de `datos/`**, salvo que haga falta un bloque nuevo.

## Reglas editoriales

- **Qué cubre:** solo variables sociales y políticas de la Argentina. Nada de economía, clima ni política internacional: eso está en datosargentina, alertahidrica y monitormundial.
- **Tono:** neutral. Se muestran datos y posiciones de todos los sectores, sin línea editorial.
- **Idioma:** español rioplatense, claro y sin jerga.
- **Datos con fuente:** cada dato lleva fuente (`f`), enlace (`url`) y fecha (`fecha`). No se inventa ni se completa de memoria: si no hay fuente, el dato queda en «—» con una nota.
- **Cifras sensibles** (votaciones, resultados, muertos en conflictos, encuestas): se verifican en al menos dos fuentes.
- **Juicios propios** (por ejemplo, la clasificación de afinidad): se marcan como «lectura propia» y se publican con su criterio.

## Criterios fijos

- **Electoral:** solo las dos últimas elecciones de cada cargo (presidente, gobernador, intendente de ciudades de más de 100.000 habitantes, Congreso nacional y legislaturas provinciales). El Congreso compara las dos últimas elecciones solo legislativas.
  - **Afinidad:** cada fuerza va a izquierda, centro o derecha según `datos/electoral/fuerzas.json` (campo `bloque` y `motivo`). El kirchnerismo y la izquierda (FIT) van juntos; Cambiemos/JxC y LLA van juntos; los partidos provinciales que no se alinean con un extremo van al centro.
  - **Tendencia:** por partido, cada fuerza contra sí misma; por afinidad, cada bloque contra sí mismo.
- **Postura de los gobernadores (lectura propia):** afín = aliado electoral de LLA en 2025 o apoyo explícito a la agenda del gobierno; neutral = acompaña algunas iniciativas y se opone a otras; opositora = confronta abiertamente. Cada clasificación lleva sus hechos con fuente.
- **Afinidades políticas:** provincia afín si sus senadores votaron con el gobierno 2/3 o más de las votaciones nominales en general desde diciembre de 2025; opositora si fue 1/3 o menos; neutral en el medio. Abstención = medio voto; ausencias no cuentan. Transferencias discrecionales (no automáticas + ATN, últimos 12 meses) divididas por el presupuesto total de cada provincia.
- **Votaciones:** lista cerrada de leyes, decretos y pliegos relevantes desde el 10/12/2023 (`datos/congreso/votaciones.json`). Se agrega una votación nueva solo si es de las más importantes del período.
- **Conflictividad:** últimos 12 meses. Tamaño del punto por personas involucradas, en 5 tramos. Daños en 4 niveles (sin daños, menores, importantes, graves).
- **Opinión pública:** solo consultoras con ficha técnica, mínimo tres por mes para el promedio.
- **Homicidios:** solo homicidios dolosos (SNIC, Ministerio de Seguridad).
- **Gobernabilidad:** estados y gravedad son lectura propia, con los criterios escritos en `datos/gobernabilidad/fracturas.json`.
- **Corrupción:** cada causa muestra su etapa judicial real (denuncia, imputación, procesamiento, juicio, condena) y, si se cerró sin condena, cómo (desestimación, sobreseimiento o absolución). Nunca se presenta una denuncia como hecho probado.

## Fuentes y accesos

- Sitios que tienen que estar habilitados en la sesión: datos.gob.ar, www.argentina.gob.ar, resultados.gob.ar, datos.jus.gob.ar, www.presupuestoabierto.gob.ar, www.electoral.gob.ar.
- Cada carpeta de `datos/` tiene su `FUENTES.md` con fuentes, controles y faltantes. Los scripts de reconstrucción están documentados ahí.
- Mapa base: `argentina.json` se genera con `geo.mjs` (topojson de departamentos de mgaitan/departamentos_argentina). Los puntos de conflictividad e intendencias se proyectan con el mismo script.

## Frecuencia

- **Semanal (viernes, publicación a las 20 h de Argentina; corte de datos el mismo viernes a la tarde):** conflictividad, opinión pública, votaciones nuevas, DNU y vetos, gobernabilidad, institucionalidad, postura de los gobernadores, alineamiento de los senadores, calendario político y prensa.
- **Cuando sale el dato:** transferencias (ATN mensual; no automáticas por año en Presupuesto Abierto), DNU firmados (base Infoleg en datos.jus.gob.ar, se actualiza cada mes), homicidios (anual, SNIC), elecciones (después de cada elección: nacionales, gobernador, intendentes y legislaturas), justicia (designaciones o cambios en la Corte).

## Paso a paso semanal

1. Clonar `francomartinlopez/sociopoliticaargentina` y leer los archivos de `datos/`.
2. Actualizar la fecha de corte en `datos/meta.json`.
3. Cargar los hechos nuevos de conflictividad, las encuestas nuevas, las votaciones nuevas, los DNU, vetos e insistencias, y las novedades del calendario.
4. Si hubo una elección: cargar el resultado por provincia y por departamento en `datos/electoral/` y correr la tendencia contra la elección anterior.
5. **Verificar:** validar el JSON; levantar `python3 -m http.server`, abrir el sitio con Playwright, revisar que no haya errores de consola ni «—» nuevos sin nota, y revisar a ojo tres bloques al azar.
6. **Publicar:** commit («Actualización semanal: corte DD/MM») y push a `main`. GitHub Pages publica solo.
7. **Avisar:** mail a francomartinlopez@gmail.com con lo más importante de la semana, el enlace al sitio y la lista de datos que quedaron sin fuente.
