---
title: Soluciones del Cuestionario Inicial - Capa Física
description: Respuestas razonadas a las preguntas del cuestionario inicial sobre categorías de cable de par trenzado, fibra óptica, medios guiados y no guiados, espectro electromagnético, estándares inalámbricos IEEE 802.11, cableado estructurado, organización del cableado en edificios, conectores y terminaciones T568A/T568B.
subtitle: Soluciones Cuestionario Inicial - Capa Física.
---

# Soluciones del Cuestionario Inicial - Capa Física

## 1. ¿Qué categorías de cable de par trenzado conoces y para qué se utilizan?

Las categorías de cable de par trenzado están definidas según el estándar **TIA/EIA-568-B** y se clasifican en función de sus prestaciones, principalmente el ancho de banda y la velocidad de transmisión que pueden soportar. Las categorías más representativas en redes de datos son las siguientes:

**Categoría 3 (Cat. 3)**: Con un ancho de banda de 16 MHz, se utilizaba en redes Ethernet de bajas prestaciones. Actualmente está obsoleta y no se utiliza en nuevas instalaciones.

**Categoría 4 (Cat. 4)**: Con un ancho de banda de 20 MHz, se empleaba en redes Token Ring de hasta 16 Mbps. También está obsoleta.

**Categoría 5 (Cat. 5)**: Con un ancho de banda de 100 MHz, soportaba redes Ethernet de hasta 100 Mbps. Actualmente está obsoleta.

**Categoría 5e (Cat. 5e)**: Con un ancho de banda de 100 MHz, soporta redes Ethernet de hasta 1000 Mbps (1 Gbps). Es la opción más económica para instalaciones básicas y se utiliza ampliamente en redes domésticas y pequeñas oficinas donde no se requiere más de 1 Gbps.

**Categoría 6 (Cat. 6)**: Con un ancho de banda de 250 MHz, soporta redes Ethernet de hasta 1 Gbps a 100 metros, y puede alcanzar 10 Gbps a distancias de hasta 37 metros. Es la opción estándar para instalaciones que requieren buen rendimiento con posibilidad de migración futura a 10 Gbps.

**Categoría 6a (Cat. 6a)**: Con un ancho de banda de 500 MHz, garantiza redes Ethernet de hasta 10 Gbps a 100 metros. Es la opción recomendada para instalaciones de alto rendimiento que requieren 10 Gbps garantizado.

**Categoría 7 (Cat. 7)**: Con un ancho de banda de 600 MHz, soporta redes Ethernet de hasta 10 Gbps. No está reconocida por el estándar TIA/EIA, por lo que su uso es limitado.

**Categoría 7a (Cat. 7a)**: Con un ancho de banda de 1000 MHz, también soporta redes Ethernet de hasta 10 Gbps. Tampoco está reconocida por TIA/EIA.

**Categoría 8 (Cat. 8)**: Con un ancho de banda de 2000 MHz, soporta redes Ethernet de hasta 25/40 Gbps a distancias de 30 metros. Está diseñada específicamente para centros de datos y aplicaciones de muy alto rendimiento.

En la actualidad (2025), para nuevas instalaciones de redes de datos se utiliza principalmente la categoría 5e para instalaciones básicas, la categoría 6 para instalaciones estándar, la categoría 6a para instalaciones de alto rendimiento, y la categoría 8 para centros de datos y aplicaciones de muy alto rendimiento.

## 2. ¿Cuándo es recomendable usar fibra óptica en lugar de cable de cobre?

La fibra óptica es recomendable en lugar del cable de cobre (par trenzado) en las siguientes situaciones:

**Distancias largas**: La fibra óptica sufre menos atenuación que el cobre, permitiendo cubrir distancias mucho mayores sin necesidad de repetidores. Mientras que el par trenzado tiene limitaciones de distancia (típicamente 100 metros para Ethernet), la fibra óptica puede transmitir señales a distancias de varios kilómetros. La fibra monomodo (OS1) puede alcanzar distancias superiores a 10 km para 1 Gbps y más de 40 km para 100 Mbps.

