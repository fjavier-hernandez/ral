---
title: Apuntes - Transmisión de datos y perturbaciones
description: Apuntes sobre transmisión de datos, técnicas de codificación y perturbaciones en redes.
subtitle: Introducción Redes
# tags:
#     - Transmisión Datos
#     - RA1
---

# 📡 TRANSMISIÓN DE DATOS Y PERTURBACIONES

La transmisión de datos es fundamental en las redes de comunicaciones. En este tema estudiamos cómo se transmiten los datos a través de diferentes medios, las técnicas de codificación utilizadas y las perturbaciones que pueden afectar a la calidad de la transmisión.

## 📚 Propuesta didáctica

En esta unidad trabajamos el **RA1 de RAL**:

> **RA1.** *Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes.*

### 🎯 Criterios de evaluación

#### Criterios de evaluación del RA1

* **CE1a**: Se han descrito los principios de funcionamiento de las redes locales.
* **CE1c**: Se han descrito los elementos de la red local y su función.
* **CE1d**: Se han identificado y clasificado los medios de transmisión.
* **CE1e**: Se ha reconocido el mapa físico de la red local.
* **CE1g**: Se han identificado estructuras alternativas.

### Contenidos

* Medios de transmisión: guiados e inalámbricos.
* Técnicas de codificación: NRZ, Manchester, AM, FM, PM.
* Tipos de transmisión: serie, paralelo, simplex, half-duplex, full-duplex.
* Perturbaciones: ruido, atenuación, distorsión.
* Soluciones a las perturbaciones: repetidores, ecualizadores, cableado apantallado.

!!! question "Cuestionario inicial"
    1. ¿Qué diferencias existen entre transmisión analógica y digital?
    2. ¿Cuáles son las ventajas e inconvenientes de la transmisión en serie frente a la paralela?
    3. ¿Qué tipos de ruido pueden afectar a una transmisión de datos?
    4. ¿Para qué sirven los repetidores en una red?
    5. ¿Qué es la codificación Manchester y por qué se utiliza?
    6. ¿Cuándo es necesario usar cableado apantallado?

## Programación de Aula (8h)

Esta unidad se imparte en la primera evaluación, con una duración estimada de 8 sesiones lectivas:

| Sesión | Contenidos | Actividades | Criterios trabajados |
|--------|------------|-------------|----------------------|
| 1 | Medios de transmisión guiados e inalámbricos | Cuestionario inicial, AC301 | CE1d |
| 2 | Técnicas de codificación (NRZ, Manchester) | Actividad AC302 | CE1a, CE1c |
| 3 | Modulación analógica (AM, FM, PM) | Actividad AC303 | CE1a, CE1c |
| 4 | Tipos de transmisión (serie/paralelo, simplex/duplex) | Actividad AC304 | CE1a, CE1g |
| 5 | Perturbaciones en la transmisión | Actividad AC305 | CE1e, CE1d |
| 6 | Soluciones a las perturbaciones | Actividad AC306 | CE1e, CE1d |
| 7 | Práctica integradora: mapa físico con perturbaciones | AC307 | CE1e, CE1d |
| 8 | Evaluación y repaso | Evaluación | Todos los criterios |

---

## 🔌 Medios de transmisión

Los medios de transmisión son el soporte físico a través del cual se propagan las señales que transportan la información. Se pueden clasificar en dos grandes grupos:

### 📡 Medios guiados

Los medios guiados utilizan un conductor físico para dirigir las señales desde el emisor hasta el receptor.

#### 🔗 Cable de par trenzado

**Características:**
- Formado por dos conductores de cobre aislados y entrelazados
- El trenzado reduce la interferencia electromagnética
- Puede ser **UTP** (no apantallado) o **STP** (apantallado)

**Categorías principales:**
- **Categoría 5e**: Velocidad hasta 1 Gbps, distancia hasta 100m
- **Categoría 6**: Velocidad hasta 10 Gbps, distancia hasta 100m
- **Categoría 6A**: Velocidad hasta 10 Gbps, distancia hasta 100m con mejor rendimiento

**Ventajas:**
- ✅ Bajo coste
- ✅ Fácil instalación
- ✅ Amplia compatibilidad

**Desventajas:**
- ❌ Limitada distancia de transmisión
- ❌ Sensible a interferencias
- ❌ Ancho de banda limitado

#### 🌐 Cable coaxial

**Características:**
- Formado por un conductor central rodeado por una malla conductora
- Separados por un dieléctrico aislante
- Todo protegido por una cubierta exterior

