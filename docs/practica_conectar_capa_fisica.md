---
title: Práctica - Conectar la Capa Física en Packet Tracer
description: Práctica para identificar características físicas de dispositivos, seleccionar módulos y conectar dispositivos usando Packet Tracer.
subtitle: Capa Física
# tags:
#     - Práctica
#     - RA2
---

# 🔌 PRÁCTICA: CONECTAR LA CAPA FÍSICA EN PACKET TRACER

Esta práctica tiene como objetivo explorar las diversas opciones disponibles en los dispositivos de interconexión de redes. Aprenderás a identificar las características físicas de los dispositivos, seleccionar los módulos correctos para la conectividad y realizar conexiones entre dispositivos de red.

## 📚 Propuesta didáctica

En esta práctica trabajamos el **RA2 de RAL**:

> **RA2.** *Reconoce los medios de transmisión y tipos de cableado de redes locales analizando sus características y campos de aplicación.*

### 🎯 Criterios de evaluación trabajados

* **CE2a**: Se han identificado los medios de transmisión utilizados en redes locales.
* **CE2b**: Se han clasificado los tipos de cableado según su aplicación.
* **CE2c**: Se han relacionado los medios de transmisión con las tecnologías de red.

### 🎯 Objetivos de la práctica

* Identificar las características físicas de los dispositivos de interconexión de redes.
* Seleccionar los módulos correctos para proporcionar la conectividad necesaria.
* Conectar correctamente los dispositivos utilizando los tipos de cable adecuados.
* Verificar la conectividad de la red configurada.

---

## 📋 Descripción de la práctica

### 🔧 Aspectos básicos

En esta actividad, explorarás las diversas opciones disponibles en los dispositivos de interconexión de redes. También deberás determinar las opciones que proporcionan la conectividad necesaria cuando debas conectar varios dispositivos. Finalmente, agregarás los módulos correctos y conectarás los dispositivos.

Esta práctica es fundamental para comprender cómo funciona físicamente la capa de red, identificando puertos, interfaces y módulos de expansión en dispositivos reales de red.

---

## 🛠️ Instrucciones detalladas

### 📊 Parte 1: Identificar las características físicas de los dispositivos de interconexión de redes

#### Paso 1: Identifique los puertos de administración de un enrutador Cisco

a. Haga clic en el **Router Este**. La **pestaña Física** debe estar activa.

b. Acérquese y expanda la ventana para ver todo el enrutador.

**Preguntas:**

- ¿Qué puertos de administración están disponibles?
- ¿Qué interfaces LAN y WAN están disponibles en el Router **Este** y cuántas hay?

c. Haga clic en la ficha **CLI**, presione la **tecla Intro** para acceder al símbolo del modo de usuario y escriba los siguientes comandos:

```
Este> show ip interface brief
```

La salida verifica el número correcto de interfaces y su designación. La interfaz vlan1 es una interfaz virtual que sólo existe en el software.

**Pregunta:**

- ¿Cuántas interfaces físicas se enumeran?

d. Ingrese los siguientes comandos:

```
Este> show interface gigabitethernet 0/0
```

**Pregunta:**

- ¿Cuál es el ancho de banda predeterminado de esta interfaz?

```
Este> show interface serial 0/0/0
```

**Pregunta:**

- ¿Cuál es el ancho de banda predeterminado de esta interfaz?

!!! note "NOTA"
    El ancho de banda en las interfaces seriales es utilizado por los procesos de enrutamiento para determinar la mejor ruta de acceso a un destino. No indica el ancho de banda real de la interfaz. El ancho de banda real se negocia con un proveedor de servicios.

#### Paso 2: Identifique los módulos de expansión

**Preguntas:**

- ¿Cuántas ranuras de expansión están disponibles para agregar más módulos al router **Este**?
- Haga clic en **Switch2**. ¿Cuántas ranuras de expansión están disponibles?

---