**Alto ancho de banda**: Cuando se requiere un ancho de banda muy superior al que puede ofrecer el cobre. La fibra óptica permite velocidades de transmisión que pueden alcanzar varios terabits por segundo, mientras que el par trenzado está limitado a velocidades menores, típicamente hasta 10 Gbps en las mejores condiciones (Cat. 6a) o 25/40 Gbps a distancias muy cortas (Cat. 8).

**Entornos con interferencias electromagnéticas**: Al transmitir información mediante pulsos de luz en lugar de señales eléctricas, la fibra óptica es completamente inmune a interferencias electromagnéticas (EMI) y radiofrecuencias (RFI). Esto la hace ideal para entornos industriales, instalaciones con alta densidad de equipos eléctricos, o lugares donde hay fuentes de interferencia electromagnética intensas.

**Requisitos de seguridad**: Cuando se requiere un nivel de seguridad superior en la transmisión. Es extremadamente difícil interceptar la señal óptica sin ser detectado, ya que cualquier intento de acceso físico a la fibra provoca una pérdida de señal detectable. Esto proporciona un nivel de seguridad superior al par trenzado.

**Conexiones entre edificios (backbone vertical y de campus)**: Para el subsistema vertical (backbone) que enlaza distribuidores de planta con el distribuidor de edificio, y especialmente para el subsistema de campus que conecta diferentes edificios. La fibra óptica es la opción estándar para estas conexiones debido a las distancias y el ancho de banda requerido.

**Centros de datos y aplicaciones críticas**: En instalaciones donde el rendimiento, la confiabilidad y la capacidad de escalabilidad son críticos, la fibra óptica ofrece ventajas significativas en términos de ancho de banda, latencia y capacidad de crecimiento futuro.

**Resistencia a condiciones ambientales adversas**: La fibra óptica es más resistente a condiciones ambientales adversas y tiene una vida útil más larga que el cobre, lo que la hace adecuada para instalaciones exteriores o en entornos hostiles.

## 3. ¿Qué diferencias hay entre los medios guiados y no guiados?

Los medios guiados y no guiados se diferencian fundamentalmente en la forma en que transportan las señales y en sus características técnicas:

**Medios guiados**:

Los medios guiados son cables físicos que interconectan los equipos. A través de ellos se emite información en forma de señales eléctricas u ópticas. Los principales medios guiados en redes de datos son:

- **Cable de par trenzado**: Transmite señales eléctricas mediante pares de conductores trenzados. Incluye variantes como UTP, FTP, STP según el tipo de blindaje.
- **Cable coaxial**: Utiliza dos conductores concéntricos para transmitir señales eléctricas.
- **Fibra óptica**: Transmite información mediante pulsos de luz que se propagan a través de un núcleo de vidrio o plástico.

**Características de los medios guiados**:

- Requieren una conexión física directa entre los dispositivos.
- La señal está confinada dentro del medio, lo que proporciona mayor seguridad y menor interferencia externa.
- Ofrecen mayor ancho de banda y velocidades de transmisión más altas y predecibles.
- Son más seguros, ya que es necesario acceso físico para interceptar la señal.
- Requieren instalación de infraestructura de cableado.
- Tienen limitaciones de distancia que varían según el tipo de medio.

**Medios no guiados**:

Los medios no guiados transportan ondas electromagnéticas sin el empleo de un conductor físico. Estas ondas se propagan a través del aire, el vacío o el agua, utilizando diferentes frecuencias del espectro electromagnético.

**Características de los medios no guiados**:

