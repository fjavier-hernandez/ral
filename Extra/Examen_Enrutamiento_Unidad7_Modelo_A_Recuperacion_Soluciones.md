# Examen Unidad 7 – Modelo A (Recuperación) – Soluciones y Puntuaciones

---

## Modelo A Recuperación – Esquema de corrección (sobre 10)

> Referencia de enunciados: `Examen_Enrutamiento_Unidad7_Modelo_A_Recuperacion.md`  
> Los puntos indicados son **máximos**; se puede restar parcialmente según errores.

### Actividad 1 – Red 10.4.120.0 *(1,25 pts)*

- **1. Máscara para 8 subredes (0,25 pts)**  
  - Con 3 bits prestados (2^3 = 8) → /27 → 255.255.255.224.
- **2. Hosts utilizables por subred (0,25 pts)**  
  - 2^5 − 2 = **30 hosts** utilizables.
- **3. Direcciones de red de las 8 subredes (0,25 pts)**  
  - Salto de 32 en el 4.º octeto:  
    10.4.120.0, 10.4.120.32, 10.4.120.64, 10.4.120.96, 10.4.120.128, 10.4.120.160, 10.4.120.192, 10.4.120.224 (todas /27).
- **4. Nodo 5 en la subred 6 (0,25 pts)**  
  - Subred 6: 10.4.120.160/27 → host 5: **10.4.120.165**.
- **5. Subred del host 10.4.120.150 (0,25 pts)**  
  - 150 está entre 128 y 159 → pertenece a **10.4.120.128/27** (subred 5).

### Actividad 2 – Empresa con 8 redes *(1,25 pts)*

- **1. Máscara por defecto (0,25 pts)**  
  - 172.25.0.0 (clase B) → /16 → **255.255.0.0**.
- **2. Máscara para ≥ 8 subredes (0,25 pts)**  
  - 2^n ≥ 8 → n = 3 (2^3 = 8). Máscara: **/19 → 255.255.224.0**.
- **3. Dir. red 1.ª, 2.ª, 5.ª y 8.ª (0,25 pts)**  
  - Salto de 32 en el 3.er octeto:  
    - 1.ª: **172.25.0.0/19**  
    - 2.ª: **172.25.32.0/19**  
    - 5.ª: (4 × 32) → **172.25.128.0/19**  
    - 8.ª: (7 × 32) → **172.25.224.0/19**.
- **4. Rango IP válidas subred 5 (0,25 pts)**  
  - Red 172.25.128.0/19 → **172.25.128.1 – 172.25.159.254** (broadcast 172.25.159.255).
- **5. Broadcast subred 8 (0,25 pts)**  
  - Red 172.25.224.0/19 → broadcast **172.25.255.255**.

### Actividad 3 – Red 172.30.0.0/22 *(1,00 pt)*

- **1. Red, broadcast, hosts (0,25 pts)**  
  - Red: **172.30.0.0/22**  
  - Broadcast: **172.30.3.255**  
  - Hosts utilizables: 2^10 − 2 = **1022**.
- **2. 4 subredes /24 (0,25 pts)**  
  - 172.30.0.0/24, 172.30.1.0/24, 172.30.2.0/24, 172.30.3.0/24.
- **3. Subred de 172.30.2.200 (0,25 pts)**  
  - **172.30.2.0/24**.
- **4. Primera y última IP válida de la subred con 172.30.1.75 (0,25 pts)**  
  - Subred 172.30.1.0/24 → **172.30.1.1 – 172.30.1.254**.

### Actividad 4 – Cuatro sedes *(1,25 pts)*

- **1. Octeto que cambia (0,25 pts)**  
  - **Tercer octeto**.
- **2. Tercer octeto en binario (0,25 pts)**  
  - 40: 00101000, 41: 00101001, 42: 00101010, 43: 00101011.
- **3. Bits iguales (0,25 pts)**  
  - Los **6 primeros bits** coinciden (001010) → /22.
- **4. Máscara superred (0,25 pts)**  
  - **255.255.252.0 (/22)**.
