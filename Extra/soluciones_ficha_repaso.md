# Soluciones – Ficha de repaso Examen Capa de Enlace y Capa de Red

**Documento para el profesor.** Soluciones detalladas de las actividades de la ficha de repaso, explicadas para alumnado de SMR.

---

## PARTE 3: Ejercicios de práctica – Soluciones

### Capa de Enlace

**1.** Trama con 64 bytes de datos útiles. ¿Tamaño total?

**Solución:**  
Con 64 bytes de datos, el campo Datos+Relleno tiene 64 bytes (como 64 ≥ 46, no hace falta relleno).  
Sumamos todos los campos:  
`7 + 1 + 6 + 6 + 2 + 64 + 4 = 90 bytes`

**Respuesta: 90 bytes**

---

**2.** Trama con 1200 bytes de datos. ¿Tamaño total?

**Solución:**  
Campos fijos: Preámbulo (7) + SDF (1) + MAC destino (6) + MAC origen (6) + Longitud/Tipo (2) + FCS (4) = 26 bytes.  
Datos: 1200 bytes.  
`Total = 26 + 1200 = 1226 bytes`

**Respuesta: 1226 bytes**

---

**3.** Trama mínima 64 bytes, cabecera (MAC destino hasta FCS) 26 bytes. ¿Tamaño mínimo de Datos+Relleno?

**Solución:**  
En este enunciado se llama “cabecera” a Preámbulo + SDF + MAC + Long/Tipo + FCS = 26 bytes.  
La trama mínima total es 64 bytes (desde MAC destino hasta FCS) o 72 bytes si se incluye Preámbulo y SDF.  
Si “cabecera” = 26 bytes y “trama mínima” = 64 (solo la parte útil), entonces:  
`Datos+Relleno = 64 − (6+6+2+4) = 64 − 18 = 46 bytes`  
Si “cabecera” = 26 incluye Preámbulo+SDF:  
`Datos+Relleno = 64 − 26` no vale porque 64 se refiere a la parte sin Preámbulo.  
La interpretación estándar: cabecera útil (MAC a FCS) = 18 bytes → **Datos+Relleno mínimo = 46 bytes**.

**Respuesta: 46 bytes**

---

**4.** 100 tramas de 1518 bytes. ¿Cuántos bytes en total?

**Solución:**  
`100 × 1518 = 151 800 bytes`

**Respuesta: 151 800 bytes**

---

**5.** FCS = 4 bytes. ¿Cuántos bits? Si el CRC detecta error, ¿qué hace el receptor?

**Solución:**  
`4 bytes × 8 bits/byte = 32 bits`  
Si el CRC detecta un error, el receptor **descarta la trama** y no la procesa. La retransmisión, si la hay, la gestiona un protocolo de capa superior (por ejemplo, TCP).

**Respuesta: 32 bits. El receptor descarta la trama.**

---

### Capa de Red

**6.** IP 192.168.5.100, máscara 255.255.255.0. Calcula: red, broadcast, primera y última IP válida, número de hosts.

**Solución:**  
Máscara /24 → los 3 primeros octetos son red, el último es host.

- **Dirección de red:** 192.168.5.0 (último octeto en 0)
- **Broadcast:** 192.168.5.255 (último octeto en 255)
- **Primera IP válida:** 192.168.5.1
- **Última IP válida:** 192.168.5.254
- **Número de hosts:** 2⁸ − 2 = 254

---

**7.** IP 172.16.50.25, máscara 255.255.0.0. Calcula: red, broadcast, hosts disponibles.

**Solución:**  
Máscara /16 → los 2 primeros octetos son red.

- **Dirección de red:** 172.16.0.0
- **Broadcast:** 172.16.255.255
- **Hosts:** 2¹⁶ − 2 = 65 534

---

**8.** IP 192.168.10.75/26. Calcula: máscara, red, broadcast, hosts.

**Solución:**  
/26 → 26 bits de red, 6 bits de host. Incremento = 2⁶ = 64.

