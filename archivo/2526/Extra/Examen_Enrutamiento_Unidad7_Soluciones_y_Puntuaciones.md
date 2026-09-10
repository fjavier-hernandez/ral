# Examen Unidad 7 – Soluciones y Puntuaciones

!!! warning "Documento interno – no publicar"
    Archivo de uso exclusivo del profesorado. No debe estar accesible al alumnado ni enlazado en la navegación.

---

## Modelo A – Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Enrutamiento_Unidad7_Modelo_A.md`  
> Los puntos indicados son **máximos**; se puede restar parcialmente según errores.

### Actividad 1 – Red 10.0.50.0 *(1,25 pts)*

Red base: `10.0.50.0/24` (bloque /24 dentro de 10.0.0.0/8). Se piden **8 subredes**.

- **1. Máscara para 8 subredes (0,25 pts)**  
  - Cálculo: `8 = 2^3` ⇒ se prestan **3 bits** al campo de host.
  - Nueva máscara: `/24 + 3 = /27` ⇒ `255.255.255.224`.
  - **Respuesta: /27 (255.255.255.224).**

- **2. Hosts utilizables por subred (0,25 pts)**  
  - Bits de host restantes: `32 − 27 = 5`.
  - Hosts utilizables: `2^5 − 2 = 30` (se descuentan red y broadcast).
  - **Respuesta: 30 hosts utilizables.**

- **3. Direcciones de red de las 8 subredes (0,25 pts)**  
  - Incremento entre subredes (4.º octeto): `2^5 = 32`.
  - Subredes: `10.0.50.0`, `10.0.50.32`, `10.0.50.64`, `10.0.50.96`, `10.0.50.128`, `10.0.50.160`, `10.0.50.192`, `10.0.50.224` (todas /27).

- **4. Nodo 10 en la subred 3 (0,25 pts)**  
  - Subred 3 (contando desde 1): red `10.0.50.64/27`.
  - Host 10 = primera dirección de red + 10 = `10.0.50.64 + 10 = 10.0.50.74`.
  - Comprobación: pertenece al rango válido `10.0.50.65 – 10.0.50.94` (broadcast `.95`). ✔
  - **Respuesta: 10.0.50.74.**

- **5. Subred del host 10.0.50.118 (0,25 pts)**  
  - Cálculo: `118 ÷ 32 = 3` resto `22` ⇒ red base = `3 × 32 = 96`.
  - **Respuesta: pertenece a `10.0.50.96/27` (rango .97–.126, broadcast .127).**

### Actividad 2 – Empresa con 30 redes *(1,25 pts)*

Red base: `172.16.0.0` (RFC 1918, clase B). Se necesitan **≥ 30 subredes**.

- **1. Máscara por defecto (0,25 pts)**  
  - Clase B (sin subdividir): `/16` ⇒ `255.255.0.0`.

- **2. Máscara para ≥ 30 subredes (0,25 pts)**  
  - Cálculo: `2^4 = 16 < 30 ≤ 2^5 = 32` ⇒ se prestan **5 bits**.
  - Nueva máscara: `/16 + 5 = /21` ⇒ `255.255.248.0` (32 subredes posibles).

- **3. Dir. red 1.ª, 2.ª, 15.ª y 30.ª (0,25 pts)**  
  - Bits de host: `32 − 21 = 11` ⇒ tamaño de bloque = `2^11 = 2048` direcciones, equivalente a un incremento de **8 en el 3.er octeto**.
  - Fórmula: subred *n* ⇒ tercer octeto = `(n − 1) × 8`.

  | Subred | Dirección de red |
  |--------|-------------------|
  | 1.ª    | `172.16.0.0/21`   |
  | 2.ª    | `172.16.8.0/21`   |
  | 15.ª   | `172.16.112.0/21` |
  | 30.ª   | `172.16.232.0/21` |

- **4. Rango IP válidas subred 15 (0,25 pts)**  
  - Subred `172.16.112.0/21` cubre tercer octeto `112–119`.
  - Primera IP: `172.16.112.1` · Última IP: `172.16.119.254` · Broadcast: `172.16.119.255`.