- No requieren conexión física entre dispositivos, permitiendo movilidad.
- La señal se propaga por el espacio, lo que permite comunicación sin cables.
- Utilizan diferentes bandas del espectro electromagnético (radiofrecuencia, microondas, infrarrojos, etc.).
- Están sujetos a interferencias del entorno y pueden verse afectados por obstáculos físicos.
- Tienen limitaciones de alcance y pueden requerir licencias para ciertas frecuencias.
- Ofrecen mayor flexibilidad y movilidad, pero generalmente con menor ancho de banda y mayor latencia que los medios guiados.
- Ejemplos incluyen Wi-Fi (IEEE 802.11), Bluetooth, comunicaciones por satélite, microondas terrestres, etc.

**Diferencias principales**:

- **Infraestructura**: Los medios guiados requieren instalación de cables, mientras que los no guiados utilizan el espacio aéreo.
- **Movilidad**: Los medios no guiados permiten movilidad, mientras que los guiados requieren conexión física.
- **Seguridad**: Los medios guiados ofrecen mayor seguridad física, mientras que los no guiados son más vulnerables a interceptación.
- **Interferencias**: Los medios guiados son menos susceptibles a interferencias externas, mientras que los no guiados pueden verse afectados por múltiples factores ambientales.
- **Ancho de banda**: Los medios guiados generalmente ofrecen mayor ancho de banda y velocidades más altas.
- **Alcance**: Los medios guiados tienen limitaciones de distancia según el tipo de cable, mientras que los no guiados dependen de la potencia de transmisión y las condiciones del entorno.

## 4. ¿Qué es el espectro electromagnético y por qué es importante en comunicaciones?

El **espectro electromagnético** es el rango completo de todas las frecuencias posibles de radiación electromagnética, desde las frecuencias más bajas (ondas de radio) hasta las más altas (rayos gamma). En el contexto de las comunicaciones, el espectro electromagnético abarca un amplio rango que va desde las frecuencias más bajas utilizadas en comunicaciones especiales hasta frecuencias extremadamente elevadas para aplicaciones avanzadas.

**Estructura del espectro electromagnético en comunicaciones**:

El espectro se divide en diferentes bandas de frecuencia, cada una asignada a diferentes tecnologías y servicios de comunicación:

- **Radioondas**: Incluyen bandas VLF, LF, MF, HF, VHF y UHF. Se utilizan para radio AM, radio FM, televisión digital terrestre (TDT) y comunicaciones de navegación.

- **Microondas**: Operan en bandas SHF y EHF. Se utilizan para Bluetooth, ZigBee, redes WLAN y WiMAX, TV por satélite, transmisión telefónica y comunicaciones con radares.

- **Infrarrojos**: Se utilizan para mandos a distancia, sistemas de control domótico y comunicación entre dispositivos de corta distancia.

- **Banda ISM (Industrial, Scientific and Medical)**: Bandas de uso libre sin necesidad de licencia, incluyendo 2,4 GHz (Wi-Fi, Bluetooth), 5 GHz (Wi-Fi de alta velocidad), 868 MHz (dispositivos IoT en Europa) y 915 MHz (aplicaciones industriales en América).

- **Luz visible**: Se utiliza en comunicaciones ópticas, fibra óptica, láser de comunicación, sistemas Li-Fi y comunicación submarina.

**Importancia del espectro electromagnético en comunicaciones**:

**Asignación de frecuencias**: El espectro electromagnético permite que diferentes tecnologías y servicios de comunicación operen en frecuencias específicas sin interferirse entre sí. Cada tecnología tiene su "carril" asignado en el espectro, lo que evita interferencias y garantiza el funcionamiento ordenado de los sistemas.

**Regulación y control**: La atribución de bandas de frecuencias se recoge en documentos oficiales como el **Cuadro Nacional de Atribución de Frecuencias (CNAF)** en España. Esta regulación es esencial para evitar interferencias entre servicios y garantizar el uso eficiente del espectro.

