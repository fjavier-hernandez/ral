# Examen Extraordinaria – Soluciones y Puntuaciones

!!! warning "Documento interno – no publicar"
    Archivo de uso exclusivo del profesorado. No debe estar accesible al alumnado ni enlazado en la navegación.

---

## Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Extraordinaria.docx`  
> Los puntos indicados son **máximos**; se puede restar parcialmente según errores.

### Actividad 1 – Preguntas de desarrollo *(2,00 pts)*

- **1. Funciones principales de la capa de enlace de datos (OSI) (0,50 pts)**  
  Cuatro funciones (basta con cuatro):
  - **Entramado (framing):** delimita el flujo de bits en tramas, marcando inicio y fin de cada una.
  - **Direccionamiento físico (MAC):** identifica origen y destino dentro del mismo enlace mediante direcciones MAC.
  - **Control de acceso al medio (MAC):** regula quién transmite y cuándo para evitar/gestionar colisiones (p. ej. CSMA/CD en Ethernet clásica).
  - **Detección y control de errores:** mediante el campo FCS/CRC se detectan tramas dañadas y se descartan.
  - *(Adicional)* **Control de flujo:** evita que un emisor rápido sature a un receptor lento.

- **2. IP públicas vs privadas y rangos RFC 1918 (0,50 pts)**  
  - **Públicas:** únicas a nivel mundial, **enrutables en Internet**, asignadas por IANA/RIR a través del ISP.
  - **Privadas:** de uso interno en una LAN, **no se enrutan en Internet**; para salir necesitan traducción **NAT/PAT**.
  - **Tres rangos privados (RFC 1918):**

  | Clase | Rango                         | Prefijo CIDR     |
  |-------|-------------------------------|------------------|
  | A     | 10.0.0.0 – 10.255.255.255     | `10.0.0.0/8`     |
  | B     | 172.16.0.0 – 172.31.255.255   | `172.16.0.0/12`  |
  | C     | 192.168.0.0 – 192.168.255.255 | `192.168.0.0/16` |

- **3. DHCP, parámetros, ventajas y comprobaciones (0,50 pts)**  
  - **Qué es:** *Dynamic Host Configuration Protocol*; asigna **automáticamente** la configuración de red a los clientes al conectarse (proceso DORA: Discover, Offer, Request, Ack).
  - **Parámetros que asigna:** **dirección IP**, **máscara de subred**, **puerta de enlace (gateway)** y **servidor(es) DNS** (además del tiempo de concesión o *lease*).
  - **Ventajas frente a la configuración manual:** evita errores de tecleo, impide **direcciones IP duplicadas**, centraliza y agiliza la gestión, y facilita la movilidad de equipos.
  - **Tres comprobaciones básicas (con `ping`):**
    - `ping 127.0.0.1` (loopback): verifica que la **pila TCP/IP local** del equipo funciona.
    - `ping <IP propia>`: verifica que la **tarjeta de red está bien configurada** con su IP.
    - `ping <gateway>`: verifica la **conectividad con el router** dentro de la LAN.
    - *(Adicional)* `ping 8.8.8.8` o `ping <web>`: verifica la **salida a Internet** y, si se hace por nombre, también la **resolución DNS**.

- **4. Dominio de colisión y dominio de difusión (0,50 pts)**  
  - **Dominio de colisión:** conjunto de dispositivos que comparten el mismo medio y cuyas transmisiones pueden **colisionar** entre sí.
  - **Dominio de difusión (broadcast):** conjunto de dispositivos que **reciben los mensajes de difusión** enviados por cualquiera de ellos.

  | Dispositivo | Dominio de colisión                           | Dominio de difusión                              |
  |-------------|-----------------------------------------------|--------------------------------------------------|
  | **Hub**     | **Extiende**: todos los puertos forman uno solo | **Extiende**: todos en el mismo                  |
  | **Switch**  | **Limita**: cada puerto es un dominio distinto  | **Extiende**: uno solo (salvo que se usen VLANs) |
  | **Router**  | **Limita**: cada interfaz es un dominio         | **Limita**: cada interfaz separa los broadcasts  |

### Actividad 2 – Subnetting: centro con 8 aulas *(2,00 pts)*

Red base: **192.168.150.0/24**. Se necesitan **8 subredes**.

- **1. Máscara por defecto (0,40 pts)**  
  - Red clase C sin dividir: **`/24`** ⇒ **`255.255.255.0`**.

- **2. Máscara subneteada para ≥ 8 subredes (0,40 pts)**  
  - Cálculo: `8 = 2³` → se prestan **3 bits** del campo de host.
  - Nuevo prefijo: `24 + 3 = /27` ⇒ **`255.255.255.224`**.
  - Hosts por subred: `2^(32−27) − 2 = 2⁵ − 2 = **30**` hosts utilizables.
  - **Incremento** en el cuarto octeto: `2⁵ = **32**`.

- **3. Direcciones de red 1.ª, 2.ª, 5.ª y 8.ª (0,40 pts)**  
  - Fórmula: subred *k* → cuarto octeto = `(k − 1) × 32`.

  | Subred | Cálculo           | Dirección de red        |
  |--------|-------------------|-------------------------|
  | 1.ª    | `(1−1) × 32 = 0`  | **192.168.150.0/27**    |
  | 2.ª    | `(2−1) × 32 = 32` | **192.168.150.32/27**   |
  | 5.ª    | `(5−1) × 32 = 128`| **192.168.150.128/27**  |
  | 8.ª    | `(8−1) × 32 = 224`| **192.168.150.224/27**  |

