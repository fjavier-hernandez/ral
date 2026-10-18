---
title: Certificación — CCST Networking y el +1
description: Certificaciones de Cisco para 1.º de SMR (CCST Networking, técnico de soporte, y CCNA, asociado de redes), trabajo para casa con Packet Tracer siguiendo el curso de Pablo Hidalgo y cómo se consigue el +1 en la nota final.
---

# Certificación: CCST Networking y el +1

En el módulo aprendes redes montando cable, armarios y switches reales en el taller. Esta página recoge la otra mitad del camino: la preparación de una **certificación** profesional de Cisco y el trabajo con **Packet Tracer** que la acompaña. Todo lo que hay aquí se hace **en casa**, a tu ritmo, y se apoya en lo que ya hemos visto en clase. No sustituye a las prácticas de taller ni a los exámenes: las completa. Las prácticas de Packet Tracer no cuentan en la nota de los RA; en su lugar, en clase hacemos prácticas de taller o de investigación con exposición. Lo que trabajes aquí, si lo haces con constancia, puede sumarte **un punto** en la nota final del módulo.

!!! tip "Cómo usar esta página"
    Lee primero qué es una certificación y cómo cuenta el +1. Si todavía no tienes Packet Tracer funcionando, empieza por la [guía inicial](packet-tracer.md). Después ve al bloque que corresponde a lo que ya hemos dado en clase (ahora, el [Bloque 1](#bloque-1-temas-1-y-2)) y sigue el orden que propone: vídeo, lectura del apartado del tema y práctica en Packet Tracer. La página crece a medida que avanza el curso; los bloques nuevos aparecen cuando cerramos cada tema.

---

## Qué es una certificación y cuál encaja en 1.º de SMR

Una **certificación** es un examen oficial, organizado por un fabricante o por una entidad independiente, que acredita ante cualquier empresa que dominas unos conocimientos concretos. A diferencia del título de Técnico en Sistemas Microinformáticos y Redes, que acredita el ciclo completo, una certificación se centra en un área muy definida y la reconocen empresas de todo el mundo. En redes, las más conocidas son las de **Cisco**, el fabricante cuyos equipos y cuyo simulador, Packet Tracer, usamos en el módulo.

Cisco tiene dos certificaciones que tienen sentido para ti. El **CCST Networking** (*Cisco Certified Support Technician Networking*, técnico de soporte certificado por Cisco en redes) es la certificación de entrada: comprueba que entiendes cómo funciona una red, que reconoces cables, conectores y puertos y que sabes hacer un diagnóstico básico. El **CCNA** (*Cisco Certified Network Associate*) es el siguiente escalón: exige configurar switches y routers, direccionamiento IP con subredes, enrutamiento y seguridad, y está pensado para quien ya trabaja o va a trabajar administrando redes. Para un primer curso de grado medio, la meta razonable es el CCST; el CCNA queda como objetivo a largo plazo, por ejemplo al terminar el ciclo.

| | CCST Networking (100-150) | CCNA (200-301) |
| --- | --- | --- |
| Nivel | Entrada: soporte técnico de redes | Asociado: administración de redes |
| Requisitos previos | Ninguno | Ninguno (se recomienda experiencia) |
| Duración del examen | 50 minutos | 120 minutos |
| Precio en Cisco | 125 US$ (en euros lo fija el centro examinador) | 300 US$ |
| Validez | 5 años | 3 años |
| Relación con RAL | Cubre buena parte de lo que vemos en el módulo | Va más allá del currículo de 1.º de SMR |

!!! warning "El CCNA cambia de versión en febrero de 2027"
    La versión actual del CCNA (v1.1) se puede examinar hasta el **2 de febrero de 2027**. Desde el **3 de febrero de 2027** entra la **v2.0**, con el mismo código 200-301 y un temario renovado. Si piensas presentarte al CCNA en algún momento del ciclo, lo harás casi seguro con la v2.0: por eso en esta página seguimos el curso de Pablo Hidalgo preparado para esa versión.

El temario oficial del CCST Networking se organiza en seis **dominios**: conceptos y estándares de red; direccionamiento y subredes; equipos finales y medios; infraestructura; diagnóstico de problemas; y seguridad. Puedes consultarlo completo en la página de Cisco ([temario del CCST Networking](https://learningnetwork.cisco.com/s/ccst-networking-exam-topics)). La tabla siguiente relaciona esos dominios con los temas del módulo, de modo que sepas qué parte ya tienes trabajada y cuál llegará más adelante.

| Dominio del CCST | Qué pide, en resumen | Dónde lo vemos en RAL |
| --- | --- | --- |
| 1. Conceptos y estándares | Modelos OSI (*Open Systems Interconnection*) y TCP/IP, tipos de red, topologías, protocolos habituales | **Tema 1** (ya visto); protocolos en los Temas 7 y 9 |
| 2. Direccionamiento y subredes | IPv4, máscaras, subredes, IPv6, direcciones públicas y privadas | Temas 5, 6 y 8 |
| 3. Equipos finales y medios | Cables, conectores, fibra, Wi‑Fi, interferencias | **Tema 2** (ya visto) y Tema 3 |
| 4. Infraestructura | Puertos de los equipos, conexión según un diagrama, conmutación y enrutamiento básicos | Temas 3, 4 y 6; los puertos y módulos ya los has visto en **PR202** |
| 5. Diagnóstico | Metodología, `ping`, `ipconfig`, comandos `show` | Tema 9; el primer `ping` ya lo hiciste en **PR103** |
| 6. Seguridad | Cortafuegos, amenazas, seguridad Wi‑Fi | Temas 3 y 9 |

---

## El +1 en la nota final {: #el-1-de-certificacion }

La programación del módulo recoge un **punto extra** en la nota final para quien completa este apartado de certificación. Funciona como un itinerario de formación de Cisco, pero dentro de nuestros apuntes: tú haces en casa las prácticas de Packet Tracer de cada bloque, las entregas en Aules y yo sigo tu avance desde allí. Este apartado explica qué tienes que hacer para conseguirlo y cómo se aplica, porque es fácil malinterpretarlo: no es una nota de un RA ni sirve para aprobar uno suspendido.

**Cómo cuenta.** Tu nota del módulo se calcula como se explica en la página de [Inicio](../index.md): primero la nota de cada RA (resultado de aprendizaje) a partir de sus actividades, y después la media ponderada de los seis RA. Si completas el apartado de certificación, a esa nota final se le suma **1 punto**, de modo que la nota puede llegar **hasta 11**. El +1 **no sustituye ni compensa** ningún RA: para aprobar el módulo sigues necesitando un 5 o más en cada uno de ellos. Dos ejemplos lo dejan claro. Si tu nota final es un 7,4 y has completado el apartado, el módulo queda en 8,4; si es un 10, queda en 11. En cambio, si tienes el RA4 con un 4, el módulo no está aprobado aunque hayas completado el apartado, porque el punto extra se suma a una nota final que ya exige todos los RA superados.

**Qué tienes que hacer.** El +1 se gana con trabajo constante a lo largo del curso, no con una entrega final. En concreto:

1. Tener Packet Tracer instalado y la sesión iniciada, como se explica en [Acceso a Packet Tracer](#acceso-a-packet-tracer).
2. Completar, bloque a bloque, las **prácticas de Packet Tracer** de esta página (en el Bloque 1, PR103 y PR202) y entregar en Aules, en su plazo, el fichero `.pkt` (o `.pka`) y el informe `.md`.
3. **Defender cada práctica en clase**, con una auditoría oral breve o una demostración: abres tu fichero, haces una comprobación (por ejemplo, un `ping` o un vistazo al modo Simulación) y explicas lo que has hecho. Una práctica entregada pero no defendida no cuenta para el +1. Todas las prácticas de Packet Tracer del módulo, incluidas las de temas posteriores como PR303, cuentan solo para el +1.
4. Seguir el resto del trabajo de cada bloque, es decir, las lecciones del curso de Pablo Hidalgo y el repaso de los apuntes, que son la preparación para entender lo que haces en cada práctica.
5. Si entregaste la práctica opcional [PR102](../01-introduccion-arquitectura/tema1.md#pr102-modelos-en-packet-tracer) del Tema 1, defenderla en la **auditoría oral** cuando se convoque: solo así suma para el +1.

En Aules verás el seguimiento de cada bloque: qué prácticas has entregado, cuáles has defendido y cuáles te faltan. Las prácticas de este apartado se corrigen solo cuando hace falta; lo que de verdad cuenta es que las hagas tú y que sepas explicarlas en la auditoría, igual que con PR102.

---

## Acceso a Packet Tracer {: #acceso-a-packet-tracer }

Packet Tracer es gratuito, pero Cisco pide una **cuenta gratuita** para descargarlo y para abrirlo: al arrancar el programa tienes que iniciar sesión con una cuenta de **NetAcad** o de **Skills for All**, que son las dos plataformas de formación de Cisco. No necesitas estar en ninguna clase ni pagar nada. Los pasos de descarga, instalación e inicio de sesión están en la [guía inicial de Packet Tracer](packet-tracer.md).

Prueba primero con tu correo **`@alu.edu.gva.es`**: es la opción recomendada, porque así todo lo del módulo queda en tu cuenta del centro. Si no consigues crear la cuenta con ese correo o el inicio de sesión falla, crea una **cuenta personal gratuita de Cisco** (en NetAcad o en Skills for All) con otro correo tuyo y úsala solo para Packet Tracer. En los dos casos, la entrega sigue siendo en Aules.

Si Packet Tracer te avisa de que no encuentra una cuenta asociada, Cisco indica que suele bastar con matricularte en su curso gratuito *Getting Started with Cisco Packet Tracer*, que es además el camino oficial para la descarga y aparece en la guía inicial ([preguntas frecuentes de Cisco](https://www.netacad.com/courses/packet-tracer/faq)).

---

## Cómo se trabaja: en casa, con Packet Tracer y el curso de Pablo Hidalgo

El hilo conductor es el curso gratuito en español **CCNA Recargado 2.0** de Pablo Hidalgo ([lista de reproducción en YouTube](https://www.youtube.com/playlist?list=PLK2CXnxpJHnY)), que prepara la nueva versión del CCNA. Son vídeos cortos, de seis a once minutos, que explican un concepto cada uno y, cada cierto número de lecciones, proponen un laboratorio de Packet Tracer. Ya conoces a este autor: sus vídeos aparecen en los Temas 1 y 2 y en la guía de Packet Tracer. Las lecciones de su curso anterior, **CCNA Completo v1.1** ([lista de reproducción](https://www.youtube.com/playlist?list=PLxnG_9vdV6-gEWV15pq89XK_W3G8vP5_0)), siguen siendo útiles para repasar, pero el itinerario de esta página va por el curso nuevo.

Si quieres un apoyo más, Cisco ofrece gratis el curso en línea **Networking Basics** en su plataforma NetAcad (*Cisco Networking Academy*) ([página del curso](https://www.netacad.com/courses/networking-basics)). Tiene 17 módulos con lecturas, cuestionarios y actividades de Packet Tracer, y Cisco lo presenta como preparación para el CCST Networking. Es **opcional**: no hace falta para el +1 y no se entrega.

La forma de trabajar cada bloque es siempre la misma. Primero ves las lecciones del vídeo. Después repasas el apartado del tema que se indica, porque los apuntes son la referencia del módulo y el vídeo es un complemento. Por último, haces la práctica de Packet Tracer y la entregas en Aules en Markdown (`.md`), junto con el fichero `.pkt`, igual que el resto de entregas del módulo.

!!! note "Por qué el vídeo no basta"
    El curso de Pablo Hidalgo prepara el CCNA, que llega más lejos que nuestro currículo, y a veces nombra conceptos que todavía no hemos visto (direcciones IP, puertos, comandos de configuración). No te preocupes si algo no lo entiendes del todo: cada bloque indica qué lecciones corresponden a lo ya dado y en qué tema verás lo demás.

---

## Bloque 1. Temas 1 y 2 {: #bloque-1-temas-1-y-2 }

Este bloque cubre lo que hemos visto hasta ahora: qué es una red y qué equipos intervienen, los modelos de capas y la encapsulación (Tema 1), y los medios de transmisión con el cable de cobre, la fibra y el Wi‑Fi (Tema 2). En el temario del CCST corresponde, sobre todo, a los dominios 1 y 3.

### Lecciones del curso de Pablo Hidalgo

La tabla relaciona cada lección del curso con el apartado de los apuntes que la explica en nuestro módulo. Ve las lecciones en orden y, al terminar cada grupo, repasa el apartado enlazado.

| Lecciones (CCNA Recargado 2.0) | Contenido | Repasa en los apuntes |
| --- | --- | --- |
| [Lección 1](https://www.youtube.com/watch?v=8vg7otknnHc) | Temario del CCNA y laboratorios | Esta página |
| [Lección 2](https://www.youtube.com/watch?v=HG7SukHUQ1E), [3](https://www.youtube.com/watch?v=dzg0-4l9CII) y [4](https://www.youtube.com/watch?v=sYRDUsufWNM) | Fundamentos de redes | Tema 1: [Sistemas en red](../01-introduccion-arquitectura/tema1.md#sistemas-en-red), [Topologías](../01-introduccion-arquitectura/tema1.md#topologias) y [Modelo OSI y modelo TCP/IP](../01-introduccion-arquitectura/tema1.md#modelo-osi-y-modelo-tcpip) |
| [Lección 5](https://www.youtube.com/watch?v=AdPkcvqKWZE), [6](https://www.youtube.com/watch?v=TMiYyKMTnqA), [7](https://www.youtube.com/watch?v=H0zxY5-reeA), [8](https://www.youtube.com/watch?v=XwPFOAq6-D8), [9](https://www.youtube.com/watch?v=5vpe4sUW7NU) y [10](https://www.youtube.com/watch?v=nTfiNKbnjeE) | Capa física | Tema 2: [Par trenzado](../02-medios-capa-fisica/tema2.md#par-trenzado), [Cable directo y cruzado](../02-medios-capa-fisica/tema2.md#cable-directo-y-cruzado) y [Fibra óptica](../02-medios-capa-fisica/tema2.md#fibra-optica) |
| [Lección 11](https://www.youtube.com/watch?v=OanaO6EF5S4) | Cisco Packet Tracer: cuenta, descarga e inicio | [Guía inicial de Packet Tracer](packet-tracer.md) |
| [Lección 12](https://www.youtube.com/watch?v=fgkJChXMYR4) y [13](https://www.youtube.com/watch?v=PpYSB5XvR8E) | Laboratorios de Packet Tracer 1 y 2 | Práctica del bloque (abajo) |

### Si haces Networking Basics (opcional)

Si sigues el curso de Networking Basics por tu cuenta, los módulos que corresponden a este bloque son el **1** (las comunicaciones en un mundo conectado), el **2** (componentes, tipos y conexiones de red), el **5** (principios de comunicación, donde aparecen los modelos de capas) y el **6** (medios de red).

### Prácticas de Packet Tracer del bloque

Las prácticas de este bloque son tres. Las dos primeras ya las conoces de clase y ahora pasan a formar parte de este apartado: se hacen en casa, se entregan en Aules, se defienden en clase y cuentan solo para el +1.

- **[PR103 — Mi primera red](pr103-primera-red.md).** Montas una LAN con un switch y cuatro PC, les das dirección IP y compruebas la conectividad con `ping` y con el modo Simulación. Es la base del dominio de diagnóstico del CCST.
- **[PR202 — Conectar la capa física](pr202-capa-fisica.md).** Identificas puertos y módulos de un router y de varios switches, eliges el cable adecuado para cada enlace y compruebas el resultado. Es justo lo que pide el dominio de infraestructura del CCST.
- **[PR102 — Modelos OSI y TCP/IP](pr102-modelos-osi.md)** (opcional). Observas la encapsulación de una petición web en el modo Simulación. Va más allá de lo visto en el Tema 1 y solo suma si la defiendes en la auditoría oral.

Cada guía enlaza con la rúbrica de su tema, que sirve para revisar la práctica cuando haga falta; ninguna de las tres puntúa en la nota de los RA. Si quieres practicar más, reproduce en Packet Tracer los laboratorios 1 y 2 de Pablo Hidalgo (lecciones 12 y 13): no se entregan, pero son un buen repaso antes de la auditoría.

---

## Próximamente

Los bloques siguientes se abrirán a medida que avancemos en el curso. El primero será el del **Tema 3**, con la práctica **PR303** de redes inalámbricas en Packet Tracer (punto de acceso, nombre de red o SSID, canal y seguridad básica) y las lecciones de Pablo Hidalgo dedicadas al Wi‑Fi. PR303 se hace en casa, cuenta solo para el +1 y no sustituye a la práctica de taller PR305, en la que montas un punto de acceso real.

---

## Autocheck de certificación

Estas preguntas siguen el estilo del CCST, pero son propias del módulo y solo tratan lo que ya hemos visto. Son distintas del Autocheck de cada tema: aquí se mezclan conceptos de los Temas 1 y 2, como en el examen real.

1. Un técnico conecta un PC a un switch con un latiguillo. ¿Qué tipo de cable usa, si no hay Auto‑MDIX, y en qué capa del modelo OSI trabaja el switch?
2. **V/F.** La PDU (unidad de datos de protocolo) de la capa de enlace es el paquete.
3. Ordena de menor a mayor alcance: WAN · PAN · LAN · MAN.
4. Un edificio tiene un motor industrial junto al tendido de cobre. ¿Qué perturbación es la más probable y qué tipo de cable la reduce?
5. Entre dos edificios separados por 250 m se quiere un enlace de 10 Gbps. ¿Cobre o fibra? Si es fibra, ¿multimodo o monomodo, y de qué clase?
6. **V/F.** En un enlace full‑dúplex entre un PC y un switch no se producen colisiones.
7. ¿Qué organismo publica la familia de estándares 802 y qué número corresponde a Ethernet y cuál al Wi‑Fi?
8. Una red Wi‑Fi del aula funciona lenta y hay muchos puntos de acceso vecinos. ¿Qué banda conviene revisar primero y por qué?
9. Elige la correcta: el conector de Ethernet sobre par trenzado es… a) RJ‑11 · b) RJ‑45 · c) BNC · d) LC
10. Cuatro PC conectados a un hub, y el hub conectado a un switch con dos PC más. ¿Cuántos dominios de colisión y de difusión hay?

!!! info "Soluciones"
    Las soluciones se publicarán aquí cuando cierre el bloque en Aules.

---

## Cómo examinarse del CCST (si decides hacerlo)

Presentarse al examen es voluntario y no forma parte de la nota del módulo. Si te animas, conviene que sepas cómo funciona. El CCST Networking se examina en un centro autorizado de **Certiport** o de **Pearson VUE**, las empresas que gestionan los exámenes de Cisco; el precio oficial es de 125 US$ y cada centro lo fija en euros. Antes de reservar, revisa en la página de Cisco ([exámenes y formación del CCST](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/support-technician/exams-training.html)) el idioma y las condiciones vigentes.

Si eres menor de edad, Cisco permite examinarse entre los 13 y los 17 años con el consentimiento de tu madre, padre o tutor legal, que debe firmar el acuerdo de certificación y confidencialidad de Cisco antes de reservar el examen; los centros Certiport piden además un formulario de consentimiento firmado ([política de Cisco sobre menores](https://www.cisco.com/site/us/en/learn/training-certifications/exams/policies.html)). Para preparar el examen no necesitas NetAcad; la cuenta solo es imprescindible para usar Packet Tracer.

---

## Qué no usar

!!! danger "Webs de respuestas y preguntas «reales» de examen"
    Cisco prohíbe usar o difundir preguntas de sus exámenes: al examinarte aceptas un acuerdo de confidencialidad, y quien lo incumple puede perder las certificaciones que tenga y quedarse sin poder examinarse nunca más. Las respuestas de las actividades de NetAcad también son material protegido. Por eso en este módulo **no se usan** páginas que publican preguntas «recordadas» del examen o respuestas de NetAcad, como ExamTopics, ITExamAnswers, ccnadesdecero, ExamCollection, Exam-Labs, Test-King, Fast2Test o certprep.io, ni canales de vídeo que resuelven las actividades de NetAcad. Además del riesgo, no aprendes: el día del examen, o el día que tengas delante un switch real en una empresa, no habrá respuestas que copiar.

---

## Glosario

**certificación**{: #certificacion }
Examen oficial de un fabricante o entidad que acredita unos conocimientos concretos ante cualquier empresa.

**CCST Networking**{: #ccst }
*Cisco Certified Support Technician Networking*: certificación de entrada de Cisco en redes (examen 100-150).

**CCNA**{: #ccna }
*Cisco Certified Network Associate*: certificación de Cisco de nivel asociado (examen 200-301).

**NetAcad**{: #netacad }
*Cisco Networking Academy*: plataforma formativa de Cisco. Desde ella se descarga Packet Tracer y se ofrecen cursos gratuitos como Networking Basics.

**dominio**{: #dominio }
Cada uno de los grandes bloques en que Cisco divide el temario de un examen.

**auditoría**{: #auditoria }
Comprobación oral y breve en la que explicas una práctica que has entregado.

*[RA]: Resultado de aprendizaje
*[PR]: Práctica
*[CCST]: Cisco Certified Support Technician
*[CCNA]: Cisco Certified Network Associate
*[NetAcad]: Cisco Networking Academy
*[SSID]: Service Set Identifier
*[PDU]: Protocol Data Unit
