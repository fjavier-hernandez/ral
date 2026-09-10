# EXAMEN MODELO B – Unidades 8 y 9: Capa de Transporte, NAT e IPv6

**Módulo:** Redes de Área Local (RAL)  
**Temas:** Capa de Transporte (Tema 8) · NAT e IPv6 (Tema 9)  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

---

**Nombre y apellidos:** _________________________________________________

**Fecha:** _______________________

---

## Tema 8 – Capa de Transporte (5 actividades)

### Actividad 1 – Sockets y multiplexación *(1,00 pts)*
El equipo `172.16.5.20` mantiene simultáneamente las siguientes conexiones:

- **MySQL** (TCP) al servidor `10.0.0.50:3306` con puerto local **49500**.
- **Telnet** (TCP) a `10.0.0.51:23` con puerto local **49510**.
- **HTTP** (TCP) a `198.51.100.30:80` con puerto local **49520**.
- **DNS** (UDP) a `8.8.8.8:53` con puerto local **49530**.

1. *(0,25)* Clasifica los **4 puertos locales** y los **4 puertos destino** como bien conocido, registrado o efímero.
2. *(0,25)* Construye una tabla con: **Protocolo**, **Socket local (IP:puerto)**, **Socket remoto (IP:puerto)**.
3. *(0,25)* ¿Cuál de las cuatro **NO** es una sesión orientada a conexión? Justifica brevemente desde la capa de transporte.
4. *(0,25)* Indica la **tupla completa** que identifica unívocamente cada una de las 4 conexiones en la red.

---

### Actividad 2 – TCP vs UDP en escenarios reales *(1,00 pts)*
Para cada escenario, indica si usarías **TCP** o **UDP** y justifica brevemente tu elección (fiabilidad, latencia, orden, conexión):

1. *(0,20)* Streaming de **TV en directo** (IPTV).
2. *(0,20)* Inicio de sesión **SSH** en un servidor remoto.
3. *(0,20)* **Telemetría IoT**: un sensor envía un dato de humedad cada 5 segundos.
4. *(0,20)* Petición y descarga de una página web por **HTTPS**.
5. *(0,20)* Solicitud **DHCP** de un equipo al arrancar.

---

### Actividad 3 – Three-way handshake y números de secuencia *(1,00 pts)*
El cliente `10.10.10.5:60100` quiere abrir una conexión TCP con el servidor `192.168.100.20:80`. El **ISN del cliente** es `4000` y el **ISN del servidor** es `9000`.

1. *(0,50)* Completa la siguiente tabla del intercambio:

   | Paso | Origen → Destino   | Flags activos | SEQ | ACK |
   |:----:|--------------------|---------------|----:|----:|
   | 1    | Cliente → Servidor | ?             | ?   | ?   |
   | 2    | Servidor → Cliente | ?             | ?   | ?   |
   | 3    | Cliente → Servidor | ?             | ?   | ?   |

2. *(0,25)* Tras el handshake, el cliente envía un primer segmento con **1 000 bytes** de datos. Indica el `SEQ` y el `ACK` que lleva ese segmento.
3. *(0,25)* ¿Qué `ACK cumulativo` devolverá el servidor al recibir esos 1 000 bytes correctamente?

---

### Actividad 4 – Segmentación TCP de un fichero *(1,00 pts)*
Una aplicación necesita transmitir un fichero de **9 200 bytes** mediante TCP. La MTU del enlace es **1 500 bytes** y las cabeceras IP y TCP ocupan **20 bytes** cada una.

1. *(0,25)* Calcula el **MSS**.
2. *(0,25)* Calcula el **número total de segmentos TCP** necesarios.
3. *(0,25)* Calcula los **bytes de datos del último segmento**.
4. *(0,25)* Si se pierden los **segmentos 3 y 4**, ¿hay que reenviar todo el fichero? Razona la respuesta desde la fiabilidad TCP.

---

### Actividad 5 – Control de flujo y congestión *(1,00 pts)*
Un emisor TCP usa **MSS = 1 KB**. Tiene `cwnd = 12 KB` y el receptor anuncia `rwnd = 8 KB`.