- **5. Superred resultante (0,25 pts)**  
  - **192.168.40.0/22** (rango 192.168.40.0 – 192.168.43.255).

### Actividad 5 – Ocho departamentos *(1,00 pt)*

- **1. Octeto variable en binario (0,25 pts)**  
  - 64–71 → 01000000, 01000001, 01000010, 01000011, 01000100, 01000101, 01000110, 01000111.
- **2. Bits iguales (0,25 pts)**  
  - **5 bits comunes** (01000) → /21.
- **3. Máscara y prefijo (0,25 pts)**  
  - **255.255.248.0 (/21)**.
- **4. Superred y rango IP (0,25 pts)**  
  - Superred: **192.168.64.0/21**  
  - Rango: **192.168.64.0 – 192.168.71.255**.

### Actividad 6 – Tabla del Router2 (tres routers) *(1,00 pt)*

- **1. IP interfaces Router2 (0,25 pts)**  
  - Criterio (primer host disponible del segmento para el router):  
    - G0/0 LAN1 (192.168.30.0/24): **192.168.30.1**  
    - G0/0 LAN2 (192.168.40.0/24): **192.168.40.1** (mediante subinterfaz o segundo G0/0 según diseño)  
    - S0/0/0 enlace R1 (10.10.10.0/30): **10.10.10.2** (R1 usa 10.10.10.1)  
    - S0/0/1 enlace R3 (10.10.10.4/30): **10.10.10.5** (R3 usa 10.10.10.6).

- **2. Tabla de rutas del Router2 (0,50 pts)**  

| Red destino      | Máscara            | Siguiente salto | Interfaz | Tipo        |
|------------------|--------------------|-----------------|----------|-------------|
| 192.168.30.0     | 255.255.255.0 /24  | —               | G0/0     | Directa     |
| 192.168.40.0     | 255.255.255.0 /24  | —               | G0/0     | Directa     |
| 10.10.10.0       | 255.255.255.252 /30 | —              | S0/0/0   | Directa     |
| 10.10.10.4       | 255.255.255.252 /30 | —              | S0/0/1   | Directa     |
| 172.20.80.0      | 255.255.255.0 /24  | 10.10.10.6      | S0/0/1   | Estática    |
| 0.0.0.0 (default)| 0.0.0.0 /0         | 10.10.10.1      | S0/0/0   | Por defecto |

- **3. Justificación directa / siguiente salto (0,25 pts)**  
  - **Directas:** 192.168.30.0/24, 192.168.40.0/24, 10.10.10.0/30 y 10.10.10.4/30, porque están conectadas físicamente a interfaces de R2.  
  - **Siguiente salto:** 172.20.80.0/24 (LAN de R3, alcanzable vía 10.10.10.6) y 0.0.0.0/0 (Internet, alcanzable vía 10.10.10.1 en R1).

### Actividad 7 – Dos routers *(0,75 pts)*

- **1. IP interfaces (0,25 pts)**  
  - R1 G0/1: **10.50.1.1/24**  
  - R1 G0/2: **172.16.250.1/30**  
  - R2 G0/0: **172.16.250.2/30**  
  - R2 G0/1: **10.50.2.1/24**.

- **2. Tabla de rutas del Router2 (0,25 pts)**  

| Red destino | Máscara              | Siguiente salto | Interfaz | Tipo        |
|-------------|----------------------|-----------------|----------|-------------|
| 10.50.2.0   | 255.255.255.0 /24    | —               | G0/1     | Directa     |
| 172.16.250.0| 255.255.255.252 /30  | —               | G0/0     | Directa     |
| 10.50.1.0   | 255.255.255.0 /24    | 172.16.250.1    | G0/0     | Estática    |
| 0.0.0.0     | 0.0.0.0 /0           | 172.16.250.1    | G0/0     | Por defecto |

- **3. Siguiente salto 10.50.1.0 y 0.0.0.0/0 (0,25 pts)**  
  - En ambos casos: **172.16.250.1** (IP del Router1 en el enlace), pues Router1 es el único vecino que conduce a las redes externas.

