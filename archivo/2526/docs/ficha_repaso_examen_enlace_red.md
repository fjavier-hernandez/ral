---
title: Ficha de repaso - Examen Capa de Enlace y Capa de Red
description: Resumen y preparación para el examen de Capa de Enlace y Capa de Red (SMR).
---

# :material-book-open-variant: Ficha de repaso para el examen

**Temas:** Capa de Enlace de Datos y Capa de Red  
**Módulo:** Redes de Área Local (RAL)  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

Esta ficha te ayuda a preparar el examen. Incluye: resumen de conceptos, fórmulas, ejercicios de cálculo y **actividades para practicar en clase** (desarrollo teórico, comandos prácticos y cálculos).

---

## PARTE 1: Conceptos para preguntas de desarrollo

### Capa de Enlace de Datos

#### 1. Funciones principales de la capa de enlace

| Función | Descripción |
|---------|-------------|
| **Formación de tramas** | Organizar bits en bloques (tramas) con cabeceras y colas |
| **Direccionamiento** | Añadir direcciones MAC (origen y destino) |
| **Detección de errores** | CRC en el campo FCS para detectar errores de transmisión |
| **Control de flujo** | Adecuar el flujo entre emisor y receptor |
| **Control de acceso al medio** | CSMA/CD cuando varios equipos comparten el medio |
| **Segmentación y agrupación** | Dividir datos grandes o agrupar datos pequeños |

#### 2. Subcapas LLC y MAC

| Subcapa | Norma | Función principal |
|---------|-------|-------------------|
| **LLC** (Logical Link Control) | IEEE 802.2 | Interfaz uniforme para la capa de red; gestión de errores y control de flujo lógico |
| **MAC** (Medium Access Control) | IEEE 802.3 (Ethernet) | Arbitrar el uso del medio compartido; empaquetar datos en tramas; CSMA/CD |

#### 3. Campos de la trama Ethernet IEEE 802.3

| Campo | Tamaño | Función |
|-------|--------|---------|
| Preámbulo | 7 bytes | Sincronización (10101010 repetido) |
| SDF (Start Frame Delimiter) | 1 byte | Delimitador de inicio (10101011) |
| MAC destino | 6 bytes | Dirección del receptor |
| MAC origen | 6 bytes | Dirección del emisor |
| Longitud/Tipo | 2 bytes | Longitud de datos o tipo de protocolo (0x0800 = IP) |
| Datos + Relleno | 46–1500 bytes | Mínimo 46 (relleno si hace falta), máximo 1500 |
| FCS (Frame Check Sequence) | 4 bytes | CRC-32 para detección de errores |

**Trama mínima:** 64 bytes (cabecera + datos). **Trama máxima:** 1518 bytes (1500 datos + 18 cabecera).

#### 4. Protocolo CSMA/CD – 4 pasos

1. **Carrier Sense (detección de portadora):** Escuchar si hay señal en el medio antes de transmitir.
2. **Multiple Access (acceso múltiple):** Si el medio está libre, transmitir.
3. **Collision Detection (detección de colisiones):** Si se detecta colisión, detener la transmisión.
4. **Backoff:** Esperar un tiempo aleatorio antes de reintentar.

**Switches:** Crean un dominio de colisión por puerto (comunicación full-duplex), por lo que eliminan las colisiones.

#### 5. Dominios de colisión y difusión

| Concepto | Definición | Hub | Switch | Router |
|----------|------------|-----|--------|--------|
| **Dominio de colisión** | Dispositivos cuyas tramas pueden colisionar | Extiende | 1 por puerto | Limita |
| **Dominio de difusión** | Dispositivos que reciben broadcast | Extiende | Extiende | Limita |

---

### Capa de Red

#### 6. IP públicas vs. privadas

| Tipo | Visibilidad | Rangos privados (RFC 1918) |
|------|-------------|----------------------------|
| **Pública** | Visible en Internet; única globalmente | — |
| **Privada** | Solo en redes locales; no enrutable en Internet | 10.0.0.0/8, 172.16.0.0–172.31.255.255, 192.168.0.0/16 |

