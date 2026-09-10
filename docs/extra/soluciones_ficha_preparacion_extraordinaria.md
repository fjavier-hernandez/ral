---
title: Soluciones - Ficha de preparación extraordinaria
description: Soluciones a las actividades de la ficha de preparación para el examen extraordinario de Redes (SMR).
---

# Soluciones – Ficha de preparación extraordinaria

Estas soluciones corresponden a las actividades de la [ficha de preparación para el examen extraordinario](../ficha_preparacion_extraordinaria.md). Resuelve primero las actividades en papel y luego comprueba aquí tus resultados.

---

## Actividad 1 – Preguntas de desarrollo *(2,00 pts)*

### 1. Funciones principales de la capa de enlace de datos (OSI) *(0,50 pts)*

Cuatro funciones (basta con cuatro):

- **Entramado (framing):** delimita el flujo de bits en **tramas**, marcando inicio y fin de cada una.
- **Direccionamiento físico (MAC):** identifica origen y destino dentro del **mismo enlace** mediante direcciones MAC.
- **Control de acceso al medio (MAC):** regula quién transmite y cuándo para evitar o gestionar colisiones (p. ej. CSMA/CD en Ethernet clásica).
- **Detección y control de errores:** mediante el campo **FCS/CRC** se detectan tramas dañadas y se descartan.
- *(Adicional)* **Control de flujo:** evita que un emisor rápido sature a un receptor lento.

### 2. IP públicas vs privadas y rangos RFC 1918 *(0,50 pts)*

- **Públicas:** únicas a nivel mundial, **enrutables en Internet**, asignadas por IANA/RIR a través del ISP.
- **Privadas:** de uso interno en una LAN, **no se enrutan en Internet**; para salir necesitan traducción **NAT/PAT**.
- **Tres rangos privados (RFC 1918):**

| Clase | Rango                         | Prefijo CIDR     |
|-------|-------------------------------|------------------|
| A     | 10.0.0.0 – 10.255.255.255     | `10.0.0.0/8`     |
| B     | 172.16.0.0 – 172.31.255.255   | `172.16.0.0/12`  |
| C     | 192.168.0.0 – 192.168.255.255 | `192.168.0.0/16` |

### 3. DHCP, parámetros, ventajas y comprobaciones *(0,50 pts)*

- **Qué es:** *Dynamic Host Configuration Protocol*; asigna **automáticamente** la configuración de red a los clientes al conectarse (proceso **DORA**: Discover, Offer, Request, Ack).
- **Parámetros que asigna:** **dirección IP**, **máscara de subred**, **puerta de enlace (gateway)** y **servidor(es) DNS** (además del tiempo de concesión o *lease*).
- **Ventajas frente a la configuración manual:** evita errores de tecleo, impide **direcciones IP duplicadas**, centraliza y agiliza la gestión, y facilita la movilidad de equipos.
- **Tres comprobaciones básicas (con `ping`):**
  - `ping 127.0.0.1` (loopback): verifica que la **pila TCP/IP local** del equipo funciona.
  - `ping <IP propia>`: verifica que la **tarjeta de red está bien configurada** con su IP.
  - `ping <gateway>`: verifica la **conectividad con el router** dentro de la LAN.
  - *(Adicional)* `ping 8.8.8.8` o `ping <web>`: verifica la **salida a Internet** y, si se hace por nombre, también la **resolución DNS**.

### 4. Dominio de colisión y dominio de difusión *(0,50 pts)*

- **Dominio de colisión:** conjunto de dispositivos que comparten el mismo medio y cuyas transmisiones pueden **colisionar** entre sí.
- **Dominio de difusión (broadcast):** conjunto de dispositivos que **reciben los mensajes de difusión** enviados por cualquiera de ellos.

| Dispositivo | Dominio de colisión                           | Dominio de difusión                              |
|-------------|-----------------------------------------------|--------------------------------------------------|
| **Hub**     | **Extiende**: todos los puertos forman uno solo | **Extiende**: todos en el mismo                  |
| **Switch**  | **Limita**: cada puerto es un dominio distinto  | **Extiende**: uno solo (salvo que se usen VLANs) |
| **Router**  | **Limita**: cada interfaz es un dominio         | **Limita**: cada interfaz separa los broadcasts  |

---

## Actividad 2 – Subnetting: empresa con 8 departamentos *(2,00 pts)*

