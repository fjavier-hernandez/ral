# Examen Tema 8 y 9 – Modelo B – Soluciones y Puntuaciones

---

## Modelo B – Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Tema_8_9_Modelo_B.md`  
> Los puntos indicados son **máximos**; se puede restar parcialmente según errores.

---

## Tema 8 – Capa de Transporte

### Actividad 1 – Sockets y multiplexación *(1,00 pts)*

- **1. Tipo de puerto (0,25 pts)**

| Puerto         | Tipo          | Servicio (si procede) |
|----------------|---------------|-----------------------|
| 49500 (local)  | Efímero       | —                     |
| 49510 (local)  | Efímero       | —                     |
| 49520 (local)  | Efímero       | —                     |
| 49530 (local)  | Efímero       | —                     |
| 3306 (destino) | Registrado    | MySQL                 |
| 23 (destino)   | Bien conocido | Telnet                |
| 80 (destino)   | Bien conocido | HTTP                  |
| 53 (destino)   | Bien conocido | DNS                   |

- **2. Tabla de sockets (0,25 pts)**

| Protocolo | Socket local         | Socket remoto         |
|-----------|----------------------|-----------------------|
| TCP       | 172.16.5.20:49500    | 10.0.0.50:3306        |
| TCP       | 172.16.5.20:49510    | 10.0.0.51:23          |
| TCP       | 172.16.5.20:49520    | 198.51.100.30:80      |
| UDP       | 172.16.5.20:49530    | 8.8.8.8:53            |

- **3. Sesión NO orientada a conexión (0,25 pts)**  
  - La consulta **DNS por UDP** (puerto 53). UDP **no realiza handshake** ni mantiene estado: simplemente envía el datagrama y espera la respuesta. Las otras tres (MySQL, Telnet, HTTP) usan **TCP**, que sí abre conexión con el three-way handshake.

- **4. Tupla de cada conexión (0,25 pts)**

  - `(TCP, 172.16.5.20, 49500, 10.0.0.50, 3306)`
  - `(TCP, 172.16.5.20, 49510, 10.0.0.51, 23)`
  - `(TCP, 172.16.5.20, 49520, 198.51.100.30, 80)`
  - `(UDP, 172.16.5.20, 49530, 8.8.8.8, 53)`

---

### Actividad 2 – TCP vs UDP en escenarios reales *(1,00 pts)*

| Nº | Escenario                       | Protocolo | Justificación breve                                                                  | Puntos |
|----|---------------------------------|-----------|--------------------------------------------------------------------------------------|--------|
| 1  | IPTV en directo                 | **UDP**   | Lo importante es la latencia; reenviar fotogramas viejos rompería el directo.        | 0,20 |
| 2  | Inicio de sesión SSH            | **TCP**   | Sesión interactiva fiable y en orden; SSH usa TCP por definición (puerto 22).        | 0,20 |
| 3  | Telemetría IoT cada 5 s         | **UDP**   | Paquetes pequeños y frecuentes; baja sobrecarga; si se pierde uno, el siguiente vale. | 0,20 |
| 4  | Página web por HTTPS            | **TCP**   | Página completa requiere fiabilidad y orden; HTTPS funciona sobre TCP.               | 0,20 |
| 5  | DHCP al arrancar                | **UDP**   | El cliente todavía no tiene IP; se hace en broadcast/UDP, sin conexión previa.       | 0,20 |

---

### Actividad 3 – Three-way handshake *(1,00 pts)*

- **1. Tabla del intercambio (0,50 pts)**

| Paso | Origen → Destino   | Flags     | SEQ  | ACK  |
|:----:|--------------------|-----------|-----:|-----:|
| 1    | Cliente → Servidor | SYN       | 4000 | —    |
| 2    | Servidor → Cliente | SYN + ACK | 9000 | 4001 |
| 3    | Cliente → Servidor | ACK       | 4001 | 9001 |

- **2. Primer segmento con datos (1 000 bytes) (0,25 pts)**  
  - El primer byte de datos del cliente es el `4001`:  
    - `SEQ = 4001`  
    - `ACK = 9001` (sigue confirmando el siguiente byte esperado del servidor).

- **3. ACK del servidor (0,25 pts)**  
  - Llegan los bytes `4001 → 5000` (1 000 bytes). Siguiente byte esperado:  
  - `ACK = 4001 + 1 000 = 5001`.

