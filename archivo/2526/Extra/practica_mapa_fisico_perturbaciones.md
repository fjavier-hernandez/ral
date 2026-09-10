---
title: Práctica - Mapa físico con perturbaciones
description: Práctica para diseñar un mapa físico de red local identificando perturbaciones y sus soluciones.
subtitle: Transmisión de Datos
# tags:
#     - Práctica
#     - RA1
---

# 🗺️ PRÁCTICA: MAPA FÍSICO CON PERTURBACIONES

Esta práctica tiene como objetivo que los estudiantes diseñen un mapa físico de una red local en una empresa ficticia, identificando los medios de transmisión utilizados y señalando posibles puntos de perturbación, así como las soluciones técnicas apropiadas.

## 📚 Propuesta didáctica

En esta práctica trabajamos el **RA1 de RAL**:

> **RA1.** *Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes.*

### 🎯 Criterios de evaluación trabajados

* **CE1d**: Se han identificado y clasificado los medios de transmisión.
* **CE1e**: Se ha reconocido el mapa físico de la red local.

### 🎯 Objetivos de la práctica

* Identificar y clasificar los diferentes medios de transmisión en una red local.
* Reconocer el mapa físico de una red local empresarial.
* Identificar puntos de perturbación en la transmisión de datos.
* Proponer soluciones técnicas para mitigar las perturbaciones.
* Desarrollar habilidades de diseño y planificación de redes.

---

## 📋 Descripción de la práctica

### 🏢 Contexto empresarial

Diseña el mapa físico de una red local para una empresa ficticia con las siguientes características:

**Características de la empresa:**
- **Nombre**: Tecnologías Avanzadas S.L.
- **Ubicación**: Edificio de 3 plantas
- **Empleados**: 25 trabajadores
- **Departamentos**: Administración, Ventas, Desarrollo, Almacén

**Distribución del edificio:**
- **Planta baja**: Recepción, Almacén, Servidor principal
- **Primera planta**: Administración, Ventas
- **Segunda planta**: Desarrollo, Sala de reuniones

### 🔧 Requisitos técnicos

**Dispositivos a conectar:**
- 25 ordenadores de sobremesa
- 8 portátiles
- 5 impresoras
- 2 servidores
- 1 router principal
- 3 switches
- 1 punto de acceso WiFi

**Servicios requeridos:**
- Conexión a Internet
- Servidor de archivos
- Servidor de correo
- Acceso WiFi en zonas comunes

---

## 🗺️ Elementos a incluir en el mapa físico

### 📡 Medios de transmisión

Identifica y documenta los siguientes medios de transmisión:

#### 🔗 Medios guiados
- **Cable de par trenzado UTP Cat6**: Para conexiones de escritorio
- **Cable de par trenzado STP Cat6A**: Para áreas con alta interferencia
- **Fibra óptica multimodo**: Para conexiones entre plantas
- **Cable coaxial**: Para conexiones de seguridad

#### 📶 Medios inalámbricos
- **WiFi 6 (802.11ax)**: Para dispositivos móviles
- **Bluetooth**: Para periféricos

### ⚠️ Puntos de perturbación identificados

#### 🔥 Ruido térmico
- **Ubicación**: Sala de servidores
- **Causa**: Alta concentración de equipos electrónicos
- **Efecto**: Degradación de la señal en cables cercanos

#### ⚡ Ruido impulsivo
- **Ubicación**: Almacén (cerca de ascensor)
- **Causa**: Motor del ascensor
- **Efecto**: Pulsos de alta amplitud que corrompen datos

#### 📡 Interferencia electromagnética (EMI)
- **Ubicación**: Primera planta (cerca de transformador eléctrico)
- **Causa**: Transformador del edificio
- **Efecto**: Interferencia en señales de radiofrecuencia

#### 📉 Atenuación
- **Ubicación**: Conexiones entre plantas
- **Causa**: Longitud excesiva de cables
- **Efecto**: Pérdida de señal en distancias largas

#### 📐 Distorsión
- **Ubicación**: Cableado cerca de conductos eléctricos
- **Causa**: Campos electromagnéticos de la instalación eléctrica
- **Efecto**: Deformación de la señal digital

---

## 🛠️ Soluciones técnicas propuestas

### 🔄 Repetidores
- **Ubicación**: Entre plantas para amplificar señal
- **Tipo**: Repetidores digitales para regenerar señal
- **Justificación**: Compensar atenuación en distancias largas

