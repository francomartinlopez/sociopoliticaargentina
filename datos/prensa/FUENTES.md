# Agresiones a periodistas: fuentes

Consulta: 25/10/2026 (última revisión: 13/11/2026). Archivo: `agresiones.json`.

- **No hay datos mensuales.** Ni FOPEA ni ADEPA publican conteos por mes en las fuentes accesibles, y el sitio monitoreo.fopea.org no se pudo abrir. El campo `mensual` queda en null.
- **No hay cifras de 2026.** En septiembre de 2026 FOPEA dijo que el récord de 2025 "ya fue superado" en 2026, sin dar números: [El Ancasti](https://www.elancasti.com.ar/politica-y-economia/entidades-periodisticas-alertaron-el-deterioro-la-libertad-prensa-y-el-avance-las-agresiones-n621411).

## Datos cargados
- **2025** (informe anual FOPEA, "El periodismo en riesgo de silencio"): 278 casos y 374 víctimas.
  - Por tipo: discurso estigmatizante 139, ataques a la integridad 58, acciones judiciales 30, acceso a la información 28, censura 10.
  - Por autor: Milei 119; paraestatal 78; no estatal 40; sin identificar 15; estatal + paraestatal = 84,4 %.
  - Fuentes: [MDZ, 30/04/2026](https://www.mdzol.com/politica/record-ataques-la-prensa-y-javier-milei-como-principal-senalado-n1509789) y [BAE Negocios, 29/04/2026](https://www.baenegocios.com/politica/fopea-registro-278-ataques-a-la-prensa-en-2025-el-mayor-nivel-en-18-anos/).
- **2024:** 179 casos: [informe PDF de FOPEA](https://monitoreo.fopea.org/wp-content/uploads/2025/04/FOPEA-Monitoreo-Anual-2024.pdf) y [Perfil, 06/05/2025](https://noticias.perfil.com/noticias/informacion-general/fopea-el-poder-politico-causo-el-52-de-los-ataques-a-la-prensa.phtml).
- **Primeros 12 meses de Milei:** 173 casos, con desglose completo por tipo y por autor: [Letra P, 10/12/2024](https://www.letrap.com.ar/politica/fopea-contabilizo-173-ataques-al-periodismo-el-gobierno-libertario-n5412990/amp).

## Advertencias
- **Categorías del sitio:** "Amenaza/intimidación" no existe como categoría en FOPEA, así que queda en null. En la sección "mapeo_categorias" del JSON está la correspondencia aproximada.
- **Autores:** FOPEA agrupa en estatal, paraestatal y no estatal. Las sumas de "funcionarios_publicos" y "fuerzas_seguridad" del período de 12 meses son agrupaciones propias, explicadas en el JSON.

## Corte del 06/11/2026
- **Dato parcial de 2026 (nuevo campo `parcial_2026`):** al 26/10/2026 FOPEA atribuye 175 agresiones al Presidente, más del 60 % del año, y dice que ya se superó el récord de 2025, sin dar el total. Serie total: 116 (2023), 179 (2024) y 278 (2025). Fuentes: [comunicado de FOPEA](https://fopea.org/fopea-pidio-la-intervencion-del-relator-especial-de-la-onu-por-la-escalada-de-agresiones-contra-el-periodismo/), [Análisis Digital](https://www.analisisdigital.com.ar/nacionales/2026/10/26/fopea-pidio-la-intervencion-de-la-onu-por-la-escalada-de-agresiones-contra-el-periodismo) y [Somos Jujuy](https://www.somosjujuy.com.ar/nacionales/fopea-llevo-onu-agresiones-milei-periodistas-pidio-intervenga-argentina-n126170).
- **Discrepancia:** los casos atribuidos a Milei en 2023 son 5 según FOPEA y 2 según Análisis Digital. Se usa FOPEA.
- **Hechos destacados cargados:** balas de goma a siete trabajadores de prensa en la Marcha Federal Universitaria (octubre); discurso en la Fundación Faro (23/10) y anuncio de acciones legales contra Saguier y Alconada Mon (24/10), según [Cadena 3](https://www.cadena3.com/noticia/politica-y-economia/fopea-denuncio-una-escalada-de-violencia-sin-precedentes-de-milei-contra-los-periodistas_606661) y [Perfil](https://www.perfil.com/noticias/politica/javier-milei-insiste-en-atacar-a-la-prensa-y-amenaza-con-acciones-legales-tras-el-cierre-del-caso-libra.phtml); pedido a la ONU (26/10).
- **Período del 30/10 al 06/11:** no se encontraron comunicados nuevos de FOPEA ni de ADEPA sobre agresiones.

### Pendientes
- `monitoreo.fopea.org/comunicados/` no respondió al pedido de permiso. Por eso no se pudo revisar el listado completo del período, y el conteo mensual sigue en null.
- No se pudo abrir la nota de El Intransigente (30/10) sobre el reclamo de AEA.
- Falta el total de agresiones de 2026.

## Corte del 13/11/2026
- **Sin dato nuevo.** Entre el 06/11 y el 13/11/2026 no se encontraron comunicados ni informes de FOPEA o ADEPA con cifras nuevas de agresiones a periodistas. Lo más reciente sigue siendo el pedido de FOPEA a la ONU (26/10), ya cargado en `parcial_2026`. Solo cambió `meta.actualizado` (2026-11-13).

### Pendientes
- La página de fopea.org (comunicado del 26/10) no respondió al pedido de permiso, así que no se pudo revisar desde ahí el listado de comunicados posteriores. `monitoreo.fopea.org/comunicados/` sigue sin revisarse.
- Siguen faltando el total de agresiones de 2026 y el conteo mensual.