---

### Actividad 4 – Segmentación TCP *(1,00 pts)*

- **1. MSS (0,25 pts)**  
  - `MSS = 1500 − 20 − 20 = 1460 B`.

- **2. Número de segmentos (0,25 pts)**  
  - `⌈9 200 / 1460⌉ = ⌈6,30⌉ = 7` segmentos.

- **3. Bytes del último segmento (0,25 pts)**  
  - 6 segmentos llenos: `6 × 1460 = 8 760 B`.  
  - Último: `9 200 − 8 760 = 440 B`.

- **4. Pérdida de los segmentos 3 y 4 (0,25 pts)**  
  - **No** se reenvía el fichero entero. TCP es fiable **byte a byte**: el receptor guarda en su buffer los segmentos `1, 2, 5, 6, 7` que han llegado (los posteriores quedan **fuera de orden**) y devuelve **ACK duplicados** pidiendo el primer byte del segmento 3. El emisor retransmite **solo los segmentos 3 y 4**; los demás no se vuelven a enviar.

---

### Actividad 5 – Control de flujo y congestión *(1,00 pts)*

- **1. Bytes en vuelo (0,25 pts)**  
  - `bytes_en_vuelo ≤ min(rwnd, cwnd) = min(8 KB, 12 KB) = 8 KB`.  
  - El cuello de botella ahora es el **receptor** (`rwnd`).

- **2. Situación de `rwnd = 0` (0,25 pts)**  
  - El emisor entra en **zero window**: **se detiene** de enviar datos. Para no quedarse bloqueado para siempre, envía **sondeos periódicos** (*zero window probes*: pequeños paquetes con 1 byte) para forzar al receptor a responder. Cuando el receptor anuncia `rwnd > 0` en un nuevo ACK, el emisor reanuda.

- **3. Reacción ante timeout (0,25 pts)**  
  - Se asume **congestión severa**:  
    - `ssthresh = cwnd / 2 = 12 / 2 = 6 KB`.  
    - `cwnd = 1 MSS = 1 KB` → vuelta a **slow start** (crecimiento exponencial hasta `ssthresh = 6 KB`, luego congestion avoidance lineal).

- **4. Diferencia rwnd vs cwnd (0,25 pts)**  
  - `rwnd` = capacidad del **buffer del receptor** (control de flujo);  
  - `cwnd` = capacidad estimada de **la red** (control de congestión).  
  - El emisor manda como mucho `min(rwnd, cwnd)`.

---

## Tema 9 – NAT e IPv6

### Actividad 6 – PAT con tabla de traducción *(1,00 pts)*

- **1. Tabla PAT (0,50 pts)**

| PC   | Socket interno         | Socket público (traducido)   | Socket remoto         | Protocolo |
|------|------------------------|------------------------------|------------------------|-----------|
| PC-A | 10.10.20.5:49152       | **203.0.113.200:49152**      | 198.51.100.40:80       | TCP       |
| PC-B | 10.10.20.6:49152       | **203.0.113.200:49152**      | 198.51.100.40:443      | TCP       |
| PC-C | 10.10.20.7:49152       | **203.0.113.200:49200**      | 198.51.100.40:80       | TCP       |

> PC-A y PC-B comparten IP pública y puerto público, **pero el puerto destino es distinto** (80 vs 443) → la 5-tupla pública es única, no hay colisión real. PC-C en cambio quiere la **misma 5-tupla** que PC-A (`203.0.113.200:49152 ↔ 198.51.100.40:80`), por lo que el router reescribe su puerto al primer libre `49200`.

- **2. ¿Hay colisión real entre PC-A y PC-B? (0,25 pts)**  
  - **No.** La 5-tupla pública es:  
    - PC-A → `(TCP, 203.0.113.200, 49152, 198.51.100.40, 80)`  
    - PC-B → `(TCP, 203.0.113.200, 49152, 198.51.100.40, 443)`  
  - Difieren en el **puerto destino**, así que el router puede demultiplexar las respuestas correctamente y **no necesita reescribir el puerto** de ninguno.