### 🔌 Parte 2: Seleccionar los módulos correctos para la conectividad

#### Paso 1: Determine qué módulos proporcionan la conectividad requerida

a. Haga clic en **Este** y, a continuación, haga clic en la ficha **Physical (Capa física)**. A la izquierda, debajo de la etiqueta **Módulos**, verá las opciones disponibles para expandir las capacidades del enrutador. Haga clic en cada módulo. En la parte inferior, se muestra una imagen y una descripción. Familiarícese con estas opciones.

**Preguntas:**

1. Necesitas conectar las PCs 1, 2 y 3 al router **Este**, pero no tienes los fondos necesarios para comprar un nuevo switch. ¿Qué módulo puedes usar para conectar las tres PCs al router **Este**?
2. ¿Cuántos hosts puedes conectar al router usando este módulo?

b. Haga clic en **Switch2**.

**Pregunta:**

- ¿Qué módulo se puede insertar para proporcionar una conexión óptica Gigabit al **Switch3**?

#### Paso 2: Agregue los módulos correctos y dispositivos de encendido

a. Haga clic en **Este** e intente insertar el módulo adecuado del paso 1a. Los módulos se agreやan haciendo clic en el módulo y arrastrándolo a la ranura vacía del dispositivo.

!!! warning "IMPORTANTE"
    No se puede agregar un módulo cuando se muestra el mensaje de encendido. Las interfaces para este modelo de router no son intercambiables en caliente. El dispositivo debe estar apagado antes de agregar o quitar módulos.

Haga clic en el interruptor de encendido ubicado a la derecha del logotipo de Cisco para apagar **el Este**. Inserte el módulo adecuado del paso 1a. Cuando haya terminado, haga clic en el interruptor de alimentación para encender el router **Este**.

!!! tip "CONSEJO"
    Si insertas el módulo incorrecto y necesitas quitarlo, arrastra el módulo hasta su imagen en la esquina inferior derecha y suelta el botón del mouse.

b. Con el mismo procedimiento, inserte el módulo que identificó en el Paso 1b en la ranura vacía más a la derecha en **Switch2**.

c. Use el comando `show ip interface brief` en **Switch2** para identificar la ranura en la que se colocó el módulo.

**Pregunta:**

- ¿En qué ranura se insertó?

---

### 🔗 Parte 3: Conectar los dispositivos

Esta puede ser la primera actividad que has realizado en la que se te requiere conectar dispositivos. Aunque es posible que no conozcas el propósito de los diferentes tipos de cables, utiliza la tabla siguiente y sigue estas pautas para conectar correctamente todos los dispositivos:

a. Seleccione el tipo de cable adecuado.

b. Haga clic en el primer dispositivo y seleccione la interfaz especificada.

c. Haga clic en el segundo dispositivo y seleccione la interfaz especificada.

d. Si conectó correctamente los dos dispositivos, verá que su puntuación aumenta.

!!! example "EJEMPLO"
    Para conectar **Este** al **Switch1**, seleccione el tipo de **cable directo de cobre**. Haga clic en **Este** y elija **GigabitEthernet0/0**. Luego, haga clic en **Switch1** y elija **GigabitEthernet0/1**. Su puntuación ahora debería ser 4/55.

!!! note "NOTA"
    Para esta actividad, las luces de enlace no están habilitadas.

#### 📋 Tabla de conexiones

