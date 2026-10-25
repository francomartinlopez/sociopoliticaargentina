# Agresiones a periodistas: fuentes

Consulta: 25/10/2026. Archivo: `agresiones.json`.

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
