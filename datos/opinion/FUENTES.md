# Fuentes y faltantes · datos/opinion

Actualizado: 2026-10-25. Cubre `encuestas.json`. Cada encuesta lleva al lado su `fuente_url`, su `fuente_fecha` y, cuando hay, `fuentes_cruce`.

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