1. *(0,25)* ¿Cuántos **bytes en vuelo** permite la situación actual? Razona la fórmula.
2. *(0,25)* Si la aplicación receptora procesa muy lento y el `rwnd` baja hasta **0**, ¿qué hace el emisor en esa situación? ¿Cómo sale del bloqueo?
3. *(0,25)* Tras un **timeout** sin recibir ACK, indica los nuevos valores de `ssthresh` y `cwnd`. Justifica brevemente la fase a la que vuelve el emisor.
4. *(0,25)* Resume en una frase la **diferencia** entre `rwnd` y `cwnd`.

---

## Tema 9 – NAT e IPv6 (5 actividades)

### Actividad 6 – PAT con tabla de traducción *(1,00 pts)*
Tres equipos de la LAN `10.10.20.0/24` salen a Internet por un router con **PAT** (única IP pública `203.0.113.200`):

- **PC-A** `10.10.20.5` abre HTTP al servidor `198.51.100.40:80` con puerto origen **49152**.
- **PC-B** `10.10.20.6` abre HTTPS al servidor `198.51.100.40:443` con puerto origen **49152** (coincide con PC-A).
- **PC-C** `10.10.20.7` abre HTTP al **mismo** servidor `198.51.100.40:80` con puerto origen **49152** (coincide con PC-A en mismo destino).

1. *(0,50)* Completa la **tabla PAT** del router. Si hay colisión real entre dos sockets públicos, asigna el primer puerto libre **49200**.

   | PC   | Socket interno         | Socket público (traducido) | Socket remoto         | Protocolo |
   |------|------------------------|----------------------------|------------------------|-----------|
   | PC-A | 10.10.20.5:49152       | 203.0.113.200:?            | 198.51.100.40:80       | TCP       |
   | PC-B | 10.10.20.6:49152       | 203.0.113.200:?            | 198.51.100.40:443      | TCP       |
   | PC-C | 10.10.20.7:49152       | 203.0.113.200:?            | 198.51.100.40:80       | TCP       |

2. *(0,25)* ¿Existe colisión real entre PC-A y PC-B? Justifica usando la tupla `(IP_pub, puerto_pub, IP_dest, puerto_dest, protocolo)`.
3. *(0,25)* Cuando el servidor responde al **PC-C**, ¿cómo decide el router que el paquete se debe entregar a PC-C y no a PC-A?

---

### Actividad 7 – NAT estático para publicar un servidor *(1,00 pts)*
Una empresa publica su servidor de correo interno (`192.168.100.25`, puerto **25 SMTP**) en la IP pública `203.0.113.80` mediante **NAT estático 1:1**. Un cliente de Internet (`198.51.100.5`) le envía un correo desde el puerto efímero **55000**.

1. *(0,50)* Completa la tabla del paquete **cliente → servidor** en los dos puntos:

   | Punto de observación        | IP origen     | Puerto orig | IP destino | Puerto dest |
   |-----------------------------|---------------|-------------|------------|-------------|
   | Fuera del router (Internet) | 198.51.100.5  | 55000       | ?          | 25          |
   | Dentro del router (LAN)     | 198.51.100.5  | 55000       | ?          | 25          |

2. *(0,25)* Completa la tabla del paquete de **respuesta servidor → cliente**:

   | Punto de observación        | IP origen | Puerto orig | IP destino    | Puerto dest |
   |-----------------------------|-----------|-------------|---------------|-------------|
   | Dentro del router (LAN)     | ?         | 25          | 198.51.100.5  | 55000       |
   | Fuera del router (Internet) | ?         | 25          | 198.51.100.5  | 55000       |

3. *(0,25)* Indica qué **columna** modifica el router en cada sentido (origen o destino, IP o puerto) y razona por qué con NAT estático 1:1 no es necesario reescribir puertos.

---

### Actividad 8 – Abreviación de direcciones IPv6 *(1,00 pts)*
Escribe la **forma abreviada** más corta válida de cada dirección (aplica ceros a la izquierda y un único `::`):

a) *(0,15)* `2001:0db8:00ab:0000:0000:0000:0000:00c1`  
b) *(0,15)* `0000:0000:0000:0000:0000:0000:0000:0000`  
c) *(0,15)* `fe80:0000:0000:0000:0000:0000:0000:000a`  
d) *(0,15)* `2001:0db8:1234:5678:0000:0000:0000:0001`  
e) *(0,15)* `fd00:1234:0000:0000:0001:0000:0000:0002`