- **3. Vuelta del paquete a PC-C (0,25 pts)**  
  - El paquete llega al router con destino `203.0.113.200:49200` y origen `198.51.100.40:80`. El router busca esa 5-tupla en su tabla PAT y encuentra la entrada correspondiente a PC-C (`10.10.20.7:49152`). Reescribe la IP/puerto destino y lo entrega a **PC-C**.

---

### Actividad 7 – NAT estático para publicar un servidor *(1,00 pts)*

- **1. Paquete cliente → servidor (0,50 pts)**

| Punto de observación        | IP origen     | Puerto orig | IP destino         | Puerto dest |
|-----------------------------|---------------|-------------|--------------------|-------------|
| Fuera del router (Internet) | 198.51.100.5  | 55000       | **203.0.113.80**   | 25          |
| Dentro del router (LAN)     | 198.51.100.5  | 55000       | **192.168.100.25** | 25          |

- **2. Paquete de respuesta servidor → cliente (0,25 pts)**

| Punto de observación        | IP origen           | Puerto orig | IP destino    | Puerto dest |
|-----------------------------|---------------------|-------------|---------------|-------------|
| Dentro del router (LAN)     | **192.168.100.25**  | 25          | 198.51.100.5  | 55000       |
| Fuera del router (Internet) | **203.0.113.80**    | 25          | 198.51.100.5  | 55000       |

- **3. Qué reescribe el router en cada sentido (0,25 pts)**  
  - **Entrada (Internet → LAN):** se modifica la **IP destino** (`203.0.113.80` → `192.168.100.25`).  
  - **Salida (LAN → Internet):** se modifica la **IP origen** (`192.168.100.25` → `203.0.113.80`).  
  - Como el mapeo es **1:1** (una IP pública por una sola IP privada), no hay ambigüedad: cada paquete entrante a esa IP pública corresponde siempre al mismo host interno, así que **no es necesario tocar puertos**.

---

### Actividad 8 – Abreviación de direcciones IPv6 *(1,00 pts)*

- **a) (0,15)** `2001:0db8:00ab:0000:0000:0000:0000:00c1` → **`2001:db8:ab::c1`**
- **b) (0,15)** `0000:0000:0000:0000:0000:0000:0000:0000` → **`::`**
- **c) (0,15)** `fe80:0000:0000:0000:0000:0000:0000:000a` → **`fe80::a`**
- **d) (0,15)** `2001:0db8:1234:5678:0000:0000:0000:0001` → **`2001:db8:1234:5678::1`**
- **e) (0,15)** `fd00:1234:0000:0000:0001:0000:0000:0002` → **`fd00:1234::1:0:0:2`**  
  (las dos rachas de ceros tienen longitud 2; por RFC 5952 se aplica `::` en la **primera**.)

- **f) Validación (0,25)**

| Dirección              | ¿Válida? | Motivo                                                                                  |
|------------------------|----------|------------------------------------------------------------------------------------------|
| `2001:db8:1::g::1`     | **No**   | **Doble motivo:** (1) `g` **no es dígito hexadecimal** (solo `0-9` y `a-f`); (2) hay **dos `::`** (ambigua). |
| `fe80::1:0:0:0:1`      | **Sí** (sintácticamente) | Tiene 5 grupos tras el `::`, así que `::` representa exactamente 2 grupos cero → 8 grupos en total. La forma **canónica** RFC 5952 sería `fe80:0:0:1::1` (aplicar `::` a la racha de ceros más larga). |

---

### Actividad 9 – Expansión de direcciones IPv6 *(1,00 pts)*

> Recuerda: una IPv6 completa tiene **8 grupos de 4 dígitos hexadecimales** (32 dígitos en total). Para expandir una dirección abreviada hay que (1) restituir los **ceros a la izquierda** de cada grupo y (2) sustituir `::` por **tantos grupos `0000` como hagan falta** para llegar a 8 grupos.

- **1. Expansión a forma completa (0,40 pts, 5 × 0,08)**

| # | Dirección abreviada              | Forma completa                                   |
|---|----------------------------------|--------------------------------------------------|
| a | `::`                             | `0000:0000:0000:0000:0000:0000:0000:0000`        |
| b | `fe80::1`                        | `fe80:0000:0000:0000:0000:0000:0000:0001`        |
| c | `2001:db8::abcd:1`               | `2001:0db8:0000:0000:0000:0000:abcd:0001`        |
| d | `ff02::1`                        | `ff02:0000:0000:0000:0000:0000:0000:0001`        |
| e | `2001:db8:cafe::5`               | `2001:0db8:cafe:0000:0000:0000:0000:0005`        |

