# Examen Tema 8 y 9 – Modelo A – Soluciones y Puntuaciones

---

## Modelo A – Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Tema_8_9_Modelo_A.md`  
> Los puntos indicados son **máximos**; se puede restar parcialmente según errores.

---

## Tema 8 – Capa de Transporte

### Actividad 1 – Sockets y multiplexación *(1,00 pts)*

- **1. Tipo de puerto (0,25 pts)**

| Puerto         | Tipo        | Servicio (si procede) |
|----------------|-------------|-----------------------|
| 51200 (local)  | Efímero     | —                     |
| 51201 (local)  | Efímero     | —                     |
| 51230 (local)  | Efímero     | —                     |
| 51240 (local)  | Efímero     | —                     |
| 443 (destino)  | Bien conocido | HTTPS                |
| 443 (destino)  | Bien conocido | HTTPS                |
| 22 (destino)   | Bien conocido | SSH                  |
| 5004 (destino) | Registrado  | RTP (streaming)       |

- **2. Tabla de sockets (0,25 pts)**

| Protocolo | Socket local         | Socket remoto         |
|-----------|----------------------|-----------------------|
| TCP       | 10.20.30.40:51200    | 198.51.100.10:443     |
| TCP       | 10.20.30.40:51201    | 198.51.100.10:443     |
| TCP       | 10.20.30.40:51230    | 192.168.5.7:22        |
| UDP       | 10.20.30.40:51240    | 203.0.113.45:5004     |

- **3. Mismo puerto efímero en dos pestañas al mismo destino (0,25 pts)**  
  - La conexión se identifica por la **5-tupla** `(protocolo, IP_orig, puerto_orig, IP_dest, puerto_dest)`. Si las dos pestañas usaran el mismo puerto efímero al mismo `IP:puerto` destino, las dos 5-tuplas serían **idénticas** y el sistema operativo no podría asociar cada respuesta a la pestaña correcta. Por eso el SO obliga a usar puertos efímeros distintos.

- **4. Tupla de cada conexión (0,25 pts)**

  - `(TCP, 10.20.30.40, 51200, 198.51.100.10, 443)`
  - `(TCP, 10.20.30.40, 51201, 198.51.100.10, 443)`
  - `(TCP, 10.20.30.40, 51230, 192.168.5.7, 22)`
  - `(UDP, 10.20.30.40, 51240, 203.0.113.45, 5004)`

---

### Actividad 2 – TCP vs UDP en escenarios reales *(1,00 pts)*

| Nº | Escenario                       | Protocolo | Justificación breve                                                                  | Puntos |
|----|---------------------------------|-----------|--------------------------------------------------------------------------------------|--------|
| 1  | Descarga 800 MB por HTTP        | **TCP**   | HTTP usa TCP; archivo grande exige fiabilidad y orden. Una pérdida sin retransmisión corromperá el zip. | 0,20 |
| 2  | DNS a 8.8.8.8                   | **UDP**   | Consulta corta, baja latencia; si se pierde, se reintenta a nivel de aplicación.     | 0,20 |
| 3  | Videollamada en directo         | **UDP**   | Prioridad: baja latencia. Reenviar paquetes antiguos no aporta nada al directo.      | 0,20 |
| 4  | NTP                             | **UDP**   | Paquetes sin estado, muy pequeños y latencia baja; abrir TCP sería sobrecarga inútil.| 0,20 |
| 5  | Correo SMTP de 12 KB            | **TCP**   | Necesita fiabilidad y entrega en orden completa para no corromper el mensaje.        | 0,20 |

---

### Actividad 3 – Three-way handshake *(1,00 pts)*

- **1. Tabla del intercambio (0,50 pts)**

| Paso | Origen → Destino   | Flags     | SEQ   | ACK    |
|:----:|--------------------|-----------|------:|-------:|
| 1    | Cliente → Servidor | SYN       | 8000  | —      |
| 2    | Servidor → Cliente | SYN + ACK | 22000 | 8001   |
| 3    | Cliente → Servidor | ACK       | 8001  | 22001  |