- **5. Broadcast subred 30 (0,25 pts)**  
  - Subred `172.16.232.0/21` ⇒ tercer octeto `232–239` ⇒ broadcast `172.16.239.255`.

### Actividad 3 – Red 10.10.0.0/22 *(1,00 pt)*

- **1. Red, broadcast, hosts (0,25 pts)**  
  - `/22` ⇒ máscara `255.255.252.0`. Bloque en el 3.er octeto = `2^(8−6) = 4` (octetos 0–3).
  - Red: `10.10.0.0` · Broadcast: `10.10.3.255`.
  - Hosts útiles: `2^10 − 2 = 1022`.

- **2. 4 subredes /24 (0,25 pts)**  
  - Pasamos de `/22` a `/24` ⇒ se toman **2 bits** adicionales ⇒ `2^2 = 4` subredes.
  - Subredes: `10.10.0.0/24`, `10.10.1.0/24`, `10.10.2.0/24`, `10.10.3.0/24`.

- **3. Subred de 10.10.2.50 (0,25 pts)**  
  - El 3.er octeto `2` indica directamente la subred `10.10.2.0/24` (rango `.1–.254`).

- **4. Primera y última IP válida subred con 10.10.3.200 (0,25 pts)**  
  - Subred `10.10.3.0/24` ⇒ primera `10.10.3.1`, última `10.10.3.254` (broadcast `.255`).

### Actividad 4 – Cuatro sedes *(1,25 pts)*

Sedes: `192.168.12.0/24`, `192.168.13.0/24`, `192.168.14.0/24`, `192.168.15.0/24`.

- **1. Octeto que cambia (0,25 pts)**  
  - Solo varía el **tercer octeto** (12, 13, 14, 15).

- **2. Tercer octeto en binario (0,25 pts)**  

  | Sede | Decimal | Binario   |
  |------|---------|-----------|
  | A    | 12      | `00001100`|
  | B    | 13      | `00001101`|
  | C    | 14      | `00001110`|
  | D    | 15      | `00001111`|

- **3. Bits iguales (0,25 pts)**  
  - Coinciden los **6 primeros bits** (`000011`); varían los 2 últimos.

- **4. Máscara superred (0,25 pts)**  
  - Bits comunes en el 3.er octeto: 6 ⇒ prefijo total `16 + 6 = /22`.
  - Máscara decimal: `255.255.252.0`.

- **5. Superred resultante (0,25 pts)**  
  - **Superred: `192.168.12.0/22`** (cubre `192.168.12.0 – 192.168.15.255`, exactamente las 4 sedes).

### Actividad 5 – Ocho departamentos *(1,00 pt)*

Redes: `192.168.32.0/24` … `192.168.39.0/24`.

- **1. Octeto variable en binario (0,25 pts)**  

  | Decimal | Binario   |
  |---------|-----------|
  | 32      | `00100000`|
  | 33      | `00100001`|
  | 34      | `00100010`|
  | 35      | `00100011`|
  | 36      | `00100100`|
  | 37      | `00100101`|
  | 38      | `00100110`|
  | 39      | `00100111`|

- **2. Bits iguales (0,25 pts)**  
  - Coinciden los **5 primeros bits** (`00100`); los 3 últimos cubren todas las combinaciones de 0 a 7.

- **3. Máscara y prefijo (0,25 pts)**  
  - Prefijo: `16 + 5 = /21` ⇒ máscara `255.255.248.0`.

- **4. Superred y rango IP (0,25 pts)**  
  - **Superred: `192.168.32.0/21`** · Rango total: `192.168.32.0 – 192.168.39.255`.

### Actividad 6 – Tabla del Router2 (tres routers) *(1,00 pt)*

Topología: `R1 ↔ R2 ↔ R3`. R2 conecta dos LAN (`192.168.10.0/24` y `192.168.20.0/24`) por su G0/0 (mediante subinterfaces o dos interfaces lógicas), enlace serie `192.168.100.0/30` con R1 y `192.168.100.4/30` con R3. R3 expone la LAN `172.16.50.0/24`. R1 ofrece la salida a Internet (ruta por defecto).

