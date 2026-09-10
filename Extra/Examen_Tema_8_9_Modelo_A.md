# EXAMEN MODELO A – Unidades 8 y 9: Capa de Transporte, NAT e IPv6

**Módulo:** Redes de Área Local (RAL)  
**Temas:** Capa de Transporte (Tema 8) · NAT e IPv6 (Tema 9)  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

---

**Nombre y apellidos:** _________________________________________________

**Fecha:** _______________________

---

## Tema 8 – Capa de Transporte (5 actividades)

### Actividad 1 – Sockets y multiplexación *(1,00 pts)*
Un equipo con IP `10.20.30.40` mantiene simultáneamente las siguientes conexiones de red:

- **Pestaña 1:** HTTPS al servidor `198.51.100.10:443` con puerto local **51200**.
- **Pestaña 2:** HTTPS al **mismo** servidor `198.51.100.10:443` con puerto local **51201**.
- **SSH** al servidor `192.168.5.7:22` con puerto local **51230**.
- **Stream UDP** al servidor `203.0.113.45:5004` con puerto local **51240**.

1. *(0,25)* Clasifica los **4 puertos locales** y los **4 puertos destino** como bien conocido, registrado o efímero.
2. *(0,25)* Construye una tabla con: **Protocolo**, **Socket local (IP:puerto)**, **Socket remoto (IP:puerto)**.
3. *(0,25)* ¿Por qué el sistema operativo **no puede** asignar el mismo puerto efímero a las dos pestañas HTTPS al mismo servidor y mismo puerto destino?
4. *(0,25)* Indica la **tupla completa** que identifica de forma unívoca cada una de las 4 conexiones.

---

### Actividad 2 – TCP vs UDP en escenarios reales *(1,00 pts)*
Para cada escenario, indica si usarías **TCP** o **UDP** y justifica brevemente tu elección (fiabilidad, latencia, orden, conexión):

1. *(0,20)* Descarga de un archivo `.zip` de **800 MB** desde un servidor HTTP.
2. *(0,20)* Resolución **DNS** del nombre `cursos.example.com` contra `8.8.8.8`.
3. *(0,20)* **Videollamada** en directo con un compañero.
4. *(0,20)* Sincronización de hora con un servidor **NTP** (paquetes muy pequeños y sin estado).
5. *(0,20)* Envío de un correo **SMTP** de 12 KB con adjunto.

---

### Actividad 3 – Three-way handshake y números de secuencia *(1,00 pts)*
El cliente `192.168.10.50:50000` quiere abrir una conexión TCP con el servidor `203.0.113.20:443`. El **ISN del cliente** es `8000` y el **ISN del servidor** es `22000`.

1. *(0,50)* Completa la siguiente tabla del intercambio:

   | Paso | Origen → Destino   | Flags activos | SEQ | ACK |
   |:----:|--------------------|---------------|----:|----:|
   | 1    | Cliente → Servidor | ?             | ?   | ?   |
   | 2    | Servidor → Cliente | ?             | ?   | ?   |
   | 3    | Cliente → Servidor | ?             | ?   | ?   |

2. *(0,25)* Tras el handshake, el cliente envía un primer segmento con **240 bytes** de datos. Indica el `SEQ` y el `ACK` que lleva ese segmento.
3. *(0,25)* ¿Qué `ACK cumulativo` devolverá el servidor al recibir esos 240 bytes correctamente?

---

### Actividad 4 – Segmentación TCP de un fichero *(1,00 pts)*
Una aplicación necesita transmitir un fichero de **18 500 bytes** mediante TCP. La MTU del enlace es **1 500 bytes** y las cabeceras IP y TCP ocupan **20 bytes** cada una.

1. *(0,25)* Calcula el **MSS**.
2. *(0,25)* Calcula el **número total de segmentos TCP** necesarios para enviar el fichero.
3. *(0,25)* Calcula los **bytes de datos del último segmento**.
4. *(0,25)* Si se pierde el **segmento número 7**, ¿qué se retransmite y por qué? Cita el mecanismo de TCP que detecta la pérdida sin esperar al timeout.