- **2. Primer segmento con datos del cliente (0,25 pts)**  
  - Tras el paso 3, el siguiente byte que el cliente puede transmitir es el `8001`. Por tanto:  
    - `SEQ = 8001`  
    - `ACK = 22001` (sigue confirmando que espera el siguiente byte del servidor).

- **3. ACK que devuelve el servidor (0,25 pts)**  
  - Llegan los bytes `8001 → 8240` (240 bytes). El siguiente byte esperado es `8241`.  
  - `ACK = 8001 + 240 = 8241`.

---

### Actividad 4 – Segmentación TCP *(1,00 pts)*

- **1. MSS (0,25 pts)**  
  - `MSS = MTU − cabIP − cabTCP = 1500 − 20 − 20 = 1460 B`.

- **2. Número de segmentos (0,25 pts)**  
  - `⌈18 500 / 1460⌉ = ⌈12,67⌉ = 13` segmentos.

- **3. Bytes del último segmento (0,25 pts)**  
  - 12 segmentos llenos transportan `12 × 1460 = 17 520 B`.  
  - Último segmento: `18 500 − 17 520 = 980 B`.

- **4. Pérdida del segmento 7 (0,25 pts)**  
  - Solo se retransmite el **segmento 7**. Los segmentos 8–13 que ya hayan llegado quedan **fuera de orden** en el buffer del receptor. El receptor envía **ACK duplicados** pidiendo el byte que falta y, tras **3 ACK duplicados**, el emisor aplica **fast retransmit** y reenvía únicamente el segmento perdido sin esperar al timeout.

---

### Actividad 5 – Control de flujo y congestión *(1,00 pts)*

- **1. Bytes en vuelo permitidos (0,25 pts)**  
  - `bytes_en_vuelo ≤ min(rwnd, cwnd) = min(10 KB, 6 KB) = 6 KB`.  
  - El cuello de botella es la red (`cwnd`), no el receptor.

- **2. Reacción ante timeout (0,25 pts)**  
  - Se asume **congestión severa**:  
    - `ssthresh = cwnd / 2 = 6 / 2 = 3 KB`.  
    - `cwnd = 1 MSS = 1 KB` → vuelta a **slow start** (crecimiento exponencial hasta `ssthresh = 3 KB` y, a partir de ahí, congestion avoidance lineal).

- **3. Reacción ante 3 ACK duplicados (0,25 pts)**  
  - **Fast retransmit + fast recovery**: la red sigue activa, así que no se vuelve a slow start.  
    - Se reenvía el segmento perdido inmediatamente.  
    - `ssthresh = cwnd / 2 = 3 KB`.  
    - `cwnd = ssthresh = 3 KB` (en fast recovery) y se sigue creciendo linealmente desde ahí.

- **4. Diferencia rwnd vs cwnd (0,25 pts)**  
  - `rwnd` lo impone el **receptor** para no desbordar **su buffer** (control de flujo); `cwnd` lo impone el **emisor** para no saturar **la red** (control de congestión). Bytes en vuelo = `min(rwnd, cwnd)`.

---

## Tema 9 – NAT e IPv6

### Actividad 6 – PAT con tabla de traducción *(1,00 pts)*

- **1. Tabla PAT (0,50 pts)**

| PC  | Socket interno         | Socket público (traducido) | Socket remoto       | Protocolo |
|-----|------------------------|----------------------------|---------------------|-----------|
| PC1 | 192.168.50.10:52000    | **198.51.100.7:52000**     | 203.0.113.10:443    | TCP       |
| PC2 | 192.168.50.11:52000    | **198.51.100.7:52050**     | 203.0.113.10:443    | TCP       |
| PC3 | 192.168.50.12:52001    | **198.51.100.7:52001**     | 203.0.113.10:80     | TCP       |

> PC1 y PC2 quieren la misma 5-tupla pública (`198.51.100.7:52000 ↔ 203.0.113.10:443`), por lo que el router **reescribe el puerto** de PC2 al primer libre `52050` y guarda esa traducción.

- **2. Vuelta del paquete a PC2 (0,25 pts)**  
  - El paquete de respuesta llega al router con destino **`198.51.100.7:52050`** (origen `203.0.113.10:443`). El router consulta su tabla PAT y, por la entrada con puerto público `52050`, sabe que corresponde a la sesión interna `192.168.50.11:52000`, así que reescribe el destino y se lo entrega a **PC2**.