**Tipos:**
- **RG-58**: Uso en redes Ethernet antiguas (10BASE2)
- **RG-6**: Televisión por cable e Internet de banda ancha
- **RG-59**: Señales de video y audio

**Ventajas:**
- ✅ Mayor ancho de banda que par trenzado
- ✅ Menor susceptibilidad a interferencias
- ✅ Mayor distancia de transmisión

**Desventajas:**
- ❌ Mayor coste
- ❌ Instalación más compleja
- ❌ Menor flexibilidad

#### 🔦 Fibra óptica

**Características:**
- Transmite señales mediante pulsos de luz
- Formada por un núcleo de vidrio o plástico
- Recubierta por una capa de material con menor índice de refracción

**Tipos:**
- **Multimodo**: Núcleo de 50-62.5 μm, distancia hasta 2 km
- **Mon modo**: Núcleo de 8-10 μm, distancia hasta 40 km

**Ventajas:**
- ✅ Ancho de banda muy elevado
- ✅ Inmune a interferencias electromagnéticas
- ✅ Distancias de transmisión muy largas
- ✅ Seguridad (difícil interceptación)

**Desventajas:**
- ❌ Alto coste
- ❌ Instalación especializada
- ❌ Equipos de conexión costosos

### 📶 Medios inalámbricos

Los medios inalámbricos utilizan el espacio libre para transmitir señales electromagnéticas.

#### 📡 Radiofrecuencia

**Características:**
- Utiliza ondas de radio para la transmisión
- Frecuencias típicas: 2.4 GHz, 5 GHz, 6 GHz
- Puede ser omnidireccional o direccional

**Estándares WiFi:**
- **802.11n (WiFi 4)**: Hasta 600 Mbps
- **802.11ac (WiFi 5)**: Hasta 6.9 Gbps
- **802.11ax (WiFi 6)**: Hasta 9.6 Gbps

**Ventajas:**
- ✅ Movilidad
- ✅ Facilidad de instalación
- ✅ Escalabilidad

**Desventajas:**
- ❌ Interferencias
- ❌ Seguridad
- ❌ Limitaciones de distancia

#### 🔴 Infrarrojos

**Características:**
- Utiliza luz infrarroja para la transmisión
- Requiere línea de vista directa
- Distancias cortas (hasta 10 metros)

**Aplicaciones:**
- Mandos a distancia
- Transferencia de datos entre dispositivos móviles
- Comunicación entre equipos en espacios cerrados

---

## 🔧 Técnicas de codificación

La codificación es el proceso de convertir la información digital en señales que puedan ser transmitidas por el medio físico.

### 📊 Codificación digital

#### 🔲 NRZ (Non-Return to Zero)

**Características:**
- **Nivel alto (1)**: Voltaje positivo
- **Nivel bajo (0)**: Voltaje negativo o cero
- No hay retorno a cero entre bits

**Ventajas:**
- ✅ Simplicidad
- ✅ Eficiencia en ancho de banda

**Desventajas:**
- ❌ Problemas de sincronización
- ❌ Componente DC

#### 🔄 Manchester

**Características:**
- **Bit 1**: Transición de alto a bajo en el centro del bit
- **Bit 0**: Transición de bajo a alto en el centro del bit
- Siempre hay transición en el centro

**Ventajas:**
- ✅ Autosincronización
- ✅ Sin componente DC
- ✅ Detección de errores

**Desventajas:**
- ❌ Doble ancho de banda
- ❌ Mayor complejidad

### 📻 Modulación analógica

#### 📡 AM (Amplitud Modulada)

**Características:**
- La amplitud de la portadora varía según la señal moduladora
- Frecuencia y fase constantes
- Sensible a ruido y interferencias

**Aplicaciones:**
- Radiodifusión AM
- Algunos sistemas de comunicación por cable

#### 📶 FM (Frecuencia Modulada)

**Características:**
- La frecuencia de la portadora varía según la señal moduladora
- Amplitud constante
- Más resistente al ruido que AM

**Aplicaciones:**
- Radiodifusión FM
- Sistemas de comunicación móvil

#### 📐 PM (Fase Modulada)

**Características:**
- La fase de la portadora varía según la señal moduladora
- Amplitud y frecuencia constantes
- Relacionada con FM

**Aplicaciones:**
- Sistemas de comunicación digital
- Modems

---

## 🔄 Tipos de transmisión

### 📏 Según el número de conductores

#### 📍 Transmisión en serie

**Características:**
- Los bits se envían uno tras otro por un único conductor
- Requiere sincronización entre emisor y receptor
- Utiliza menos cables

