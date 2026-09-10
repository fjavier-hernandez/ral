---
title: Ficha de repaso - Examen NAT e IPv6
description: Resumen y preparación para el examen del tema de NAT (estático, dinámico, PAT) e IPv6 (formato, prefijos, tipos de dirección y coexistencia) (SMR).
---

# :material-book-open-variant: Ficha de repaso para el examen

**Tema:** NAT e IPv6 (Unidad 9)  
**Módulo:** Redes de Área Local (RAL)  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

Esta ficha te ayuda a preparar el examen de **NAT e IPv6**. Incluye un resumen de conceptos y fórmulas de referencia y **actividades de práctica** del mismo tipo que el examen: identificación de IPs privadas, traducción NAT/PAT con tablas, terminología NAT, abreviatura y expansión de direcciones IPv6, prefijos, tipos de dirección y mecanismos de coexistencia IPv4/IPv6. El examen será íntegramente de actividades prácticas.

[Consulta las **soluciones de las actividades**](./extra/ficha_repaso_tema_9_nat_ipv6_soluciones.md) para comprobar tus resultados después de practicar.

---

## PARTE 1: Conceptos y fórmulas de referencia

### Direcciones IPv4 privadas (RFC 1918)

| Clase | Rango | Prefijo CIDR | Nº de redes |
|-------|-------|--------------|-------------|
| A | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | 1 |
| B | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 16 |
| C | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 256 |

Las IPs privadas **no se enrutan** en Internet: para salir hay que **traducirlas** a una IP pública (**NAT**).

### Tipos de NAT

| Tipo | Mapeo | Cuándo se usa | IPs públicas necesarias |
|------|-------|---------------|-------------------------|
| **NAT estático** | 1 privada ↔ 1 pública fija | Publicar un **servidor** con IP pública estable | 1 pública por cada host mapeado |
| **NAT dinámico** | IPs privadas ↔ pool público (asignación dinámica 1:1) | Varios hosts internos que salen a Internet ocasionalmente | Tantas públicas como sesiones simultáneas |
| **PAT** (NAT con sobrecarga) | Muchas privadas ↔ **una** pública (se traducen **IP + puerto**) | Redes domésticas y oficinas: muchos hosts saliendo por una sola IP pública | **1 pública** (se multiplexan con puertos) |

### Tabla de traducción PAT

El router con PAT mantiene una tabla de 4 (o más) columnas:

| Socket interno (LAN) | Socket público (WAN) | Socket remoto | Protocolo |
|----------------------|----------------------|---------------|-----------|
| IP_privada:puerto | IP_pública:puerto_traducido | IP_destino:puerto_destino | TCP/UDP |

Si dos hosts internos usan el **mismo puerto origen**, el router **cambia** uno de ellos al primer puerto libre para que cada sesión tenga un socket público único.

### Terminología NAT (local/global, interna/externa)

| Término | Qué es |
|---------|--------|
| **Local interna** | IP **privada** del host dentro de la LAN (origen real) |
| **Global interna** | IP **pública** que el router muestra hacia Internet por ese host |
| **Local externa** | Cómo el host interno **ve** al destino (normalmente igual que la global externa) |
| **Global externa** | IP **pública real** del destino en Internet |

- **Interna** = el equipo **traducido** (suele ser el origen de la sesión).
- **Externa** = el **destino** (no lo traduce este NAT).

### IPv6: formato y abreviatura

- Longitud: **128 bits** (frente a 32 de IPv4).
- Representación: **8 grupos** de **4 dígitos hexadecimales** separados por `:`.
- Cada grupo son **16 bits** → dirección completa 32 dígitos hex.

Reglas de abreviatura:

1. **Ceros a la izquierda** de cada grupo se pueden omitir: `0db8` → `db8`, `0001` → `1`, `0000` → `0`.
2. Una **única secuencia de grupos todos cero** se puede sustituir por `::`. **Solo un `::`** por dirección (si hubiera dos sería ambigua).

Ejemplo:

`2001:0db8:0000:0000:0000:0000:00cd:00ef` → `2001:db8::cd:ef`.

### Prefijos IPv6

Notación `/n`: los primeros **n bits** identifican la red. Tamaños típicos:

| Prefijo | Capacidad | Uso típico |
|--------:|-----------|------------|
| `/32` | 65 536 bloques /48 | Asignación a un ISP |
| `/48` | 65 536 subredes /64 | Bloque para empresa mediana/grande |
| `/56` | 256 subredes /64 | Bloque residencial delegado por ISP |
| `/64` | `2^64` direcciones | **Subred de un enlace** LAN típico |
| `/128` | 1 dirección | Host/loopback |