### Actividad 8 – Taller mecánico *(0,75 pts)*

- **1. Cuadro de planificación (0,25 pts)**  

| VLAN ID | Nombre       | Subred             | Rango IP válidas         | Puertos |
|---------|--------------|--------------------|--------------------------|---------|
| 10      | Oficina      | 192.168.70.0/27    | 192.168.70.1–30          | 1–5     |
| 20      | Diagnóstico  | 192.168.70.32/27   | 192.168.70.33–62         | 6–15    |
| 30      | Clientes     | 192.168.70.64/27   | 192.168.70.65–94         | 20–24   |

- **2. Cuestionario (0,25 pts)**  
  - Wi‑Fi de clientes debe aislarse por **seguridad** (equipos no gestionados), **segmentación** y para evitar broadcasts y accesos a recursos internos del taller.  
  - Ping entre VLANs **no funciona sin router ni switch capa 3**: las VLANs separan dominios de broadcast y capa 2; se necesita enrutamiento inter‑VLAN para pasar entre subredes.
- **3. Esquema de switch (0,25 pts)**  
  - Puertos 1–5 → VLAN 10 Oficina; 6–15 → VLAN 20 Diagnóstico; 20–24 → VLAN 30 Clientes.

### Actividad 9 – Hospital *(0,75 pts)*

- **1. 3 VLANs ID, nombre, subred, puertos (0,25 pts)**  

| VLAN ID | Nombre           | Subred             | Puertos |
|---------|------------------|--------------------|---------|
| 10      | Médicos          | 10.80.10.0/26      | 1–10    |
| 20      | Enfermería       | 10.80.20.0/26      | 11–30   |
| 30      | WiFi_Pacientes   | 10.80.30.0/27      | 45–46   |

- **2. Dispositivo para comunicar Médicos y Enfermería (0,25 pts)**  
  - **Router o switch capa 3** (enrutamiento inter‑VLAN / SVIs), porque cada VLAN está en una subred distinta y requiere pasar de capa 2 a capa 3.
- **3. Esquema de switch (0,25 pts)**  
  - Diagrama coherente con puertos 1–10 en VLAN 10, 11–30 en VLAN 20, 45–46 en VLAN 30.

### Actividad 10 – Subnetting y tabla de rutas *(1,00 pt)*

- **1. Máscara y 4 subredes /26 (0,25 pts)**  
  - Máscara: **/26 → 255.255.255.192**.  

| Subred | Dirección de red    | Rango válido                   | Broadcast          |
|--------|---------------------|--------------------------------|--------------------|
| S1     | 10.100.100.0/26     | 10.100.100.1 – 10.100.100.62   | 10.100.100.63      |
| S2     | 10.100.100.64/26    | 10.100.100.65 – 10.100.100.126 | 10.100.100.127     |
| S3     | 10.100.100.128/26   | 10.100.100.129 – 10.100.100.190| 10.100.100.191     |
| S4     | 10.100.100.192/26   | 10.100.100.193 – 10.100.100.254| 10.100.100.255     |

- **2. IP interfaces + 4 rutas directas (0,50 pts)**  
  - IP del router (primera válida): **10.100.100.1, 10.100.100.65, 10.100.100.129, 10.100.100.193**.  

| Red destino      | Máscara              | Interfaz | Tipo    |
|------------------|----------------------|----------|---------|
| 10.100.100.0     | 255.255.255.192 /26  | G0/0     | Directa |
| 10.100.100.64    | 255.255.255.192 /26  | G0/1     | Directa |
| 10.100.100.128   | 255.255.255.192 /26  | G0/2     | Directa |
| 10.100.100.192   | 255.255.255.192 /26  | G0/3     | Directa |

- **3. Esquema router + 4 subredes (0,25 pts)**  
  - Diagrama con el router central y las 4 subredes colgando de G0/0, G0/1, G0/2 y G0/3 con sus direcciones de red /26.

---

Este archivo sirve como guía rápida de corrección con **soluciones numéricas clave** y **puntos máximos por apartado**, manteniendo la escala total de **10 puntos**.