### ⚖️ Ecualizadores
- **Ubicación**: En puntos de alta distorsión
- **Tipo**: Ecualizadores adaptativos
- **Justificación**: Corregir distorsión de amplitud

### 🛡️ Cableado apantallado
- **Ubicación**: Almacén y primera planta
- **Tipo**: STP Cat6A
- **Justificación**: Reducir interferencia electromagnética

### 🔧 Otras soluciones
- **Separación de cableado**: Mantener distancia de 30cm con instalación eléctrica
- **Toma de tierra**: Correcta instalación de sistemas de puesta a tierra
- **Filtros**: Instalación de filtros de línea para equipos sensibles

---

## 📊 Criterios de evaluación

### 🎯 Evaluación técnica (70%)

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Identificación de medios** | 20% | Correcta clasificación y justificación de medios de transmisión |
| **Detección de perturbaciones** | 25% | Identificación precisa de puntos de perturbación y sus causas |
| **Soluciones propuestas** | 25% | Apropiadas y técnicamente correctas |

### 🎨 Evaluación del diseño (30%)

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Claridad del mapa** | 15% | Diseño claro y fácil de interpretar |
| **Presentación** | 15% | Formato profesional y organizado |

---

## 🛠️ Herramientas recomendadas

### 🎨 Software de diseño
- **Excalidraw**: Para crear diagramas de red
- **Draw.io**: Alternativa gratuita
- **Visio**: Para presentaciones profesionales

### 📝 Documentación
- **Word/Google Docs**: Para el informe técnico
- **PowerPoint/Google Slides**: Para presentación oral

---

## 📋 Entregables

### 🗺️ Mapa físico de la red
- **Formato**: Digital (Excalidraw o similar)
- **Contenido**: 
  - Distribución física de dispositivos
  - Medios de transmisión utilizados
  - Puntos de perturbación identificados
  - Soluciones técnicas implementadas

### 📄 Informe técnico
- **Formato**: PDF
- **Contenido**:
  - Descripción de la empresa y requisitos
  - Justificación de medios de transmisión
  - Análisis de perturbaciones
  - Soluciones propuestas y su justificación
  - Conclusiones y recomendaciones

### 🎤 Presentación oral
- **Duración**: 10-15 minutos
- **Contenido**:
  - Exposición del mapa físico
  - Explicación de perturbaciones identificadas
  - Justificación de soluciones propuestas
  - Ronda de preguntas

---

## ⏰ Cronograma de trabajo

| Sesión | Actividad | Duración |
|--------|-----------|----------|
| **1** | Análisis de requisitos y diseño inicial | 2 horas |
| **2** | Identificación de perturbaciones | 1 hora |
| **3** | Propuesta de soluciones técnicas | 1 hora |
| **4** | Elaboración del mapa físico | 2 horas |
| **5** | Redacción del informe técnico | 2 horas |
| **6** | Preparación de presentación | 1 hora |
| **7** | Presentación oral | 15 minutos/grupo |

---

## 📚 Recursos de apoyo

### 📖 Documentación técnica
- Apuntes de transmisión de datos
- Estándares de cableado (TIA/EIA-568)
- Manuales de equipos de red

### 🔗 Enlaces útiles
- [Guía de diseño de redes locales](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/network-design.html)
- [Estándares de cableado estructurado](https://www.tiaonline.org/)
- [Herramientas de diseño de red](https://www.draw.io/)

---

## 🎓 Competencias desarrolladas

### 🔧 Competencias técnicas
- Análisis de requisitos de red
- Diseño de infraestructura de red
- Identificación y resolución de problemas técnicos
- Aplicación de estándares de la industria

### 🤝 Competencias transversales
- Trabajo en equipo
- Comunicación técnica
- Presentación de resultados
- Resolución de problemas

---

## ✅ Checklist de entrega

Antes de entregar, verifica que incluyas:

- [ ] Mapa físico completo con todos los elementos
- [ ] Identificación de al menos 5 tipos de perturbaciones
- [ ] Propuesta de soluciones técnicas para cada perturbación
- [ ] Justificación técnica de las decisiones tomadas
- [ ] Informe técnico completo y bien estructurado
- [ ] Presentación oral preparada
- [ ] Archivos en formato PDF con nombre correcto (AC307.pdf)

---

!!! tip "<span style=\"font-size: 1.4em;\"><strong>CONSEJO FINAL</strong></span>"
    <span style=\"font-size: 1.3em;\">Recuerda que un buen diseño de red no solo considera los aspectos técnicos, sino también la escalabilidad, mantenibilidad y coste-efectividad de la solución propuesta.</span>