**Diversidad de aplicaciones**: Diferentes bandas del espectro son adecuadas para diferentes tipos de comunicación. Por ejemplo, las frecuencias bajas pueden atravesar obstáculos y cubrir grandes distancias (radio AM), mientras que las frecuencias altas ofrecen mayor ancho de banda pero menor alcance (Wi-Fi de 5 GHz).

**Eficiencia espectral**: El uso eficiente del espectro permite maximizar la capacidad de comunicación disponible. Tecnologías modernas como OFDM (utilizado en Wi-Fi y LTE) permiten utilizar el espectro de forma más eficiente.

**Innovación tecnológica**: El desarrollo de nuevas tecnologías de comunicación depende de la disponibilidad y asignación adecuada de bandas del espectro. Por ejemplo, el despliegue de 5G requiere la asignación de nuevas bandas de frecuencia.

**Comunicaciones inalámbricas**: Todas las comunicaciones inalámbricas (Wi-Fi, Bluetooth, telefonía móvil, satélites, etc.) dependen del espectro electromagnético para funcionar. Sin el espectro, no sería posible la comunicación sin cables.

**Compatibilidad internacional**: La estandarización del uso del espectro permite la compatibilidad de dispositivos entre países y regiones, facilitando el comercio internacional y la comunicación global.

En resumen, el espectro electromagnético es el recurso fundamental que permite todas las comunicaciones inalámbricas. Su correcta gestión, asignación y regulación es esencial para el funcionamiento de las telecomunicaciones modernas, desde la radio y la televisión hasta las redes móviles 5G y las comunicaciones por satélite.

## 5. ¿Cuáles son los principales estándares inalámbricos IEEE 802.11?

Los estándares **IEEE 802.11** definen las especificaciones técnicas para redes de área local inalámbricas (WLAN), comúnmente conocidas como Wi-Fi. Estos estándares han evolucionado significativamente desde su creación, mejorando la velocidad, eficiencia y capacidades de las redes inalámbricas.

**IEEE 802.11a (Wi-Fi 2, 1999)**:

- Opera exclusivamente en la banda de **5 GHz**.
- Velocidad máxima de hasta **54 Mbps**.
- Utiliza tecnología **OFDM** con 12 canales.
- Ventaja principal: menos interferencias que la banda de 2,4 GHz.
- Menor alcance que 802.11b debido a la mayor frecuencia.

**IEEE 802.11b (Wi-Fi 1, 1999)**:

- Opera en la banda de **2,4 GHz**.
- Velocidad máxima de hasta **11 Mbps**.
- Fue muy popular en sus inicios pero actualmente está obsoleto.
- Mayor alcance que 802.11a pero más susceptible a interferencias.

**IEEE 802.11g (Wi-Fi 3, 2003)**:

- Opera en la banda de **2,4 GHz**.
- Velocidad máxima de hasta **54 Mbps**.
- Utiliza tecnología **OFDM**.
- Compatible con dispositivos 802.11b.
- Fue un estándar muy extendido antes de la llegada de 802.11n.

**IEEE 802.11n (Wi-Fi 4, 2009)**:

- Opera en bandas de **2,4 GHz y 5 GHz** (dual-band).
- Velocidad máxima de hasta **600 Mbps**.
- Utiliza tecnología **MIMO** (Multiple Input Multiple Output) y canales de 40 MHz.
- Retrocompatible con estándares anteriores.
- Representó un salto significativo en rendimiento y es aún muy utilizado.

**IEEE 802.11ac (Wi-Fi 5, 2013)**:

- Opera exclusivamente en la banda de **5 GHz**.
- Velocidad máxima de hasta **6,77 Gbps** (en condiciones óptimas).
- Utiliza tecnología **MU-MIMO** (Multi-User MIMO) y canales de 160 MHz.
- Modulación **256-QAM**.
- Diseñado para alta densidad de dispositivos y mejor rendimiento en entornos con múltiples usuarios simultáneos.

**IEEE 802.11ax (Wi-Fi 6, 2019)**:

- Opera en bandas de **2,4 GHz, 5 GHz y 6 GHz** (tri-band).
- Velocidad máxima de hasta **9,6 Gbps**.
- Utiliza tecnología **OFDMA** (Orthogonal Frequency Division Multiple Access) y **TWT** (Target Wake Time).
- Optimizado para entornos con muchos dispositivos IoT y mejor gestión de interferencias.
- Mejor eficiencia energética y menor latencia.
- Es el estándar actual más avanzado y ampliamente desplegado.

**IEEE 802.11be (Wi-Fi 7, 2024)**:

- Opera en bandas de **2,4 GHz, 5 GHz y 6 GHz**.
- Velocidad máxima de hasta **46 Gbps**.
- Utiliza tecnología **Multi-Link** y canales de **320 MHz**.
- Modulación **4096-QAM**.
- Representa la última generación de Wi-Fi, diseñado para aplicaciones de muy alto rendimiento y baja latencia.

**Características comunes de los estándares IEEE 802.11**:

Todos estos estándares comparten características fundamentales:

- **Compatibilidad hacia atrás**: Los estándares más recientes suelen ser compatibles con versiones anteriores, permitiendo que dispositivos antiguos funcionen en redes modernas (aunque con limitaciones de velocidad).

- **Seguridad**: Todos los estándares modernos incluyen protocolos de seguridad como WPA3, aunque los más antiguos pueden requerir actualizaciones.

- **Modos de operación**: Todos soportan modos de infraestructura (con punto de acceso) y ad-hoc (punto a punto).

- **Regulación**: Todos deben cumplir con las regulaciones locales sobre el uso del espectro radioeléctrico, que pueden variar entre países.

La evolución de los estándares IEEE 802.11 ha permitido que las redes Wi-Fi pasen de ser una tecnología complementaria a convertirse en la principal forma de conectividad en muchos entornos, ofreciendo velocidades y capacidades que compiten con las conexiones cableadas en muchos escenarios de uso.

## 6. ¿Qué elementos componen un sistema de cableado estructurado?

Un **sistema de cableado estructurado** es una infraestructura de telecomunicaciones completa y estandarizada que proporciona la organización jerárquica del cableado en edificios. Está diseñado según estándares internacionales como **ISO/IEC 11801** y **TIA/EIA-568**, que garantizan la interoperabilidad y el rendimiento óptimo del sistema.

Según el contenido del tema de Capa Física, el cableado estructurado forma parte de la infraestructura de red y comprende todos los elementos físicos y lógicos necesarios para establecer la conectividad entre dispositivos en una red local. Esta infraestructura incluye:

**Medios de transmisión**: Los diferentes tipos de cables (par trenzado, coaxial, fibra óptica) que transportan la información según las necesidades de cada instalación.

**Conectores y terminaciones**: Las interfaces entre medios y equipos, incluyendo los conectores RJ para par trenzado, conectores de fibra óptica y coaxiales, así como las terminaciones estándar T568A y T568B.

**Equipos de distribución**: Los dispositivos que gestionan el tráfico de datos y organizan las conexiones, como switches, routers, paneles de parcheo y armarios de distribución.

**Organización jerárquica**: El sistema se organiza en diferentes niveles que conectan las áreas de trabajo con los puntos de distribución, permitiendo una estructura escalable y mantenible.

**Estándares y normativas**: El cumplimiento de estándares internacionales como TIA/EIA-568 garantiza que la instalación sea compatible con diferentes tecnologías y pueda evolucionar sin necesidad de rehacer toda la infraestructura.

El cableado estructurado permite centralizar los servicios de voz, datos y otros servicios en una única infraestructura, facilitando la gestión, el mantenimiento y la evolución de la red. La correcta planificación e implementación de esta infraestructura es crucial para garantizar la escalabilidad, mantenibilidad y rendimiento de la red.

