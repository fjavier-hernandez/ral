# AGENTS.md

Instrucciones para los agentes (Cursor y otros) que trabajen en este repositorio. Léelas antes de tocar nada y síguelas en cada tarea.

## Objetivo del repositorio

Este repositorio contiene los apuntes del módulo profesional **Redes de Área Local (RAL)** del ciclo formativo de grado medio de **Sistemas Microinformáticos y Redes (SMR)**, primer curso, curso 2026-2027. Se publican con MkDocs (tema Material) en GitHub Pages: <https://fjavier-hernandez.github.io/ral/>.

El repositorio es **público**: todo lo que se suba, aunque no aparezca en la web, puede leerlo cualquiera. Además, cada push a `main` despliega la web automáticamente (`.github/workflows/ci.yml`), así que fusionar una PR equivale a publicar.

## Estructura

| Ruta | Contenido | ¿Se publica en la web? |
| --- | --- | --- |
| `mkdocs.yml` | Configuración del sitio y navegación (`nav`). | Define la web |
| `docs/index.md` | Portada del módulo, con la evaluación. | Sí |
| `docs/00-normas/` | Normas del taller. | Sí |
| `docs/01-introduccion-arquitectura/` … `docs/09-servicios-diagnostico-proteccion/` | Un directorio por tema (`temaN.md` e `img/`), del Tema 1 al Tema 9. | Se construyen todos; en la `nav` están los que ya se han publicado |
| `docs/certificacion/` | Packet Tracer y guías de prácticas orientadas a la certificación (PR102, PR103, PR202, PR303). | Sí |
| `docs/90-guias/` | Guías auxiliares. | Se construye (no está en `exclude_docs`) |
| `docs/tema01.md` | Borrador huérfano; el canónico es `01-introduccion-arquitectura/tema1.md`. | No (`exclude_docs`) |
| `Planificación/` | Copia versionada de la PD (`PD_RAL_2026_27.md` y `figuras/`). Uso interno. | No |
| `Extra/` | Material interno nuevo del curso 2026-2027. | No |
| `archivo/2526/` | Material del curso 2025-2026 (apuntes, fichas, scripts). | No, pero es legible en el repositorio |
| `includes/` | Fragmentos reutilizables. | Según se incluyan |

Antes de crear un fichero nuevo, comprueba en qué carpeta va y si debe aparecer en la `nav` o quedar excluido.

## Compilar en local

Para comprobar el sitio en local:

```bash
pip install "mkdocs-material[imaging]" mkdocs-print-site-plugin
mkdocs build --strict
mkdocs serve
```

`mkdocs build --strict` no debe dar avisos de enlaces rotos. Ten en cuenta que MkDocs construye **todos** los ficheros de `docs/`, aunque no estén en la `nav`: lo que no deba verse tiene que ir en `exclude_docs` o fuera de `docs/`.

## Estilo de los apuntes

- Escribe en **castellano**, con frases completas y bien construidas.
- **Todo bien explicado, aunque el texto crezca.** Cada concepto se presenta, se explica y, cuando ayude, se acompaña de un ejemplo. Es preferible un párrafo más largo y claro que uno corto que obligue al alumnado a buscar fuera.
- **Nada de texto telegráfico**: no se encadenan fragmentos sin verbo, flechas o listas de palabras sueltas en lugar de explicaciones.
- **Nada de tono coloquial**: registro académico, cercano pero correcto, sin muletillas, sin bromas y sin expresiones de chat.
- **Siglas**: la primera vez que aparecen en cada tema se escriben completas, con la sigla entre paréntesis, por ejemplo «red de área local (LAN)». Después se puede usar solo la sigla.
- **No repetir lo ya visto**: si un concepto se explicó en otro tema, se enlaza a ese apartado (enlace relativo con ancla) con una frase de recordatorio, en lugar de volver a explicarlo.
- Usa los elementos de Material con mesura: admoniciones (`!!! note`, `!!! tip`, `!!! warning`) para los avisos y bloques de código con el lenguaje indicado.

## Imágenes y diagramas

- Las **capturas que se leen mal** (borrosas, pequeñas, con texto ilegible o con datos que no deben verse) se **rehacen como diagramas SVG** propios y se guardan junto al tema, en su carpeta `img/`.
- Las **fotos reales** de equipos o materiales llevan **crédito** (autor, fuente y licencia) en el pie de la figura.
- Toda imagen lleva un texto alternativo (`alt`) descriptivo.
- No se suben imágenes sin licencia de uso.