Red base: **192.168.200.0/24**. Se necesitan **8 subredes**.

### 1. Máscara por defecto *(0,40 pts)*

- Red clase C sin dividir: **`/24`** → **`255.255.255.0`**.

### 2. Máscara subneteada para ≥ 8 subredes *(0,40 pts)*

- Cálculo de bits prestados: `8 = 2³` → hacen falta **3 bits** prestados del campo de host.
- Nuevo prefijo: `24 + 3 = /27`.
- Máscara decimal: **`255.255.255.224`**.
- Hosts por subred: `2^(32−27) − 2 = 2⁵ − 2 = **30 hosts** utilizables.
- **Incremento** entre direcciones de red: `2⁵ = **32**` en el **cuarto octeto**.

### 3. Direcciones de red de la 1.ª, 2.ª, 5.ª y 8.ª subred *(0,40 pts)*

Fórmula: subred *k* → cuarto octeto = `(k − 1) × 32`.

| Subred | Cálculo          | Dirección de red       |
|--------|------------------|------------------------|
| 1.ª    | `(1−1) × 32 = 0` | **192.168.200.0/27**   |
| 2.ª    | `(2−1) × 32 = 32`| **192.168.200.32/27**  |
| 5.ª    | `(5−1) × 32 = 128`| **192.168.200.128/27**|
| 8.ª    | `(8−1) × 32 = 224`| **192.168.200.224/27**|

Listado completo de las 8 subredes (comprobación):

`192.168.200.0`, `.32`, `.64`, `.96`, `.128`, `.160`, `.192`, `.224` (todas `/27`).

### 4. Primera y última IP válida de la subred 5 *(0,40 pts)*

- Subred 5: **192.168.200.128/27** → cubre el cuarto octeto **128–159**.
- **Primera IP válida:** `192.168.200.128 + 1` = **192.168.200.129**.
- **Última IP válida:** broadcast − 1 = `192.168.200.159 − 1` = **192.168.200.158**.
- *(Broadcast de la subred 5: 192.168.200.159.)*

### 5. Broadcast de la subred 8 *(0,40 pts)*

- Subred 8: **192.168.200.224/27** → cubre el cuarto octeto **224–255**.
- **Broadcast:** **192.168.200.255** (última dirección del bloque).

---

## Actividad 3 – Subnetting: red 192.168.120.0/24 *(2,00 pts)*

### 1. Red, broadcast y hosts sin subdividir *(0,50 pts)*

- **Dirección de red:** **192.168.120.0**.
- **Dirección de broadcast:** **192.168.120.255**.
- **Hosts utilizables:** `2^(32−24) − 2 = 2⁸ − 2 = **254**`.

### 2. Cuatro subredes /26 *(0,50 pts)*

- De `/24` a `/26` se prestan **2 bits** → `2² = 4` subredes.
- **Incremento** en el cuarto octeto: `2^(8−2) = **64**`.

| Subred | Dirección de red          |
|--------|---------------------------|
| 1      | **192.168.120.0/26**      |
| 2      | **192.168.120.64/26**     |
| 3      | **192.168.120.128/26**    |
| 4      | **192.168.120.192/26**    |

Tabla completa de rangos (referencia):

| Subred /26            | Primera IP        | Última IP         | Broadcast         |
|-----------------------|-------------------|-------------------|-------------------|
| 192.168.120.0/26      | 192.168.120.1     | 192.168.120.62    | 192.168.120.63    |
| 192.168.120.64/26     | 192.168.120.65    | 192.168.120.126   | 192.168.120.127   |
| 192.168.120.128/26    | 192.168.120.129   | 192.168.120.190   | 192.168.120.191   |
| 192.168.120.192/26    | 192.168.120.193   | 192.168.120.254   | 192.168.120.255   |

### 3. Subred del host 192.168.120.175 *(0,50 pts)*

- Cuarto octeto `175` → buscar el bloque de 64 que lo contiene:
  - `175 ÷ 64 = 2` (parte entera) → `2 × 64 = 128`.
- El host pertenece a **192.168.120.128/26** (rango `.129 – .190`).

### 4. Primera y última IP válida de la subred con 192.168.120.45 *(0,50 pts)*

- Cuarto octeto `45` → `45 ÷ 64 = 0` → bloque que empieza en `0`.
- Subred: **192.168.120.0/26**.
- **Primera IP válida:** **192.168.120.1**.
- **Última IP válida:** **192.168.120.62** (broadcast `.63`).

---

## Actividad 4 – Supernetting: cuatro sedes *(2,00 pts)*

Sedes: **192.168.20.0/24**, **192.168.21.0/24**, **192.168.22.0/24**, **192.168.23.0/24**.

### 1. Octeto que cambia *(0,40 pts)*

- Solo varía el **tercer octeto** (20, 21, 22, 23).

### 2. Tercer octeto en binario *(0,40 pts)*

| Sede | Decimal (3.º octeto) | Binario (8 bits) |
|------|----------------------|------------------|
| A    | 20                   | `00010100`       |
| B    | 21                   | `00010101`       |
| C    | 22                   | `00010110`       |
| D    | 23                   | `00010111`       |

### 3. Bits iguales por la izquierda *(0,40 pts)*

Comparando los cuatro valores, coinciden los **6 primeros bits**: `000101`.

Los **2 bits de la derecha** (posiciones 7 y 8) cubren las cuatro combinaciones `00`, `01`, `10`, `11` → de 20 a 23.

### 4. Nueva máscara de la superred *(0,40 pts)*

- Bits de red en el tercer octeto: **6** → prefijo total: `16 + 6 = **/22**`.
- Máscara decimal: **`255.255.252.0`**.

### 5. Superred resultante y justificación *(0,40 pts)*

- **Superred:** **192.168.20.0/22**.
- **Rango total:** **192.168.20.0 – 192.168.23.255**.

**Justificación:** las cuatro redes son **contiguas** (20, 21, 22, 23) y están **alineadas** en un bloque `/22` (el tercer octeto `20` es múltiplo de 4: `20 ÷ 4 = 5`). Con **6 bits comunes** obtenemos el prefijo **más corto** (superred **mínima**) que engloba exactamente esas cuatro `/24` sin incluir redes adicionales fuera del bloque.

---

## Actividad 5 – VLANs en una oficina pequeña *(2,00 pts)*

### 1. Diseño de 2 VLANs *(0,75 pts)*

Ejemplo de tabla válida (los IDs pueden variar si son coherentes):

| ID VLAN | Nombre     | Equipos incluidos                          | Puertos asignados |
|---------|------------|--------------------------------------------|-------------------|
| 10      | Oficina    | 3 PCs, 1 impresora, 1 teléfono IP          | 1–6               |
| 20      | Invitados  | 1 punto de acceso Wi‑Fi                    | 7–12              |

**Razonamiento:** cada zona del enunciado se asigna a una VLAN distinta. Los puertos del switch se configuran en modo **access** y cada puerto pertenece a **una sola VLAN**, de modo que el tráfico de Oficina e Invitados queda **aislado en capa 2**.

### 2. ¿Qué es una VLAN y qué ventaja aporta la segmentación? *(0,50 pts)*

- Una **VLAN** (*Virtual LAN*) es una **red lógica** creada dentro de un switch: agrupa puertos (y los equipos conectados) como si estuvieran en una LAN independiente, **aunque compartan el mismo hardware**.
- **Ventaja de la segmentación lógica:** separa **dominios de difusión** sin necesidad de switches físicos distintos. Reduce el tráfico broadcast innecesario, mejora la **seguridad** (los invitados no ven por defecto los equipos de oficina) y facilita la **organización** de la red por zonas o departamentos.

### 3. ¿Funcionará el `ping` entre Oficina e Invitados sin otro dispositivo? *(0,75 pts)*

- **No funcionará** (al menos no de forma fiable entre subredes distintas; en la práctica, **no** si cada VLAN está en una subred IP diferente y no hay enrutamiento).
- **Justificación:** cada VLAN constituye un **dominio de difusión** separado. Un switch de capa 2 **no reenvía** tráfico entre VLANs: solo conmuta dentro de la misma VLAN. Si un PC de **Oficina** envía un `ping`, la trama ARP/broadcast y los frames dirigidos a otra VLAN **no llegan** al Wi‑Fi de **Invitados** porque están en la VLAN 20. Para comunicar dos VLANs hace falta un dispositivo de **capa 3** (router o switch multilayer) que realice **enrutamiento inter‑VLAN**.

---

*Vuelve a la [ficha de preparación](../ficha_preparacion_extraordinaria.md) para seguir practicando.*