- **1. IP interfaces Router2 (0,25 pts)**  
  - Criterio del enunciado: **primer host válido del segmento para el router**. En enlaces /30 entre dos routers, R1 toma `.1` y R2 toma `.2`; R3 toma `.5` y R2 toma `.6` (cada router se queda con un host distinto del par).

  | Interfaz Router2     | Red                | IP/Máscara          |
  |----------------------|--------------------|---------------------|
  | G0/0.10 (LAN1)       | `192.168.10.0/24`  | `192.168.10.1/24`   |
  | G0/0.20 (LAN2)       | `192.168.20.0/24`  | `192.168.20.1/24`   |
  | S0/0/0 (enlace R1)   | `192.168.100.0/30` | `192.168.100.2/30`  |
  | S0/0/1 (enlace R3)   | `192.168.100.4/30` | `192.168.100.6/30`  |

- **2. Tabla rutas Router2 (0,50 pts)**  

  | Red destino       | Máscara/Prefijo | Siguiente salto    | Interfaz salida |
  |-------------------|-----------------|--------------------|-----------------|
  | `192.168.10.0`    | `/24`           | — *(directa)*      | G0/0.10         |
  | `192.168.20.0`    | `/24`           | — *(directa)*      | G0/0.20         |
  | `192.168.100.0`   | `/30`           | — *(directa)*      | S0/0/0          |
  | `192.168.100.4`   | `/30`           | — *(directa)*      | S0/0/1          |
  | `172.16.50.0`     | `/24`           | `192.168.100.5`    | S0/0/1          |
  | `0.0.0.0`         | `/0`            | `192.168.100.1`    | S0/0/0          |

- **3. Justificación directa / siguiente salto (0,25 pts)**  
  - **Directas**: redes en las que R2 tiene una interfaz configurada (`192.168.10.0/24`, `192.168.20.0/24`, `192.168.100.0/30`, `192.168.100.4/30`). El router las añade automáticamente al instalar la IP en la interfaz.
  - **Siguiente salto**: redes que R2 no toca físicamente. Para `172.16.50.0/24` el router envía el tráfico al extremo remoto del enlace que lleva a R3 (`192.168.100.5`). La ruta por defecto `0.0.0.0/0` apunta a R1 (`192.168.100.1`) porque por allí se llega a Internet.

### Actividad 7 – Dos routers *(0,75 pts)*

Topología: R1 (Internet, LAN `192.168.1.0/24` y enlace `192.168.100.0/30`) ↔ R2 (enlace y LAN `192.168.2.0/24`).

- **1. IP interfaces (0,25 pts)**  

  | Router | Interfaz | Red                | IP/Máscara          |
  |--------|----------|--------------------|---------------------|
  | R1     | G0/1     | `192.168.1.0/24`   | `192.168.1.1/24`    |
  | R1     | G0/2     | `192.168.100.0/30` | `192.168.100.1/30`  |
  | R2     | G0/0     | `192.168.100.0/30` | `192.168.100.2/30`  |
  | R2     | G0/1     | `192.168.2.0/24`   | `192.168.2.1/24`    |

- **2. Tabla rutas Router2 (0,25 pts)**  

  | Red destino       | Máscara/Prefijo | Siguiente salto    | Interfaz salida |
  |-------------------|-----------------|--------------------|-----------------|
  | `192.168.2.0`     | `/24`           | — *(directa)*      | G0/1            |
  | `192.168.100.0`   | `/30`           | — *(directa)*      | G0/0            |
  | `192.168.1.0`     | `/24`           | `192.168.100.1`    | G0/0            |
  | `0.0.0.0`         | `/0`            | `192.168.100.1`    | G0/0            |

- **3. Siguiente salto 192.168.1.0 y 0.0.0.0/0 (0,25 pts)**  
  - En ambas entradas el siguiente salto es **`192.168.100.1`** (interfaz G0/2 de R1), porque la única salida de R2 hacia el resto de redes y hacia Internet es a través de R1.

### Actividad 8 – Clínica dental *(0,75 pts)*

Switch de 24 puertos con 3 grupos: Recepción (≈ 4 dispositivos), Consultas (≈ 8) e Invitados (1 AP).

