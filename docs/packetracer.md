---
title: Introducción Packet tracer
description: Guía inical para uso del simulador Packet tracer.
subtitle: Guía inical Packet tracer
# tags:
#     - Introducción Redes
#     - RA1
---

# Cisco Packet Tracer

## ¿Qué es Packet Tracer?

**Packet Tracer** es una herramienta de simulación desarrollada por **Cisco Systems** que permite diseñar, configurar y simular redes informáticas sin necesidad de hardware físico. Es ampliamente utilizada en entornos educativos, especialmente en los cursos de **Cisco Networking Academy**, para enseñar conceptos de redes y practicar la configuración de dispositivos como routers, switches, PCs, servidores, etc.

### Características principales

- 🖥️ **Simulación de redes**: Permite crear topologías de red complejas con dispositivos virtuales.
- 🎨 **Interfaz gráfica intuitiva**: Facilita el diseño visual de redes.
- 💻 **Práctica de comandos CLI**: Se pueden usar comandos reales de Cisco IOS en los dispositivos simulados.
- 🔍 **Modo de simulación**: Permite observar el paso a paso del tráfico de red (paquetes) para entender cómo se comporta la red.
- 🧑‍🏫 **Ideal para estudiantes**: No requiere conocimientos avanzados para empezar, pero permite profundizar en configuraciones avanzadas.
- 🧭 **Multiplataforma**: Disponible para Windows, macOS y Linux.

### Usos comunes en FP

- Configuración de redes **LAN y WAN**.
- Prácticas de **direccionamiento IP**, **VLANs**, **routing estático y dinámico**.
- Simulación de servicios como **DHCP**, **DNS**, **HTTP**, **FTP**, etc.
- Diagnóstico y resolución de problemas de red.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/pCo4554JpG8?start=3" 
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen 
          title="YouTube video player"></iframe>
</div>

---

> 📌 *Packet Tracer es una herramienta esencial para el aprendizaje práctico en el ámbito de las redes, especialmente útil en el módulo de Redes de Área Local del ciclo de grado medio en Sistemas Microinformáticos y Redes.*

## **Instalación de Packet Tracer:**

