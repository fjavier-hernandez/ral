---
title: Certificación CCNA y el +1
description: Certificación CCNA (Cisco Certified Network Associate, asociado de redes certificado por Cisco) para 1.º de SMR (Sistemas Microinformáticos y Redes), recorrido del curso de Pablo Hidalgo, prácticas de Packet Tracer para casa y cómo se consigue el +1 en la nota final.
---

# Certificación CCNA y el +1

En el módulo aprendes redes montando cable, armarios y switches reales en el taller. Esta página recoge la otra mitad del camino: la preparación de la certificación profesional **CCNA** de Cisco y el trabajo con **Packet Tracer** que la acompaña. Todo lo que hay aquí se hace **en casa**, a tu ritmo, y se apoya en lo que ya hemos visto en clase. No sustituye a las prácticas de taller ni a los exámenes, sino que los completa. Las prácticas de Packet Tracer no cuentan en la nota de los RA (resultados de aprendizaje); en su lugar, en clase hacemos prácticas de taller o de investigación con exposición. Lo que trabajes aquí, si lo haces con constancia, puede sumarte **hasta un punto** en la nota final del módulo.

!!! tip "Cómo usar esta página"
    Lee primero qué es el CCNA y cómo cuenta el +1. Si todavía no tienes Packet Tracer funcionando, empieza por la [guía inicial](packet-tracer.md). Después sigue el [recorrido CCNA](#recorrido-ccna) en el orden que propone: lección del curso, repaso del apartado de los apuntes y, cuando toca, práctica de Packet Tracer.

---

## Qué es una certificación y por qué el CCNA

Una **certificación** es un examen oficial, organizado por un fabricante o por una entidad independiente, que acredita ante cualquier empresa que dominas unos conocimientos concretos. A diferencia del título de Técnico en Sistemas Microinformáticos y Redes, que acredita el ciclo completo, una certificación se centra en un área muy definida y la reconocen empresas de todo el mundo. En redes, las más conocidas son las de **Cisco**, el fabricante cuyos equipos y cuyo simulador, Packet Tracer, usamos en el módulo.

La certificación que seguimos es el **CCNA** (*Cisco Certified Network Associate*, asociado de redes certificado por Cisco), que se obtiene con un único examen, el **200-301**. Es la certificación de redes más conocida del mercado y la que suelen pedir las ofertas de empleo de técnico de redes. Exige entender cómo viaja la información por una red, conectar y diagnosticar cables e interfaces, configurar switches y routers, trabajar con direcciones IP y subredes, y aplicar seguridad básica. Va más allá del currículo de 1.º de SMR, pero puedes seguir su recorrido desde ya: buena parte de lo que pide coincide con lo que vemos en el módulo. Quienes superen la auditoría de prácticas y destaquen tendrán la oportunidad de presentarse al examen oficial, y espero que lo hagan.

| | CCNA (200-301) |
| --- | --- |
| Nivel | Asociado: instalación, configuración y diagnóstico de redes |
| Requisitos previos | Ninguno (Cisco recomienda experiencia previa) |
| Duración del examen | 120 minutos |
| Precio en Cisco | 300 US$ (en euros, el que fije Pearson VUE) |
| Idiomas | Inglés y japonés |
| Validez | 3 años |
| Relación con RAL | Cubre buena parte de los Temas 1 a 9 y llega más lejos |

!!! warning "El CCNA cambia de versión en febrero de 2027"
    La versión actual del examen (v1.1) se puede hacer hasta el **2 de febrero de 2027**. Desde el **3 de febrero de 2027** solo existe la **v2.0**, con el mismo código 200-301 y un temario renovado. Si piensas presentarte en algún momento del ciclo, lo harás con la v2.0; por eso el recorrido de esta página sigue el curso de Pablo Hidalgo preparado para esa versión.

El temario oficial de la v2.0 se organiza en cinco **dominios**, cada uno con su peso en el examen. Puedes consultarlo completo en la página de Cisco ([temario del CCNA v2.0](https://learningnetwork.cisco.com/s/ccna-v2-exam-topics)). La tabla siguiente relaciona esos dominios con los temas del módulo.

| Dominio del CCNA v2.0 | Qué pide, en resumen | Dónde lo vemos en RAL |
| --- | --- | --- |
| 1. Infraestructura y conectividad (25 %) | Cables de cobre y fibra, interfaces, Wi‑Fi, direcciones IPv4 e IPv6, conectividad de los equipos | **Tema 2** y Tema 3; direcciones en los Temas 5, 6 y 8 |
| 2. Conmutación y acceso a la red (25 %) | Switches, VLAN, enlaces troncales, alimentación por Ethernet o PoE, `ping` y `traceroute` | Temas 3, 4 y 6; el primer `ping` se trabaja en **PR103** |
| 3. Enrutamiento IP (20 %) | Tabla de rutas, rutas estáticas, OSPF | Tema 6 |
| 4. Servicios de red y seguridad (20 %) | DHCP, DNS, NAT, listas de acceso, seguridad de los puertos | Temas 8 y 9 |
| 5. IA, operación y gestión de la red (10 %) | Gestión y automatización de redes | Tema 9, en parte; el resto queda fuera del currículo de 1.º |

Los fundamentos del **Tema 1** (tipos de red, topologías, modelos OSI y TCP/IP, encapsulación) no aparecen como dominio propio, pero son la base de todos: el curso de Pablo Hidalgo empieza por ellos.

---

## El +1 en la nota final {: #el-1-de-certificacion }

La programación del módulo recoge **hasta un punto extra** en la nota final para quien completa este apartado de certificación. Funciona como un itinerario de formación de Cisco, pero dentro de nuestros apuntes: tú haces en casa las prácticas de Packet Tracer, las entregas en Aules y yo sigo tu avance desde allí. Este apartado explica qué tienes que hacer para conseguirlo y cómo se aplica, porque es fácil malinterpretarlo: no es una nota de un RA ni sirve para aprobar uno suspendido.

**Las dos partes del +1.** El punto se gana en dos mitades, y la segunda solo se suma si tienes la primera:

- **0,5 puntos por las prácticas.** Entregas las prácticas de Packet Tracer de este apartado y superas la **auditoría** del profesor, en la que defiendes en clase lo que has hecho.
- **0,5 puntos más, hasta el punto entero, por el examen.** Si, además, apruebas un **examen de certificación**, el +1 queda completo. Cómo se acredita ese examen para el +1 se concretará en Aules.

**Cómo cuenta.** Tu nota del módulo se calcula como se explica en la página de [Inicio](../index.md): primero la nota de cada RA a partir de sus actividades, y después la media ponderada de los seis RA. A esa nota final se le suma lo que hayas conseguido en este apartado (0,5 o 1 punto), y la nota puede llegar **hasta 11**. El +1 **no sustituye ni compensa** ningún RA: para aprobar el módulo sigues necesitando un 5 o más en cada uno de ellos. Unos ejemplos lo dejan claro. Si tu nota final es un 7,4 y has entregado y defendido las prácticas, el módulo queda en 7,9; si además has aprobado el examen de certificación, queda en 8,4. Con un 10 y el punto entero, la nota es un 11. En cambio, si tienes el RA4 con un 4, el módulo no está aprobado aunque hayas completado el apartado, porque el punto extra se suma a una nota final que ya exige todos los RA superados.

**Qué tienes que hacer.** La primera mitad se gana con trabajo constante a lo largo del curso, no con una entrega final. En concreto:

1. Tener Packet Tracer instalado y la sesión iniciada, como se explica en [Acceso a Packet Tracer](#acceso-a-packet-tracer).
2. Seguir el [recorrido CCNA](#recorrido-ccna): las lecciones del curso de Pablo Hidalgo y el repaso de los apuntes, que son la preparación para entender lo que haces en cada práctica.
3. Completar las **prácticas de Packet Tracer** en el punto del recorrido en que aparecen y entregar en Aules, en su plazo, el fichero `.pkt` (o `.pka`) y el informe `.md`. Todas las prácticas de Packet Tracer del módulo, por ejemplo PR303, cuentan solo para el +1.
4. **Superar la auditoría de cada práctica en clase**, con una explicación oral breve o una demostración: abres tu fichero, haces una comprobación (por ejemplo, un `ping` o un vistazo al modo Simulación) y explicas lo que has hecho. Una práctica entregada pero no defendida no cuenta para el +1. La práctica opcional [PR102](pr102-modelos-osi.md) solo suma si la defiendes del mismo modo.
5. Para la segunda mitad, aprobar el examen de certificación y acreditarlo como se indique en Aules.

En Aules verás el seguimiento: qué prácticas has entregado, cuáles has defendido y cuáles te faltan. Las prácticas de este apartado se corrigen solo cuando hace falta; lo que de verdad cuenta es que las hagas tú y que sepas explicarlas en la auditoría.

---

## Acceso a Packet Tracer {: #acceso-a-packet-tracer }

Packet Tracer es gratuito, pero Cisco pide una **cuenta gratuita** para descargarlo y para abrirlo: al arrancar el programa tienes que iniciar sesión con una cuenta de **NetAcad** (*Cisco Networking Academy*) o de **Skills for All**, que son las dos plataformas de formación de Cisco. No necesitas estar en ninguna clase ni pagar nada. Los pasos de descarga, instalación e inicio de sesión están en la [guía inicial de Packet Tracer](packet-tracer.md).

Prueba primero con tu correo **`@alu.edu.gva.es`**: es la opción recomendada, porque así todo lo del módulo queda en tu cuenta del centro. Si no consigues crear la cuenta con ese correo o el inicio de sesión falla, crea una **cuenta personal gratuita de Cisco** (en NetAcad o en Skills for All) con otro correo tuyo y úsala solo para Packet Tracer. En los dos casos, la entrega sigue siendo en Aules.

Si Packet Tracer te avisa de que no encuentra una cuenta asociada, Cisco indica que suele bastar con matricularte en su curso gratuito *Getting Started with Cisco Packet Tracer*, que es además el camino oficial para la descarga y aparece en la guía inicial ([preguntas frecuentes de Cisco](https://www.netacad.com/courses/packet-tracer/faq)).

---

## Cómo se trabaja: el curso de Pablo Hidalgo

El hilo conductor es el curso gratuito en español **CCNA Recargado 2.0** de Pablo Hidalgo ([lista de reproducción en YouTube](https://www.youtube.com/playlist?list=PLK2CXnxpJHnY)), que prepara la versión 2.0 del CCNA. Son vídeos de seis a diez minutos que explican un concepto cada uno y, cada cierto número de lecciones, proponen un laboratorio de Packet Tracer. Ya conoces a este autor: sus vídeos aparecen en los Temas 1 y 2 y en la guía de Packet Tracer.

Algunas lecciones, sobre todo los laboratorios, están reservadas a los **miembros de pago** del canal. No las necesitas: en el recorrido se indican como opcionales, y las prácticas de esta página cubren ese trabajo. Cuando el curso nuevo todavía no ha llegado a un concepto, el recorrido remite a una lección pública del curso anterior del mismo autor, **CCNA Completo v1.1** ([lista de reproducción](https://www.youtube.com/playlist?list=PLxnG_9vdV6-gEWV15pq89XK_W3G8vP5_0)).

La forma de trabajar cada tramo es siempre la misma. Primero ves las lecciones. Después repasas el apartado de los apuntes que se indica, porque los apuntes son la referencia del módulo y el vídeo es un complemento. Por último, si el tramo tiene práctica, la haces en Packet Tracer y la entregas en Aules en Markdown (`.md`), junto con el fichero `.pkt`, igual que el resto de entregas del módulo.

!!! note "Por qué el vídeo no basta"
    El curso de Pablo Hidalgo prepara el CCNA, que llega más lejos que nuestro currículo, y a veces nombra conceptos que el módulo trata en otro tema (direcciones IP, puertos, comandos de configuración). No te preocupes si algo no lo entiendes del todo: cada tramo indica el apartado de los apuntes que corresponde.

---

## El recorrido CCNA {: #recorrido-ccna }

El recorrido sigue el orden del curso de Pablo Hidalgo, que es el orden en que el CCNA construye los conocimientos: primero los fundamentos, después la capa física y Packet Tracer, luego el Wi‑Fi y la capa de enlace. Las prácticas no van en el orden de los temas del módulo, sino en el punto del curso que corresponde a su nivel. Por eso PR202, que es del Tema 2, va antes que PR103, que es del Tema 1: conectar cables y módulos solo pide capa física, mientras que dar direcciones IP y comprobar con `ping` pide algo más. PR102, la más exigente, cierra el recorrido.

| Tramo | Lecciones (CCNA Recargado 2.0) | Repasa en los apuntes | Práctica |
| --- | --- | --- | --- |
| 1. Temario | [Lección 1](https://www.youtube.com/watch?v=8vg7otknnHc) | Esta página | — |
| 2. Fundamentos de redes | [Lección 2](https://www.youtube.com/watch?v=HG7SukHUQ1E), [3](https://www.youtube.com/watch?v=dzg0-4l9CII) y [4](https://www.youtube.com/watch?v=sYRDUsufWNM) | Tema 1: [Sistemas en red](../01-introduccion-arquitectura/tema1.md#sistemas-en-red), [Topologías](../01-introduccion-arquitectura/tema1.md#topologias), [PDU y encapsulación](../01-introduccion-arquitectura/tema1.md#pdu-y-encapsulacion) y [Modelo OSI y modelo TCP/IP](../01-introduccion-arquitectura/tema1.md#modelo-osi-y-modelo-tcpip) | — |
| 3. Capa física | [Lección 5](https://www.youtube.com/watch?v=AdPkcvqKWZE), [6](https://www.youtube.com/watch?v=TMiYyKMTnqA), [7](https://www.youtube.com/watch?v=H0zxY5-reeA), [8](https://www.youtube.com/watch?v=XwPFOAq6-D8), [9](https://www.youtube.com/watch?v=5vpe4sUW7NU) y [10](https://www.youtube.com/watch?v=nTfiNKbnjeE) | Tema 2: [Cable directo y cruzado](../02-medios-capa-fisica/tema2.md#cable-directo-y-cruzado) y [Fibra óptica](../02-medios-capa-fisica/tema2.md#fibra-optica) | — |
| 4. Packet Tracer | [Lección 11](https://www.youtube.com/watch?v=OanaO6EF5S4); lecciones 12 y 13, laboratorios 1 y 2 (solo miembros, opcionales) | [Guía inicial de Packet Tracer](packet-tracer.md) | **[PR202](pr202-capa-fisica.md)** |
| 5. Wi‑Fi | Lección 14 (solo miembros, opcional), [15](https://www.youtube.com/watch?v=ESquFnfym7Q) y [16](https://www.youtube.com/watch?v=MeGor4SxCCM) | Tema 2: [Medios no guiados y Wi‑Fi básico](../02-medios-capa-fisica/tema2.md#medios-no-guiados-y-wifi-basico) | — |
| 6. Primera red con direcciones IP | Del curso v1.1: [Lección 7](https://www.youtube.com/watch?v=r-K5yZe2Ea8) y [8](https://www.youtube.com/watch?v=gQH8ezSOHh8) (IPv4 y su configuración en Windows) | Tema 1: [Sistemas en red](../01-introduccion-arquitectura/tema1.md#sistemas-en-red) | **[PR103](pr103-primera-red.md)** |
| 7. Capa de enlace | [Lección 17](https://www.youtube.com/watch?v=ZdAWUfH8BcY) y [18](https://www.youtube.com/watch?v=CGc6XrXp_cU) | Tema 1: [PDU y encapsulación](../01-introduccion-arquitectura/tema1.md#pdu-y-encapsulacion); la capa de enlace se verá a fondo en el Tema 4 | **[PR102](pr102-modelos-osi.md)** (opcional) |

Las tres prácticas se hacen en casa, se entregan en Aules, se defienden en la auditoría y cuentan solo para el +1:

- **[PR202 — Conectar la capa física](pr202-capa-fisica.md).** Identificas puertos y módulos de un router y de varios switches, eliges el cable adecuado para cada enlace y compruebas el resultado. Corresponde al primer punto del dominio 1 del CCNA: interfaces y cables de cobre y fibra.
- **[PR103 — Mi primera red](pr103-primera-red.md).** Montas una LAN con un switch y cuatro PC, les das dirección IP y compruebas la conectividad con `ping` y con el modo Simulación. Es el primer contacto con el diagnóstico de conectividad que pide el CCNA.
- **[PR102 — Modelos OSI y TCP/IP](pr102-modelos-osi.md)** (opcional). Observas la encapsulación de una petición web en el modo Simulación y localizas las direcciones MAC de la trama, que se explican en las lecciones 17 y 18. Los puertos, DNS y TCP que también aparecen se tratan en los Temas 7 y 9.

Cada guía enlaza con la rúbrica de su tema, que sirve para revisar la práctica cuando haga falta; ninguna de las tres puntúa en la nota de los RA.

---

## Autocheck de certificación

Estas preguntas siguen el estilo del CCNA, pero son propias del módulo. Son distintas del Autocheck de cada tema: aquí se mezclan conceptos de los Temas 1 y 2, como en el examen real.

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

## Cómo examinarse del CCNA (si decides hacerlo)

Presentarse al examen es voluntario. Si te animas, conviene que sepas cómo funciona. El CCNA lo gestiona **Pearson VUE**, la empresa que organiza los exámenes de Cisco, y se puede hacer en uno de sus centros autorizados o en línea desde casa, con vigilancia por cámara. El precio oficial es de 300 US$ y el examen dura 120 minutos. Ten en cuenta que no se ofrece en español, solo en inglés y en japonés. Antes de reservar, revisa en la página de Cisco ([temario y datos del examen](https://learningnetwork.cisco.com/s/ccna-v2-exam-topics)) las condiciones vigentes.

Si eres menor de edad, Cisco permite examinarse entre los 13 y los 17 años con el consentimiento de tu madre, padre o tutor legal, que debe firmar el acuerdo de certificación y confidencialidad de Cisco antes de reservar el examen; si te examinas en línea, además tiene que estar presente al inicio con su documento de identidad ([política de Cisco sobre menores](https://www.cisco.com/site/us/en/learn/training-certifications/exams/policies.html)). Para preparar el examen no necesitas NetAcad; la cuenta solo es imprescindible para usar Packet Tracer.

---

## Qué no usar

!!! danger "Webs de respuestas y preguntas «reales» de examen"
    Cisco prohíbe usar o difundir preguntas de sus exámenes: al examinarte aceptas un acuerdo de confidencialidad, y quien lo incumple puede perder las certificaciones que tenga y quedarse sin poder examinarse nunca más. Las respuestas de las actividades de NetAcad también son material protegido. Por eso en este módulo **no se usan** páginas que publican preguntas «recordadas» del examen o respuestas de NetAcad, como ExamTopics, ITExamAnswers, ccnadesdecero, ExamCollection, Exam-Labs, Test-King, Fast2Test o certprep.io, ni canales de vídeo que resuelven las actividades de NetAcad. Además del riesgo, no aprendes: el día del examen, o el día que tengas delante un switch real en una empresa, no habrá respuestas que copiar.

---

## Glosario

**certificación**{: #certificacion }
Examen oficial de un fabricante o entidad que acredita unos conocimientos concretos ante cualquier empresa.

**CCNA**{: #ccna }
*Cisco Certified Network Associate*: certificación de Cisco de nivel asociado en redes (examen 200-301).

**NetAcad**{: #netacad }
*Cisco Networking Academy*: plataforma formativa de Cisco. Desde ella, o desde Skills for All, se descarga Packet Tracer.

**dominio**{: #dominio }
Cada uno de los grandes bloques en que Cisco divide el temario de un examen.

**auditoría**{: #auditoria }
Comprobación oral y breve en la que explicas una práctica que has entregado.

*[RA]: Resultado de aprendizaje
*[PR]: Práctica
*[CCNA]: Cisco Certified Network Associate
*[NetAcad]: Cisco Networking Academy
*[SSID]: Service Set Identifier
*[PDU]: Protocol Data Unit
*[PoE]: Power over Ethernet
*[SMR]: Sistemas Microinformáticos y Redes
