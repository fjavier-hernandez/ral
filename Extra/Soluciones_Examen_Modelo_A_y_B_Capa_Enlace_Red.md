# Soluciones – Examen Modelo A y Modelo B (Capa de Enlace y Capa de Red)

!!! warning "Documento interno – solo profesorado"
    Este archivo es de uso exclusivo del profesorado. No debe estar accesible al alumnado. Se encuentra en la carpeta **Extra**, fuera de la documentación publicada.

Las soluciones siguen **tal cual** la redacción y los criterios de los apuntes (tema 5 Capa de Enlace, tema 6 Capa de Red) y de la ficha de repaso del examen.

---

## SOLUCIONES EXAMEN MODELO A

### PARTE 1: PREGUNTAS DE DESARROLLO

**1. Funciones principales de la capa de enlace de datos en el modelo OSI (al menos cuatro).**

Según los apuntes y la ficha de repaso, las funciones de la capa de enlace son:

| Función | Descripción |
|---------|-------------|
| **Formación de tramas** | Organizar bits en bloques (tramas) con cabeceras y colas |
| **Direccionamiento** | Añadir direcciones MAC (origen y destino) |
| **Detección de errores** | CRC en el campo FCS para detectar errores de transmisión |
| **Control de flujo** | Adecuar el flujo entre emisor y receptor |
| **Control de acceso al medio** | CSMA/CD cuando varios equipos comparten el medio |
| **Segmentación y agrupación** | Dividir datos grandes o agrupar datos pequeños |

Además: delimitación de trama, sincronización, tratamiento de errores (descartar tramas erróneas, solicitar retransmisiones), recuperación de fallos.

---

**2. Campos principales de una trama Ethernet IEEE 802.3 y tamaño en bytes (al menos cuatro).**

Según el tema 5 y la ficha de repaso:

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

---

**3. Diferencia entre direcciones IP públicas y privadas. Tres rangos de IP privadas.**

Según el tema 6 y la ficha:

| Tipo | Visibilidad | Rangos privados (RFC 1918) |
|------|-------------|----------------------------|
| **Pública** | Visible en Internet; única globalmente | — |
| **Privada** | Solo en redes locales; no enrutable en Internet | 10.0.0.0/8, 172.16.0.0–172.31.255.255, 192.168.0.0/16 |

**Rangos privados más utilizados:**

- **10.0.0.0 – 10.255.255.255** (10.0.0.0/8)
- **172.16.0.0 – 172.31.255.255** (172.16.0.0/12)
- **192.168.0.0 – 192.168.255.255** (192.168.0.0/16)

Los hosts con IP privada pueden salir a Internet mediante un router (NAT) que tenga IP pública; desde Internet no se puede acceder directamente a ellos.

---

**4. Proceso del protocolo ARP paso a paso. Qué ocurre si el host no conoce la MAC del destino.**

Según el tema 6 y la ficha de repaso (proceso ARP en la misma red):

1. El host necesita la **MAC** de una **IP conocida** (misma red).
2. Envía **ARP Request** por **broadcast** (MAC destino FF:FF:FF:FF:FF:FF): «¿Qué dispositivo tiene la IP X.X.X.X?»
3. Solo el host con esa IP responde con **ARP Reply** en **unicast**, indicando su dirección MAC.
4. El solicitante **guarda la relación IP→MAC** en su **tabla ARP**.
5. **Envía la trama** con la MAC destino correcta.

Si no conoce la MAC, no puede montar la trama de capa 2; por eso debe usar ARP antes para obtener la MAC asociada a esa IP.

---

**5. Protocolo DHCP: qué es, para qué sirve, parámetros que asigna, ventajas y comprobaciones.**

Según la ficha de repaso:

- **Qué es / para qué sirve:** Protocolo que asigna **automáticamente** los parámetros de red a los clientes (Dynamic Host Configuration Protocol).
- **Parámetros que asigna:** Dirección IP, máscara de red, puerta de enlace, servidores DNS.
- **Ventajas frente a configuración manual:** Facilita la administración, evita conflictos de IP, permite reutilizar direcciones cuando los clientes se desconectan.

