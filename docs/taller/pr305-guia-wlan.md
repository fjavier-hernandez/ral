# PR305 — Guía de taller: NIC y WLAN real

Antes de empezar, repasad las [normas del taller](../00-normas/normas_taller.md). Esta guía desarrolla paso a paso la práctica **PR305** del [Tema 3](../03-cableado-estructurado/tema3.md#pr305-taller-wlan-real). Se trabaja por grupos en el aula-taller con equipos de sobremesa del centro y con los puntos de acceso y routers Wi‑Fi del taller. La rúbrica y la entrega son las del tema.

!!! warning "Antes de empezar"
    - El router o AP del grupo **no se conecta nunca a la red del centro** (ni a las rosetas de la pared ni al switch del aula). Si se conecta, su servidor DHCP (el servicio que reparte direcciones IP) puede dejar sin red a otros equipos del instituto. Cada grupo trabaja con la red propia de su router.
    - El equipo se abre **siempre apagado y desenchufado**.

## Material por grupo

- Un equipo de sobremesa con una NIC (*Network Interface Card*, tarjeta de red) PCIe ya instalada, o un adaptador USB Wi‑Fi.
- Un router o punto de acceso (AP, *Access Point*) Wi‑Fi del taller con su alimentador.
- Un latiguillo RJ‑45. Podéis usar los que hicisteis en la [PR201](pr201-guia-crimpado.md).
- Un destornillador de estrella y un portátil o un móvil para hacer de cliente Wi‑Fi.

## Fase 1. Extraer y volver a montar la NIC (CE3b)

Los equipos del taller ya tienen la tarjeta de red instalada. El objetivo es **extraerla, identificarla y volver a montarla** correctamente, como haríais al sustituir una tarjeta averiada.

1. Apagad el equipo desde el sistema operativo y **desenchufad el cable de corriente**. Con el equipo ya desenchufado, mantened pulsado el botón de encendido unos segundos para descargar la energía que queda en la fuente.
2. **Descarga de electricidad estática.** Antes de tocar ningún componente, tocad con la mano una parte metálica **sin pintar** del chasis. Repetidlo cada vez que os mováis o cojáis algo. Sujetad la tarjeta siempre por los bordes, sin tocar los contactos dorados ni los chips.
3. Abrid la tapa lateral y localizad la tarjeta en su ranura **PCIe** (*PCI Express*, el bus de expansión de la placa base). Haced una **foto antes de tocar nada**.
4. Quitad el tornillo o la pestaña que la sujeta al chasis y tirad de ella hacia arriba con suavidad y de forma recta. Si la ranura tiene una patilla de bloqueo, liberadla primero.
5. **Identificad la tarjeta**: anotad el fabricante, el modelo, el tipo de ranura (x1, x4…) y la dirección MAC (*Media Access Control*, el identificador físico de la tarjeta) si viene en la pegatina. Haced una foto de la tarjeta.
6. Volved a montarla: alineadla con la ranura, presionad de forma uniforme hasta que encaje del todo y atornilladla al chasis. Cerrad la tapa.
7. Si vuestro grupo usa un adaptador USB Wi‑Fi en lugar de una tarjeta PCIe, conectadlo a un puerto USB del equipo y anotad igualmente el fabricante y el modelo.

## Fase 2. Driver y comprobación en el sistema (CE4f)

El **driver** (controlador) es el software que permite al sistema operativo usar la tarjeta.

1. Encended el equipo y abrid el **Administrador de dispositivos** (clic derecho en Inicio). En «Adaptadores de red» debe aparecer la tarjeta **sin** triángulo amarillo.
2. Si aparece con aviso, o como «Dispositivo desconocido», instalad o actualizad el driver siguiendo la guía de Microsoft [Actualizar controladores manualmente en Windows](https://support.microsoft.com/es-es/windows/actualizar-controladores-manualmente-en-windows-ec62f46c-ff14-c91d-eead-d7126dc1f7b6). Si Windows no lo encuentra, buscadlo en la web del fabricante con el modelo que anotasteis, por ejemplo en el [centro de descargas de TP‑Link](https://www.tp-link.com/es/support/download/) o en el [soporte de D‑Link](https://www.dlink.com/es/es/support).
3. Abrid una consola (`cmd`) y ejecutad `ipconfig /all`. Comprobad que aparece el adaptador y anotad su dirección física (MAC).
4. Haced una **captura** del Administrador de dispositivos y otra de `ipconfig /all`.

## Fase 3. Restablecer y conectar el AP

1. Conectad el alimentador del router o AP y esperad a que arranque.
2. **Restablecedlo a valores de fábrica**: con un clip, mantened pulsado el botón *Reset* unos 10 segundos hasta que parpadeen los LED. Así borráis la configuración del grupo anterior.
3. Mirad la **etiqueta** de la parte inferior: indica la dirección de acceso (por ejemplo `192.168.0.1`, `192.168.1.1` o `tplinkwifi.net`), el usuario y la contraseña de fábrica.
4. Conectad el equipo a un puerto **LAN** del router con el latiguillo. El puerto **WAN** o *Internet* se queda **libre**.
5. Abrid el navegador y entrad en la dirección de la etiqueta. Si el modelo os pide crear una contraseña de administración, poned una del grupo y anotadla.

!!! tip "Si no tenéis AP o queréis ver un modelo antes de tocarlo"
    TP‑Link publica [emuladores oficiales](https://emulator.tp-link.com/) del panel web de sus routers y AP. Buscad vuestro modelo para practicar la configuración sin el equipo real.

## Fase 4. Configurar la WLAN (CE4a–CE4d, CE4i)

En el panel web, en el apartado *Wireless* o *Inalámbrico*:

1. **Modo de funcionamiento**: dejadlo como **punto de acceso** o *router*, según el modelo. Anotad qué otros modos ofrece (repetidor, cliente, puente) y para qué sirve cada uno.
2. **SSID** (*Service Set Identifier*, el nombre de la red): `RAL-GrupoX`, cambiando la X por el número de vuestro grupo.
3. **Banda y canal**: en 2,4 GHz usad solo los canales **1, 6 u 11**, que son los que no se solapan entre sí. Elegid el que tenga menos redes vecinas (fase 6). Si el equipo tiene 5 GHz, configurad también esa banda.
4. **Seguridad**: **WPA2‑Personal** con cifrado **AES**, o **WPA3** si el equipo lo admite. La clave tiene que tener al menos 12 caracteres. No uséis WEP ni WPA, porque son inseguros.
5. **Red de invitados**: si el equipo la tiene, activadla con otro SSID (`RAL-GrupoX-Invitados`) y su propia clave, y comprobad la opción que impide a los invitados ver la red principal.
6. Guardad los cambios y haced una **captura** de cada pantalla de configuración.

## Fase 5. Conectar un cliente y comprobar (CE4e)

1. Conectad un portátil o un móvil a vuestro SSID.
2. Comprobad que el cliente ha recibido una IP del rango del router y anotadla.
3. Desde el equipo de sobremesa, haced `ping` a la IP del cliente. Haced una captura del resultado.
4. En el panel del router, buscad la **lista de clientes conectados** (*DHCP Clients* o *Wireless Clients*) y haced una captura en la que se vea el cliente.

## Fase 6. Canales e interferencias

1. Con un móvil Android, instalad [WiFiAnalyzer](https://play.google.com/store/apps/details?id=com.vrem.wifianalyzer) (gratuita y de código abierto) y mirad el gráfico de canales.
2. En un portátil con Windows, podéis usar el comando `netsh wlan show networks mode=bssid`, que lista las redes cercanas con su canal y su intensidad. Está explicado en la [documentación de `netsh wlan` de Microsoft](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/netsh-wlan).
3. Anotad en qué canales están las redes vecinas y justificad el canal que habéis elegido. Haced una captura.

## Fase 7. Dejarlo todo como estaba

1. Restableced el router o AP a valores de fábrica con el botón *Reset*.
2. Desconectad el latiguillo y el alimentador y guardad el material en su caja.
3. Comprobad que el equipo de sobremesa arranca y sigue viendo su tarjeta de red.

## Ampliación opcional: firmware DD-WRT

Esta fase solo se hace si el profesor lo autoriza y sobre los modelos que él indique. **DD‑WRT** es un firmware libre (el software interno del router) que sustituye al del fabricante y añade funciones avanzadas. El objetivo es comparar las dos interfaces y sus opciones.

!!! danger "Riesgo de dejar el router inservible"
    Si se carga un firmware que no corresponde exactamente al modelo **y a la versión de hardware** del router, o si se corta la corriente durante la carga, el equipo puede quedar inutilizado. Por eso:

    - Comprobad el modelo y la versión (por ejemplo «V9») en la etiqueta del router.
    - Buscadlo en la [base de datos oficial de routers de DD‑WRT](https://dd-wrt.com/support/router-database/). Si no aparece como compatible, **no se instala**.
    - Antes de nada, descargad el **firmware original** del fabricante para ese modelo y versión, por ejemplo desde el [centro de descargas de TP‑Link](https://www.tp-link.com/es/support/download/), para poder volver atrás.
    - Cargad el firmware **siempre por cable**, nunca por Wi‑Fi, y no toquéis el router hasta que termine.

1. Antes de instalar nada, explorad la [demostración oficial de la interfaz de DD‑WRT](https://dd-wrt.com/demo/) para saber qué os vais a encontrar.
2. Seguid la [guía oficial de instalación de DD‑WRT](https://wiki.dd-wrt.com/wiki/index.php/Installation) y las instrucciones específicas que la base de datos indique para vuestro modelo. Algunos modelos necesitan primero un fichero de tipo *factory-to-ddwrt* y después otro de tipo *webflash*.
3. Tras la instalación, la dirección de acceso suele pasar a ser `192.168.1.1`. Repetid la configuración de la fase 4 (SSID, canal, WPA2 y red de invitados) en DD‑WRT.
4. Haced una **tabla comparativa** entre el firmware original y DD‑WRT: opciones de modo (AP, repetidor, cliente, puente), seguridad, red de invitados, control de potencia de emisión, estadísticas y facilidad de uso.
5. Al terminar, volved a cargar el firmware original si el profesor lo pide.

Añadid la tabla comparativa y las capturas de DD‑WRT al `PR305.md`. Como alternativa a DD‑WRT existe [OpenWrt](https://openwrt.org/toh/start), con su propia lista de equipos compatibles.

## Entrega

Un fichero `PR305.md` por grupo, subido a Aules, con:

- Las fotos de la tarjeta (antes, fuera de la ranura y montada) y sus datos: fabricante, modelo, ranura y MAC.
- Las capturas del Administrador de dispositivos y de `ipconfig /all`.
- Las capturas de la configuración: modo, SSID, banda, canal, seguridad y red de invitados.
- La IP del cliente, el `ping` y la lista de clientes del router.
- El análisis de canales y por qué elegisteis el vuestro.
- Si hicisteis la ampliación, la tabla comparativa entre el firmware original y DD‑WRT.
- Las incidencias que hayáis tenido y cómo las resolvisteis.

La calificación sigue la rúbrica de la [PR305 en el Tema 3](../03-cableado-estructurado/tema3.md#pr305-taller-wlan-real).