- **1. Cuadro de planificación (0,25 pts)**  

  | VLAN | Nombre     | Subred              | Hosts útiles | Puertos del switch |
  |------|------------|---------------------|--------------|--------------------|
  | 10   | Recepción  | `192.168.1.0/27`    | 30           | 1–5                |
  | 20   | Consultas  | `192.168.1.32/27`   | 30           | 6–17               |
  | 30   | Invitados  | `192.168.1.64/28`   | 14           | 18 (AP Wi‑Fi)      |

  - Justificación: cada VLAN obtiene su propia subred y rango de puertos coherente con el número de equipos.

- **2. Cuestionario (0,25 pts)**  
  - El Wi‑Fi de invitados **no debe compartir VLAN con Recepción** porque (a) se mezclarían el dominio de difusión y el direccionamiento, y (b) por seguridad: cualquier visitante podría ver el tráfico de la red interna.
  - Un PC de Consultas **no puede hacer ping a uno de Recepción** sin un router/switch L3: las VLAN aíslan el tráfico de capa 2; sin un dispositivo de capa 3 que enrute entre subredes diferentes, los paquetes nunca cruzan de una a otra.

- **3. Esquema de switch (0,25 pts)**  
  - Diagrama coherente con la tabla anterior (los puertos 1–5 etiquetados como VLAN 10, 6–17 como VLAN 20 y 18 como VLAN 30).

### Actividad 9 – Instituto *(0,75 pts)*

- **1. 3 VLANs ID, nombre, subred, puertos (0,25 pts)**  

  | VLAN | Nombre        | Subred              | Puertos |
  |------|---------------|---------------------|---------|
  | 10   | Administración| `10.10.10.0/27`     | 1–10    |
  | 20   | Aulas         | `10.10.20.0/27`     | 11–35   |
  | 30   | Invitados     | `10.10.30.0/28`     | 45–46   |

- **2. Dispositivo para comunicar Admin y Aulas (0,25 pts)**  
  - Es necesario un **router** o un **switch de capa 3 (multilayer)** con enrutamiento inter‑VLAN. Las VLANs operan en capa 2 y aislan dominios de broadcast: sin enrutamiento entre las subredes asociadas no hay comunicación.

- **3. Esquema de switch (0,25 pts)**  
  - Diagrama claro con los puertos mapeados a cada VLAN según la tabla anterior.

### Actividad 10 – Subnetting y tabla de rutas *(1,00 pt)*

Red base `192.168.80.0/24` dividida en **4 subredes** con un único router de 4 interfaces.

- **1. Máscara y 4 subredes /26 (0,25 pts)**  
  - `4 = 2^2` ⇒ se prestan **2 bits** ⇒ máscara `/26` (`255.255.255.192`).
  - Bloque = `2^(32−26) = 64` direcciones por subred (62 hosts útiles).

  | Subred | Red               | Rango válido            | Broadcast       |
  |--------|-------------------|-------------------------|-----------------|
  | S1     | `192.168.80.0/26` | `.1 – .62`              | `192.168.80.63` |
  | S2     | `192.168.80.64/26`| `.65 – .126`            | `192.168.80.127`|
  | S3     | `192.168.80.128/26`| `.129 – .190`          | `192.168.80.191`|
  | S4     | `192.168.80.192/26`| `.193 – .254`          | `192.168.80.255`|

- **2. IP interfaces + 4 rutas directas (0,50 pts)**  
  - Cada interfaz toma la **primera IP válida** de su subred:

  | Interfaz | Subred             | IP/Máscara            |
  |----------|--------------------|-----------------------|
  | G0/0     | `192.168.80.0/26`  | `192.168.80.1/26`     |
  | G0/1     | `192.168.80.64/26` | `192.168.80.65/26`    |
  | G0/2     | `192.168.80.128/26`| `192.168.80.129/26`   |
  | G0/3     | `192.168.80.192/26`| `192.168.80.193/26`   |

  - **Tabla de rutas (todas directamente conectadas, sin siguiente salto):**

  | Red destino        | Máscara/Prefijo | Siguiente salto | Interfaz salida |
  |--------------------|-----------------|-----------------|-----------------|
  | `192.168.80.0`     | `/26`           | — *(directa)*   | G0/0            |
  | `192.168.80.64`    | `/26`           | — *(directa)*   | G0/1            |
  | `192.168.80.128`   | `/26`           | — *(directa)*   | G0/2            |
  | `192.168.80.192`   | `/26`           | — *(directa)*   | G0/3            |

