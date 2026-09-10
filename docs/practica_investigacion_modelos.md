---
title: Práctica - Investigación de los modelos TCP/IP y OSI en Packet Tracer
description: Práctica para examinar el tráfico web HTTP y mostrar elementos de la suite de protocolos TCP/IP usando Packet Tracer.
subtitle: Arquitecturas de Redes
# tags:
#     - Práctica
#     - RA1
---

# 🔬 PRÁCTICA: INVESTIGACIÓN DE LOS MODELOS TCP/IP Y OSI EN PACKET TRACER

Esta práctica tiene como objetivo proporcionar una base para comprender la suite de protocolos TCP/IP y su relación con el modelo OSI. Utilizando el modo de simulación de Packet Tracer, los estudiantes podrán ver el contenido de los datos que se envían a través de la red en cada capa.

## 📚 Propuesta didáctica

En esta práctica trabajamos el **RA1 de RAL**:

> **RA1.** *Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes.*

### 🎯 Criterios de evaluación trabajados

* **CE1a**: Se han descrito los principios de funcionamiento de las redes locales.
* **CE1c**: Se han descrito los elementos de la red local y su función.

### 🎯 Objetivos de la práctica

* Examinar el tráfico web HTTP utilizando el modo de simulación de Packet Tracer.
* Mostrar y analizar elementos de la suite de protocolos TCP/IP.
* Comprender el proceso de encapsulamiento de datos en las diferentes capas.
* Identificar las PDU (Unidades de Datos de Protocolo) en cada capa.
* Relacionar los modelos OSI y TCP/IP con el funcionamiento real de la red.

---

## 📋 Descripción de la práctica

### 🔧 Aspectos básicos

Esta actividad de simulación tiene como objetivo proporcionar una base para comprender la suite de protocolos TCP/IP y la relación con el modelo OSI. El modo de simulación permite ver el contenido de los datos que se envían a través de la red en cada capa.

A medida que los datos se desplazan por la red, se dividen en partes más pequeñas y se identifican de modo que las piezas se puedan volver a unir cuando lleguen al destino. A cada pieza se le asigna un nombre específico (**unidad de datos del protocolo [PDU]**) y se la asocia a una capa específica de los modelos TCP/IP y OSI.

El modo de simulación de Packet Tracer permite ver cada una de las capas y la PDU asociada. Los siguientes pasos guían al usuario a través del proceso de solicitud de una página web desde un servidor web mediante la aplicación de navegador web disponible en una PC cliente.

### 🎯 Escenario de trabajo

- **Cliente web**: PC con navegador web
- **Servidor web**: Servidor HTTP con página web
- **Red local**: Conexión directa entre cliente y servidor
- **Protocolos**: HTTP, TCP, IP, Ethernet, DNS, ARP

---

## 🛠️ Instrucciones detalladas

### 📊 Parte 1: Examinar el tráfico web HTTP

#### Paso 1: Cambiar del modo de tiempo real al modo de simulación

1. **Cambio de modo**:
   - En la esquina inferior derecha de la interfaz de Packet Tracer, hacer clic en el ícono del modo de **Simulación**.
   - Seleccionar **HTTP** en Filtros de lista de eventos.

2. **Configuración de filtros**:
   - Hacer clic en el botón **Editar filtros** en la parte inferior del panel de simulación.
   - Alternar la casilla de verificación **Mostrar todo/ninguno** hasta que se desactiven todas las casillas.
   - Seleccionar únicamente **HTTP**.
   - Cerrar la ventana Editar filtros.

#### Paso 2: Generar tráfico web (HTTP)

1. **Acceder al cliente web**:
   - Hacer clic en **Cliente web** en el panel del extremo izquierdo.
   - Hacer clic en la ficha **Escritorio** y luego en el ícono **Navegador web**.

2. **Realizar solicitud HTTP**:
   - En el campo de dirección URL, introducir: `http://www.osi.local`
   - Hacer clic en **Ir**.

3. **Capturar eventos**:
   - Hacer clic en **Capturar/Avanzar** cuatro veces.
   - Observar que aparecen cuatro eventos en la Lista de eventos.

4. **Examinar la primera PDU**:
   - Hacer clic en el primer cuadro coloreado debajo de la columna **Lista de eventos > Información**.
   - Asegurarse de que esté seleccionada la ficha **Modelo OSI**.
   - Hacer clic en **Capa 7** en la columna Capas de salida.