## Soluciones y autoevaluación

- Las **soluciones del Autocheck** y de las prácticas **no se publican antes de la fecha de entrega**. Mientras tanto se guardan fuera de la `nav` o en una carpeta excluida con `exclude_docs`, y se publican después de la entrega.
- Antes de añadir una solución, comprueba la fecha de entrega en la programación de aula o en Aules. Si no la conoces, no la publiques y pregunta.
- Las **claves y soluciones de exámenes y pruebas no se publican nunca**, ni en la web ni en el repositorio.

## Datos personales: nunca

El repositorio es público y todo lo que se suba puede leerlo cualquiera. **Nunca** se escriben ni se suben:

- horarios del profesorado o de los grupos;
- nombres, notas, listas o cualquier otro dato del **alumnado** o de sus familias;
- **DNI**, NIA, correos o teléfonos personales;
- **firmas** o documentos firmados;
- rutas locales del ordenador del profesor (OneDrive, Descargas, etc.), credenciales, tokens ni claves.

Si una tarea necesita esos datos, se trabaja fuera del repositorio. Si encuentras alguno ya subido, avísalo en la descripción de la PR en vez de dejarlo pasar.

## Evaluación

- La evaluación es **competencial** y tiene como referentes los **resultados de aprendizaje (RA)**. La nota se calcula por RA, con los pesos que fija la programación didáctica (PD).
- Los **criterios de evaluación (CE)** solo sirven para **verificar la cobertura**, es decir, para comprobar qué actividades o instrumentos evidencian cada CE. **No** llevan porcentajes ni pesos propios.
- No se usa la palabra «criterial» en ningún documento.
- Los RA y los CE se copian literalmente de la normativa del módulo; no se inventan ni se renombran.

## Forma de trabajar con Git

- Trabaja siempre en una **rama nueva** con un nombre descriptivo. Nunca hagas commit directamente en la rama por defecto.
- Cuando termines, abre una **pull request (PR)** con un resumen claro de lo que cambia y por qué.
- **No fusiones** la PR: la revisa y la acepta el profesor.
- No despliegues el sitio (`deploy.sh`, `mkdocs gh-deploy`) salvo que se pida expresamente.
- Antes de abrir la PR, ejecuta `mkdocs build --strict` y revisa que en el diff no haya datos personales ni soluciones que no deban publicarse.

## Word de la programación didáctica

Si existe `Planificación/build_docx.sh`, el Word de la PD se genera desde la raíz del repositorio con:

```bash
bash Planificación/build_docx.sh
```

Necesita `pandoc` y `python3` (con `python-docx`). El script usa `reference.docx` y los filtros de `Planificación/` para el formato, el índice con hipervínculos y las tablas. Edita siempre el Markdown de la PD y vuelve a generar el Word; no edites el `.docx` a mano. Si el script no existe en este repositorio, no lo crees sin que se pida.

## Específico de este repositorio

- **Módulo y ciclo**: Redes de Área Local, 1.º de SMR (grado medio), curso 2026-2027.
- **Temas**: nueve temas, desde la introducción y la arquitectura de redes hasta los servicios, el diagnóstico y la protección. Las prácticas se codifican como `PRnNN` (por ejemplo, PR303 es la tercera práctica del Tema 3).
- **Pesos de los RA**: consulta la PD en `Planificación/PD_RAL_2026_27.md`. No los copies a otros documentos con valores distintos.
- **Publicación por fases**: un tema puede existir en `docs/` sin estar en la `nav`; se añade a la `nav` cuando se publica para el alumnado.
- **Planificación privada**: la programación de aula, la matriz de CE, el calendario y el horario están en el almacenamiento privado del profesor, no en este repositorio. No escribas sus rutas locales aquí.
- **Exámenes**: los enunciados, las claves y las soluciones de exámenes no se suben al repositorio (tampoco a `archivo/`).
- **Word de la PD**: `Planificación/build_docx.sh` todavía no está en `main`; llega con la PR #2 (fichas de las unidades de programación). Hasta que se fusione, la sección anterior no se aplica en `main`.