**Comprobaciones básicas (orden recomendado):**

| Comprobación | Comando ejemplo | Qué verifica |
|--------------|-----------------|--------------|
| Stack TCP/IP | `ping 127.0.0.1` | Que el protocolo funciona en el equipo |
| Interfaz de red | `ping IP_local` | Que la tarjeta de red responde |
| Puerta de enlace | `ping 192.168.1.1` | Conectividad con el router |
| Internet | `ping 8.8.8.8` | Conectividad con redes externas |
| DNS | `ping www.google.com` | Resolución de nombres a IP |

---

### PARTE 2: EJERCICIOS DE CÁLCULO (MODELO A)

**1. Trama Ethernet con 64 bytes de datos útiles. Tamaño total.**

Según la ficha: los **campos fijos** (Preámbulo + SDF + MAC destino + MAC origen + Longitud/Tipo + FCS) suman **26 bytes**. El campo **Datos+Relleno** debe ser al menos 46 bytes; si los datos útiles son 64 bytes, no hace falta relleno, así que Datos+Relleno = 64 bytes.

**Total = 26 + 64 = 90 bytes.**

---

**2. Trama mínima 64 bytes; cabecera (desde MAC destino hasta FCS) = 26 bytes. Tamaño mínimo de Datos+Relleno.**

Según el enunciado: la parte “cabecera” (desde MAC destino hasta FCS) ocupa 26 bytes. La trama mínima de 64 bytes se refiere a esa sección (MAC destino hasta FCS), por tanto:

**Datos + Relleno mínimo = 64 − 26 = 38 bytes.**

(En el estándar, “desde MAC destino hasta FCS” son 6+6+2+4 = 18 bytes, y entonces Datos+Relleno mínimo = 64−18 = 46 bytes; si el examen da 26 bytes de cabecera, se aplica 64−26 = 38.)

---

**3. IP 172.16.50.25, máscara 255.255.0.0.**

Según la ficha (máscara /16):

- **Dirección de red:** 172.16.0.0  
- **Broadcast:** 172.16.255.255  
- **Número de hosts disponibles:** 2¹⁶ − 2 = **65 534**

---

**4. Direcciones IP inválidas y por qué.**

Según la ficha: **cada octeto debe estar entre 0 y 255**.

- **192.168.1.1** — Válida (rango privado; todos los octetos ≤ 255).
- **256.10.10.10** — **Inválida:** el primer octeto 256 no es válido (máximo 255).
- **192.168.1.255** — **Válida** en una red /24: es la dirección de **broadcast** de 192.168.1.0/24; como valor de octeto está permitido.
- **10.0.0.300** — **Inválida:** el último octeto 300 no es válido (máximo 255).
- **172.16.0.1** — Válida (rango privado).

---

**5. Red 192.168.1.0/24, router 192.168.1.1, 30 ordenadores y 2 impresoras.**

Según la ficha (red /24):

- **Hosts utilizables:** 2⁸ − 2 = 254. Se necesitan 30 + 2 = 32. **Sí hay suficientes direcciones.**
- **Ejemplo primer ordenador:** IP **192.168.1.2**, máscara **255.255.255.0**, puerta de enlace **192.168.1.1**.
- **Última IP válida:** **192.168.1.254** (192.168.1.255 es la dirección de broadcast).

---

## SOLUCIONES EXAMEN MODELO B

### PARTE 1: PREGUNTAS DE DESARROLLO

**1. Subcapas LLC y MAC: norma y función principal.**

Según el tema 5 y la ficha de repaso:

| Subcapa | Norma | Función principal |
|---------|-------|-------------------|
| **LLC** (Logical Link Control) | IEEE 802.2 | Interfaz uniforme para la capa de red; gestión de errores y control de flujo lógico |
| **MAC** (Medium Access Control) | IEEE 802.3 (Ethernet) | Arbitrar el uso del medio compartido; empaquetar datos en tramas; CSMA/CD |