---

### Actividad 5 – Control de flujo y congestión *(1,00 pts)*
Un emisor TCP usa **MSS = 1 KB**. El receptor anuncia `rwnd = 10 KB` y el emisor tiene actualmente `cwnd = 6 KB`.

1. *(0,25)* ¿Cuántos **bytes en vuelo** como máximo puede tener el emisor en este instante? Razona la fórmula.
2. *(0,25)* Si se produce un **timeout** sin recibir ACK, ¿qué nuevos valores toman `ssthresh` y `cwnd`? Explica brevemente la fase a la que vuelve.
3. *(0,25)* Si en lugar de timeout el emisor recibe **3 ACK duplicados**, ¿qué mecanismo aplica y qué valores toman `ssthresh` y `cwnd`?
4. *(0,25)* Resume en una frase la **diferencia** entre control de flujo (`rwnd`) y control de congestión (`cwnd`).

---

## Tema 9 – NAT e IPv6 (5 actividades)

### Actividad 6 – PAT con tabla de traducción *(1,00 pts)*
Tres equipos de la LAN `192.168.50.0/24` salen a Internet por un router con **PAT** que dispone de la **única IP pública** `198.51.100.7`:

- **PC1** `192.168.50.10` abre HTTPS al servidor `203.0.113.10:443` con puerto origen **52000**.
- **PC2** `192.168.50.11` abre HTTPS al **mismo** servidor `203.0.113.10:443` con puerto origen **52000** (coincide con PC1).
- **PC3** `192.168.50.12` abre HTTP al servidor `203.0.113.10:80` con puerto origen **52001**.

1. *(0,50)* Completa la **tabla PAT** del router. Si hay colisión real, asigna el primer puerto libre **52050**.

   | PC  | Socket interno          | Socket público (traducido) | Socket remoto       | Protocolo |
   |-----|-------------------------|----------------------------|---------------------|-----------|
   | PC1 | 192.168.50.10:52000     | 198.51.100.7:?             | 203.0.113.10:443    | TCP       |
   | PC2 | 192.168.50.11:52000     | 198.51.100.7:?             | 203.0.113.10:443    | TCP       |
   | PC3 | 192.168.50.12:52001     | 198.51.100.7:?             | 203.0.113.10:80     | TCP       |

2. *(0,25)* Cuando el servidor responde al **PC2**, ¿con qué **socket destino** llega el paquete al router? ¿Cómo decide el router que debe entregárselo a PC2 y no a PC1?
3. *(0,25)* Justifica por qué con PAT **no basta** con traducir solo la IP origen.

---

### Actividad 7 – NAT estático para publicar un servidor *(1,00 pts)*
Un instituto quiere publicar su servidor web interno (`172.16.20.80`, puerto **80**) en la IP pública `198.51.100.99` usando **NAT estático 1:1**. Un cliente de Internet (`203.0.113.55`) accede desde el puerto efímero **60000**.

1. *(0,50)* Completa la tabla del paquete **cliente → servidor** en los dos puntos:

   | Punto de observación        | IP origen      | Puerto orig | IP destino | Puerto dest |
   |-----------------------------|----------------|-------------|------------|-------------|
   | Fuera del router (Internet) | 203.0.113.55   | 60000       | ?          | 80          |
   | Dentro del router (LAN)     | 203.0.113.55   | 60000       | ?          | 80          |

2. *(0,25)* Completa la tabla del paquete de **respuesta servidor → cliente**:

   | Punto de observación        | IP origen | Puerto orig | IP destino     | Puerto dest |
   |-----------------------------|-----------|-------------|----------------|-------------|
   | Dentro del router (LAN)     | ?         | 80          | 203.0.113.55   | 60000       |
   | Fuera del router (Internet) | ?         | 80          | 203.0.113.55   | 60000       |