- **3. Esquema router + 4 subredes (0,25 pts)**  
  - Diagrama coherente con las redes y las interfaces de la tabla anterior (un router central con 4 ramales, una subred por interfaz).

---

## Modelo B – Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Enrutamiento_Unidad7_Modelo_B.md`.

### Actividad 1 – Red 192.168.200.0/26 *(1,25 pts)*

- **1. Red, broadcast, hosts /26 (0,25 pts)**  
  - `/26` ⇒ máscara `255.255.255.192`. Bits de host = 6 ⇒ `2^6 − 2 = 62` hosts.
  - Red: `192.168.200.0` · Broadcast: `192.168.200.63`.

- **2. 4 subredes del mismo tamaño (0,50 pts)**  
  - `4 = 2^2` ⇒ se prestan **2 bits** sobre `/26` ⇒ nuevo prefijo `/28` (`255.255.255.240`).
  - Bloque = `2^(32−28) = 16` direcciones por subred (14 hosts útiles).
  - Subredes: `192.168.200.0/28`, `192.168.200.16/28`, `192.168.200.32/28`, `192.168.200.48/28`.

- **3. Rangos y broadcast por subred (0,50 pts)**  

  | Subred | Red                  | Primer host           | Último host            | Broadcast              |
  |--------|----------------------|-----------------------|------------------------|------------------------|
  | S1     | `192.168.200.0/28`   | `192.168.200.1`       | `192.168.200.14`       | `192.168.200.15`       |
  | S2     | `192.168.200.16/28`  | `192.168.200.17`      | `192.168.200.30`       | `192.168.200.31`       |
  | S3     | `192.168.200.32/28`  | `192.168.200.33`      | `192.168.200.46`       | `192.168.200.47`       |
  | S4     | `192.168.200.48/28`  | `192.168.200.49`      | `192.168.200.62`       | `192.168.200.63`       |

### Actividad 2 – Red 10.10.0.0/22 *(1,25 pts)*

Misma red que la **Actividad 3 del Modelo A**: la solución numérica es idéntica (red, broadcast, 4 subredes /24, pertenencia y rangos), aplicando aquí la distribución de puntos del Modelo B.

- **1. Red, broadcast y hosts (0,21 pts)**  
  - Red `10.10.0.0/22`, broadcast `10.10.3.255`, `2^10 − 2 = 1022` hosts útiles.
- **2. 4 subredes /24 (0,21 pts)**  
  - `10.10.0.0/24`, `10.10.1.0/24`, `10.10.2.0/24`, `10.10.3.0/24`.
- **3. Subred de 10.10.2.50 (0,21 pts)**  
  - `10.10.2.0/24` (el 3.er octeto identifica directamente la subred).
- **4. Primera y última IP de la subred con 10.10.3.200 (0,20 pts)**  
  - Subred `10.10.3.0/24` ⇒ primera `10.10.3.1`, última `10.10.3.254`.

### Actividad 3 – Red 192.168.88.0 *(1,25 pts)*

- **1. Máscara para 32 subredes (0,25 pts)**  
  - `32 = 2^5` ⇒ se prestan **5 bits** ⇒ `/24 + 5 = /29` ⇒ `255.255.255.248`.

- **2. Hosts por subred (0,25 pts)**  
  - Bits de host = 3 ⇒ `2^3 − 2 = 6` hosts utilizables por subred.

- **3. Redes 1, 16 y 32 (0,50 pts)**  
  - Incremento (4.º octeto) = `2^3 = 8`. Subred *n* ⇒ `(n − 1) × 8`.

  | Subred | Dirección de red       |
  |--------|------------------------|
  | 1.ª    | `192.168.88.0/29`      |
  | 16.ª   | `192.168.88.120/29`    |
  | 32.ª   | `192.168.88.248/29`    |