#### 7. Máscara de red

- **Función:** Separar parte de red y parte de host en una IP.
- **Bits en 1:** red. **Bits en 0:** host.
- **Misma red:** Si (IP1 AND máscara) = (IP2 AND máscara) → misma red.

#### 8. Proceso ARP (misma red)

1. El host necesita la MAC de una IP conocida.
2. Envía **ARP Request** por broadcast (MAC destino FF:FF:FF:FF:FF:FF).
3. Solo el host con esa IP responde con **ARP Reply** en unicast.
4. El solicitante guarda IP→MAC en su tabla ARP.
5. Envía la trama con la MAC destino correcta.

#### 9. Protocolo ICMP

- **Función:** Mensajes de control y error en redes IP.
- **Herramientas:** `ping` (Echo Request/Reply, comprobar conectividad), `traceroute`/`tracert` (ruta y saltos).

#### 10. DHCP y comprobaciones básicas

**DHCP (Dynamic Host Configuration Protocol):** Protocolo que asigna automáticamente los parámetros de red a los clientes.

**Parámetros que asigna:** Dirección IP, máscara de red, puerta de enlace, servidores DNS.

**Ventajas frente a configuración manual:** Facilita la administración, evita conflictos de IP, permite reutilizar direcciones cuando los clientes se desconectan.

**Comprobaciones básicas (orden recomendado):**

| Comprobación | Comando ejemplo | Qué verifica |
|--------------|-----------------|--------------|
| Stack TCP/IP | `ping 127.0.0.1` | Que el protocolo funciona en el equipo |
| Interfaz de red | `ping IP_local` | Que la tarjeta de red responde |
| Puerta de enlace | `ping 192.168.1.1` | Conectividad con el router |
| Internet | `ping 8.8.8.8` | Conectividad con redes externas |
| DNS | `ping www.google.com` | Resolución de nombres a IP |

---

## PARTE 2: Fórmulas y trucos para ejercicios de cálculo

### Capa de Enlace – Tramas Ethernet

**Tamaños fijos de cada campo (en bytes):**

| Campo | Bytes |
|-------|-------|
| Preámbulo | 7 |
| SDF | 1 |
| MAC destino | 6 |
| MAC origen | 6 |
| Longitud/Tipo | 2 |
| Datos + Relleno | 46 a 1500 (variable) |
| FCS | 4 |

#### **Cálculo del tamaño total de la trama**

El tamaño total de la trama es la suma de todos los campos. El único que cambia es **Datos+Relleno**; el resto tiene tamaño fijo.

**Paso 1 – Sumar los campos fijos**

Todo lo que no es Datos+Relleno tiene un tamaño fijo:

- Preámbulo (7) + SDF (1) + MAC destino (6) + MAC origen (6) + Longitud/Tipo (2) + FCS (4)  
- **Total campos fijos = 7 + 1 + 6 + 6 + 2 + 4 = 26 bytes**

**Paso 2 – Calcular el tamaño de Datos+Relleno**

- Si los **datos útiles** que enviamos son **menos de 46 bytes**, hay que añadir **relleno** hasta llegar a 46 (el mínimo que exige Ethernet).
- Si los datos son **46 bytes o más**, no se añade relleno: el campo Datos+Relleno es exactamente el tamaño de los datos.
- El máximo de Datos+Relleno es **1500 bytes**.

**Paso 3 – Aplicar la fórmula**

`Tamaño total de la trama = 26 + (tamaño del campo Datos+Relleno)`

**Paso 4 – Ejemplos**

| Caso | Datos útiles | Datos+Relleno | Cálculo | Total |
|------|--------------|---------------|---------|--------|
| Trama mínima | &lt; 46 bytes | 46 (con relleno) | 26 + 46 | **72 bytes** |
| Ejemplo medio | 1200 bytes | 1200 | 26 + 1200 | **1226 bytes** |
| Trama máxima | 1500 bytes | 1500 | 26 + 1500 | **1526 bytes** |