- **3. Por qué no basta con traducir solo la IP (0,25 pts)**  
  - Si solo se reescribiera la IP, los sockets públicos de PC1 y PC2 serían idénticos (`198.51.100.7:52000`) hacia el mismo servidor y mismo puerto. El router **no podría distinguir** a quién entregar la respuesta. Por eso PAT traduce **IP + puerto** y mantiene una tabla de sesiones.

---

### Actividad 7 – NAT estático para publicar un servidor *(1,00 pts)*

- **1. Paquete cliente → servidor (0,50 pts)**

| Punto de observación        | IP origen      | Puerto orig | IP destino       | Puerto dest |
|-----------------------------|----------------|-------------|-------------------|-------------|
| Fuera del router (Internet) | 203.0.113.55   | 60000       | **198.51.100.99** | 80          |
| Dentro del router (LAN)     | 203.0.113.55   | 60000       | **172.16.20.80**  | 80          |

- **2. Paquete de respuesta servidor → cliente (0,25 pts)**

| Punto de observación        | IP origen          | Puerto orig | IP destino    | Puerto dest |
|-----------------------------|--------------------|-------------|---------------|-------------|
| Dentro del router (LAN)     | **172.16.20.80**   | 80          | 203.0.113.55  | 60000       |
| Fuera del router (Internet) | **198.51.100.99**  | 80          | 203.0.113.55  | 60000       |

- **3. Qué reescribe el router en cada sentido (0,25 pts)**  
  - **Entrada (Internet → LAN):** se modifica la **IP destino** (`198.51.100.99` → `172.16.20.80`).  
  - **Salida (LAN → Internet):** se modifica la **IP origen** (`172.16.20.80` → `198.51.100.99`).  
  - Como el mapeo es **1:1** (una IP pública por una sola IP privada), no existe ambigüedad: cada paquete entrante a esa IP pública pertenece al mismo host interno, así que **no hace falta tocar puertos**.

---

### Actividad 8 – Abreviación de direcciones IPv6 *(1,00 pts)*

- **a) (0,15)** `2001:0db8:0000:0000:0000:0000:0000:0050` → **`2001:db8::50`**
- **b) (0,15)** `fe80:0000:0000:0000:0a1b:2c3d:4e5f:6789` → **`fe80::a1b:2c3d:4e5f:6789`**
- **c) (0,15)** `2001:0abc:0000:0000:0001:0000:0000:0010` → **`2001:abc::1:0:0:10`**  
  (las dos rachas de ceros tienen longitud 2; por RFC 5952 se usa `::` en la **primera**.)
- **d) (0,15)** `0000:0000:0000:0000:0000:0000:0000:0001` → **`::1`**
- **e) (0,15)** `fd00:1234:5678:0000:0000:0000:0000:000a` → **`fd00:1234:5678::a`**

- **f) Validación (0,25)**

| Dirección              | ¿Válida? | Motivo                                                                             |
|------------------------|----------|------------------------------------------------------------------------------------|
| `2001::db8::1`         | **No**   | Aparecen **dos `::`**; la abreviatura sería ambigua (no se sabe cuántos grupos cero representa cada una). Solo se admite **un `::`** por dirección. |
| `2001:db8:zzzz::1`     | **No**   | Contiene `zzzz`, que **no son dígitos hexadecimales** (solo se permiten `0-9` y `a-f`). |

---

### Actividad 9 – Expansión de direcciones IPv6 *(1,00 pts)*

> Recuerda: una IPv6 completa tiene **8 grupos de 4 dígitos hexadecimales** (32 dígitos en total). Para expandir una dirección abreviada hay que (1) restituir los **ceros a la izquierda** de cada grupo y (2) sustituir `::` por **tantos grupos `0000` como hagan falta** para llegar a 8 grupos.

- **1. Expansión a forma completa (0,40 pts, 5 × 0,08)**

