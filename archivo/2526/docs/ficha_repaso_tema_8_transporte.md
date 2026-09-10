---
title: Ficha de repaso - Examen Capa de Transporte
description: Resumen y preparación para el examen de la capa de transporte (puertos, sockets, UDP, TCP, multiplexación, control de flujo y segmentación) (SMR).
---

# :material-book-open-variant: Ficha de repaso para el examen

**Tema:** Capa de Transporte (Unidad 8)  
**Módulo:** Redes de Área Local (RAL)  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

Esta ficha te ayuda a preparar el examen de la **capa de transporte**. Incluye un resumen de conceptos y fórmulas de referencia y **actividades de práctica** del mismo tipo que el examen: cálculo de puertos y multiplexación, elección TCP vs UDP en casos reales, handshake y números de secuencia, control de flujo y congestión, y segmentación. El examen será íntegramente de actividades prácticas.

[Consulta las **soluciones de las actividades**](./extra/ficha_repaso_tema_8_transporte_soluciones.md) para comprobar tus resultados después de practicar.

---

## PARTE 1: Conceptos y fórmulas de referencia

### Puertos y sockets

- Un **puerto** es un número de **16 bits** (0–65535) que identifica una aplicación dentro de un host.
- Un **socket** es el par `IP:puerto`. Una conexión en la red queda identificada por **dos sockets**: `IP_origen:puerto_origen ↔ IP_destino:puerto_destino`.
- **Multiplexación:** varias conversaciones simultáneas se distinguen por la tupla `(IP_orig, puerto_orig, IP_dest, puerto_dest, protocolo)`.

### Tipos de puertos

| Tipo | Rango | Uso |
|------|-------|-----|
| **Bien conocidos (well-known)** | 0 – 1023 | Servicios estándar (HTTP, HTTPS, SSH, SMTP, DNS, etc.) |
| **Registrados (registered)** | 1024 – 49151 | Aplicaciones de usuario (MySQL 3306, RDP 3389, HTTP-alt 8080, etc.) |
| **Dinámicos/efímeros** | 49152 – 65535 | Asignados temporalmente por el SO a las aplicaciones cliente |

### Puertos bien conocidos (repaso rápido)

| Puerto | Servicio | Puerto | Servicio |
|-------:|----------|-------:|----------|
| 20/21 tcp | FTP datos / control | 80 tcp | HTTP |
| 22 tcp | SSH / SCP / SFTP | 110 tcp | POP3 |
| 23 tcp | Telnet | 143 tcp | IMAP4 |
| 25 tcp | SMTP | 443 tcp | HTTPS |
| 53 tcp/udp | DNS | 993 tcp | IMAP4 sobre SSL |
| 67/68 udp | DHCP | 995 tcp | POP3 sobre SSL |
| 69 udp | TFTP | 3306 tcp | MySQL |

### Protocolo UDP

- **No orientado a conexión, no fiable.** Cabecera de solo **8 bytes** (4 campos de 2 bytes):
    - Puerto origen, Puerto destino, Longitud, Checksum.
- Ventaja: **baja latencia** y poca sobrecarga.
- Usos típicos: DNS, DHCP, TFTP, VoIP, streaming en directo, juegos online, telemetría IoT.

### Protocolo TCP

- **Orientado a conexión, fiable, con control de flujo y congestión.**
- Cabecera típica de 20 bytes (sin opciones). Campos clave:
    - Puerto origen / Puerto destino.
    - **Número de secuencia (SEQ)** → número del primer byte de datos del segmento.
    - **Número de acuse de recibo (ACK)** → siguiente byte que se espera recibir.
    - **Flags:** SYN, ACK, FIN, RST, PSH, URG.
    - **Ventana** → tamaño libre del buffer del receptor (control de flujo).

#### Establecimiento (three-way handshake)

1. Cliente → Servidor: **SYN=1**, `SEQ=x` (ISN del cliente).
2. Servidor → Cliente: **SYN=1, ACK=1**, `SEQ=y`, `ACK=x+1`.
3. Cliente → Servidor: **ACK=1**, `SEQ=x+1`, `ACK=y+1`.

#### Cierre (4 pasos)

`FIN → ACK → FIN → ACK`, cada extremo cierra su sentido de envío.

### Números de secuencia y ACK (regla práctica)