Para un prefijo `/n`, el bloque abarca `2^(128−n)` direcciones.

### Tipos de dirección IPv6

| Tipo | Prefijo / dirección | Uso |
|------|---------------------|-----|
| **Loopback** | `::1` | Bucle local (como 127.0.0.1 en IPv4) |
| **Indefinida** | `::` (`::/128`) | Origen cuando aún no se conoce IP propia |
| **Link-local** | `fe80::/10` | Comunicación **solo en el enlace**, se autoconfigura siempre |
| **ULA (privada)** | `fc00::/7` (en la práctica `fd00::/8`) | Uso privado dentro de una organización (equivalente a RFC 1918) |
| **Global unicast** | `2000::/3` | IPv6 públicas routables |
| **Multicast** | `ff00::/8` (p. ej. `ff02::1` todos los nodos del enlace) | Entrega a un grupo |

### Coexistencia IPv4 / IPv6

- **Pila dual:** cada nodo tiene IPv4 e IPv6 a la vez.
- **Túneles:** encapsulan IPv6 sobre IPv4 (o viceversa) para atravesar redes que solo soportan una familia.
- **Traducción:** un dispositivo intermedio traduce cabeceras entre IPv4 e IPv6 (ej. NAT-PT / NAT64).

### Resumen PARTE 1

| Tema | Reglas / pasos clave |
|------|----------------------|
| **Privadas RFC 1918** | 10/8, 172.16/12, 192.168/16. No enrutables en Internet. |
| **NAT estático** | 1 privada ↔ 1 pública fija. Publicar servidores. |
| **NAT dinámico** | Pool público; asignación 1:1 por sesión. |
| **PAT** | 1 pública para muchos hosts; traduce **IP + puerto**. |
| **IPv6 abreviada** | Quitar ceros a la izquierda + un solo `::` para grupos de ceros. |
| **Prefijos** | /48 → 65 536 /64; /56 → 256 /64; /64 = enlace LAN típico. |
| **Coexistencia** | Pila dual, túneles, traducción. |

---

## PARTE 2: Actividades de práctica (tipo examen)

<!-- Todas las actividades son prácticas. Resuélvelas en papel como en el examen. Cuando termines, puedes comprobar tus respuestas en las [soluciones de la ficha de repaso](../Extra/ficha_repaso_tema_9_nat_ipv6_soluciones.md).

--- -->

### Direcciones IPv4 privadas y públicas

**Actividad 1 – Identifica privadas y públicas (RFC 1918)**  
Para cada una de las siguientes IPv4, indica si es **pública** o **privada**. Si es privada, especifica a qué rango RFC 1918 pertenece (10/8, 172.16/12 o 192.168/16).

a) `10.25.100.5`  
b) `172.15.0.1`  
c) `172.16.0.1`  
d) `172.31.255.254`  
e) `172.32.0.1`  
f) `192.168.10.1`  
g) `192.169.1.1`  
h) `8.8.8.8`  
i) `100.64.0.1`  
j) `203.0.113.50`

---

### NAT estático

**Actividad 2 – Publicar un servidor con NAT estático**  
Una empresa tiene en su DMZ un servidor interno en `192.168.20.100` y quiere que sea accesible desde Internet usando la IP pública `198.51.100.50`. El router aplica **NAT estático** 1:1 entre ambas.

Un cliente de Internet (`203.0.113.10`) abre una conexión TCP hacia la web del servidor en el puerto 80. El puerto origen efímero del cliente es `54321`.

Completa las dos tablas:

**a) Paquete del cliente → servidor (antes y después de NAT):**

| Punto de observación | IP origen | Puerto orig | IP destino | Puerto dest |
|----------------------|-----------|-------------|------------|-------------|
| Fuera del router (Internet) | `203.0.113.10` | `54321` | ? | `80` |
| Dentro del router (LAN) | `203.0.113.10` | `54321` | ? | `80` |

**b) Paquete de respuesta servidor → cliente:**

| Punto de observación | IP origen | Puerto orig | IP destino | Puerto dest |
|----------------------|-----------|-------------|------------|-------------|
| Dentro del router (LAN) | ? | `80` | `203.0.113.10` | `54321` |
| Fuera del router (Internet) | ? | `80` | `203.0.113.10` | `54321` |