3. *(0,25)* Indica qué **columna** modifica el router en cada sentido (origen o destino, IP o puerto) y justifica por qué este NAT no necesita reescribir puertos.

---

### Actividad 8 – Abreviación de direcciones IPv6 *(1,00 pts)*
Escribe la **forma abreviada** más corta válida de cada dirección (aplica ceros a la izquierda y un único `::`):

a) *(0,15)* `2001:0db8:0000:0000:0000:0000:0000:0050`  
b) *(0,15)* `fe80:0000:0000:0000:0a1b:2c3d:4e5f:6789`  
c) *(0,15)* `2001:0abc:0000:0000:0001:0000:0000:0010`  
d) *(0,15)* `0000:0000:0000:0000:0000:0000:0000:0001`  
e) *(0,15)* `fd00:1234:5678:0000:0000:0000:0000:000a`

f) *(0,25)* Indica si las siguientes son **válidas o inválidas** y por qué:

- `2001::db8::1`
- `2001:db8:zzzz::1`

---

### Actividad 9 – Expansión de direcciones IPv6 *(1,00 pts)*

1. *(0,40)* Escribe la **forma completa** (8 grupos de 4 dígitos hex, 32 dígitos en total) de cada dirección abreviada:

   - a) `::1`
   - b) `2001:db8::1`
   - c) `fe80::a:b:c:d`
   - d) `ff02::2`
   - e) `2001:db8:abcd::1234`

2. *(0,30)* Para la dirección abreviada `fe80::1:0:0:5`:

   - a) Expándela a forma completa (8 grupos de 4 hex).
   - b) Indica **cuántos grupos** de ceros representa el `::` en este caso.
   - c) Reescríbela en su **forma canónica** (es decir, aplicando `::` a la racha de ceros más larga).

3. *(0,30)* Indica si las siguientes representaciones IPv6 son **válidas** y, en caso negativo, **por qué** (justifica brevemente):

   - a) `2001:db8:1:2:3:4:5`
   - b) `2001:db8::1::5`
   - c) `2001:db8:0:0:0:0:0:1`

---

### Actividad 10 – Identificación de tipos de dirección IPv6 *(1,00 pts)*

1. *(0,25)* Asocia cada **tipo de dirección IPv6** con su **prefijo o dirección de referencia**. Escribe la respuesta en forma de tabla:

   - Loopback
   - Indefinida
   - Link-local
   - Multicast
   - Global unicast

2. *(0,50)* Indica el **tipo** (loopback, indefinida, link-local, ULA, global unicast o multicast) al que pertenece cada una de las siguientes direcciones:

   - a) `::1`
   - b) `::`
   - c) `fe80::1`
   - d) `fe80::abcd:1`
   - e) `fc00::5`
   - f) `fd12:3456::a`
   - g) `2001:db8::1`
   - h) `2400:cb00::1`
   - i) `ff02::1`
   - j) `ff02::2`

3. *(0,25)* Para las tres direcciones siguientes, indica su **tipo** y describe brevemente un **uso típico** (en qué situación aparece o para qué se utiliza):

   - a) `fe80::1`
   - b) `2001:db8:cafe::1`
   - c) `ff02::1`

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

| Bloque              | Actividades  | Puntos (sobre 10) |
|---------------------|--------------|-------------------|
| Capa de Transporte  | 1, 2, 3, 4, 5 | 5,00              |
| NAT e IPv6          | 6, 7, 8, 9, 10 | 5,00            |
| **Total**           | 10            | **10 puntos**    |

**Dificultad por tipo de pregunta**

| Nivel   | Criterio                                                                                       |
|---------|------------------------------------------------------------------------------------------------|
| **Baja**  | Aplicación directa: clasificar puertos, abreviar IPv6, fórmulas inmediatas (MSS, hosts).      |
| **Media** | Aplicación en contexto: tablas NAT/PAT, cálculo de SEQ/ACK, segmentación, prefijos.           |
| **Alta**  | Razonamiento: justificar elección TCP/UDP, reacción ante pérdidas, decisión interna del router. |