- **Máscara:** 255.255.255.192
- Último octeto 75: 75 ÷ 64 = 1,… → red en 64
- **Dirección de red:** 192.168.10.64
- **Broadcast:** 192.168.10.64 + 64 − 1 = 192.168.10.127
- **Hosts:** 2⁶ − 2 = 62

---

**9.** Indica cuáles son inválidas y por qué: 192.168.1.1, 256.10.10.10, 192.168.1.255, 10.0.0.300, 172.16.0.1.

**Solución:**  
Cada octeto debe estar entre 0 y 255.

- **192.168.1.1** → Válida
- **256.10.10.10** → Inválida (256 > 255)
- **192.168.1.255** → Válida (puede ser broadcast en /24)
- **10.0.0.300** → Inválida (300 > 255)
- **172.16.0.1** → Válida

---

**10.** Red 192.168.1.0/24, router 192.168.1.1. ¿Hay sitio para 30 PCs y 2 impresoras? Ejemplo de configuración del primer PC. ¿Última IP válida?

**Solución:**  
/24 → 254 hosts válidos. Se necesitan 30 + 2 = 32. 32 < 254 → sí hay suficientes.

**Ejemplo primer PC:**  
- IP: 192.168.1.2  
- Máscara: 255.255.255.0  
- Puerta de enlace: 192.168.1.1  

**Última IP válida:** 192.168.1.254

---

## PARTE 4: Actividades de desarrollo – Soluciones modelo

### Actividad 1 – Funciones de la capa de enlace

**Respuesta modelo:**  
Formación de tramas, direccionamiento (MAC), detección de errores (CRC), control de flujo, control de acceso al medio (CSMA/CD), segmentación y agrupación.

---

### Actividad 2 – Subcapas LLC y MAC

**Respuesta modelo:**  
LLC: norma IEEE 802.2, interfaz uniforme para la capa de red y gestión de errores.  
MAC: norma IEEE 802.3, acceso al medio compartido, empaquetado en tramas y CSMA/CD.

---

### Actividad 3 – Campos de la trama

**Respuesta modelo:**  
Esquema: Preámbulo (7) | SDF (1) | MAC destino (6) | MAC origen (6) | Longitud/Tipo (2) | Datos+Relleno (46–1500) | FCS (4).  
Trama mínima: 64 bytes (solo parte útil) o 72 bytes (con Preámbulo y SDF). Trama máxima: 1518 bytes (estándar) o 1526 (con Preámbulo y SDF).

---

### Actividad 4 – CSMA/CD

**Respuesta modelo:**  
1) Detección de portadora, 2) Acceso múltiple, 3) Detección de colisiones, 4) Backoff.  
Los switches dan un dominio de colisión por puerto y permiten full-duplex, por lo que no hay colisiones.

---

### Actividad 5 – Dominios

**Respuesta modelo:**  
Dominio de colisión: dispositivos cuyas tramas pueden colisionar. Hub lo extiende; switch limita (1 por puerto); router lo limita.  
Dominio de difusión: dispositivos que reciben broadcast. Hub y switch lo extienden; router lo limita.

---

### Actividad 6 – IP pública y privada

**Respuesta modelo:**  
Rangos privados: 10.0.0.0/8, 172.16.0.0–172.31.255.255, 192.168.0.0/16.  
- 8.8.8.8: pública  
- 192.168.1.1: privada  
- 10.0.0.1: privada  
- 172.16.5.10: privada  

---

### Actividad 7 – Máscara de red

**Solución:**  
192.168.1.100 y 192.168.1.50: misma red (192.168.1.0).  
192.168.2.10 está en 192.168.2.0.  
Con máscara 255.255.255.0, 192.168.1.50 y 192.168.2.10 están en redes distintas.

---

### Actividad 8 – Proceso ARP

**Orden correcto:**  
1) El host envía ARP Request por broadcast.  
2) Recibe ARP Reply del destinatario.  
3) Guarda IP-MAC en la tabla ARP.  
4) Envía la trama con la MAC correcta.

---

### Actividad 9 – ICMP

**Respuesta modelo:**  
`ping` comprueba conectividad (Echo Request/Reply). Ejemplo: `ping 8.8.8.8`  
`traceroute` muestra la ruta (tracert en Windows). Ejemplo: `traceroute www.google.com` o `tracert www.google.com`