- **4. Host 7 en subred 20 (0,25 pts)**  
  - Subred 20 ⇒ red `(20 − 1) × 8 = 152` ⇒ `192.168.88.152/29` (rango válido `.153 – .158`, broadcast `.159`).
  - Aplicando literalmente “host 7” como séptimo desplazamiento desde la dirección de red: `192.168.88.152 + 7 = 192.168.88.159`.
  - **Aclaración técnica**: en /29 solo hay **6 hosts asignables** (.153–.158); por tanto, esa séptima posición coincide con la dirección de **broadcast** y, en una asignación real, no podría usarse para un host.

- **5. Subred de 192.168.88.211 (0,25 pts)**  
  - `211 ÷ 8 = 26` resto `3` ⇒ red base `26 × 8 = 208`.
  - **Respuesta: `192.168.88.208/29`** (subred 27.ª; rango `.209 – .214`, broadcast `.215`).

### Actividad 4 – Ocho departamentos *(1,00 pt)*

Mismo enunciado que la **Actividad 5 del Modelo A**: solución de supernetting idéntica.

- Octetos en binario `00100000–00100111`; 5 bits comunes; máscara `/21` (`255.255.248.0`); **superred `192.168.32.0/21`** que cubre `192.168.32.0 – 192.168.39.255`.

### Actividad 5 – Tres redes contiguas *(1,00 pt)*

Redes a resumir: `192.168.100.0/24`, `192.168.101.0/24`, `192.168.102.0/24`.

- **1. ¿Se pueden agrupar? (0,25 pts)**  
  - Sí: son **contiguas** (100, 101, 102) y todas comparten el mismo prefijo `/24`, por lo que son candidatas a una superred.

- **2. Octeto variable en binario (0,25 pts)**  

  | Decimal | Binario   |
  |---------|-----------|
  | 100     | `01100100`|
  | 101     | `01100101`|
  | 102     | `01100110`|

- **3. Bits coincidentes y máscara (0,25 pts)**  
  - Comparando bit a bit por la izquierda, los **6 primeros bits** son iguales (`011001`); los 2 últimos varían.
  - Máscara: `16 + 6 = /22` ⇒ `255.255.252.0`.

- **4. Superred CIDR (0,25 pts)**  
  - **Superred: `192.168.100.0/22`** (cubre `192.168.100.0 – 192.168.103.255`; observa que incluye también `192.168.103.0/24`, dirección que se reserva al hacer la agregación).

### Actividad 6 – Tabla del Router1 (tres routers) *(1,25 pts)*

Topología: R1 ↔ R2 ↔ R3. Enlaces serie `192.168.100.0/30` (R1–R2) y `192.168.100.4/30` (R2–R3). LANs internas detrás de R2 (`192.168.10.0/24`, `192.168.20.0/24`, `172.16.100.0/24`) y detrás de R3 (`192.168.30.0/24`). R1 ofrece la salida a Internet por su interfaz G0/0.

- **1. IP interfaz Router1 hacia Router2 (0,25 pts)**  
  - Enlace `192.168.100.0/30`, hosts útiles `.1` y `.2`. R1 toma `192.168.100.1/30`; R2 toma `192.168.100.2/30`.

- **2. Tabla de rutas estáticas (0,75 pts)**  

  | Red destino       | Máscara/Prefijo | Siguiente salto         | Interfaz salida |
  |-------------------|-----------------|-------------------------|-----------------|
  | `192.168.100.0`   | `/30`           | — *(directa)*           | S0/0/0          |
  | *(red ISP)*       | *(/30, /29…)*   | — *(directa)*           | G0/0            |
  | `192.168.10.0`    | `/24`           | `192.168.100.2`         | S0/0/0          |
  | `192.168.20.0`    | `/24`           | `192.168.100.2`         | S0/0/0          |
  | `172.16.100.0`    | `/24`           | `192.168.100.2`         | S0/0/0          |
  | `192.168.30.0`    | `/24`           | `192.168.100.2`         | S0/0/0          |
  | `0.0.0.0`         | `/0`            | *IP del gateway del ISP*| G0/0            |