---

**2. Funcionamiento del protocolo CSMA/CD. Cuatro pasos. Por qué los switches eliminan las colisiones.**

Según el tema 5 y la ficha:

**Cuatro pasos:**

1. **Carrier Sense (detección de portadora):** Escuchar si hay señal en el medio antes de transmitir.
2. **Multiple Access (acceso múltiple):** Si el medio está libre, transmitir.
3. **Collision Detection (detección de colisiones):** Si se detecta colisión, detener la transmisión.
4. **Backoff:** Esperar un tiempo aleatorio antes de reintentar.

**Switches:** Crean un **dominio de colisión por puerto** (comunicación full-duplex), por lo que **eliminan las colisiones**.

---

**3. Dominio de colisión y dominio de difusión. Qué hacen hub, switch y router.**

Según el tema 5 y la ficha:

| Concepto | Definición | Hub | Switch | Router |
|----------|------------|-----|--------|--------|
| **Dominio de colisión** | Dispositivos cuyas tramas pueden colisionar | Extiende | 1 por puerto | Limita |
| **Dominio de difusión** | Dispositivos que reciben broadcast | Extiende | Extiende | Limita |

---

**4. Máscara de red: qué es, para qué sirve, cómo se usa para saber si dos hosts están en la misma red.**

Según el tema 6 y la ficha:

- **Qué es:** Número de 32 bits que indica qué parte de la dirección IP corresponde a la **red** y qué parte al **host**.
- **Para qué sirve:** Identificar red y host; determinar si dos hosts están en la misma red.
- **Uso:** Los **bits en 1** indican red; los **bits en 0** indican host. **Misma red** si **(IP₁ AND máscara) = (IP₂ AND máscara)**.

---

**5. Protocolo ICMP: qué es, para qué se usa, dos herramientas.**

Según el tema 6 y la ficha:

- **Qué es:** Protocolo de la capa de red para **mensajes de control y error** en redes IP.
- **Para qué se usa:** Comprobar conectividad, notificar errores (host inalcanzable, TTL agotado), diagnóstico.
- **Herramientas:** **`ping`** (Echo Request/Reply, comprobar conectividad) y **`traceroute`** / **`tracert`** (mostrar ruta y saltos hasta el destino).

---

### PARTE 2: EJERCICIOS DE CÁLCULO (MODELO B)

**1. Trama Ethernet con 1200 bytes de datos. Tamaño total.**

Campos fijos = 26 bytes. Datos+Relleno = 1200 bytes (no hace falta relleno).

**Total = 26 + 1200 = 1226 bytes.**

---

**2. 100 tramas de 1518 bytes. Bytes totales.**

100 × 1518 = **151 800 bytes.**

---

**3. FCS = 4 bytes. ¿Cuántos bits? Si el CRC detecta error, ¿qué hace el receptor?**

- 4 bytes = **32 bits**.
- Si el CRC detecta un error, el **receptor descarta la trama** (no la entrega a capas superiores). El protocolo de capa superior puede solicitar retransmisión si lo soporta.

---

**4. IP 192.168.5.100, máscara 255.255.255.0.**

Según la ficha (máscara /24):

- **Dirección de red:** 192.168.5.0  
- **Broadcast:** 192.168.5.255  
- **Primera IP válida:** 192.168.5.1  
- **Última IP válida:** 192.168.5.254  
- **Número de hosts que se pueden conectar:** 2⁸ − 2 = **254**

---

**5. Dirección 192.168.10.75 con prefijo /24.**

- **Máscara de subred:** 255.255.255.0 (/24).  
- **Dirección de red:** 192.168.10.0  
- **Broadcast:** 192.168.10.255  
- **Hosts que se pueden conectar:** **254**

---

*Soluciones alineadas con **docs/05enlace.md**, **docs/06red.md** y **docs/ficha_repaso_examen_enlace_red.md**. Uso exclusivo del profesorado.*