*   Descarga el Packet Tracer desde la [Página Oficial de Cisco Netcad](https://www.netacad.com/resources/lab-downloads?courseLang=es-XL).
*   Instala siguiendo las instrucciones del instalador.
*   Una vez instalado ejecútalo y selecciona la primera opción (Networking Academy)
*   No es obligatorio pero accederás a un sinfín de cursos certificados de Cisco.

### Interfaz de Usuario

Packet Tracer es una herramienta que permite simular redes reales. Proporcione tres menús principales que puede utilizar para lo siguiente:

*   Puede agregar dispositivos y conectarlos a través de cables o de forma inalámbrica.
*   Puede seleccionar, eliminar, inspeccionar, etiquetar y agrupar componentes dentro de la red.
*   Administre su red

El menú de administración de red le permite hacer lo siguiente:

*   Abrir una red existente/de muestra
*   Guarda tu red actual
*   Modifica tu perfil de usuario o tus preferencias

### 🎬 Video: Navegación por la interfaz de Packet Tracer

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/XBnJUFnyvak"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="YouTube video player"></iframe>
</div>



## Implementación de dispositivos

### 🎬 Video: Implementación de dispositivos en Packet Tracer



<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/KgLeIjlk2so?list=PLjd5U-zhuKDYieZE3qS9gyaaNZpszANbx"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen 
          title="YouTube video player"></iframe>
</div>


### Configuración de GUI y CLI

Packet Tracer proporciona varias pestañas para configurar los dispositivos. Las pestañas disponibles dependen del tipo de dispositivo que se esté configurando:

- **Física**
- **Configuración**
- **CLI**
- **Escritorio**
- **Servicios**

> **Nota:** Es posible que veas otras pestañas en diferentes dispositivos. Estas pestañas adicionales están fuera del alcance de este curso.

---

#### 🧩 Pestaña Física

Permite interactuar con el dispositivo: encenderlo, apagarlo o instalar módulos como tarjetas de red inalámbricas (NIC).

---

#### 🖱️ Pestaña Configuración

Ofrece dos formas de configurar dispositivos intermedios (como routers y switches):

- **GUI exclusiva de Packet Tracer**: Ideal para quienes no dominan la CLI.
- **CLI simulada**: Se muestran los comandos equivalentes en la ventana **Comandos IOS equivalentes**.

Esto facilita el aprendizaje del sistema operativo IOS de Cisco.

> Por ejemplo, si se configura el nombre del dispositivo como `MyRouter`, se muestra el comando CLI equivalente en la ventana correspondiente.

También permite **guardar, cargar, borrar y exportar** archivos de configuración.

---

#### 💻 Pestaña CLI

Proporciona acceso directo a la línea de comandos de dispositivos Cisco. Requiere conocimientos previos de IOS.

> **Nota:** Los comandos introducidos desde la pestaña Configuración también se reflejan aquí.

---

#### 🖥️ Pestaña Escritorio

Disponible en dispositivos finales como PCs y portátiles. Permite configurar:

- IP
- Conexión inalámbrica
- Navegador web
- Símbolo del sistema
- Otras aplicaciones

---

#### 🛠️ Pestaña Servicios

Exclusiva de servidores. Permite configurar servicios como:

- HTTP
- DHCP
- DNS
- Otros servicios de red

---

### Actividad Supervisada PTTA

### Usando actividades PTTA - Modelo Lógico y Físico

El siguiente paso es la actividad con tutoría de Packet Tracer. ¡Aquí hay algunos videos tutoriales que quizás quiera revisar antes de lanzarse!


#### 🎬 Video: Cómo usar actividades .pka en Packet Tracer

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/G0pkHyo3rwg?list=PLjd5U-zhuKDYieZE3qS9gyaaNZpszANbx"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen 
          title="YouTube video player"></iframe>
</div>


<!-- 
[Ver video sobre actividades .pka](https://www.youtube.com/watch?v=ENL6v5lHn9g) <!-- Sustituye este enlace por el real si tienes otro -->




<!-- ### Packet Tracer: cree una red simple


En esta actividad de Packet Tracer, completará los siguientes objetivos:

*   Parte 1: Crear una red simple
*   Parte 2: Configurar los dispositivos finales y verificar la conectividad -->

#### 🎬 Video: Funciones avanzadas de Packet Tracer

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/TZtYOfj6SE0?list=PLjd5U-zhuKDYieZE3qS9gyaaNZpszANbx"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="YouTube video player"></iframe>
</div>


#### 🎬 Video: Navegación por la interfaz de Packet Tracer

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/6v_tiQpKoL0"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="YouTube video player"></iframe>
</div>

---

#### 🎬 Video: Implementación de dispositivos en Packet Tracer



<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/elCwLFaBdbI"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="YouTube video player"></iframe>
</div>

---

Packet Tracer proporciona varias pestañas para configurar dispositivos:

- **Física**: encendido/apagado, instalación de módulos (NIC, etc.).
- **Configuración (GUI)**: configuración básica con equivalencia CLI.
- **CLI**: acceso completo a la línea de comandos Cisco IOS.
- **Escritorio**: configuración IP, navegador, símbolo del sistema.
- **Servicios**: configuración de servicios como HTTP, DHCP, DNS.

> **Nota**: Las pestañas varían según el dispositivo. Algunas pestañas son exclusivas de Packet Tracer y no simulan funcionalidad real.

---

#### 🧑‍🏫 Cargar Actividades


### 🎬 Video: Cómo usar actividades .pka en Packet Tracer

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/6S_F-7nZZ8c"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="YouTube video player"></iframe>
</div>

---