- **3. Mismo siguiente salto (0,25 pts)**  
  - Todas las redes internas (`192.168.10.0/24`, `192.168.20.0/24`, `172.16.100.0/24`, `192.168.30.0/24`) están **detrás de R2** desde el punto de vista de R1: solo se llega a ellas por el enlace serie `192.168.100.0/30`. Por eso, todas las rutas estáticas no directas usan como **siguiente salto la IP de R2 en ese enlace (`192.168.100.2`)** y como **interfaz de salida S0/0/0**.

### Actividad 7 – Tabla del Router3 y ruta por defecto *(1,25 pts)*

- **1. IP de interfaces Router3 (0,25 pts)**  

  | Interfaz | Red                | IP/Máscara          |
  |----------|--------------------|---------------------|
  | S0/0/0   | `192.168.100.4/30` | `192.168.100.5/30`  |
  | G0/1     | `192.168.30.0/24`  | `192.168.30.1/24`   |

  - En `192.168.100.4/30` los hosts útiles son `.5` y `.6`; R3 se queda con `.5` y R2 con `.6`.

- **2. Tabla de rutas Router3 (0,75 pts)**  
  - Versión **detallada** (una entrada por red interna):

  | Red destino       | Máscara/Prefijo | Siguiente salto    | Interfaz salida |
  |-------------------|-----------------|--------------------|-----------------|
  | `192.168.30.0`    | `/24`           | — *(directa)*      | G0/1            |
  | `192.168.100.4`   | `/30`           | — *(directa)*      | S0/0/0          |
  | `192.168.10.0`    | `/24`           | `192.168.100.6`    | S0/0/0          |
  | `192.168.20.0`    | `/24`           | `192.168.100.6`    | S0/0/0          |
  | `172.16.100.0`    | `/24`           | `192.168.100.6`    | S0/0/0          |
  | `192.168.100.0`   | `/30`           | `192.168.100.6`    | S0/0/0          |
  | `0.0.0.0`         | `/0`            | `192.168.100.6`    | S0/0/0          |

  - Versión **compacta** (igual de válida, sustituye las entradas estáticas internas por una única ruta por defecto, ya que R3 solo tiene una salida hacia el resto de la red):

  | Red destino       | Máscara/Prefijo | Siguiente salto    | Interfaz salida |
  |-------------------|-----------------|--------------------|-----------------|
  | `192.168.30.0`    | `/24`           | — *(directa)*      | G0/1            |
  | `192.168.100.4`   | `/30`           | — *(directa)*      | S0/0/0          |
  | `0.0.0.0`         | `/0`            | `192.168.100.6`    | S0/0/0          |

- **3. Significado 0.0.0.0/0 y siguiente salto (0,25 pts)**  
  - `0.0.0.0/0` es la **ruta por defecto**: representa “cualquier red no incluida en la tabla”. Se usa cuando R3 recibe un paquete cuyo destino no coincide con ninguna entrada específica.
  - El **siguiente salto** es `192.168.100.6` (la IP de R2 en el enlace `/30`), porque toda la red — incluida la salida a Internet — está accesible únicamente a través de R2.

### Actividad 8 – Oficina pequeña *(0,75 pts)*

Red base `192.168.50.0/24`; tres VLANs: Recepción, Contabilidad, WiFi_Visitantes.

- **1. 3 subredes (0,25 pts)**  
  - División en 3 subredes `/26` (la 4.ª queda libre como reserva). Cada `/26` ofrece 62 hosts útiles, suficiente para los grupos.

  | VLAN              | Subred              | Rango válido          | Broadcast        |
  |-------------------|---------------------|-----------------------|------------------|
  | 10 Recepción      | `192.168.50.0/26`   | `.1 – .62`            | `192.168.50.63`  |
  | 20 Contabilidad   | `192.168.50.64/26`  | `.65 – .126`          | `192.168.50.127` |
  | 30 WiFi_Visitantes| `192.168.50.128/26` | `.129 – .190`         | `192.168.50.191` |

- **2. ID y nombre por VLAN (0,25 pts)**  
  - VLAN 10 “Recepción”, VLAN 20 “Contabilidad”, VLAN 30 “WiFi_Visitantes” (asignación coherente con la tabla anterior).

