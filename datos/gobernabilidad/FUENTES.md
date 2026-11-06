# Gobernabilidad: fuentes

Consulta: 25/10/2026; corte semanal del 30/10/2026. Archivo: `fracturas.json`. No había archivos previos en esta carpeta.

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

## Corte del 30/10/2026
- **PRO (28/10):** no firmó el dictamen del Presupuesto 2027 y pidió siete cambios; Goerling se opone a suspender las PASO y Macri dio por estancada la negociación electoral (La Nación, 30/10; El Cronista, 28/10; Diario Popular). Gravedad sugerida 2 (lectura propia).
- **CGT (28/10):** archivó el quinto paro general y evalúa un paro de 2 a 4 horas y un acto en un estadio (Infobae, 28/10; contexto en BAE, 29/09). Gravedad sugerida 2.
- **Fracturas abiertas:** 11 (entradas cuyo estado empieza con «abierta»).
- **No cargado:** renuncia de César Lencina, subsecretario de Ciencia y Tecnología, con efecto el 29/10 tras 37 días en el cargo (Canal 26): es tercera línea.

## Corte del 06/11/2026
Búsqueda del 30/10 al 06/11/2026 (WebSearch + WebFetch). Se agregaron tres entradas al timeline (31 en total) y se actualizaron seis relaciones.
- **Reforma electoral en el Senado (01/11):** la suspensión de las PASO sigue trabada. LLA tiene 21 bancas, necesita 37 y habría acercado 11 de los 16 votos que le faltan. Se oponen los radicales Abad, Kroneberger y Fama; el PRO tiene reparos; Jaldo la rechaza; Cornejo no definió el voto de Mendoza; Sáenz y Passalacqua la condicionan. Fuentes: Filo.news (01/11), Los Andes (02/11) y Memo (30/10, columna; de ahí se toma solo la cita de Cornejo). Gravedad sugerida 2 (lectura propia).
- **Presupuesto 2027 trabado (04/11):** además de lo que pide el PRO (ya cargado el 28/10), la UCR reclama fondos para universidades, discapacidad y la AUH; Provincias Unidas critica los subsidios al transporte del AMBA, y los bloques provinciales piden fondos para las cajas previsionales. El dictamen pasó a noviembre (11 o 17/11) y la sesión podría ser el 18 o el 25/11. Fuentes: Infobae (04/11), Diario Panorama (04/11), El Litoral (28/10) y Letra P (27/10). Gravedad sugerida 2.
- **Renuncia de Daniel González**, secretario de Coordinación de Energía y Minería: anunciada el 22/10 y oficializada el 30/10 (Decreto 1304/2026, con efecto el 01/11); el cargo no se cubre. Fuentes: El Cronista (22/10), Infobae (30/10) y Noticias Argentinas (30/10). Se carga con fecha del anuncio, cerrada, gravedad 1. Es segunda línea.
- **Relaciones actualizadas:**
  - Vicepresidenta: invitada a la recepción al papa León XIV del 08/11; el mismo día se conoció su programa de alivio de deudas para empleados del Senado (La Gaceta, 03/11; Canal 26, 05/11). Sigue en «ruptura».
  - PRO: el 02/11 postergó la definición de la alianza con LLA para 2027 (iProfesional e Informe Digital, 02/11).
  - UCR, gobernadores que negocian y Gabinete: con los hechos de arriba.
  - Gobernadores opositores: se cierra el faltante de septiembre y octubre. El 30/10 la Corte Suprema aceptó la demanda bonaerense por el fondo del transporte del interior y le dio a la Nación 60 días para responder (El Tribuno e InfoRegión, 30/10). También se suman el cruce Milei–Quintela (28/10) y las críticas de Insfrán (04/11).
- **Fracturas abiertas:** 13, dos más que el corte anterior. Se cuentan las entradas cuyo estado empieza con «abierta».

### Pendientes
- **CGT:** el cese de actividades de 4 a 6 horas (El Monterizo, 28/10) o de 2 a 4 horas (Letra P) se definiría después de la visita del Papa (07-11/11), en un Consejo Directivo sin fecha confirmada. La nota de Letra P sobre el documento que la CGT le llevará a León XIV no muestra fecha de publicación. No se cargó una entrada nueva: solo se actualizó la lectura de la relación.
- **Sebastián Pareja** (diputado, armador de LLA bonaerense): el 06/11 se presentó una denuncia por enriquecimiento ilícito (Juzgado Federal 7, Casanello; Código Baires, 06/11; elDiarioAR, 05/11). Es una denuncia, no un hecho probado, y corresponde a `institucionalidad/corrupcion.json`. Agencia Nova (06/11) dice que su entorno atribuye la causa a la interna con Santiago Caputo, pero la cita es de fuentes sin nombre y es una sola: no se cargó como hecho de la interna de LLA.
- **Villarruel:** la nota de MDZ del 31/10 sobre sus diferencias económicas con Milei no abrió (error del sitio). La de El Destape sobre la «crisis del papel» redirigió y no se leyó.
- **Interna de LLA (Karina Milei–Santiago Caputo):** no se encontró un hecho nuevo con fecha de la semana y dos fuentes.
- **Renuncias:** no se encontraron otras de primera o segunda línea entre el 30/10 y el 06/11. Ya se designó un reemplazo para César Lencina (tercera línea, Perfil y Prensa Mercosur, 01/11), pero no se carga.
