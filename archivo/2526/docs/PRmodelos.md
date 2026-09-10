# Modelos TCP/IP y OSI en acción con Packet Tracer
# Práctica 2.1 - Análisis de los modelos TCP/IP y OSI en acción con Packet Tracer

## Objetivos

- Comprender la relación entre los modelos OSI y TCP/IP.
- Analizar el proceso de encapsulamiento de datos en una red.
- Observar el tráfico HTTP, DNS, ARP y TCP en una simulación de red.

## Requisitos

- Cisco Packet Tracer instalado.
- Archivo de simulación proporcionado por el profesor (topología con cliente y servidor web).

---

## Parte 1: Análisis del tráfico HTTP

### Paso 1: Activar el modo de simulación

1. Abre Packet Tracer y carga la topología.
2. Cambia de **Tiempo real** a **Simulación** (parte inferior derecha).
3. En el panel de simulación, haz clic en **Editar filtros**.
4. Desactiva todos los protocolos y selecciona solo **HTTP**.

### Paso 2: Generar tráfico HTTP

1. Haz clic en el **Cliente Web**.
2. Ve a la pestaña **Escritorio** y abre el **Navegador Web**.
3. Introduce la URL: `www.osi.local` y pulsa **Ir**.
4. Pulsa el botón **Capturar/Avanzar** cuatro veces.

### Paso 3: Analizar la PDU

1. Haz clic en el primer evento HTTP de la lista.
2. En la pestaña **Modelo OSI**, selecciona la **Capa 7**.
   - ¿Qué ocurre? → *"The HTTP client sends a HTTP request to the server."*
3. En la **Capa 4**, observa el **puerto de destino**: `80`.
4. En la **Capa 3**, observa la **IP de destino**: `192.168.1.254`.
5. En la **Capa 2**, se muestran las direcciones MAC origen y destino.

### Paso 4: Detalles de la PDU

- En la pestaña **Detalles de la PDU saliente**:
  - **Capa 3 (IP)**: IP origen y destino.
  - **Capa 4 (TCP)**: Puerto origen `1027`, puerto destino `80`.
  - **Capa 7 (HTTP)**: Host → `www.osi.local`.

---

## Parte 2: Otros protocolos de la suite TCP/IP

### Paso 1: Mostrar todos los eventos

1. En **Filtros de eventos**, selecciona **Mostrar todo**.
2. Aparecerán eventos de **ARP**, **DNS**, **TCP** y **HTTP**.

### Paso 2: Analizar evento DNS

1. Haz clic en el primer evento **DNS**.
2. En la pestaña **Modelo OSI**, capa 7:
   - *"The DNS client sends a DNS query to the DNS server."*
3. En **Detalles de la PDU saliente**, sección **Consulta DNS**:
   - Nombre: `www.osi.local`.
4. En la respuesta DNS (último evento DNS):
   - Dirección IP devuelta: `192.168.1.254`.

### Paso 3: Analizar eventos TCP

1. Haz clic en el evento **TCP** posterior al primer HTTP.
2. En la capa 4:
   - *"The TCP connection is successful"*
   - *"The device sets the connection state to ESTABLISHED"*
3. En el último evento TCP:
   - *"The device closes the connection"*

---

## Preguntas de repaso

1. ¿Qué puerto escucha el servidor web para solicitudes HTTP?
   - **Puerto 80**
2. ¿Qué puerto escucha el servidor DNS?
   - **Puerto 53**
3. ¿Qué diferencias observas entre las capas de entrada y salida en la respuesta del servidor?
   - **Se intercambian las direcciones IP, MAC y los puertos origen/destino.**

---

© Cisco Networking Academy  
Adaptado para el módulo de **Redes de Área Local** – SMR  
Profesor: Fº Javier Hernández Illán