| # | Dirección abreviada              | Forma completa                                   |
|---|----------------------------------|--------------------------------------------------|
| a | `::1`                            | `0000:0000:0000:0000:0000:0000:0000:0001`        |
| b | `2001:db8::1`                    | `2001:0db8:0000:0000:0000:0000:0000:0001`        |
| c | `fe80::a:b:c:d`                  | `fe80:0000:0000:0000:000a:000b:000c:000d`        |
| d | `ff02::2`                        | `ff02:0000:0000:0000:0000:0000:0000:0002`        |
| e | `2001:db8:abcd::1234`            | `2001:0db8:abcd:0000:0000:0000:0000:1234`        |

- **2. Análisis de `fe80::1:0:0:5` (0,30 pts; 0,10 cada apartado)**

  - **a)** Antes de `::` hay **1 grupo** (`fe80`) y después hay **4 grupos** (`1`, `0`, `0`, `5`). Por tanto `::` representa `8 − 1 − 4 = 3` grupos cero. Forma completa:  
    `fe80:0000:0000:0000:0001:0000:0000:0005`.
  - **b)** El `::` representa **3 grupos** de ceros consecutivos.
  - **c)** En esta dirección hay dos rachas de ceros: una de **3 grupos** (posiciones 2–4) y otra de **2 grupos** (posiciones 6–7). La forma canónica RFC 5952 aplica `::` a la **racha más larga**, que es la primera. Por tanto la forma canónica coincide con la dada: **`fe80::1:0:0:5`** (ya estaba canonicalizada).

- **3. Validez de las representaciones (0,30 pts, 3 × 0,10)**

| # | Dirección                         | ¿Válida? | Motivo                                                                             |
|---|-----------------------------------|----------|------------------------------------------------------------------------------------|
| a | `2001:db8:1:2:3:4:5`              | **No**   | Solo tiene **7 grupos** y no usa `::`. Una IPv6 sin `::` debe llevar **exactamente 8 grupos**. |
| b | `2001:db8::1::5`                  | **No**   | Aparece **dos veces `::`**. Solo se admite **un único `::`** por dirección.        |
| c | `2001:db8:0:0:0:0:0:1`            | **Sí**   | Tiene 8 grupos correctos. Es válida sintácticamente, aunque su **forma canónica** sería `2001:db8::1`. |

---

### Actividad 10 – Identificación de tipos de dirección IPv6 *(1,00 pts)*

- **1. Asociación tipo ↔ prefijo de referencia (0,25 pts, 5 × 0,05)**

| Tipo de dirección  | Prefijo / dirección de referencia |
|--------------------|-----------------------------------|
| Loopback           | `::1` (`::1/128`)                 |
| Indefinida         | `::` (`::/128`)                   |
| Link-local         | `fe80::/10`                       |
| Multicast          | `ff00::/8`                        |
| Global unicast     | `2000::/3`                        |

- **2. Clasificación de 10 direcciones (0,50 pts, 10 × 0,05)**

| # | Dirección              | Tipo            |
|---|------------------------|-----------------|
| a | `::1`                  | Loopback        |
| b | `::`                   | Indefinida      |
| c | `fe80::1`              | Link-local      |
| d | `fe80::abcd:1`         | Link-local      |
| e | `fc00::5`              | ULA (privada)   |
| f | `fd12:3456::a`         | ULA (privada)   |
| g | `2001:db8::1`          | Global unicast  |
| h | `2400:cb00::1`         | Global unicast  |
| i | `ff02::1`              | Multicast       |
| j | `ff02::2`              | Multicast       |

- **3. Tipo + uso típico (0,25 pts, 3 × ≈0,083)**

| # | Dirección              | Tipo            | Uso típico                                                                                  |
|---|------------------------|-----------------|---------------------------------------------------------------------------------------------|
| a | `fe80::1`              | Link-local      | Comunicación dentro del **mismo enlace**; se autoconfigura siempre (SLAAC, NDP). Es la IP típica que un host usa para hablar con su router del enlace. |
| b | `2001:db8:cafe::1`     | Global unicast  | Dirección **routable en Internet**. El bloque `2001:db8::/32` está reservado a **documentación y ejemplos** (RFC 3849). |
| c | `ff02::1`              | Multicast       | Grupo "**todos los nodos del enlace**"; lo usa, por ejemplo, NDP para descubrir vecinos.    |

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