!!! tip "Aclaración"
    - **Con 64 bytes de datos**, el campo **Datos+Relleno** tiene **64 bytes** (como 64 ≥ 46, no hace falta relleno). El tamaño total sería **26 + 64 = 90 bytes**.  
    - No confundas **"64 bytes de datos"** con **"trama mínima de 64 bytes"**: la trama mínima de 64 bytes se refiere solo a la parte desde **MAC destino hasta FCS**, sin contar **Preámbulo** ni **SDF**.

!!! warning "Importante: datos útiles vs. campo Datos+Relleno"
    - Cuando hablamos de **"datos útiles"** nos referimos a la información real que queremos transmitir en la trama Ethernet, es decir, la carga de datos aportada por la capa superior.  
    - No incluye los bytes de relleno ni los campos de cabecera/tráiler (como MAC, FCS, etc.). Si los datos útiles no alcanzan el mínimo exigido (46 bytes), se añade relleno para completar el campo **Datos+Relleno**.

!!! note "Nota"
    La **trama mínima de 64 bytes** se refiere únicamente a la parte útil (desde **MAC destino** hasta **FCS**), es decir, **sin contar Preámbulo ni SDF**.  

    - En esa sección: `6 + 6 + 2 + 4 = 18` bytes fijos, por lo que  
    **Datos + Relleno mínimo = 64 − 18 = 46 bytes**.
    - **Trama máxima estándar (sin VLAN):** 1518 bytes = 1500 datos + 18 de cabecera (MAC+Long/Tipo+FCS)
    - **FCS:** 4 bytes = 32 bits. Si el CRC detecta un error → el receptor descarta la trama.

### Capa de Red – Subredes

**Con máscara estándar /24 (255.255.255.0):**

- Red: últimos 8 bits en 0 (ej. 192.168.1.0)
- Broadcast: últimos 8 bits en 255 (ej. 192.168.1.255)
- Hosts válidos: 2⁸ − 2 = **254**

**Con máscara /16 (255.255.0.0):**

- Red: últimos 16 bits en 0
- Broadcast: últimos 16 bits en 255
- Hosts: 2¹⁶ − 2 = **65 534**

**Con prefijo CIDR /26:**

- Máscara: 255.255.255.192
- Bits de host: 32 − 26 = 6 → Hosts = 2⁶ − 2 = **62**
- Incremento: 2⁶ = 64 (redes: .0, .64, .128, .192)

**Reglas rápidas:**

- Primera IP válida = dirección de red + 1
- Última IP válida = broadcast − 1
- Dirección de red y broadcast no se asignan a hosts

**Validación de IP:** Cada octeto debe estar entre 0 y 255. Ejemplos inválidos: 256.x.x.x, x.x.x.300, 4.4.4.4.4 (5 octetos).

---

## PARTE 3: Ejercicios de práctica

### Capa de Enlace

**1.** Trama con 64 bytes de datos útiles. Preámbulo=7, SDF=1, MAC=6+6, Long/Tipo=2, FCS=4. Datos+Relleno mínimo 46 bytes. ¿Tamaño total?

**2.** Trama con 1200 bytes de datos. ¿Tamaño total? (Preámbulo, SDF, MAC, Long/Tipo, Datos, FCS)

**3.** Trama mínima 64 bytes, cabecera (MAC destino hasta FCS) 26 bytes. ¿Tamaño mínimo de Datos+Relleno?

**4.** 100 tramas de 1518 bytes. ¿Cuántos bytes en total?

**5.** FCS = 4 bytes. ¿Cuántos bits? Si el CRC detecta error, ¿qué hace el receptor?

### Capa de Red

**6.** IP 192.168.5.100, máscara 255.255.255.0. Calcula: red, broadcast, primera y última IP válida, número de hosts.

