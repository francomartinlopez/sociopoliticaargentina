# Gobernabilidad: fuentes

Consulta: 25/10/2026. Archivo: `fracturas.json`. No había archivos previos en esta carpeta.

## Qué es dato y qué es lectura propia
- **Datos con fuente:** fechas, actores y qué pasó. Cada entrada del timeline lleva al menos dos URL.
- **Lectura propia:** `estado`, `gravedad_sugerida` (con su criterio en `meta.criterio_gravedad`) y `estado_sugerido` de las relaciones.
- **Período:** del 10/12/2023 al 25/10/2026, con 26 entradas en el timeline.

## Fuentes principales
- **Gabinete:**
  - Recuentos de [InfoRegión (04/03/2026)](https://www.inforegion.com.ar/2026/03/04/renuncia-en-el-gabinete-uno-por-uno-los-ministros-que-dejaron-el-gobierno-de-javier-milei/), [Ámbito](https://www.ambito.com/politica/gabinete-javier-milei-cuantas-bajas-tuvo-y-quienes-son-los-funcionarios-que-dejaron-el-gobierno-que-asumio-n6204923) e [Infobae (02/06/2026)](https://www.infobae.com/economia/2026/06/02/cuantos-funcionarios-dejaron-el-gobierno-desde-su-inicio-en-2023-y-cual-es-el-ministerio-que-mas-bajas-tuvo/). Este último da 258 altos funcionarios salientes y 8 cambios de ministros, según un informe privado de Pablo Salinas.
  - Cada salida se cruzó con notas del día.
- **Adorni y Santilli:**
  - Renuncia de Adorni (27/06/2026) y jura de Santilli (30/06/2026): DW vía Teletica, Canal 26 y La Gaceta.
  - Supresión del Ministerio del Interior por Decreto 571/2026: [Tiempo de San Juan, 03/07/2026](https://www.tiempodesanjuan.com/politica/el-gobierno-reorganizo-su-estructura-elimino-el-ministerio-del-interior-y-transfirio-sus-funciones-a-la-jefatura-de-gabinete_1783101694).
- **Vicepresidencia:** Sitio Andino y Misiones Online (10/07/2025), iProfesional (23/07/2025), Los Andes e iProfesional (03/08/2026).
- **PRO:**
  - Designación de auditores de la AGN: El Economista (18/12/2025), Palabras del Derecho (amparo, 21/12/2025) y BAE (Santilli, 22/12/2025).
  - Pelea entre Macri y Milei: iProfesional (07/07/2026).
  - Recomposición: El Economista (13/08/2026).
- **UCR:** La Nación (06/08/2026).
- **Gobernadores:**
  - Provincias Unidas: Ámbito (30/07/2026) y Noticias NQN (06/08/2025).
  - Reunión con Santilli: C5N (16/09/2026).
  - Disputa con Kicillof: Letra P (11/04/2026).
- **CGT:**
  - Fechas de los cuatro paros: Diario de Cuyo (16/02/2026) y Los Andes (19/02/2026).
  - Plan de protesta: El Economista (12/08/2026).
  - Diálogo congelado: Canal 26 (01/05/2026).
- **Bloques en el Congreso:**
  - Diputados: [La Gaceta, 03/12/2025](https://www.lagaceta.com.ar/nota/1115372/politica/nuevo-mapa-diputados-como-quedaron-bloques-tras-jura-nuevos-legisladores.html).
  - Senado: acta oficial 2623, reutilizada de `datos/afinidades/senadores.json`.

## Correcciones al pedido
- **Manuel Adorni ya no es jefe de Gabinete.** Renunció el 27/06/2026 y desde el 30/06/2026 el cargo lo ocupa Diego Santilli. Su causa se carga como "ex jefe de Gabinete" en `institucionalidad/corrupcion.json`.
- **El Ministerio del Interior ya no existe.** Desde julio de 2026 sus funciones están en una Vicejefatura de Interior a cargo de Gustavo Coria.

## Discrepancias
- **Ferraro:** el pedido de renuncia fue el 25/01/2024 (El Economista, "a 45 días de asumir"). Ámbito fecha la salida el 26/02/2024 y la oficialización fue el 05/03/2024. Se usa la fecha del pedido.
- **Werthein:** la renuncia trascendió el 21/10/2025; Ámbito la fecha el 22/10.
- **Marra:** la nota de Noticias NQN es del 30/01/2025. La de iProfesional sobre la expulsión podría ser anterior y no se verificó su fecha.
- **Cambios de ministros:** el recuento propio da 11 personas y 12 cambios; Infobae (Salinas) da 8 cambios de ministros al 01/06/2026. La diferencia probablemente se explica porque Salinas no cuenta a los jefes de Gabinete ni las salidas para asumir bancas, pero no se pudo confirmar.

## Faltantes
- **Composición de Diputados en 2026:** no se encontró una actualización posterior al 03/12/2025, así que los pases de bloque de 2026 no están reflejados.
- **Gobernadores opositores:** no se encontró ningún hecho de septiembre u octubre de 2026. El último registrado es la audiencia en la Corte con Buenos Aires (21/04/2026).
- **Interna de LLA:** detalle de la disputa Karina Milei–Santiago Caputo de marzo y abril de 2026. El Observador quedó fuera de la lista de dominios permitidos y se usó Infobae (10/06/2026), que se basa en fuentes reservadas.
- **Resolución del amparo del PRO sobre la AGN:** no se encontró.
- **Quinto paro de la CGT:** a la fecha de corte no se encontró ninguno convocado.