---

### Actividad 10 – DHCP

**Respuesta modelo:**  
Parámetros: IP, máscara, puerta de enlace, DNS.  
Ventajas: administración sencilla, menos conflictos, reutilización de IPs.  
Comprobaciones: ping 127.0.0.1 (stack TCP/IP), ping IP_local (interfaz), ping gateway (router), ping 8.8.8.8 (Internet), ping www.google.com (DNS).

---

## Actividades prácticas (comandos) – Guía de corrección

### P1 – Comprobaciones con ping

**Qué revisar:**  
Que ejecuten los pings en orden y anoten si hay respuesta. Si falta alguno (p. ej. gateway o DNS), indicar qué está fallando (configuración, router, ISP, DNS).

---

### P2 – Consultar configuración

**Qué revisar:**  
Que aparezcan IP, máscara, puerta de enlace y DNS. En Windows: `ipconfig` o `ipconfig /all`. En Linux: `ip addr` o `ifconfig`.

---

### P3 – Tabla ARP

**Qué revisar:**  
Que identifiquen IP, MAC y tipo (dinámico/estático). Columnas típicas: dirección IP, dirección física (MAC), tipo.

---

### P4 – Tabla de rutas

**Qué revisar:**  
Que localicen la ruta 0.0.0.0/0 y la puerta de enlace asociada.

---

### P5 – Validar direcciones IP

**Solución:**  
- 192.168.1.1 → Válida  
- 256.1.1.1 → Inválida (256 > 255)  
- 10.0.0.300 → Inválida (300 > 255)  
- 172.16.0.0 → Válida (puede ser dirección de red)  
- 192.168.1.256 → Inválida (256 > 255)  
- 127.0.0.1 → Válida (loopback)  

---

## Actividades prácticas de cálculo – Tramas Ethernet

**C1.** 80 bytes de datos → `26 + 80 = 106 bytes`

**C2.** 500 bytes de datos → `26 + 500 = 526 bytes`

**C3.** Cabecera (MAC destino hasta FCS) = 6+6+2+4 = 18 bytes. Trama mínima 64 bytes solo de esa parte:  
`Datos+Relleno = 64 − 18 = 46 bytes`  
(Nota: si el enunciado dice “cabecera 26 bytes”, suele referirse a Preámbulo+SDF+MAC+Long/Tipo+FCS; entonces la parte útil mínima es 64 y Datos+Relleno = 64 − (6+6+2+4) = 46.)

**C4.** `50 × 1518 = 75 900 bytes`

**C5.** 4 bytes = 32 bits. Si hay error CRC, el receptor descarta la trama.

---

## Actividades prácticas de cálculo – Direcciones IP

**C6.** 192.168.3.150 /24  
- Red: 192.168.3.0  
- Broadcast: 192.168.3.255  
- Primera IP: 192.168.3.1  
- Última IP: 192.168.3.254  
- Hosts: 254  

**C7.** 10.20.100.50 /8  
- Red: 10.0.0.0  
- Broadcast: 10.255.255.255  
- Hosts: 2²⁴ − 2 = 16 777 214  

**C8.** 172.16.25.100 /26  
- Máscara: 255.255.255.192  
- Incremento: 64. Último octeto 100 → 64 ≤ 100 < 128 → red en .64  
- Red: 172.16.25.64  
- Broadcast: 172.16.25.127  
- Hosts: 62  

**C9.** 192.168.0.200 /25  
- Máscara: 255.255.255.128  
- Incremento: 128. 200 ≥ 128 → red en .128  
- Red: 192.168.0.128  
- Broadcast: 192.168.0.255  
- Hosts: 2⁷ − 2 = 126  

**C10.** Red 192.168.10.0/24  
- Hosts válidos: 254  
- Necesarios: 40 + 3 = 43 → sí hay suficientes  
- Ejemplo primer PC: IP 192.168.10.2, máscara 255.255.255.0, puerta 192.168.10.1  
- Última IP válida: 192.168.10.254  