f) *(0,25)* Indica si las siguientes son **válidas o inválidas** y por qué (puede haber **más de una razón**):

- `2001:db8:1::g::1`
- `fe80::1:0:0:0:1`

---

### Actividad 9 – Expansión de direcciones IPv6 *(1,00 pts)*

1. *(0,40)* Escribe la **forma completa** (8 grupos de 4 dígitos hex, 32 dígitos en total) de cada dirección abreviada:

   - a) `::`
   - b) `fe80::1`
   - c) `2001:db8::abcd:1`
   - d) `ff02::1`
   - e) `2001:db8:cafe::5`

2. *(0,30)* Para la dirección `2001:db8:0:0:0:0:0:5`:

   - a) Expándela a forma completa (8 grupos de 4 hex, 32 dígitos en total).
   - b) Indica **cuántos grupos consecutivos de ceros** contiene.
   - c) Reescríbela en su **forma canónica** abreviada (es decir, aplicando `::` a la racha de ceros más larga).

3. *(0,30)* Indica si las siguientes representaciones IPv6 son **válidas** y, en caso negativo, **por qué** (justifica brevemente):

   - a) `fe80:::1`
   - b) `2001:0db8:1:2:3:4:5:6:7`
   - c) `fd00:0:0:0:0:0:0:1`

---

### Actividad 10 – Identificación de tipos de dirección IPv6 *(1,00 pts)*

1. *(0,25)* Asocia cada **tipo de dirección IPv6** con su **prefijo o dirección de referencia**. Escribe la respuesta en forma de tabla:

   - Loopback
   - Indefinida
   - Link-local
   - ULA (privada)
   - Global unicast

2. *(0,50)* Indica el **tipo** (loopback, indefinida, link-local, ULA, global unicast o multicast) al que pertenece cada una de las siguientes direcciones:

   - a) `::`
   - b) `::1`
   - c) `fe80::abcd`
   - d) `fe80::1234:5678`
   - e) `fc00:1234::1`
   - f) `fd2a::abcd`
   - g) `2001:db8:1::a`
   - h) `2606:4700:10::1`
   - i) `ff02::1`
   - j) `ff02::2`

3. *(0,25)* Para las tres direcciones siguientes, indica su **tipo** y describe brevemente un **uso típico** (en qué situación aparece o para qué se utiliza):

   - a) `::1`
   - b) `fdab:1234::1`
   - c) `ff02::2`

---

## Resumen de puntuación (sobre 10)

| Actividad | Tema | Enunciado breve                          | Puntos |
|-----------|------|------------------------------------------|--------|
| 1         | 8    | Sockets y multiplexación                 | 1,00   |
| 2         | 8    | TCP vs UDP en escenarios                 | 1,00   |
| 3         | 8    | Three-way handshake (SEQ/ACK)            | 1,00   |
| 4         | 8    | Segmentación TCP                         | 1,00   |
| 5         | 8    | Control de flujo y congestión            | 1,00   |
| 6         | 9    | PAT con tabla de traducción              | 1,00   |
| 7         | 9    | NAT estático para servidor               | 1,00   |
| 8         | 9    | Abreviación de direcciones IPv6          | 1,00   |
| 9         | 9    | Expansión de direcciones IPv6            | 1,00   |
| 10        | 9    | Tipos de dirección IPv6                  | 1,00   |
|           |      | **Total**                                | **10** |

---

## CRITERIOS DE CALIFICACIÓN

| Bloque              | Actividades   | Puntos (sobre 10) |
|---------------------|---------------|-------------------|
| Capa de Transporte  | 1, 2, 3, 4, 5 | 5,00              |
| NAT e IPv6          | 6, 7, 8, 9, 10 | 5,00             |
| **Total**           | 10            | **10 puntos**     |

**Dificultad por tipo de pregunta**

| Nivel   | Criterio                                                                                       |
|---------|------------------------------------------------------------------------------------------------|
| **Baja**  | Aplicación directa: clasificar puertos, abreviar IPv6, fórmulas inmediatas (MSS, hosts).      |
| **Media** | Aplicación en contexto: tablas NAT/PAT, cálculo de SEQ/ACK, segmentación, prefijos.           |
| **Alta**  | Razonamiento: justificar elección TCP/UDP, reacción ante pérdidas, decisión interna del router. |
