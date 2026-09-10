---
title: Redes de área local
description: Apuntes y planificación del módulo profesional Redes de área local (0225) — curso 2026-2027
hide: toc
---

# Redes de área local

Apuntes y organización docente del módulo **0225 — Redes de área local** del CFGM de *Sistemas Microinformáticos y Redes* (SMR), conforme al [Real Decreto 1691/2007](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2008-819), impartido en el [IES Macià Abela](https://portal.edu.gva.es/iesmaciaabela/) de Crevillent.

**Curso 2026-2027.** Sitio vivo: solo se publica lo necesario para el momento del curso. El material del curso 2025-26 está archivado en el repositorio (`archivo/2526/`), no en la navegación pública.

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
| RA1 | Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes. | 15 |
| RA2 | Despliega el cableado de una red local interpretando especificaciones y aplicando técnicas de montaje. | 15 |
| RA3 | Interconecta equipos en redes locales cableadas describiendo estándares de cableado y aplicando técnicas de montaje de conectores. | 20 |
| RA4 | Instala equipos en red, describiendo sus prestaciones y aplicando técnicas de montaje. | 20 |
| RA5 | Mantiene una red local interpretando recomendaciones de los fabricantes de hardware o software y estableciendo la relación entre disfunciones y sus causas. | 15 |
| RA6 | Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y equipos para prevenirlos. | 15 |

!!! note "Pesos"
    Partida 15 / 15 / 20 / 20 / 15 / 15 (alineada con la PD 25-26). Se revisarán si el horario definitivo o la cobertura real de CE lo exigen.

## Carga horaria (provisional 2026-27)

!!! warning "Provisional — citar PD 25-26 hasta horario / FE definitivos"
    Según la **programación didáctica 2025-26** del módulo:

    | Concepto | Horas |
    | --- | ---: |
    | **Total módulo** | **233 h** |
    | Formación en el **centro** | **133 h** |
    | Formación en **empresa (FE)** | **100 h** |

    El calendario escolar 2026-27 y la distribución exacta de sesiones semanales / FE se actualizarán cuando estén fijados. **No** se usan aquí las cifras contradictorias del index antiguo (196 h, 28 semanas, “10 semanas dual”, etc.).

## Temas del curso (exactamente 9)

| Tema | Título | Alcance (borrador) | Estado material | RA principales |
| ---: | --- | --- | --- | --- |
| **1** | [Introducción. Arquitectura de redes](tema01.md) | Fusión UT1+UT2 25-26: tipos, componentes, topologías, OSI/TCP-IP | **Publicado** | RA1 |
| **2** | Medios de transmisión y capa física | Par trenzado, fibra, Wi‑Fi básico, conectores; recorte de teoría excesiva | A crear (legado UT3) | RA2, RA3 |
| **3** | Cableado estructurado y componentes | Racks, paneles, electrónica de red, normativa de edificio | A crear (legado UT4) | RA2, RA3, RA4 |
| **4** | Capa de enlace | Tramas, MAC, switches, dominios; intro mínima a VLAN (1 línea) si hace falta | A adaptar (legado UT5) | RA1, RA4 |
| **5** | Capa de red | IPv4, máscaras, CIDR, ARP, ICMP, DHCP | A adaptar (legado UT6) | RA1, RA4 |
| **6** | Enrutamiento, subnetting y VLANs | **Único sitio fuerte de VLAN**; subnetting, supernetting, rutas | A adaptar (legado UT7) | RA3, RA4 |
| **7** | Capa de transporte | Puertos, TCP/UDP, herramientas básicas | A adaptar (legado UT8) | RA4, RA5 |
| **8** | NAT e IPv6 | NAT/PAT e IPv6 a nivel SMR | A adaptar (legado UT9) | RA4, RA5 |
| **9** | Servicios, diagnóstico y protección | Fusión planificada de antiguas UT10+UT11+UT12: aplicación + conflictos/diagnóstico + protección/**PRL** | **A crear** (sin material 25-26) | RA5, RA6 |

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
| **Peso** | 15 % | 15 % | 20 % | 20 % | 15 % | 15 % |

``` mermaid
timeline
    title Planificación temporal — RAL 2026-27 (borrador)
    section 1ª Evaluación
        Fundamentos : T1 Introducción y arquitectura : T2 Medios y capa física : T3 Cableado y componentes
    section 2ª Evaluación
        Núcleo LAN : T4 Capa de enlace : T5 Capa de red : T6 Enrutamiento subnetting y VLANs
    section 3ª Evaluación
        Servicios y cierre : T7 Transporte : T8 NAT e IPv6 : T9 Diagnóstico y protección
```

!!! tip "Núcleo evaluable (aprendizaje del curso pasado)"
    Enlace / IP / subnetting / VLAN concentran gran parte de la evaluación útil. Se adelantan en 2.ª evaluación para no acumular al final. El Tema 9 cubre el hueco de **diagnóstico (RA5)** y **PRL (RA6)** que en 25-26 quedó sin material propio.

## Evaluación

La evaluación **no es criterial por CE suelto**: se califican los **RA** mediante medias ponderadas de los instrumentos asignados a cada RA, comprobando que se cubren los CE trabajados en las actividades. **Los RA no son compensables entre sí** (alineado con la PD anterior / instrucciones del departamento).

### Instrumentos de evaluación (IE)

| Instrumento | Icono | Descripción | Escala |
| --- | --- | --- | --- |
| Actividad de clase | :simple-readdotcv: **AC** | Microevidencia de aula | **0–1** |
| Práctica | :simple-neutralinojs: **PR** | Práctica / simulación / laboratorio | **0–10** |
| Proyecto | :material-calendar: **PY** | Entregable mayor con rúbrica | **0–30** |
| Prueba objetiva | :material-pen: **PO** | Examen escrito o en ordenador | **0–100** |

Opcionales de refuerzo / profundización (si se usan): AR / AP, sin sustituir los IE anteriores.

**Cálculo:** para cada RA, media ponderada de los IE que lo evalúan. Las calificaciones se publican en **Aules**.

Cada actividad indica el RA, los CE que trabaja y su escala. Codificación: prefijo del IE + número de tema (ej. `AC102` = actividad de clase 02 del Tema 1; `PR101` = práctica 01 del Tema 1).

## Materiales

- Este sitio MkDocs (Material).
- [Normas del taller](normas_taller.md) — lectura obligatoria.
- Aules (entregas y calificaciones).
- Excalidraw y Cisco Packet Tracer (a partir del Tema 1).
- Herramientas y cableado del taller (Temas 2–3 y Tema 9 / PRL).

## Publicación actual

| Página | Contenido |
| --- | --- |
| [Inicio](index.md) | Esta planificación |
| [Normas del taller](normas_taller.md) | Resumen alumnado |
| [Tema 1](tema01.md) | Introducción. Arquitectura de redes |

Los Temas 2–9 se irán publicando cuando estén listos. El legado 25-26 no se elimina: vive en `archivo/2526/` del repositorio (no en la nav).

*[CFGM]: Ciclo Formativo de Grado Medio  
*[SMR]: Sistemas Microinformáticos y Redes  
*[RA]: Resultado de aprendizaje  
*[CE]: Criterio de evaluación  
*[IE]: Instrumento de evaluación  
*[FE]: Formación en empresa  
*[PD]: Programación didáctica