## 7. ¿Cómo se organiza el cableado horizontal y vertical en un edificio?

La organización del cableado horizontal y vertical en un edificio forma parte del **cableado estructurado**, que es la organización jerárquica del cableado en edificios según los estándares internacionales como **ISO/IEC 11801** y **TIA/EIA-568**.

**Cableado horizontal**:

El **cableado horizontal** es la parte del sistema que conecta las áreas de trabajo (donde se encuentran los equipos de usuario) con los puntos de distribución en cada planta del edificio. Este cableado:

- Emplea principalmente **cable de par trenzado** de diferentes categorías según los requisitos de velocidad y distancia.
- Tiene limitaciones de distancia que dependen del tipo de cable utilizado. Para par trenzado, la distancia máxima típica es de 100 metros entre equipos, lo que incluye el cable horizontal y los latiguillos en cada extremo.
- Puede utilizar diferentes tipos de canalizaciones (canaletas, bandejas, suelos técnicos) según las características del edificio y las necesidades de la instalación.
- Se organiza por plantas, con cada nivel del edificio teniendo su propio subsistema horizontal que converge en un punto de distribución.

**Cableado vertical (Backbone)**:

El **cableado vertical o backbone** es la parte del sistema que conecta los diferentes niveles del edificio, formando la columna vertebral de la red. Este cableado:

- Enlaza los puntos de distribución de cada planta con el distribuidor principal del edificio.
- Puede utilizar **par trenzado** para distancias cortas, pero generalmente se emplea **fibra óptica** para cubrir mayores distancias y proporcionar mayor ancho de banda.
- La fibra óptica es especialmente adecuada para el backbone debido a su capacidad de cubrir distancias largas (la fibra monomodo puede alcanzar varios kilómetros) y su inmunidad a interferencias electromagnéticas.
- Debe discurrir por canalizaciones dedicadas exclusivamente para telecomunicaciones, sin compartir espacios con otros servicios del edificio.

**Principios de organización**:

La organización del cableado en edificios se basa en principios que garantizan:

- **Flexibilidad**: La capacidad de adaptarse a cambios en la disposición de espacios y equipos sin necesidad de rehacer toda la instalación.
- **Escalabilidad**: La posibilidad de ampliar la red conforme crecen las necesidades.
- **Mantenibilidad**: La facilidad de acceso y gestión de los cables y equipos para facilitar el mantenimiento.
- **Estandarización**: El cumplimiento de estándares internacionales que garantizan la compatibilidad y la calidad de la instalación.

Esta organización jerárquica permite que la infraestructura de red sea eficiente, mantenible y capaz de evolucionar con las necesidades del edificio y las tecnologías de comunicación, cumpliendo con los estándares de cableado estructurado.

## 8. ¿Qué tipos de conectores se utilizan para cable de par trenzado?

El cable de par trenzado utiliza conectores tipo **RJ (Registered Jack)**, diseñados específicamente para la conexión de equipos en redes de datos y telefonía. Estos conectores se clasifican según dos parámetros: el número de **posiciones** (ranuras disponibles) y el número de **contactos** (conectores metálicos que se utilizan).

**Conector RJ-9**:

- Es el más pequeño de los conectores RJ.
- Se utiliza para conectar los auriculares del teléfono.
- Es un conector **4P4C** (4 posiciones, 4 contactos).
- No se utiliza en redes de datos, solo para telefonía.

**Conector RJ-11**:

- Es un conector dedicado mayoritariamente a la **telefonía analógica**.
- Tiene seis posiciones sobre las que se asientan dos contactos (**6P2C**).
- Su uso principal es conectar el terminal telefónico a la red.
- La variante del RJ-11 que emplea un par de contactos más (**6P4C**) se llama **RJ-14**.
- No se utiliza para redes de datos Ethernet.

**Conector RJ-45**:

- Es el conector estándar empleado para cable de par trenzado en **redes Ethernet**.
- Es del tipo **8P8C** (8 posiciones, 8 contactos), lo que significa que utiliza todas sus posiciones para recibir los cuatro pares del cable de par trenzado.
- Este conector también soporta el uso de menos pares, dando lugar a las variantes 8P6C, 8P4C y 8P2C, casi todas dedicadas a telefonía o líneas RDSI.
- El conector RJ-45 puede ser o no apantallado. Si lo es, por encima de la carcasa plástica tiene un armazón metálico que lo protege de interferencias.
- Los conectores apantallados suelen utilizarse con cableado que tenga algún tipo de blindaje (FTP, STP, etc.).
- Es el conector más utilizado en redes locales modernas.

**Características técnicas de los conectores RJ**:

**Sistema de conexión**: Los conectores RJ utilizan un sistema de conexión mediante pestaña que se engancha al conector hembra, proporcionando una conexión segura y fácil de desconectar cuando es necesario.

**Compatibilidad**: Los conectores RJ están diseñados para ser compatibles con los estándares de cableado estructurado, especialmente con las normas TIA/EIA-568 que definen las terminaciones T568A y T568B.

**Aplicaciones según el tipo de conector**:

- **RJ-9**: Solo para auriculares de teléfono.
- **RJ-11/RJ-14**: Para telefonía analógica y RDSI.
- **RJ-45**: Para redes Ethernet (10BASE-T, 100BASE-TX, 1000BASE-T, 10GBASE-T, etc.).

**Consideraciones de instalación**:

- Los conectores RJ-45 deben instalarse siguiendo las terminaciones estándar T568A o T568B.
- Es importante mantener la integridad del trenzado de los pares hasta el punto de conexión para minimizar interferencias.
- Los conectores apantallados deben conectarse correctamente a tierra para que el blindaje sea efectivo.
- La calidad del conector y su instalación afecta directamente al rendimiento de la conexión, especialmente en categorías altas (Cat. 6 y superiores).

**Evolución y estándares**:

Los conectores RJ han evolucionado para soportar las mayores velocidades y categorías de cable. Los conectores modernos para Cat. 6 y superiores están diseñados para mantener las especificaciones de rendimiento y reducir la diafonía y las interferencias.

En resumen, aunque existen varios tipos de conectores RJ, el **RJ-45 (8P8C)** es el estándar universal para cable de par trenzado en redes Ethernet, siendo el conector más utilizado en instalaciones de cableado estructurado para redes de datos.

## 9. ¿Cómo se realiza la terminación de cables según los estándares T568A y T568B?

La **terminación** de cables de par trenzado se refiere a la posición específica de los hilos de colores dentro del conector RJ-45. Esta posición está regulada en la norma **TIA/EIA-568-B**, que define dos terminaciones estándar: **T568A** y **T568B**.

**Estándar T568A**:

En la terminación T568A, los hilos se ordenan de izquierda a derecha (visto desde el frente del conector) de la siguiente manera:

1. **Blanco/Verde** (par 3, hilo rayado)
2. **Verde** (par 3, hilo sólido)
3. **Blanco/Naranja** (par 2, hilo rayado)
4. **Azul** (par 1, hilo sólido)
5. **Blanco/Azul** (par 1, hilo rayado)
6. **Naranja** (par 2, hilo sólido)
7. **Blanco/Marrón** (par 4, hilo rayado)
8. **Marrón** (par 4, hilo sólido)

**Estándar T568B**:

En la terminación T568B, los hilos se ordenan de izquierda a derecha de la siguiente manera:

1. **Blanco/Naranja** (par 2, hilo rayado)
2. **Naranja** (par 2, hilo sólido)
3. **Blanco/Verde** (par 3, hilo rayado)
4. **Azul** (par 1, hilo sólido)
5. **Blanco/Azul** (par 1, hilo rayado)
6. **Verde** (par 3, hilo sólido)
7. **Blanco/Marrón** (par 4, hilo rayado)
8. **Marrón** (par 4, hilo sólido)