Indica también qué **columna** modifica el router en cada sentido (origen o destino, IP o puerto).

---

### PAT / NAT con sobrecarga

**Actividad 3 – Tabla PAT con colisión de puerto origen**  
Tres PCs de la LAN `192.168.1.0/24` salen a Internet mediante **PAT** con la única IP pública `198.51.100.20`:

- **PC1:** `192.168.1.10`, abre HTTP al servidor `203.0.113.80:80` con puerto origen **49200**.
- **PC2:** `192.168.1.11`, abre HTTP al mismo servidor `203.0.113.80:80` con puerto origen **49200** (coincide con PC1).
- **PC3:** `192.168.1.12`, abre HTTPS al servidor `203.0.113.80:443` con puerto origen **50001**.

Completa la tabla de traducciones PAT del router. En caso de colisión, asigna al segundo equipo el **primer puerto libre** (usa, por ejemplo, `50200`).

| PC | Socket interno | Socket público (traducido) | Socket remoto | Protocolo |
|----|----------------|-----------------------------|----------------|-----------|
| PC1 | 192.168.1.10:49200 | 198.51.100.20:? | 203.0.113.80:80 | TCP |
| PC2 | 192.168.1.11:49200 | 198.51.100.20:? | 203.0.113.80:80 | TCP |
| PC3 | 192.168.1.12:50001 | 198.51.100.20:? | 203.0.113.80:443 | TCP |

Responde además:

1. ¿Por qué **no basta** con traducir solo la IP en el caso de PC1 y PC2?
2. Cuando el servidor responde al PC2, ¿qué socket destino lleva el paquete que llega al router? ¿Y cómo decide el router que debe reenviarse al PC2 y no al PC1?

---

### Terminología NAT

**Actividad 4 – Local interna / global interna / local externa / global externa**  
El PC-A tiene IP `192.168.10.20` (LAN). El router corporativo con NAT tiene IP pública `203.0.113.5`. El PC-A accede al servidor web público `93.184.216.34` (puerto 80).

Completa la tabla de terminología NAT para el tráfico **PC-A → servidor web**:

| Término | Dirección |
|---------|-----------|
| Local interna | ? |
| Global interna | ? |
| Local externa | ? |
| Global externa | ? |

Responde también:

1. ¿Cuál es el **dispositivo traducido** desde el punto de vista del NAT?
2. ¿Qué IP ve el servidor web como **origen** de la petición? ¿Por qué?

---

### NAT dinámico vs PAT

**Actividad 5 – Dimensionado de pool NAT**  
Una empresa tiene 40 PCs en la LAN `10.50.0.0/24` que navegan por Internet. Dispone de las siguientes opciones:

- **Opción A:** NAT dinámico con un pool de **8 IPs públicas**.
- **Opción B:** PAT con **1 sola IP pública**.

Responde:

1. Con la opción A, ¿cuántos PCs pueden salir a Internet **al mismo tiempo**? Justifica.
2. Con la opción B (PAT), ¿cuántas sesiones simultáneas puede haber como máximo (teórico)? ¿Qué recurso es el que limita?
3. ¿Cuál de las dos opciones es más adecuada para una red doméstica típica y por qué?

---

### IPv6 – Abreviatura

**Actividad 6 – Abreviar direcciones IPv6**  
Escribe la forma **más corta** válida de cada una de las siguientes direcciones IPv6 (aplica ceros a la izquierda + `::`):

a) `2001:0db8:0000:0000:0000:0000:0000:0001`  
b) `fe80:0000:0000:0000:abcd:ef01:2345:6789`  
c) `2001:0abc:0000:0001:0000:0000:0000:0002`  
d) `0000:0000:0000:0000:0000:0000:0000:0000`  
e) `fc00:0db8:0000:1234:0000:0000:0000:cdef`

Indica también si las siguientes son **válidas** o **inválidas** y por qué:

f) `2001:db8::1::5`  
g) `2001:db8:gggg::1`  
h) `fe80::abcd:0:0:1`

---

**Actividad 7 – Expandir direcciones IPv6**  
Escribe en forma **completa** (32 dígitos hexadecimales, 8 grupos de 4) cada dirección abreviada:

a) `::1`  
b) `2001:db8::`  
c) `fe80::1234:5:6:7`  
d) `ff02::2`

---

### IPv6 – Tipos de dirección

**Actividad 8 – Identificar el tipo de dirección IPv6**  
Indica el **tipo** (global unicast, link-local, ULA, loopback, multicast o indefinida) y una breve observación sobre el uso de cada dirección:

a) `::1`  
b) `fe80::1`  
c) `fc00:abcd::10`  
d) `2001:db8:acad::1`  
e) `ff02::1`  
f) `::`  
g) `fd12:3456:789a::1`  
h) `ff02::2`

---

### IPv6 – Prefijos y subnetización

**Actividad 9 – Prefijo /64**  
Dada la dirección `2001:db8:acad:1234::100/64`, responde:

1. Escribe el **prefijo de red** (sin sufijo de host) en **forma abreviada**.
2. Indica la **primera** y la **última** dirección del bloque `/64` en forma desarrollada (sin `::`, con todos los grupos).
3. ¿Cuántos bits quedan para el **identificador de interfaz**?
4. ¿Cuántas direcciones de host contiene el bloque (en forma `2^x`)?

---

**Actividad 10 – Subnetizar un /48 en /64**  
Una empresa recibe del ISP el bloque `2001:db8:abcd::/48`. Desea crear **8 subredes /64** para ocho departamentos.

1. ¿Cuántos bits quedan disponibles para identificar subredes dentro del `/48`?
2. Escribe las **8 primeras subredes** `/64` que puede usar, en forma abreviada.
3. ¿Cuántas subredes `/64` puede crear la empresa en total con ese `/48`?

---

**Actividad 11 – Bloque residencial /56**  
Un ISP delega al router de casa el prefijo `2001:db8:cafe:ab00::/56`.

1. ¿Cuántas subredes `/64` puede usar el router internamente con ese `/56`?
2. Escribe las 4 primeras subredes `/64` (en forma abreviada si procede).
3. Si solo hay una LAN doméstica, ¿qué prefijo debería asignarle el router a esa LAN y qué tamaño tiene?

---

### IPv4 vs IPv6 en un escenario real

**Actividad 12 – Comparación IPv4+PAT vs IPv6 nativo**  
Un hogar tiene **6 dispositivos** (2 PCs, 2 móviles, 1 TV y 1 consola). El router recibe del ISP:

- En **IPv4**: una única IP pública `84.10.20.30` y aplica **PAT** a la LAN `192.168.1.0/24`.
- En **IPv6**: un prefijo `/56` delegado (`2001:db8:cafe::/56`).

Responde:

1. ¿Cuántas IPv4 públicas necesita el router para que los 6 dispositivos naveguen? ¿Qué técnica lo hace posible?
2. Si un servidor en Internet recibe conexiones simultáneas de los 6 dispositivos por IPv4, ¿qué IP origen ve en todas ellas? ¿Cómo las diferencia?
3. En IPv6, ¿qué IP origen verá el servidor para cada dispositivo? ¿Necesita el router aplicar NAT?
4. ¿Qué ventaja fundamental aporta IPv6 frente a IPv4+PAT respecto a las **conexiones entrantes** hacia los dispositivos internos?
5. Cita dos mecanismos de **coexistencia** IPv4/IPv6 y describe brevemente cuándo usarías cada uno.

---

## Checklist antes del examen

- [ ] Reconocer IPs privadas (RFC 1918) y públicas, y los tres rangos privados
- [ ] Construir la tabla de traducción de **NAT estático** (publicación de un servidor interno)
- [ ] Construir la tabla de traducción **PAT** y resolver colisiones de puerto origen
- [ ] Explicar la terminología NAT: **local/global** e **interna/externa**
- [ ] Dimensionar un **pool NAT dinámico** y justificar PAT frente a NAT dinámico
- [ ] Abreviar IPv6 aplicando ceros a la izquierda y un único `::`
- [ ] Expandir IPv6 a su forma completa de 8 grupos × 4 hex
- [ ] Identificar si una dirección IPv6 es válida y por qué no lo es (doble `::`, dígitos no hex, etc.)
- [ ] Clasificar direcciones IPv6: loopback, indefinida, link-local (fe80::/10), ULA (fc00::/7), global (2000::/3) y multicast (ff00::/8)
- [ ] Calcular rangos de un prefijo `/64` y subnetizar `/48` o `/56` en `/64`
- [ ] Explicar los mecanismos de coexistencia: pila dual, túneles y traducción

---
<!-- 
*Documento de apoyo para preparar el examen. Consulta el tema 9 (NAT e IPv6) para más detalle. [Soluciones de las actividades](../Extra/ficha_repaso_tema_9_nat_ipv6_soluciones.md).* -->
