---
title: Redes de área local
description: Apuntes y planificación del módulo profesional Redes de área local (0225) — curso 2026-2027
hide: toc
---

# Redes de área local

Apuntes y organización del módulo **0225 — Redes de área local** del CFGM de *Sistemas Microinformáticos y Redes* (SMR), conforme al [Real Decreto 1691/2007](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2008-819), impartido en el [IES Macià Abela](https://portal.edu.gva.es/iesmaciaabela/) de Crevillent.

**Curso 2026-2027.** En este sitio encontrarás la planificación del módulo y los temas que vayamos publicando a lo largo del curso.

## Competencias profesionales

Las ^^competencias profesionales^^ asociadas al módulo:

* **(d)** Replantear el cableado y la electrónica de redes locales en pequeños entornos y su conexión con redes de área extensa canalizando a un nivel superior los supuestos que así lo requieran.
* **(e)** Instalar y configurar redes locales cableadas, inalámbricas o mixtas y su conexión a redes públicas, asegurando su funcionamiento en condiciones de calidad y seguridad.
* **(f)** Instalar, configurar y mantener servicios multiusuario, aplicaciones y dispositivos compartidos en un entorno de red local, atendiendo a las necesidades y requerimientos especificados.
* **(g)** Realizar las pruebas funcionales en sistemas microinformáticos y redes locales, localizando y diagnosticando disfunciones, para comprobar y ajustar su funcionamiento.
* **(h)** Mantener sistemas microinformáticos y redes locales, sustituyendo, actualizando y ajustando sus componentes, para asegurar el rendimiento del sistema en condiciones de calidad y seguridad.

## Objetivos generales

* **(d)** Representar la posición de los equipos, líneas de transmisión y demás elementos de una red local, analizando la morfología, condiciones y características del despliegue, para replantear el cableado y la electrónica de la red.
* **(e)** Ubicar y fijar equipos, líneas, canalizaciones y demás elementos de una red local cableada, inalámbrica o mixta, aplicando procedimientos de montaje y protocolos de calidad y seguridad, para instalar y configurar redes locales.
* **(f)** Interconectar equipos informáticos, dispositivos de red local y de conexión con redes de área extensa, ejecutando los procedimientos para instalar y configurar redes locales.
* **(g)** Localizar y reparar averías y disfunciones en los componentes físicos y lógicos para mantener sistemas microinformáticos y redes locales.
* **(h)** Sustituir y ajustar componentes físicos y lógicos para mantener sistemas microinformáticos y redes locales.

## Resultados de aprendizaje

| Código | Descripción | Peso (%) |
| ------ | ----------- | -------- |
| RA1 | Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes. | **20** |
| RA2 | Despliega el cableado de una red local interpretando especificaciones y aplicando técnicas de montaje. | **12** |
| RA3 | Interconecta equipos en redes locales cableadas describiendo estándares de cableado y aplicando técnicas de montaje de conectores. | **18** |
| RA4 | Instala equipos en red, describiendo sus prestaciones y aplicando técnicas de montaje. | **25** |
| RA5 | Mantiene una red local interpretando recomendaciones de los fabricantes de hardware o software y estableciendo la relación entre disfunciones y sus causas. | **15** |
| RA6 | Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y equipos para prevenirlos. | **10** |

!!! note "Pesos 2026-27"
    Partida **20 / 12 / 18 / 25 / 15 / 10** (suma 100 %). Ajustada según la carga real de evidencias del banco de actividades (más peso a diagnóstico **RA5**; **RA4** se mantiene como núcleo con NetAcad). La evaluación **no** es criterial por CE: los CE sirven para comprobar cobertura.

``` mermaid
pie showData
    title Peso de cada RA en la nota del módulo
    "RA1 — Estructura LAN" : 20
    "RA2 — Despliegue cableado" : 12
    "RA3 — Interconexión" : 18
    "RA4 — Instalación equipos" : 25
    "RA5 — Mantenimiento / diagnóstico" : 15
    "RA6 — PRL y medio ambiente" : 10
```

## Carga horaria

!!! warning "Provisional"
    Distribución de horas del módulo (sujeta a horario y formación en empresa definitivos):

    | Concepto | Horas |
    | --- | ---: |
    | **Total módulo** | **233 h** |
    | Formación en el **centro** | **133 h** |
    | Formación en **empresa (FE)** | **100 h** |

    La FE **no tiene fecha fijada** todavía (Dual en blanco). Mientras tanto, el curso se temporaliza sobre las **133 h de centro**.

## Temas del curso

| Tema | Título | Qué trabajamos | Estado | RA principales |
| ---: | --- | --- | --- | --- |
| **1** | [Introducción. Arquitectura de redes](01-introduccion-arquitectura/tema1.md) | Tipos de redes, componentes, topologías, modelos OSI y TCP/IP | **Publicado** | RA1 |
| **2** | Medios de transmisión y capa física | Par trenzado, fibra, Wi‑Fi básico y conectores | Se publicará cuando toque | RA2, RA3 |
| **3** | Cableado estructurado y componentes | Racks, paneles, electrónica de red, WLAN/NetAcad | Se publicará cuando toque | RA2, RA3, RA4 |
| **4** | Capa de enlace | Tramas, direcciones MAC, switches y dominios de colisión/difusión | Se publicará cuando toque | RA1, RA4 |
| **5** | Capa de red | IPv4, máscaras, CIDR, ARP, ICMP y DHCP | Se publicará cuando toque | RA1, RA4 |
| **6** | Enrutamiento, subnetting y VLANs | Subnetting, supernetting, rutas estáticas, VLANs y NetAcad | Se publicará cuando toque | RA3, RA4 |
| **7** | Capa de transporte | Puertos, TCP/UDP y herramientas básicas | Se publicará cuando toque | RA4, RA5 |
| **8** | NAT e IPv6 | Traducción de direcciones (NAT/PAT) e introducción a IPv6 | Se publicará cuando toque | RA4, RA5 |
| **9** | Servicios, diagnóstico y protección | Servicios de aplicación, diagnóstico de averías, protección y PRL | Se publicará cuando toque | RA5, RA6 |

### Mapa tema × RA

| Temas | RA1 | RA2 | RA3 | RA4 | RA5 | RA6 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1. Introducción. Arquitectura de redes | X | | | | | |
| 2. Medios y capa física | | X | X | | | |
| 3. Cableado estructurado y componentes | | X | X | X | | |
| 4. Capa de enlace | X | | | X | | |
| 5. Capa de red | X | | | X | | |
| 6. Enrutamiento, subnetting y VLANs | | | X | X | | |
| 7. Capa de transporte | | | | X | X | |
| 8. NAT e IPv6 | | | | X | X | |
| 9. Servicios, diagnóstico y protección | | | | | X | X |
| **Peso** | 20 % | 12 % | 18 % | 25 % | 15 % | 10 % |

``` mermaid
timeline
    title Planificación temporal — RAL 2026-27 (orientativa)
    section 1ª Evaluación — sep–nov
        Fundamentos : T1 Introducción y arquitectura : T2 Medios y capa física : T3 Cableado WLAN NetAcad
    section 2ª Evaluación — nov–ene
        Núcleo LAN : T4 Capa de enlace : T5 Capa de red : T6 Enrutamiento VLAN NetAcad
    section 3ª Evaluación — ene–feb
        Servicios y cierre : T7 Transporte : T8 NAT e IPv6 : T9 Diagnóstico y protección
    section Margen
        Centro / FE : 133 sesiones de centro planificadas : FE 100 h sin fecha aún
```

!!! tip "Núcleo del curso"
    Enlace, direccionamiento IP, subnetting y VLANs concentran una parte importante de la evaluación (2.ª evaluación, antes del margen de FE). El Tema 9 cierra el bloque de centro con **diagnóstico (RA5)** y **prevención de riesgos (RA6)**. Ritmo: **7 sesiones/semana × 55 min**; **1 h del cómputo 133 = 1 sesión**.

## Evaluación

La evaluación se organiza por **resultados de aprendizaje (RA)**. Cada RA se califica con la media ponderada de los instrumentos que lo evalúan. Se comprueba que las actividades cubren los criterios de evaluación (CE) del BOE, pero **la nota no se calcula por % de CE** (evaluación **no criterial**). **Los RA no son compensables entre sí.**

### «Quesitos»: cómo se obtiene la nota

Imagina la nota del módulo como una **tarta** repartida en seis quesitos (los RA). Cada quesito tiene un tamaño fijo (el peso de la tabla anterior). Dentro de cada quesito, tu nota es la **media ponderada** de las AC, PR, PY y PO de ese RA.

``` mermaid
flowchart LR
  subgraph IE["Instrumentos"]
    AC["AC 0–1"]
    PR["PR 0–10"]
    PY["PY 0–30"]
    PO["PO 0–100"]
  end
  subgraph RA["Nota de cada RA"]
    N1["RA1"]
    N2["RA2"]
    N3["RA3"]
    N4["RA4"]
    N5["RA5"]
    N6["RA6"]
  end
  NF["Nota final del módulo"]
  PLUS["+1 NetAcad / CCNA"]
  IE --> RA
  N1 -->|"× 0,20"| NF
  N2 -->|"× 0,12"| NF
  N3 -->|"× 0,18"| NF
  N4 -->|"× 0,25"| NF
  N5 -->|"× 0,15"| NF
  N6 -->|"× 0,10"| NF
  PLUS -.->|"si se concede"| NF
```

**Ejemplo (simplificado):** si en RA4 tienes prácticas y un examen, se promedian (según pesos internos que se indiquen en Aules) y ese resultado cuenta un **25 %** de la nota del módulo. Suspender un RA no se compensa con otro.

### Instrumentos de evaluación (IE)

| Instrumento | Icono | Descripción | Escala |
| --- | --- | --- | --- |
| Actividad de clase | :simple-readdotcv: **AC** | Microevidencia de aula | **0–1** |
| Práctica | :simple-neutralinojs: **PR** | Práctica / simulación / laboratorio / NetAcad | **0–10** |
| Proyecto | :material-calendar: **PY** | Entregable mayor con rúbrica | **0–30** |
| Prueba objetiva | :material-pen: **PO** | Examen escrito o en ordenador | **0–100** |
| NetAcad / CCNA | :simple-cisco: **+1** | Certificación o aprovechamiento de la *class* NetAcad | **+1 en la nota final** |

**Resumen de los instrumentos:**

- Opcionales de refuerzo / profundización (si se usan): AR / AP, sin sustituir los IE anteriores.
- **Cálculo:** para cada RA, media ponderada de los IE que lo evalúan → nota del RA. Nota del módulo = suma de (nota RA × peso). Las calificaciones se publican en **Aules**.
- Cada actividad indica el RA, los CE que trabaja y su escala. Codificación: prefijo del IE + número de tema (ej. `AC102` = actividad de clase 02 del Tema 1; `PR101` = práctica 01 del Tema 1).
- **Cisco NetAcad:** el profesor es instructor; el alumnado trabaja en la *class* del curso. Las prácticas **PR303** (WLAN) y **PR603** (VLAN/enrutamiento + preparación) forman parte del itinerario. Si cumples el criterio publicado en Aules (p. ej. finalizar módulos / evidencia de certificación), se aplica **+1 punto sobre la nota final** del módulo. Ese +1 **no sustituye** ningún RA.
- Las entregas en Aules son **obligatorias en Markdown** (`.md`). No se aceptan PDF.

!!! note "Cómo empezar con Markdown y VS Code"
    - Guía de Markdown: [tutorialmarkdown.com/guia](https://tutorialmarkdown.com/guia)
    - Documentación de Visual Studio Code: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)

## Materiales

- Este sitio web de apuntes.
- [Normas del taller](00-normas/normas_taller.md) — lectura obligatoria.
- Aules (entregas en `.md` y calificaciones).
- Diagramas: [Excalidraw](https://excalidraw.com/), [draw.io (diagrams.net)](https://app.diagrams.net/) o [Dia](https://wiki.gnome.org/Apps/Dia).
- Simulación: [Cisco Packet Tracer](https://www.netacad.com/es/cisco-packet-tracer).
- Formación NetAcad / CCNA (class del curso; acceso según indique el profesor).
- Editor de entregas: Visual Studio Code + Markdown.
- Herramientas y cableado del taller (Temas 2–3 y Tema 9).

## Contenidos publicados

| Página | Contenido |
| --- | --- |
| [Inicio](index.md) | Planificación del módulo |
| [Normas del taller](00-normas/normas_taller.md) | Normas de uso del taller |
| [Tema 1](01-introduccion-arquitectura/tema1.md) | Introducción. Arquitectura de redes |

Los Temas 2–9 se publicarán en la **navegación** cuando toque trabajarlos en clase. Mientras tanto, en este Inicio aparecen como «Se publicará cuando toque».

*[CFGM]: Ciclo Formativo de Grado Medio  
*[SMR]: Sistemas Microinformáticos y Redes  
*[RA]: Resultado de aprendizaje  
*[CE]: Criterio de evaluación  
*[IE]: Instrumento de evaluación  
*[FE]: Formación en empresa  
*[CCNA]: Cisco Certified Network Associate