- Si un segmento tiene `SEQ=S` y transporta `N` bytes → el siguiente segmento debe llevar `SEQ = S + N`.
- El receptor devuelve un **ACK cumulativo**: `ACK = siguiente byte esperado`. Si llegan los bytes 2000–2499, el ACK será **2500**.
- Si se pierde un segmento intermedio, el receptor sigue devolviendo el ACK del **último byte contiguo** que ha recibido (ACK duplicado). Solo el segmento perdido se retransmite.

### Control de flujo (ventana deslizante) y congestión

- El receptor anuncia en cada ACK su **ventana (rwnd)** → bytes que puede aceptar todavía.
- El emisor puede tener **como máximo `rwnd` bytes en vuelo** sin ACK.
- Si la aplicación receptora lee lento → buffer lleno → `rwnd` decrece → emisor frena.
- **Control de congestión:** el emisor usa una segunda ventana `cwnd` que crece tras ACKs válidos y se reduce cuando detecta pérdidas (timeouts o ACK duplicados).

### Segmentación

- **MSS (Maximum Segment Size)** = tamaño máximo de datos por segmento TCP.
- Regla: `MSS = MTU − cabecera IP (20 B) − cabecera TCP (20 B)` → con MTU 1500 → MSS 1460.
- Nº de segmentos para enviar `B` bytes = `⌈ B / MSS ⌉`.
- Último segmento = `B − (n−1) × MSS` bytes (puede ser menor que MSS).

### Resumen PARTE 1

| Tema | Fórmulas / pasos clave |
|------|------------------------|
| **Puertos** | 0–1023 bien conocidos; 1024–49151 registrados; 49152–65535 efímeros. Socket = `IP:puerto`. |
| **UDP** | Cabecera 8 B (4 campos × 2 B). Sin conexión, sin fiabilidad, baja latencia. |
| **TCP handshake** | SYN → SYN+ACK → ACK. Cierre: FIN → ACK → FIN → ACK. |
| **Secuencia** | `SEQ_siguiente = SEQ_actual + bytes_segmento`. ACK cumulativo = siguiente byte esperado. |
| **Ventana** | Máx. bytes en vuelo = `min(rwnd, cwnd)`. |
| **Segmentación** | `MSS = MTU − 40`. Nº segmentos = `⌈ B / MSS ⌉`. |

---

## PARTE 2: Actividades de práctica (tipo examen)

<!-- Todas las actividades son prácticas. Resuélvelas en papel como en el examen. Cuando termines, puedes comprobar tus respuestas en las [soluciones de la ficha de repaso](../Extra/ficha_repaso_tema_8_transporte_soluciones.md).

--- -->

### Puertos, sockets y multiplexación

**Actividad 1 – Clasificación de puertos**  
Dada la siguiente lista de números de puerto, clasifica cada uno como **bien conocido**, **registrado** o **efímero (dinámico)**. Para los que correspondan a servicios estándar, indica también el servicio asociado.

`22`, `80`, `443`, `25`, `53`, `3306`, `8080`, `1234`, `49200`, `60000`

---

**Actividad 2 – Sockets en una sesión HTTPS**  
Un navegador en el PC `192.168.1.50` abre **tres pestañas** simultáneas al servidor web `203.0.113.10` por HTTPS. El sistema operativo asigna los puertos efímeros **49152**, **49165** y **49178** a cada pestaña.

1. Escribe el **socket cliente** (IP:puerto) de cada pestaña.
2. Escribe el **socket servidor** con el que hablan las tres.
3. Explica por qué el servidor puede distinguir las tres conexiones aunque compartan IP origen e IP/puerto destino. ¿Qué tupla identifica cada conexión?

---

**Actividad 3 – Multiplexación en un equipo**  
Un PC con IP `192.168.1.20` tiene abiertas al mismo tiempo estas sesiones:

- Una sesión **SSH** al servidor A (`172.16.0.5`, puerto 22 TCP).
- **Dos pestañas** HTTPS al servidor B (`203.0.113.20`, puerto 443 TCP).
- Una llamada de **VoIP** (UDP) al servidor C (`203.0.113.99`, puerto 3478).

Construye una tabla con estas columnas: **Protocolo**, **Socket local (IP:puerto)**, **Socket remoto (IP:puerto)**. Asigna tú puertos efímeros válidos a las sesiones cliente. Razona por qué el PC no puede usar el mismo puerto efímero para las dos pestañas al mismo servidor y mismo puerto destino.

---

### TCP vs UDP aplicado a casos reales

**Actividad 4 – Elección de protocolo de transporte**  
Para cada escenario indica qué protocolo usarías (**TCP** o **UDP**) y justifica brevemente tu elección basándote en fiabilidad, latencia, orden y necesidad de conexión:

1. Descarga de una imagen ISO de **4 GB** desde un servidor FTP.
2. Videollamada en directo con un compañero.
3. Consulta **DNS** del nombre `www.ejemplo.com` contra `8.8.8.8`.
4. Envío de un correo SMTP de 5 KB a un servidor.
5. Juego online multijugador tipo *shooter* en primera persona.
6. Transmisión de **telemetría IoT**: un sensor envía un dato de temperatura cada segundo.
7. Transferencia bancaria mediante HTTPS.
8. Arranque de un equipo que descarga su configuración por **TFTP**.

---

### Establecimiento de conexión TCP

**Actividad 5 – Three-way handshake**  
El cliente `192.168.1.100:49152` quiere abrir una conexión TCP con el servidor `10.0.0.5:443`. El ISN del cliente es **1000** y el ISN del servidor es **5000**. Completa la tabla del intercambio:

| Paso | Origen → Destino | Flags activos | SEQ | ACK |
|:----:|------------------|---------------|----:|----:|
| 1 | Cliente → Servidor | ? | ? | ? |
| 2 | Servidor → Cliente | ? | ? | ? |
| 3 | Cliente → Servidor | ? | ? | ? |

1. Rellena los valores de **Flags**, **SEQ** y **ACK** de los tres segmentos.
2. Explica con tus palabras qué representa el campo **SEQ** y qué representa el campo **ACK**.
3. Después del paso 3, ¿qué **SEQ** llevaría el primer segmento con datos que envíe el cliente?

---

### Segmentación y números de secuencia

**Actividad 6 – Números de secuencia TCP**  
Un emisor TCP envía tres segmentos consecutivos con estos datos:

- Segmento 1: `SEQ = 2000`, **500 bytes** de datos.
- Segmento 2: `SEQ = ?`,   **300 bytes** de datos.
- Segmento 3: `SEQ = ?`,   **200 bytes** de datos.

1. Calcula el **SEQ** de los segmentos 2 y 3.
2. Si el receptor recibe correctamente los tres, ¿qué **ACK cumulativo** devuelve?
3. Si el segmento **2** se pierde y llegan el 1 y el 3, ¿qué ACK devolverá el receptor cada vez que reciba un segmento?
4. ¿Qué se retransmite en TCP: todo el flujo o solo el segmento perdido? Razónalo.

---

**Actividad 7 – Segmentación de un fichero**  
Una aplicación debe enviar un archivo de **24 000 bytes** mediante TCP. La MTU del enlace es **1 500 bytes**. Las cabeceras IP y TCP ocupan **20 bytes** cada una.

1. Calcula el **MSS**.
2. ¿Cuántos **segmentos TCP** se enviarán en total?
3. ¿Cuántos bytes de datos transporta el **último segmento**?
4. Si se pierde el **segmento número 5**, ¿hay que reenviar todo el archivo? Razona la respuesta desde el punto de vista de la fiabilidad TCP.

---

### Control de flujo y congestión

**Actividad 8 – Ventana deslizante**  
Un servidor anuncia al cliente una ventana de recepción `rwnd = 8 KB`. El cliente envía segmentos con **1 KB** de datos cada uno.

1. ¿Cuántos segmentos como máximo puede enviar el cliente **sin recibir ningún ACK**?
2. El receptor confirma `ACK` hasta el tercer segmento y anuncia ahora `rwnd = 4 KB`. ¿Cuántos segmentos nuevos podrá enviar el emisor antes de tener que esperar a más ACKs?
3. Si la aplicación del receptor **está bloqueada** y deja de leer el buffer, ¿qué le pasa al `rwnd` anunciado en los siguientes ACK? ¿Cómo afecta esto al emisor?
4. Diferencia en una frase **control de flujo** (`rwnd`) y **control de congestión** (`cwnd`).

---

**Actividad 9 – Pérdidas y reacción del emisor**  
Un flujo TCP está enviando datos con `cwnd = 16 KB` y `MSS = 1 KB`. El receptor empieza a devolver **ACK duplicados** con el mismo número (ACK repetido tres veces).

1. ¿Qué está indicando el receptor con ese comportamiento?
2. ¿Qué acción toma el emisor al recibir **tres ACK duplicados**? (Nombra el mecanismo.)
3. Si más tarde se produjera un **timeout** sin recibir ACK, ¿cómo reaccionaría `cwnd`? Compara con el caso anterior.