| Dispositivo | Interfaz | Tipo de cable | Dispositivo | Interfaz |
|------------|----------|---------------|-------------|----------|
| East | GigabitEthernet0/0 | Cable de cobre directo | Switch1 | GigabitEthernet0/1 |
| East | GigabitEthernet0/1 | Cable de cobre directo | Switch4 | GigabitEthernet0/1 |
| East | FastEthernet0/1/0 | Cable de cobre directo | PC1 | FastEthernet0 |
| East | FastEthernet0/1/1 | Cable de cobre directo | PC2 | FastEthernet0 |
| East | FastEthernet0/1/2 | Cable de cobre directo | PC3 | FastEthernet0 |
| Switch1 | FastEthernet0/1 | Cable de cobre directo | PC4 | FastEthernet0 |
| Switch1 | FastEthernet0/2 | Cable de cobre directo | PC5 | FastEthernet0 |
| Switch1 | FastEthernet0/3 | Cable de cobre directo | PC6 | FastEthernet0 |
| Switch4 | GigabitEthernet0/2 | Cable de cobre cruzado | Switch3 | GigabitEthernet3/1 |
| Switch3 | GigabitEthernet5/1 | Fibra | Switch2 | GigabitEthernet5/1 |
| Switch2 | FastEthernet0/1 | Cable de cobre directo | PC7 | FastEthernet0 |
| Switch2 | FastEthernet1/1 | Cable de cobre directo | PC8 | FastEthernet0 |
| Switch2 | FastEthernet2/1 | Cable de cobre directo | PC9 | FastEthernet0 |
| Switch2 | Gigabit3/1 | Cable de cobre directo | AccessPoint | Port 0 |
| East | Serial0/0/0 | DCE serial (conectar primero a East) | West | Serial0/0/0 |

---

### ✅ Parte 4: Verificar la conectividad

#### Paso 1: Comprobar el estado de la interfaz en Este

a. Haga clic en la ficha **CLI** e introduzca los siguientes comandos:

```
Este> show ip interface brief
```

Compare la salida con lo siguiente:

| Interface | IP-Address | OK? | Method | Status | Protocol |
|-----------|------------|-----|--------|--------|----------|
| GigabitEthernet0/0 | 172.30.1.1 | YES | manual | up | up |
| GigabitEthernet0/1 | 172.31.1.1 | YES | manual | up | up |
| Serial0/0/0 | 10.10.10.1 | YES | manual | up | up |
| Serial0/0/1 | unassigned | YES | unset | down | down |
| FastEthernet0/1/0 | unassigned | YES | unset | up | up |
| FastEthernet0/1/1 | unassigned | YES | unset | up | up |
| FastEthernet0/1/2 | unassigned | YES | unset | up | up |
| FastEthernet0/1/3 | unassigned | YES | unset | down | down |
| Vlan1 | 172.29.1.1 | YES | manual | up | up |

Si todo el cableado es correcto, las salidas deben coincidir.

#### Paso 2: Conecte dispositivos inalámbricos, portátiles y TabletPC

a. Haga clic en el portátil y seleccione la pestaña **Config**. Seleccione la interfaz **Wireless0**. Ponga una marca en la casilla marcada **On** junto a **Estado del puerto**. En unos segundos debería aparecer la conexión inalámbrica.

b. Haga clic en la ficha **Escritorio** de la computadora portátil. Haga clic en el icono del **navegador web** del Dock para abrir el navegador web. Escriba `www.cisco.pka` en el cuadro URL y haga clic en **Ir**. La página debe mostrar **Cisco Packet Tracer**.

c. Haga clic en **TabletPC** y seleccione la pestaña **Config**. Seleccione la interfaz **Wireless0**. Ponga una marca en la casilla marcada **On** junto a **Estado del puerto**. En unos segundos debería aparecer la conexión inalámbrica.

d. Repita los pasos del paso 2b para comprobar que se muestra la página.

#### Paso 3: Cambie el método de acceso de la TabletPC

a. Haga clic en **TabletPC** y seleccione la pestaña **Config**. Seleccione la interfaz **Wireless0**. Desmarque la casilla **On** junto a **Estado del puerto**. Ahora debería ser claro y la conexión inalámbrica se caerá.

b. Haga clic en la interfaz **3G/4G Cell1**. Ponga una marca en la casilla marcada **On** junto a **Estado del puerto**. Dentro de unos segundos debería aparecer la conexión celular.