**7.** IP 172.16.50.25, máscara 255.255.0.0. Calcula: red, broadcast, hosts disponibles.

**8.** IP 192.168.10.75/26. Calcula: máscara, red, broadcast, hosts.

**9.** Indica cuáles son inválidas y por qué: 192.168.1.1, 256.10.10.10, 192.168.1.255, 10.0.0.300, 172.16.0.1.

**10.** Red 192.168.1.0/24, router 192.168.1.1. ¿Hay sitio para 30 PCs y 2 impresoras? Ejemplo de configuración del primer PC. ¿Última IP válida?

---

## PARTE 4: Actividades para practicar en clase

### Actividades de desarrollo (preguntas teóricas)

**Actividad 1 – Funciones de la capa de enlace (por parejas)**  
Uno explica al otro las funciones de la capa de enlace sin mirar. El compañero corrige o completa. Cambiar roles.

**Actividad 2 – Subcapas LLC y MAC**  
Completa en papel: LLC → norma ______, función ______. MAC → norma ______, función ______. Comprueba con el resumen.

**Actividad 3 – Campos de la trama**  
Dibuja un esquema de la trama Ethernet con los 7 campos y sus tamaños en bytes. Indica cuál es el mínimo y el máximo de la trama.

**Actividad 4 – CSMA/CD**  
Explica en voz alta los 4 pasos del protocolo CSMA/CD. Indica por qué los switches eliminan las colisiones.

**Actividad 5 – Dominios**  
En un diagrama con hub, switch y router, marca con colores distintos el dominio de colisión y el de difusión. Explica qué hace cada dispositivo.

**Actividad 6 – IP pública y privada**  
Escribe los tres rangos de IP privadas. Indica si estas IPs son públicas o privadas: 8.8.8.8, 192.168.1.1, 10.0.0.1, 172.16.5.10.

**Actividad 7 – Máscara de red**  
Con IP 192.168.1.100 y máscara 255.255.255.0, ¿están en la misma red 192.168.1.50 y 192.168.2.10? Razona.

**Actividad 8 – Proceso ARP**  
Ordena y explica los pasos: “El host envía ARP Request por broadcast”, “Guarda IP-MAC en la tabla ARP”, “Recibe ARP Reply”, “Envía la trama con la MAC correcta”.

**Actividad 9 – ICMP**  
¿Qué hace `ping`? ¿Y `traceroute`? Escribe un ejemplo de comando para cada uno.

**Actividad 10 – DHCP**  
Lista los 4 parámetros que asigna DHCP. Indica 3 ventajas frente a la configuración manual. Nombra 3 comprobaciones con `ping` y qué verifica cada una.

---

### Actividades prácticas (comandos y configuración)

**Actividad P1 – Comprobaciones con ping**  
En tu equipo, ejecuta en orden: `ping 127.0.0.1`, `ping` (tu IP local), `ping` (tu puerta de enlace), `ping 8.8.8.8`, `ping www.google.com`. Anota si cada uno responde correctamente y qué indica.

**Actividad P2 – Consultar configuración de red**  
- **Windows:** `ipconfig` o `ipconfig /all`  
- **Linux:** `ip addr` o `ifconfig`  
Anota tu IP, máscara, puerta de enlace y DNS.

**Actividad P3 – Tabla ARP**  
- **Windows:** `arp -a`  
- **Linux:** `ip neigh` o `arp -n`  
Identifica entradas de equipos de tu red. Explica qué representa cada columna.

**Actividad P4 – Tabla de rutas**  
- **Windows:** `route print`  
- **Linux:** `ip route` o `route -n`  
Localiza la ruta por defecto (0.0.0.0). Indica cuál es tu puerta de enlace.

**Actividad P5 – Validar direcciones IP**  
De estas IPs, indica cuáles son inválidas y por qué: 192.168.1.1, 256.1.1.1, 10.0.0.300, 172.16.0.0, 192.168.1.256, 127.0.0.1.