---

### Interpretación de escenarios y comandos

**Actividad 10 – Interpretación de `netstat`**  
En un equipo se ejecuta `netstat -an` y se obtiene esta salida simplificada:

```
Proto  Local Address          Foreign Address        State
TCP    192.168.1.10:49800     142.250.190.14:443     ESTABLISHED
TCP    192.168.1.10:49821     52.84.229.23:443       ESTABLISHED
TCP    192.168.1.10:22        0.0.0.0:0              LISTENING
TCP    192.168.1.10:49850     10.0.0.7:3306          ESTABLISHED
UDP    192.168.1.10:5353      *:*                    -
```

1. Indica, línea por línea, si se trata de una **conexión saliente**, una **entrante** o un **servicio** ofrecido por el equipo.
2. ¿Qué servicio está publicando el equipo en el puerto 22 y qué puertos se están usando como **efímeros**?
3. ¿A qué tipo de aplicación corresponde la línea UDP 5353 (pista: descubrimiento de servicios en red local)?
4. A partir de los puertos destino, deduce qué protocolo de aplicación se está usando en cada conexión TCP establecida.

---

### Cortafuegos y políticas de puertos

**Actividad 11 – Reglas de cortafuegos (política restrictiva)**  
Una empresa separa su LAN `192.168.0.0/24` de Internet mediante un cortafuegos con **política restrictiva** (por defecto, **denegar**). Requisitos:

- Permitir **navegación web** saliente (HTTP y HTTPS) para toda la LAN.
- Permitir consultas **DNS** salientes únicamente al servidor `8.8.8.8`.
- Permitir acceso **SSH entrante** desde cualquier IP **solo** hacia el servidor interno `192.168.0.10`.
- Denegar **todo lo demás**.

1. Escribe la tabla de reglas con columnas: **Orden**, **Dirección** (entrante/saliente), **Origen**, **Destino**, **Protocolo/puerto**, **Acción**.
2. Explica por qué conviene terminar con una regla explícita de `deny any any`, aunque la política por defecto ya sea restrictiva.
3. Si un usuario necesita usar FTP (puertos 20/21) con la política actual, ¿funcionará? Razona.

---

**Actividad 12 – Apertura de puertos y NAT (introducción al tema 9)**  
En casa tienes un router con PAT y una LAN `192.168.1.0/24`. Quieres publicar un servidor web propio en el PC `192.168.1.50:80` para que sea accesible desde Internet.

1. ¿Qué problema hay si no configuras nada en el router? ¿Por qué PAT **no** entrega por sí solo las conexiones entrantes al servidor interno?
2. ¿Qué tipo de regla de **redirección de puertos** (port forwarding / NAT estático) deberías configurar? Escribe la regla en forma de tabla: **IP pública:puerto → IP interna:puerto** y **protocolo**.
3. Indica desde el lado cliente **qué socket destino** tendrá que poner un navegador en Internet para acceder a tu servidor, suponiendo que la IP pública del router es `203.0.113.40`.

---

## Checklist antes del examen

- [ ] Clasificar un puerto como bien conocido, registrado o efímero e identificar los servicios estándar más habituales
- [ ] Construir sockets `IP:puerto` y entender qué tupla identifica una conexión en la red
- [ ] Explicar la **multiplexación** (varias conexiones simultáneas en el mismo host)
- [ ] Distinguir **UDP vs TCP** y justificar cuál usar en cada caso real (streaming, DNS, FTP, VoIP, etc.)
- [ ] Describir el **three-way handshake** con flags y números de secuencia
- [ ] Calcular el siguiente `SEQ` y el `ACK cumulativo` a partir de los bytes enviados
- [ ] Calcular el **MSS** y el número de segmentos a partir del tamaño del archivo y la MTU
- [ ] Interpretar la **ventana deslizante** (`rwnd`) y diferenciarla del control de congestión (`cwnd`)
- [ ] Entender la reacción de TCP ante pérdidas: ACK duplicados, fast retransmit, timeout
- [ ] Interpretar la salida de **`netstat`** y reconocer servicios en escucha vs conexiones establecidas
- [ ] Redactar reglas de **cortafuegos** con política restrictiva (permitir/denegar por puertos)

---
<!-- 
*Documento de apoyo para preparar el examen. Consulta el tema 8 (Capa de Transporte) para más detalle. [Soluciones de las actividades](../Extra/ficha_repaso_tema_8_transporte_soluciones.md).* -->