- **2. Análisis de `2001:db8:0:0:0:0:0:5` (0,30 pts; 0,10 cada apartado)**

  - **a)** La dirección ya tiene 8 grupos pero sin ceros a la izquierda. Forma completa:  
    `2001:0db8:0000:0000:0000:0000:0000:0005`.
  - **b)** Contiene una racha de **5 grupos consecutivos de ceros** (posiciones 3 a 7).
  - **c)** Aplicando `::` a la única racha de ceros (que además es la más larga), la **forma canónica** es:  
    **`2001:db8::5`**.

- **3. Validez de las representaciones (0,30 pts, 3 × 0,10)**

| # | Dirección                         | ¿Válida? | Motivo                                                                             |
|---|-----------------------------------|----------|------------------------------------------------------------------------------------|
| a | `fe80:::1`                        | **No**   | Aparecen **tres `:` seguidos** (`:::`). Solo se admite el separador `:` entre grupos y, como mucho, **un único `::`** para grupos de ceros. |
| b | `2001:0db8:1:2:3:4:5:6:7`         | **No**   | Tiene **9 grupos**. Una IPv6 debe llevar **exactamente 8 grupos** de 16 bits.      |
| c | `fd00:0:0:0:0:0:0:1`              | **Sí**   | Tiene 8 grupos correctos. Es válida sintácticamente, aunque su **forma canónica** sería `fd00::1`. |

---

### Actividad 10 – Identificación de tipos de dirección IPv6 *(1,00 pts)*

- **1. Asociación tipo ↔ prefijo de referencia (0,25 pts, 5 × 0,05)**

| Tipo de dirección  | Prefijo / dirección de referencia |
|--------------------|-----------------------------------|
| Loopback           | `::1` (`::1/128`)                 |
| Indefinida         | `::` (`::/128`)                   |
| Link-local         | `fe80::/10`                       |
| ULA (privada)      | `fc00::/7` (en la práctica `fd00::/8`) |
| Global unicast     | `2000::/3`                        |

- **2. Clasificación de 10 direcciones (0,50 pts, 10 × 0,05)**

| # | Dirección              | Tipo            |
|---|------------------------|-----------------|
| a | `::`                   | Indefinida      |
| b | `::1`                  | Loopback        |
| c | `fe80::abcd`           | Link-local      |
| d | `fe80::1234:5678`      | Link-local      |
| e | `fc00:1234::1`         | ULA (privada)   |
| f | `fd2a::abcd`           | ULA (privada)   |
| g | `2001:db8:1::a`        | Global unicast  |
| h | `2606:4700:10::1`      | Global unicast  |
| i | `ff02::1`              | Multicast       |
| j | `ff02::2`              | Multicast       |

- **3. Tipo + uso típico (0,25 pts, 3 × ≈0,083)**

| # | Dirección              | Tipo            | Uso típico                                                                                  |
|---|------------------------|-----------------|---------------------------------------------------------------------------------------------|
| a | `::1`                  | Loopback        | **Bucle local** del propio host (equivalente a `127.0.0.1` en IPv4); se usa para probar la pila TCP/IP local. |
| b | `fdab:1234::1`         | ULA (privada)   | Dirección **privada** dentro de una organización (equivalente IPv6 a las RFC 1918); no se enruta en Internet. |
| c | `ff02::2`              | Multicast       | Grupo "**todos los routers del enlace**"; lo usa, por ejemplo, un host para encontrar al router IPv6 con NDP/RA. |

---

## Resumen de puntuaciones

| Actividad | Tema | Puntos máximos |
|-----------|------|----------------|
| 1         | 8    | 1,00           |
| 2         | 8    | 1,00           |
| 3         | 8    | 1,00           |
| 4         | 8    | 1,00           |
| 5         | 8    | 1,00           |
| 6         | 9    | 1,00           |
| 7         | 9    | 1,00           |
| 8         | 9    | 1,00           |
| 9         | 9    | 1,00           |
| 10        | 9    | 1,00           |
| **Total** |      | **10,00**      |