- **3. PCs en VLANs distintas sin router (0,25 pts)**  
  - **No se pueden comunicar.** Las VLAN aíslan los dominios de difusión en capa 2 y, además, cada una está en una subred IP distinta. Sin un router (o un switch de capa 3 con SVIs/inter‑VLAN routing), los paquetes no atraviesan la frontera entre subredes y los PCs son inalcanzables entre sí.

### Actividad 9 – Tres plantas (trunk) *(0,75 pts)*

- **1. Modos Access/Trunk (0,25 pts)**  
  - Puertos a equipos finales (PC‑Almacén1, PC‑Admin1, PC‑Almacén2, PC‑Admin2, PC‑Almacén3, PC‑Admin3): **Access** asignados a su VLAN (Almacén o Administración).
  - Enlaces entre switches (Sótano P24 ↔ Planta 1 P23, Planta 1 P24 ↔ Planta 2 P24): **Trunk**, porque deben transportar varias VLANs (Almacén y Administración) a la vez.

- **2. Trama etiquetada hasta PC‑Almacén3 (0,25 pts)**  
  - Camino: `PC‑Almacén1 → SW Sótano (P2 Access, sin etiqueta) → Trunk Sótano‑P1 (etiquetada 802.1Q VLAN Almacén) → SW Planta 1 → Trunk P1‑P2 (etiquetada 802.1Q VLAN Almacén) → SW Planta 2 → P2 Access (sin etiqueta) → PC‑Almacén3`.
  - **Estándar de etiquetado: IEEE 802.1Q** (las etiquetas viajan únicamente por los enlaces trunk; los puertos Access entregan la trama sin etiqueta al PC).

- **3. Trunk roto como Access VLAN Almacén (0,25 pts)**  
  - Si el puerto P24 del SW Planta 1 hacia Planta 2 deja de ser trunk y pasa a Access para la VLAN Almacén, ese enlace **solo transporta VLAN Almacén**.
  - Resultado: las tramas de la VLAN Administración **no cruzan ese enlace**, por lo que **PC‑Admin de Planta 1 y PC‑Admin de Planta 2 dejan de comunicarse**.

### Actividad 10 – Diseño completo (dos edificios) *(1,00 pt)*

Red base: `10.20.0.0/22`. División en 4 subredes `/24` (se prestan 2 bits, `2^2 = 4`).

- **1. 4 subredes /24 desde /22 (0,25 pts)**  
  - `10.20.0.0/24`, `10.20.1.0/24`, `10.20.2.0/24`, `10.20.3.0/24`.

- **2. Subred por grupo + IDs VLAN (0,25 pts)**  

  | Grupo               | VLAN | Subred           | Rango válido        |
  |---------------------|------|------------------|---------------------|
  | Ventas (Edif. A)    | 10   | `10.20.0.0/24`   | `.1 – .254`         |
  | Admin A (Edif. A)   | 20   | `10.20.1.0/24`   | `.1 – .254`         |
  | Almacén (Edif. B)   | 30   | `10.20.2.0/24`   | `.1 – .254`         |
  | Admin B (Edif. B)   | 40   | `10.20.3.0/24`   | `.1 – .254`         |

- **3. Diagrama + Access/Trunk (0,25 pts)**  
  - Cada switch (SW‑A en Edificio A, SW‑B en Edificio B) tiene puertos **Access** asignados a las VLANs de su edificio (10/20 en SW‑A; 30/40 en SW‑B).
  - El enlace **SW‑A ↔ SW‑B** debe configurarse en **Trunk (802.1Q)** para que, sobre un solo cable, viajen las cuatro VLANs etiquetadas y se mantenga la separación L2 entre edificios.

- **4. Dispositivo Ventas–Admin (0,25 pts)**  
  - Para que Ventas (VLAN 10, Edificio A) hable con Admin B (VLAN 40, Edificio B) hace falta un **router** o un **switch de capa 3 (multilayer)** que realice **enrutamiento inter‑VLAN** entre las cuatro subredes. Sin ese dispositivo L3, las VLAN están aisladas.

---

Este archivo sirve como guía rápida de corrección con **soluciones numéricas clave** y **puntos máximos por apartado**, manteniendo la escala total de **10 puntos** en cada modelo.