---

### Actividades prácticas de cálculo – Tramas Ethernet

Resuelve en papel. Datos de referencia: Preámbulo = 7 bytes, SDF = 1 byte, MAC destino = 6 bytes, MAC origen = 6 bytes, Longitud/Tipo = 2 bytes, FCS = 4 bytes. Datos+Relleno mínimo = 46 bytes.

**C1.** Una trama Ethernet tiene 80 bytes de datos útiles. Calcula el tamaño total de la trama en bytes (incluye Preámbulo, SDF, MAC, Longitud/Tipo, Datos+Relleno y FCS).

**C2.** ¿Cuántos bytes ocupa en total una trama Ethernet que transporta 500 bytes de datos? (Incluye Preámbulo, SDF, direcciones MAC, Longitud/Tipo, Datos y FCS).

**C3.** En Ethernet, la trama mínima es de 64 bytes. Si la cabecera (desde MAC destino hasta FCS) ocupa 26 bytes, ¿cuál es el tamaño mínimo del campo Datos+Relleno?

**C4.** Una red Ethernet transmite tramas de 1518 bytes. Si se envían 50 tramas de ese tamaño, ¿cuántos bytes se transmiten en total?

**C5.** El campo FCS ocupa 4 bytes. ¿Cuántos bits son? Si el CRC detecta un error, ¿qué hace el receptor con esa trama?

---

### Actividades prácticas de cálculo – Direcciones IP

Resuelve en papel. Indica todos los pasos.

**C6.** Dada la dirección IP 192.168.3.150 con máscara 255.255.255.0, calcula: dirección de red, dirección de broadcast, primera IP válida, última IP válida, número de hosts.

**C7.** Dada la dirección IP 10.20.100.50 con máscara 255.0.0.0, calcula: dirección de red, dirección de broadcast, número de hosts disponibles.

**C8.** Dada la dirección 172.16.25.100 con prefijo /26: ¿cuál es la máscara de subred? Calcula la dirección de red, la de broadcast y cuántos hosts se pueden conectar.

**C9.** Dada la dirección 192.168.0.200 con máscara 255.255.255.128 (/25): calcula dirección de red, broadcast y número de hosts.

**C10.** Un aula tiene la red 192.168.10.0/24. El router usa 192.168.10.1. Se quieren configurar 40 ordenadores y 3 impresoras. ¿Hay suficientes direcciones? Proporciona un ejemplo de configuración para el primer ordenador. ¿Cuál es la última IP válida?

---

### Actividades de cálculo (ejercicios escritos)

Resuelve los ejercicios de la PARTE 3 en papel, sin mirar las fórmulas. Comprueba los resultados con el resumen de la PARTE 2. Si fallas, repasa la fórmula correspondiente y vuelve a intentarlo.

---

## Checklist antes del examen

- [ ] Conocer las 4+ funciones de la capa de enlace
- [ ] Saber LLC (802.2) y MAC (802.3) y su función
- [ ] Recordar tamaños de los campos de la trama Ethernet
- [ ] Explicar los 4 pasos de CSMA/CD
- [ ] Diferenciar dominio de colisión y de difusión (hub, switch, router)
- [ ] Rangos de IP privadas (10.x, 172.16–31.x, 192.168.x)
- [ ] Usar la máscara para saber si dos hosts están en la misma red
- [ ] Describir el proceso ARP paso a paso
- [ ] ICMP: ping y traceroute
- [ ] DHCP: qué es, parámetros que asigna, ventajas
- [ ] Comprobaciones básicas: ping localhost, IP local, gateway, IP externa, DNS
- [ ] Calcular red, broadcast y hosts con /24, /16, /26
- [ ] Validar direcciones IP (0–255 por octeto)

---

*Documento de apoyo para preparar el examen. Consulta los temas 5 (Capa de Enlace) y 6 (Capa de Red) para más detalle.*