**Diferencia principal entre T568A y T568B**:

La diferencia fundamental entre ambas terminaciones es que en **T568B, los pares 2 y 3 están intercambiados respecto a T568A**. Específicamente:
- En T568A: el par 2 (naranja) está en las posiciones 3 y 6, y el par 3 (verde) está en las posiciones 1 y 2.
- En T568B: el par 2 (naranja) está en las posiciones 1 y 2, y el par 3 (verde) está en las posiciones 3 y 6.

Los pares 1 (azul) y 4 (marrón) mantienen las mismas posiciones en ambas terminaciones.

**Recomendación normativa**:

Según la norma, la terminación a emplear para la mayor parte del tendido de cableado de la red debería ser **T568A**. Sin embargo, debido a que típicamente se ha usado la terminación **T568B** (definida en normas anteriores), muchas instalaciones de redes siguen empleando dicha terminación en lugar de la T568A. Lo importante es mantener la consistencia en toda la instalación.

**Tipos de cable según la terminación**:

Con estas terminaciones pueden crearse dos tipos de cable:

**Cable directo (straight-through)**:

- Utiliza la **misma terminación en los dos extremos** (T568A-T568A o T568B-T568B).
- Este cable es el que se usa para la mayoría de las conexiones en la red.
- Se utiliza para conectar equipos diferentes, como un ordenador a un switch, un switch a un router, etc.
- Es el tipo de cable más común en instalaciones de red.

**Cable cruzado (crossover)**:

- Utiliza **diferente terminación en los dos extremos** (normalmente T568A en un extremo y T568B en el otro).
- Este cable se utiliza para conectar directamente dos equipos del mismo tipo sin necesidad de un dispositivo intermedio.
- Tradicionalmente se usaba para conectar dos ordenadores directamente, o dos switches entre sí.
- Con los switches modernos que soportan Auto-MDIX, los cables cruzados son menos necesarios, ya que los dispositivos pueden detectar y ajustar automáticamente la configuración.

**Proceso de terminación**:

Para realizar correctamente la terminación de un cable:

1. **Pelar la cubierta exterior**: Retirar aproximadamente 2-3 cm de la cubierta exterior del cable, teniendo cuidado de no dañar los hilos internos.

2. **Desenrollar y ordenar los pares**: Desenrollar los pares trenzados y ordenar los hilos según la terminación elegida (T568A o T568B).

3. **Cortar a la medida**: Cortar los hilos de forma que queden todos a la misma longitud (aproximadamente 1,5 cm).

4. **Insertar en el conector**: Insertar los hilos en el conector RJ-45 en el orden correcto, asegurándose de que todos los hilos lleguen hasta el final del conector y que la cubierta exterior quede dentro del conector para proporcionar sujeción.

5. **Crimpar**: Utilizar una herramienta de crimpado para fijar el conector, asegurándose de que los contactos metálicos perforan correctamente los hilos y que el conector queda firmemente sujeto al cable.

6. **Verificar**: Comprobar la continuidad y el orden de los hilos utilizando un comprobador de cables (cable tester).

**Consideraciones importantes**:

- Es fundamental mantener el trenzado de los pares hasta el punto de conexión para minimizar interferencias y diafonía.
- La calidad de la terminación afecta directamente al rendimiento del cable, especialmente en categorías altas (Cat. 6 y superiores).
- Para categorías 6 y superiores, se recomienda el uso de conectores y herramientas de crimpado de alta calidad.
- A partir de la categoría 6, por norma no se permite la fabricación casera de latiguillos; deben utilizarse cables certificados de fábrica.

La correcta terminación de los cables según los estándares T568A o T568B es esencial para garantizar el funcionamiento adecuado de la red y cumplir con las especificaciones de rendimiento de cada categoría de cable.