**Ventajas:**
- ✅ Menor coste de cableado
- ✅ Distancias mayores
- ✅ Menos interferencias

**Desventajas:**
- ❌ Velocidad menor
- ❌ Mayor complejidad

**Aplicaciones:**
- USB
- RS-232
- Ethernet

#### 📊 Transmisión en paralelo

**Características:**
- Múltiples bits se envían simultáneamente por varios conductores
- Un conductor por bit
- Mayor velocidad de transmisión

**Ventajas:**
- ✅ Mayor velocidad
- ✅ Simplicidad de sincronización

**Desventajas:**
- ❌ Mayor coste de cableado
- ❌ Limitaciones de distancia
- ❌ Problemas de sincronización a alta velocidad

**Aplicaciones:**
- Buses internos del ordenador
- Conexiones IDE/SATA antiguas

### 🔄 Según la dirección de transmisión

#### ➡️ Simplex

**Características:**
- Transmisión unidireccional
- Un dispositivo siempre emite, otro siempre recibe
- No hay comunicación bidireccional

**Ejemplos:**
- Televisión
- Radiodifusión
- Sensores de temperatura

#### 🔄 Half-Duplex

**Características:**
- Transmisión bidireccional alternada
- Solo un dispositivo puede transmitir a la vez
- Requiere control de acceso al medio

**Ejemplos:**
- Walkie-talkies
- Ethernet con hubs
- RS-485

#### ↔️ Full-Duplex

**Características:**
- Transmisión bidireccional simultánea
- Ambos dispositivos pueden transmitir y recibir al mismo tiempo
- Requiere canales separados o multiplexación

**Ejemplos:**
- Teléfono
- Ethernet con switches
- USB

---

## ⚠️ Perturbaciones en la transmisión

Las perturbaciones son fenómenos que degradan la calidad de la señal durante la transmisión, afectando la integridad de los datos.

### 🔇 Ruido

#### 🔥 Ruido térmico

**Características:**
- Generado por el movimiento aleatorio de electrones en los conductores
- Presente en todos los sistemas electrónicos
- Independiente de la señal
- Aumenta con la temperatura

**Efectos:**
- Degradación de la relación señal/ruido
- Errores en la recepción de datos
- Limitación de la distancia de transmisión

#### ⚡ Ruido impulsivo

**Características:**
- Pulsos de alta amplitud y corta duración
- Causado por fenómenos externos (rayos, motores, etc.)
- Puede corromper múltiples bits

**Fuentes:**
- Descargas eléctricas
- Motores eléctricos
- Sistemas de encendido de vehículos
- Aparatos domésticos

#### 📡 Interferencia electromagnética (EMI)

**Características:**
- Señales no deseadas de otras fuentes
- Puede ser radiada o conducida
- Frecuencias específicas

**Fuentes:**
- Transmisores de radio
- Motores eléctricos
- Lámparas fluorescentes
- Equipos informáticos

### 📉 Atenuación

**Características:**
- Reducción de la amplitud de la señal con la distancia
- Proporcional a la longitud del medio
- Dependiente de la frecuencia

**Efectos:**
- Reducción de la relación señal/ruido
- Limitación de la distancia máxima
- Degradación de la calidad de la señal

**Factores que influyen:**
- Resistencia del conductor
- Capacitancia del cable
- Inductancia del cable
- Frecuencia de la señal

### 📐 Distorsión

#### ⏰ Distorsión de retardo

**Características:**
- Diferentes frecuencias viajan a velocidades distintas
- Causa dispersión temporal de la señal
- Especialmente problemática en señales digitales

**Efectos:**
- Ensanchamiento de los pulsos
- Interferencia entre símbolos
- Errores de sincronización

#### 📊 Distorsión de amplitud

**Características:**
- Diferentes frecuencias sufren atenuaciones distintas
- Causada por la respuesta en frecuencia no plana del medio
- Afecta la forma de la señal

**Efectos:**
- Deformación de la forma de onda
- Pérdida de información
- Errores de demodulación

---

## 🛠️ Soluciones a las perturbaciones

### 🔄 Repetidores

**Función:**
- Regeneran la señal digital
- Amplifican la señal analógica
- Corrigen la atenuación

**Tipos:**
- **Repetidores digitales**: Regeneran la señal sin amplificar el ruido
- **Repetidores analógicos**: Amplifican señal y ruido por igual

**Aplicaciones:**
- Extensión de redes Ethernet
- Sistemas de telefonía
- Transmisiones de radio

### ⚖️ Ecualizadores

**Función:**
- Compensan la distorsión de amplitud
- Corrigen la respuesta en frecuencia del canal
- Mejoran la calidad de la señal