- **4. Primera y última IP válida de la subred 5 (0,40 pts)**  
  - Subred `192.168.150.128/27` cubre el cuarto octeto **128–159**.
  - **Primera IP:** **192.168.150.129** · **Última IP:** **192.168.150.158** (broadcast `192.168.150.159`).

- **5. Broadcast de la subred 8 (0,40 pts)**  
  - Subred `192.168.150.224/27` cubre el cuarto octeto **224–255**.
  - **Broadcast:** **192.168.150.255**.

### Actividad 3 – Subnetting: red 192.168.88.0/24 *(2,00 pts)*

- **1. Red, broadcast y hosts sin subdividir (0,50 pts)**  
  - **Dirección de red:** **192.168.88.0**  
  - **Broadcast:** **192.168.88.255**  
  - **Hosts utilizables:** `2⁸ − 2 = **254**`.

- **2. Cuatro subredes /26 (0,50 pts)**  
  - De `/24` a `/26` se prestan **2 bits** → `2² = 4` subredes.
  - **Incremento** en el cuarto octeto: `2^(8−2) = **64**`.
  - Direcciones de red: **192.168.88.0/26**, **192.168.88.64/26**, **192.168.88.128/26**, **192.168.88.192/26**.

- **3. Subred del host 192.168.88.190 (0,50 pts)**  
  - Cuarto octeto `190` → `190 ÷ 64 = 2` (entero) → `2 × 64 = 128`.
  - Pertenece a **192.168.88.128/26** (rango `.129 – .190`, broadcast `.191`).

- **4. Primera y última IP válida de la subred con 192.168.88.72 (0,50 pts)**  
  - Cuarto octeto `72` → `72 ÷ 64 = 1` → bloque que empieza en `64`.
  - Subred: **192.168.88.64/26**.
  - **Primera IP:** **192.168.88.65** · **Última IP:** **192.168.88.126** (broadcast `192.168.88.127`).

### Actividad 4 – Supernetting: cuatro delegaciones *(2,00 pts)*

Delegaciones: **192.168.96.0/24**, **192.168.97.0/24**, **192.168.98.0/24**, **192.168.99.0/24**.

- **1. Octeto que cambia (0,40 pts)**  
  - Solo varía el **tercer octeto** (96, 97, 98, 99).

- **2. Tercer octeto en binario (0,40 pts)**  

  | Delegación | Decimal (3.º octeto) | Binario (8 bits) |
  |------------|----------------------|------------------|
  | Norte      | 96                   | `01100000`       |
  | Centro     | 97                   | `01100001`       |
  | Sur        | 98                   | `01100010`       |
  | Este       | 99                   | `01100011`       |

- **3. Bits iguales por la izquierda (0,40 pts)**  
  - Coinciden los **6 primeros bits**: `011000`.

- **4. Nueva máscara de la superred (0,40 pts)**  
  - Prefijo total: `16 + 6 = **/22**` ⇒ **`255.255.252.0`**.

- **5. Superred resultante y justificación (0,40 pts)**  
  - **Superred:** **192.168.96.0/22** (rango `192.168.96.0 – 192.168.99.255`).
  - **Justificación:** las cuatro redes son **contiguas** y están **alineadas** en un bloque `/22` (el tercer octeto `96` es múltiplo de 4: `96 ÷ 4 = 24`). Con **6 bits comunes** se obtiene la superred **mínima** que engloba exactamente esas cuatro `/24`.

### Actividad 5 – VLANs en un taller mecánico *(2,00 pts)*

- **1. Diseño de 2 VLANs (0,75 pts)**  

  | ID VLAN | Nombre          | Equipos incluidos                            | Puertos asignados |
  |---------|-----------------|----------------------------------------------|-------------------|
  | 30      | Taller          | 4 PCs, 1 impresora de etiquetas, 1 escáner   | 1–6               |
  | 40      | WiFi_Clientes   | 1 punto de acceso Wi‑Fi                      | 7–12              |

  - Cada zona del enunciado se asigna a una VLAN distinta; los puertos del switch se configuran en modo **access** (un puerto = una VLAN).

- **2. ¿Qué es una VLAN y ventaja de la segmentación? (0,50 pts)**  
  - Una **VLAN** es una **red lógica** dentro de un switch que agrupa puertos como si formaran una LAN independiente.
  - **Ventaja:** separa **dominios de difusión**, reduce broadcasts innecesarios, mejora la **seguridad** (los clientes en WiFi no acceden por defecto a los equipos del taller) y organiza la red por zonas.

- **3. ¿Funcionará el `ping` entre Taller y WiFi_Clientes? (0,75 pts)**  
  - **No funcionará** sin un dispositivo de capa 3 adicional.
  - **Justificación:** cada VLAN forma un **dominio de difusión** separado. Un switch de capa 2 **no reenvía** tráfico entre VLANs distintas. El `ping` del PC del **Taller** no alcanzará dispositivos en **WiFi_Clientes** porque están en la VLAN 40; hace falta un **router** o **switch multilayer** para enrutamiento inter‑VLAN.

---

Este archivo sirve como guía rápida de corrección con **soluciones numéricas clave** y **puntos máximos por apartado**, manteniendo la escala total de **10 puntos**.