#### 📝 Preguntas de análisis - Parte 1

**Pregunta 1**: ¿Qué información se indica en los pasos numerados directamente debajo de los cuadros Capas de entrada y Capas de salida?

**Pregunta 2**: ¿Cuál es el valor del puerto Dst para la capa 4 en la columna Capas de salida?

**Pregunta 3**: ¿Cuál es el destino? ¿Valor IP para la Capa 3 en la columna Capas de salida?

**Pregunta 4**: ¿Qué información se muestra en la Capa 2 en la columna Capas de salida?

5. **Examinar detalles de PDU**:
   - Hacer clic en la ficha de **Detalles de la PDU saliente**.
   - Comparar la información entre las diferentes secciones.

#### 📝 Preguntas de análisis - Detalles de PDU

**Pregunta 5**: ¿Cuál es la información común que se indica en la sección IP de Detalles de PDU comparada con la información que se indica en la ficha Modelo OSI? ¿Con qué capa se relaciona?

**Pregunta 6**: ¿Cuál es la información frecuente que se indica en la sección IP de Detalles de PDU comparada con la información que se indica en la ficha Modelo OSI?

**Pregunta 7**: ¿Cuál es el host que se indica en la sección HTTP de Detalles de PDU? ¿Con qué capa se relacionaría esta información en la ficha Modelo OSI?

6. **Examinar eventos adicionales**:
   - Hacer clic en el primer cuadro coloreado debajo de la columna **Lista de eventos > Tipo**.
   - Avanzar al siguiente cuadro **Tipo** de HTTP y hacer clic en el cuadro coloreado.
   - Comparar las columnas **Capas de entrada** y **Capas de salida**.

#### 📝 Pregunta de comparación

**Pregunta 8**: Compare la información que se muestra en la columna Capas de entrada con la de la columna Capas de salida: ¿cuáles son las diferencias principales?

7. **Finalizar análisis de HTTP**:
   - Hacer clic en la ficha **Inbound PDU Details** (Detalles de PDU entrante).
   - Hacer clic en el último cuadro coloreado de la columna Información.

#### 📝 Pregunta final de la Parte 1

**Pregunta 9**: ¿Cuántas fichas se muestran con este evento y por qué? Explique.

---

### 🌐 Parte 2: Mostrar elementos de la suite de protocolos TCP/IP

#### Paso 1: Ver eventos adicionales

1. **Configurar filtros para todos los protocolos**:
   - Cerrar todas las ventanas de información de PDU abiertas.
   - En la sección **Filtros de lista de eventos > Eventos visibles**, hacer clic en **Mostrar todo**.

#### 📝 Pregunta de análisis

**Pregunta 10**: ¿Qué tipos de eventos adicionales se muestran?

2. **Examinar protocolo DNS**:
   - Hacer clic en el primer evento de **DNS** en la columna **Información**.
   - Examinar las fichas **Modelo OSI** y **Detalles de PDU**.
   - Hacer clic en la ficha de **Detalles de la PDU saliente**.

#### 📝 Preguntas sobre DNS

**Pregunta 11**: ¿Qué información se indica en **NOMBRE**: en la sección **CONSULTA DNS**?

3. **Examinar respuesta DNS**:
   - Hacer clic en el último cuadro coloreado **Información** de DNS en la lista de eventos.

#### 📝 Preguntas sobre respuesta DNS

**Pregunta 12**: ¿En qué dispositivo se capturó la PDU?

**Pregunta 13**: ¿Cuál es el valor que se indica junto a **DIRECCIÓN**: en la sección **RESPUESTA DE DNS** de Detalles de la PDU entrante?

4. **Examinar protocolo TCP**:
   - Buscar el primer evento de **HTTP** en la lista.
   - Hacer clic en el cuadro coloreado del evento de **TCP** que le sigue inmediatamente.
   - Resaltar **capa 4** en la ficha **Modelo OSI**.

#### 📝 Preguntas sobre TCP

**Pregunta 14**: En la lista numerada que está directamente debajo de Capas de entrada y Capas de salida, ¿cuál es la información que se muestra en los elementos 4 y 5?

5. **Examinar cierre de conexión TCP**:
   - Hacer clic en el último evento de TCP.
   - Resaltar capa 4 en la ficha **Modelo OSI**.
   - Examinar los pasos que se indican directamente a continuación de **Capas de entrada** y **Capas de salida**.