c. Repita el proceso de verificación del acceso web.

!!! warning "IMPORTANTE"
    No debe tener tanto la interfaz Wireless0 como las interfaces 3G/4G Cell1 activas al mismo tiempo. Esto puede causar confusión al dispositivo al intentar conectarse a algunos recursos.

#### Paso 4: Compruebe la conectividad de los otros equipos

Todos los equipos deben tener conectividad con el sitio web y entre sí. Aprenderás a usar las pruebas de conectividad en muchos laboratorios próximos.

---

## 📊 Criterios de evaluación

### 🎯 Evaluación técnica (70%)

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Identificación de interfaces** | 25% | Correcta identificación de puertos y características físicas |
| **Selección de módulos** | 25% | Selección adecuada de módulos según necesidades de conectividad |
| **Conexión de dispositivos** | 20% | Conexiones correctas según tabla proporcionada |

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
  - Capturas de pantalla de las configuraciones realizadas
  - Tabla de conexiones completada con estados verificados
  - Explicaciones sobre la selección de módulos y tipos de cable

### 🖼️ Evidencias gráficas
- **Capturas de pantalla** de:
  - Interfaces identificadas en los dispositivos
  - Módulos seleccionados y añadidos
  - Conexiones realizadas
  - Salida de comandos `show ip interface brief`
  - Verificación de conectividad web

---

## ⏰ Cronograma de trabajo

| Sesión | Actividad | Duración |
|--------|-----------|----------|
| **1** | Parte 1: Identificación de características físicas | 1 hora |
| **2** | Parte 2: Selección e inserción de módulos | 1 hora |
| **3** | Parte 3: Conexión de dispositivos | 1 hora |
| **4** | Parte 4: Verificación de conectividad | 1 hora |
| **5** | Documentación y respuestas | 1 hora |

---

## 📚 Conceptos clave a demostrar

### 🔌 Características físicas
- **Puertos de administración**: Consola, AUX
- **Interfaces LAN/WAN**: GigabitEthernet, FastEthernet, Serial
- **Ranuras de expansión**: Módulos intercambiables

### 🔧 Tipos de cables
- **Cable de cobre directo**: Para conexiones disímiles (PC-Switch, PC-Router, Router-Switch)
- **Cable de cobre cruzado**: Para conexiones similares (Switch-Switch, Router-Router)
- **Cable de fibra óptica**: Para conexiones de alta velocidad
- **Cable serial DCE**: Para conexiones punto a punto WAN

### 📡 Conectividad inalámbrica
- **Wireless**: Conexión WiFi a Access Points
- **3G/4G**: Conexión celular para dispositivos móviles

---

## ✅ Checklist de entrega

Antes de entregar, verifica que incluyas:

- [ ] Respuestas a todas las preguntas planteadas
- [ ] Capturas de pantalla de interfaces identificadas
- [ ] Evidencia de módulos añadidos correctamente
- [ ] Tabla de conexiones con verificaciones
- [ ] Salida del comando `show ip interface brief`
- [ ] Verificación de conectividad web
- [ ] Documento en formato PDF con nombre correcto (PR308.pdf)

---

## 🎓 Competencias desarrolladas

### 🔧 Competencias técnicas
- Identificación de componentes físicos de dispositivos de red
- Selección de módulos de expansión apropiados
- Conocimiento de tipos de cables y su aplicación
- Configuración y verificación de conectividad básica

### 🤝 Competencias transversales
- Análisis técnico
- Resolución de problemas
- Documentación técnica
- Trabajo metodológico

---

!!! tip "<span style=\"font-size: 1.4em;\"><strong>CONSEJO FINAL</strong></span>"
    <span style=\"font-size: 1.3em;\">Esta práctica te proporcionará una base sólida para comprender la capa física de las redes. Presta especial atención a los diferentes tipos de cables y cuándo usar cada uno, ya que es fundamental para el trabajo futuro con redes.</span>

