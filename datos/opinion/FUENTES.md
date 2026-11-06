# Fuentes y faltantes · datos/opinion

Actualizado: 2026-11-06. Cubre `encuestas.json`. Cada encuesta lleva al lado su `fuente_url`, su `fuente_fecha` y, cuando hay, `fuentes_cruce`.

## Criterio
- Encuestas nacionales con campo entre el 01/11/2025 y el 25/10/2026, de consultoras que publican ficha técnica (n, campo, método o margen).
- **Promedio mensual** (`promedio_mensual`): promedio simple, sin ponderar, de aprobación y desaprobación. Entran las encuestas con `tipo_medicion = "gestion"`, fecha de fin de campo conocida y `en_promedio = true`. Cada encuesta cuenta en el mes en que terminó el campo, no en el del rótulo del informe (`mes_etiqueta_informe`). Se redondea a 1 decimal.
- Quedan afuera del promedio, aunque figuran en el archivo: las mediciones de imagen del presidente (Opina Argentina, Giacobbe, Zentrix dic-2025) y las olas sin fecha de campo.

## Encuestadoras y fuentes usadas
- **D'Alessio IROL–Berensztein:** PDF propios en dalessio.com.ar/xpublico (informes mensuales de Humor Social y Político).
- **AtlasIntel (Latam Pulse / Bloomberg):** atlasintel.org (ficha), Bloomberg Línea, LPO, El Economista y Perfil.
- **UdeSA, ESPOP-LOOP:** Mercado, iProfesional, Conclusión e Infobae (oct-2026).
- **Management & Fit:** El Cronista, LPO, Letra P, Crónica, Noticias y Conclusión.
- **Zentrix (Monitor de Opinión Pública):** PDF de dic-2025 (vía InfoPlatense), iProfesional, La Voz de Rosario, Punto Capital, Grupo La Provincia, APF Digital, Infocielo y Diario de Cuyo.
- **Zuban Córdoba:** El Ancasti, El Economista, Portal Tortuga, Alto Que Radio, Perfil, Ámbito y Los Primeros. El portfolio de zubancordoba.com abre, pero sus PDF quedaron bloqueados para esta herramienta.
- **Otras:** Analogías (iProfesional), Equipo Mide (Noticias), Pulso Research (Perfil, Ámbito), Opina Argentina (BAE, Tiempo de San Juan) y Giacobbe (Noticias).
- **Índice de Confianza en el Gobierno (UTDT):** serie mensual en `indice_confianza_gobierno_utdt`. No es aprobación.
- **Confianza en instituciones:** QSocial (Ámbito, La Capital MdP, El Litoral, Infobae). ESPOP mide satisfacción con los poderes del Estado, no confianza (campo `satisfaccion_poderes`).

## Cambios de esta revisión (25/10/2026)
- **Julio 2026 pasa a 3 encuestadoras.** Se encontró la ficha de Management & Fit: campo del 20 al 31/07, 2.600 casos (2.200 ponderados), modo mixto, ±2,1 (El Cronista, 10/08/2026), y entra en el promedio. La ficha de Zentrix también quedó completa: 21 al 30/07, 1.468 casos, online, ±2,1.
- **Nuevas:** Zentrix sep-2026 (22 al 30/09, n=1.438, 35,2/56,8, entra en el promedio), Zentrix dic-2025 (solo imagen, con ficha), Zentrix ago-2026, Pulso Research mar-2026 y Zuban mar-2026. Las tres últimas no tienen fecha de campo y quedan fuera del promedio.
- **Fichas completadas:** ESPOP oct-2026 (n=1.000, ±3,15, problemas, satisfacción con los poderes, imagen de Bullrich), Zuban sep-2026 (imagen negativa de 7 dirigentes) y Zuban jul-2026 (n=2.000).
- **Verificadas contra la fuente:** dalessio-2025-12 y atlas-2025-11 coinciden. Los promedios de los meses que no cambiaron dieron igual al recalcularlos.

## Discrepancias registradas
- **Zentrix sep-2026, problemas:** El Destape da 54,3 / 48,4 / 39,6; Grupo La Provincia y APF Digital coinciden en 50,1 / 49,8 / 40,9. Se usan estos últimos.
- **Zuban jul-2026, aprobación:** 33,4 según Perfil y Ámbito; 34 según Los Primeros.
- **ESPOP mar-2026, aprobación:** 39 según Mercado; 38 según iProfesional.
- **M&F may-2026, aprobación:** Safras da 37,8/58,4; LPO y Conclusión, 37,9/58,1.
- El resto de las discrepancias está en el campo `notas` de cada encuesta.