#### 📝 Pregunta sobre cierre TCP

**Pregunta 15**: ¿Cuál es el propósito de este evento, según la información proporcionada en el último elemento de la lista (debe ser el elemento 4)?

---

## 🎯 Preguntas de desafío

### 🌐 Análisis de puertos de servidor

Basándose en la información analizada durante la captura de Packet Tracer:

**Pregunta 16**: ¿Qué número de puerto escucha el servidor web para detectar la solicitud web?

**Pregunta 17**: ¿Qué puerto escucha el servidor web para detectar una solicitud de DNS?

---

## 📊 Criterios de evaluación

### 🎯 Evaluación técnica (70%)

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Comprensión de encapsulamiento** | 25% | Correcta identificación de PDU en cada capa |
| **Análisis de protocolos** | 25% | Identificación y explicación de protocolos TCP/IP |
| **Relación OSI-TCP/IP** | 20% | Comprensión de la correspondencia entre modelos |

### 🎨 Evaluación del trabajo (30%)

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Respuestas a preguntas** | 15% | Respuestas correctas y justificadas |
| **Presentación** | 15% | Documento bien estructurado y claro |

---

## 🛠️ Herramientas requeridas

### 💻 Software
- **Cisco Packet Tracer** (versión actualizada)
- **Archivo de práctica**: Descargar el archivo .pkt correspondiente

### 📝 Documentación
- **Word/Google Docs**: Para el informe de respuestas
- **Capturas de pantalla**: Para evidenciar los resultados

---

## 📋 Entregables

### 📄 Informe de respuestas
- **Formato**: PDF
- **Contenido**:
  - Respuestas a todas las preguntas planteadas
  - Capturas de pantalla de los eventos más importantes
  - Explicaciones detalladas del proceso de encapsulamiento
  - Análisis de la correspondencia entre modelos OSI y TCP/IP

### 🖼️ Evidencias gráficas
- **Capturas de pantalla** de:
  - Configuración de filtros
  - PDU en diferentes capas
  - Detalles de protocolos (HTTP, DNS, TCP)
  - Ventanas de información de PDU

---

## ⏰ Cronograma de trabajo

| Sesión | Actividad | Duración |
|--------|-----------|----------|
| **1** | Configuración inicial y Parte 1 (HTTP) | 2 horas |
| **2** | Parte 2 (Protocolos TCP/IP) y análisis | 2 horas |
| **3** | Respuestas y documentación | 1 hora |

---

## 📚 Conceptos clave a demostrar

### 🔄 Proceso de encapsulamiento
- **Capa 7 (Aplicación)**: Datos HTTP
- **Capa 4 (Transporte)**: Segmentos TCP
- **Capa 3 (Red)**: Datagramas IP
- **Capa 2 (Enlace)**: Tramas Ethernet
- **Capa 1 (Física)**: Bits

### 🌐 Protocolos analizados
- **HTTP**: Protocolo de aplicación web
- **DNS**: Resolución de nombres
- **TCP**: Control de transporte
- **IP**: Encaminamiento de red
- **Ethernet**: Acceso al medio
- **ARP**: Resolución de direcciones

---

## ✅ Checklist de entrega

Antes de entregar, verifica que incluyas:

- [ ] Respuestas a todas las 17 preguntas planteadas
- [ ] Capturas de pantalla de eventos clave
- [ ] Explicación del proceso de encapsulamiento
- [ ] Análisis de correspondencia entre modelos
- [ ] Documento en formato PDF con nombre correcto

---

## 🎓 Competencias desarrolladas

### 🔧 Competencias técnicas
- Comprensión del modelo OSI y TCP/IP
- Análisis de protocolos de red
- Interpretación de PDU en diferentes capas
- Uso de herramientas de simulación

### 🤝 Competencias transversales
- Análisis crítico
- Documentación técnica
- Resolución de problemas
- Trabajo metodológico

---

!!! tip "<span style=\"font-size: 1.4em;\"><strong>CONSEJO FINAL</strong></span>"
    <span style=\"font-size: 1.3em;\">Esta práctica es fundamental para comprender cómo funcionan realmente las redes. Presta especial atención al proceso de encapsulamiento y desencapsulamiento, ya que es la base de toda comunicación en red.</span>