**Tipos:**
- **Ecualizadores lineales**: Filtros adaptativos
- **Ecualizadores no lineales**: Decision feedback equalizers (DFE)

**Aplicaciones:**
- Modems
- Sistemas de comunicación digital
- Transmisiones de alta velocidad

### 🛡️ Cableado apantallado

**Función:**
- Reduce la interferencia electromagnética
- Protege contra el ruido externo
- Mejora la relación señal/ruido

**Tipos:**
- **STP (Shielded Twisted Pair)**: Apantallamiento individual
- **FTP (Foiled Twisted Pair)**: Apantallamiento global
- **S/FTP**: Apantallamiento individual y global

**Aplicaciones:**
- Entornos industriales
- Instalaciones con alta interferencia
- Sistemas críticos

### 🔧 Otras soluciones

#### 📡 Diversidad espacial

**Función:**
- Múltiples antenas en diferentes posiciones
- Reduce los efectos del desvanecimiento
- Mejora la fiabilidad

#### 🔄 Codificación de canal

**Función:**
- Añade redundancia a la información
- Permite detectar y corregir errores
- Mejora la robustez de la transmisión

**Tipos:**
- **Códigos de bloque**: Hamming, Reed-Solomon
- **Códigos convolucionales**: Turbo codes, LDPC

---

## 🛠️ Actividades

!!! tip "<span style=\"font-size: 1.4em;\"><strong>Formato de entrega</strong></span>"
    <span style=\"font-size: 1.3em;\">Para la entrega de las actividades, genera un documento con la práctica descrita a continuación. Deberás crear un archivo PDF con el siguiente formato de nombre: <strong>ACXXX.pdf</strong>, donde las X representan el número de la actividad. Una vez finalizada la práctica, sube el archivo a Aules (antes de la fecha de vencimiento) para su calificación.</span>

### AC301: Clasificación de medios de transmisión
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1d

**Descripción:**  
Completa una tabla comparativa con los distintos medios de transmisión (guiados e inalámbricos), indicando sus características, ventajas, desventajas y ejemplos de uso en redes locales.

**Producto final:**  
Tabla en formato digital con ejemplos reales (fibra óptica en casa, WiFi en el instituto, etc.).

### AC302: Técnicas de codificación digital
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1a, CE1c

**Descripción:**  
Realiza esquemas gráficos de las técnicas de codificación NRZ y Manchester, mostrando cómo se codifican diferentes secuencias de bits. Incluye las ventajas e inconvenientes de cada técnica.

**Producto final:**  
Documento con esquemas y análisis comparativo.

### AC303: Modulación analógica
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1a, CE1c

**Descripción:**  
Explica las técnicas de modulación AM, FM y PM mediante diagramas y ejemplos. Indica las aplicaciones típicas de cada una.

**Producto final:**  
Documento explicativo con diagramas y ejemplos de aplicación.

### AC304: Tipos de transmisión
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1a, CE1g

**Descripción:**  
Compara los tipos de transmisión serie vs paralelo y simplex vs half-duplex vs full-duplex. Incluye ejemplos de aplicaciones reales para cada tipo.

**Producto final:**  
Tabla comparativa con ejemplos de uso.

### AC305: Perturbaciones en la transmisión
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1e, CE1d

**Descripción:**  
Identifica y describe los diferentes tipos de perturbaciones (ruido, atenuación, distorsión) que pueden afectar a una transmisión de datos. Incluye sus causas y efectos.

**Producto final:**  
Documento explicativo con ejemplos de cada tipo de perturbación.

### AC306: Soluciones a las perturbaciones
**Tipo:** Individual  
**Duración:** 1 sesión  
**Criterios trabajados:** CE1e, CE1d

**Descripción:**  
Describe las diferentes soluciones técnicas para combatir las perturbaciones en la transmisión (repetidores, ecualizadores, cableado apantallado, etc.).

**Producto final:**  
Documento con descripción de soluciones y casos de aplicación.

### AC307: Mapa físico con perturbaciones
**Tipo:** Trabajo en grupo  
**Duración:** 2 sesiones  
**Criterios trabajados:** CE1e, CE1d

**Descripción:**  
Diseña un mapa físico de una red local en una empresa ficticia, incluyendo los medios de transmisión y señalando posibles puntos de perturbación (ruido, atenuación, distorsión). Justifica el uso de repetidores, ecualizadores o cableado apantallado.

**Herramientas:** Excalidraw, papel, presentación oral.

**Producto final:**  
Mapa físico de la red con identificación de perturbaciones y soluciones propuestas.