## Faltantes
- **Diciembre 2025 y enero 2026:** una sola encuestadora con ficha y aprobación de gestión (D'Alessio). AtlasIntel dic-2025 tiene ficha (10 al 15/12, n=5.139), pero las cifras están en un PDF que no se pudo leer. Zentrix dic-2025 mide solo imagen. Zentrix ene-2026 y M&F ene-2026 no aparecen con ficha en la prensa.
- **Octubre 2026:** 3 encuestas (AtlasIntel, ESPOP y D'Alessio). Faltan las olas de M&F, Zuban y Zentrix de octubre, que todavía no se publicaron o no se encontraron.
- **Sin aparición con ficha en el período:** Poliarquía (solo como campo del índice UTDT), Taquion, CB Consultora, Synopsis, Isonomía y Opina Argentina (esta mide imagen, no gestión).
- **Confianza en instituciones:** solo QSocial (may-2026), y le faltan Justicia y Medios. No se encontraron cifras de la Argentina por institución en el Latinobarómetro 2026.
- **Índice UTDT de octubre 2026:** no publicado al 25/10.

## Cambios del corte del 30/10/2026
- **Octubre 2026 pasa a 5 encuestadoras:** promedio 36,2 % de aprobación y 59,6 % de desaprobación (AtlasIntel, D'Alessio, ESPOP, Zuban Córdoba y Synopsis). Antes: 37,8 / 59,1 con tres.
- **Zuban Córdoba oct-2026:** campo 16 al 19/10, 1.600 casos online, ±2,45; aprobación 34,1 y desaprobación 65,2. Coinciden Parlamentario, InfoPlatense y El Intransigente (26/10/2026).
- **Synopsis oct-2026 (nueva encuestadora con ficha):** campo 12 al 17/10, 1.259 casos, ±2,8; evaluación positiva 33,6, regular 10,7 y negativa 55,6. Grupo La Provincia (ficha), DataClave (30/10) y El Censor del Oeste (29/10). Método no informado. Discrepancia: «muy mala» 42 (Grupo La Provincia) o 44,2 (DataClave).
- **Índice UTDT de octubre:** 1,95 (+0,9 % contra septiembre), campo del 5 al 16/10 (Forbes y Economis, 26/10/2026).
- **No cargada:** Celag (El Destape, 26/10/2026), 2.000 casos presenciales, imagen de Milei 38,6 / 58,2: mide imagen, no gestión, y no informa fechas de campo.
- **Siguen faltando en octubre:** Management & Fit y Zentrix (de Zentrix solo se publicaron datos de ingresos, sin aprobación ni ficha).

## Cambios del corte del 06/11/2026
- **Octubre 2026 pasa a 8 encuestadoras:** promedio 34,7 % de aprobación y 59,9 % de desaprobación (AtlasIntel, D'Alessio, ESPOP, Zuban Córdoba, Synopsis, Zentrix, Analogías y Pulso Research). Antes: 36,2 / 59,6 con cinco.
- **Zentrix oct-2026 (cargada):** campo 19 al 30/10, 1.278 casos, online autoadministrado con cuotas y ponderación, ±2,7 (teórico); aprueba 36,2, desaprueba 55,5, ni una ni otra 8. Ficha en 25 se Informa (01/11) y Perfil (04/11); cifras coinciden en El Sol (02/11), El Cronista (04/11), Deuda Prometida (02/11) y Prensa Latina (01/11). Imagen de Milei 35,9 / 58. Pasa a ser la última encuesta con problemas (respuesta múltiple).
- **Analogías oct-2026 (cargada, publicada el 18/10 y no tomada en el corte anterior):** campo 10 al 14/10, 2.863 casos; gestión 31,5 positiva y 59,5 negativa (InfoPlatense, 18/10). El Cronista (25/10) confirma campo, n e imagen positiva de Milei (38,9); el sitio de la consultora confirma «seis de cada diez» negativa y saldo de -28. Método y margen no informados: entra con el mismo criterio que analogias-2026-02.
- **Pulso Research oct-2026 (cargada):** campo 13 al 21/10, 1.006 casos; gestión 28,9 positiva y 66,4 negativa (EsChaco, 04/11). Grupo La Provincia coincide en las cifras y aporta imagen de siete dirigentes, pero no informa ficha ni fecha. Método y margen no informados.
- **Noviembre 2026:** no se encontraron encuestas con campo terminado en noviembre. No se agregó la fila del mes en `promedio_mensual` (quedaría en «—»; el gráfico de `index.html` no admite valores nulos en la línea). Se agrega cuando haya datos, con alerta si hay menos de tres encuestadoras.
- `meta.generado` y `meta.actualizado`: 2026-11-06.

### No cargadas
- **Management & Fit oct-2026:** no se publicó o no se encontró. La última ola encontrada sigue siendo septiembre (14 al 28/09).
- **Opina Argentina, Poliarquía, Taquion, CB Consultora, Isonomía, Giacobbe, Circuitos, Opinaia, Trespuntozero, Proyección y Rubikon:** sin olas nacionales nuevas con aprobación de gestión y ficha en el período. Proyección (1 al 13/10, 1.231 casos, InfoPlatense 23/10) no informa aprobación de gestión. Trespuntozero (con La Sastrería, septiembre) no mide aprobación.

### Pendientes
- **Índice UTDT de noviembre:** todavía no publicado (sale hacia fin de mes).
- **Revisar olas viejas encontradas en esta búsqueda, fuera del alcance del corte:** Management & Fit feb-2026 (9 al 24/02, 2.600 casos, mixto, ±2,1; aprueba 46,8, desaprueba 50,7; El Cronista, 03/03/2026), que no está en el archivo y podría cambiar el promedio de febrero; Analogías sep-2026 (5 al 8/09, 2.932 casos, IVR, ±2,0; Fénix 95.1 y Ámbito), donde las fuentes no coinciden en si 58,1 es gestión o imagen; Poliarquía sep-2026 (La Nación, 18/09/2026), sin revisar.
- **Páginas que no abrieron:** MDZ (03/11, nota sobre varias encuestas), El Intransigente (19/10, cuatro mediciones) y Conclusión (encuesta de octubre con 60 % de rechazo, consultora no identificada). El PDF del informe de Analogías (Google Drive) no se abrió.
- **Siguen faltando:** Management & Fit de octubre; segunda fuente con ficha para Pulso Research oct-2026; método y margen de Analogías y Pulso Research.
