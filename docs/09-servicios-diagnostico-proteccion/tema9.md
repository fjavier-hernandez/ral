---
title: Tema 9 — Servicios, diagnóstico y protección
description: Capa de aplicación (DHCP, DNS, HTTP, FTP); resolución de incidencias; protección, soporte y PRL.
---

# Tema 9. Servicios, diagnóstico y protección

Cerramos el módulo uniendo tres piezas que en el día a día del técnico van juntas: los **servicios de aplicación** que usa el usuario, el **diagnóstico de incidencias** cuando algo falla y las medidas de **protección, soporte y prevención de riesgos**.

!!! tip "Primera clase"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). No hace falta estudiar el tema completo antes: el cuestionario sirve para ver qué sabes al empezar.

## Propuesta didáctica

Trabajamos sobre todo los **RA5** y **RA6** del módulo Redes de área local (0225):

> **RA5.** *Mantiene una red local interpretando recomendaciones de los fabricantes de hardware o software y estableciendo la relación entre disfunciones y sus causas.*

> **RA6.** *Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y equipos para prevenirlos.*

También reforzamos, de forma puntual, la identificación de **protocolos de aplicación** (relacionado con el trabajo previo de capas).

### Criterios de evaluación (RA5)

* **CE5a**: Se han identificado incidencias y comportamientos anómalos.
* **CE5b**: Se ha identificado si la disfunción es debida al hardware o al software.
* **CE5c**: Se han monitorizado las señales visuales de los dispositivos de interconexión.
* **CE5d**: Se han verificado los protocolos de comunicaciones.
* **CE5e**: Se ha localizado la causa de la disfunción.
* **CE5f**: Se ha restituido el funcionamiento sustituyendo equipos o elementos.
* **CE5g**: Se han solucionado las disfunciones software (configurando o reinstalando).
* **CE5h**: Se ha elaborado un informe de incidencias.

### Criterios de evaluación (RA6)

* **CE6a**: Se han identificado los riesgos y el nivel de peligrosidad que suponen la manipulación de los materiales, herramientas, útiles, máquinas y medios de transporte.
* **CE6b**: Se han operado las máquinas respetando las normas de seguridad.
* **CE6c**: Se han identificado las causas más frecuentes de accidentes en la manipulación de materiales, herramientas, máquinas de corte y conformado, entre otras.
* **CE6d**: Se han descrito los elementos de seguridad (protecciones, alarmas, pasos de emergencia, entre otros) de las máquinas y los equipos de protección individual (calzado, protección ocular, indumentaria, entre otros) que se deben emplear en las operaciones de montaje y mantenimiento.
* **CE6e**: Se ha relacionado la manipulación de materiales, herramientas y máquinas con las medidas de seguridad y protección personal requeridos.
* **CE6f**: Se han identificado las posibles fuentes de contaminación del entorno ambiental.
* **CE6g**: Se han clasificado los residuos generados para su retirada selectiva.
* **CE6h**: Se ha valorado el orden y la limpieza de instalaciones y equipos como primer factor de prevención de riesgos.

### Contenidos

* Capa de aplicación TCP/IP: idea de servicio cliente/servidor.
* Servicios habituales en LAN/Internet: **DHCP**, **DNS**, **HTTP/HTTPS**, **FTP/TFTP** (visión SMR).
* Tipos de incidencias: IP duplicada, DNS, cableado, saturación, configuración.
* Método de diagnóstico: identificar → aislar → resolver → verificar → documentar.
* Herramientas: `ping`, `tracert`/`traceroute`, `ipconfig`/`ip`, `nslookup`/`dig`, `netstat`, captura básica.
* Protección y soporte: filtrado, firewall, logs, actualizaciones, copias de seguridad, documentación.
* PRL y protección ambiental en taller de redes (EPI, riesgos eléctricos, RAEE, orden y limpieza).

### Programación de aula (orientativa, ~14–16 h)

| Sesiones | Contenidos | Actividades |
| --- | --- | --- |
| 1 | Presentación + cuestionario inicial | Cuestionario |
| 2–4 | Capa de aplicación: DHCP, DNS, HTTP/FTP | **AC901–AC903** |
| 5–6 | Packet Tracer: servicios de aplicación | **PR901** |
| 7–9 | Diagnóstico de incidencias + herramientas | AC904, AC905, **PR902** |
| 10–11 | Protección, vigilancia, soporte y documentación | AC906, AC907 |
| 12–13 | PRL y protección ambiental en el taller | **AC908**, vínculo con [Normas del taller](../00-normas/normas_taller.md) |
| 14–16 | Proyecto: incidente completo + informe | **PY901** / PO cuando toque |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Antes de empezar — responde con lo que sepas"
    1. ¿Qué hace un servidor DHCP? ¿Y un DNS?
    2. ¿Qué diferencia hay entre HTTP y HTTPS?
    3. ¿Qué harías si dos PCs de la misma LAN “pierden” la red a la vez?
    4. Nombra tres comandos para diagnosticar conectividad en Windows o Linux.
    5. ¿Qué es un firewall y para qué sirve en una red local?
    6. ¿Por qué es útil documentar la red (planos, inventario, historial de incidencias)?
    7. ¿Qué riesgos hay al crimpar cables o manipular un rack conectado a la corriente?
    8. ¿Qué son los RAEE y dónde deben depositarse?

!!! warning "Soluciones"
    Las soluciones se trabajan en clase o se publican en Aules cuando proceda.

---

## Capa de aplicación

En TCP/IP, la **capa de aplicación** es la más cercana al usuario: los programas intercambian datos mediante **protocolos de aplicación**. En OSI, muchas de esas funciones se reparte entre aplicación, presentación y sesión; en la práctica SMR trabajamos la visión **TCP/IP**.

Un **servicio de red** permite compartir recursos (impresión, archivos, nombres, direcciones…) entre equipos. Lo habitual es el modelo **cliente/servidor**: el cliente solicita; el servidor responde.

| Servicio | Idea clave | Puerto habitual |
| --- | --- | --- |
| **DHCP** | Asigna IP, máscara, puerta de enlace, DNS… | UDP 67/68 |
| **DNS** | Traduce nombres ↔ direcciones IP | UDP/TCP 53 |
| **HTTP / HTTPS** | Acceso a contenido web | TCP 80 / 443 |
| **FTP / TFTP** | Transferencia de ficheros | TCP 21 (+datos) / UDP 69 |

!!! note "Relación con temas previos"
    Ya usaste puertos y TCP/UDP en el [Tema 7](../07-capa-transporte/tema7.md). Aquí nos centramos en **qué hace** cada servicio y cómo comprobarlo.

### DHCP

El **DHCP** (*Dynamic Host Configuration Protocol*) evita configurar a mano cada host. El servidor gestiona un **pool** de direcciones y entrega parámetros de red.

Modos habituales de asignación:

- **Manual / reserva**: IP fija asociada a una MAC (impresoras, servidores).
- **Automática**: se asigna y se mantiene hasta que el cliente la libera.
- **Dinámica (con lease)**: la IP se usa un tiempo limitado y se renueva.

Ventajas: menos errores de IP duplicada, configuración centralizada, menos tiempo de administración.  
Riesgo: si cae el servidor DHCP (y no hay reservas/estáticas), muchos clientes pueden perder conectividad al renovar.

### DNS

Memorizar direcciones IP es incómodo. El **DNS** (*Domain Name System*) resuelve **nombres** a direcciones (y viceversa).

- Se puede configurar el DNS en el **equipo** o en el **router** (los clientes suelen heredar el del router).
- Además del DNS del ISP existen resolvers públicos (p. ej. 1.1.1.1, 8.8.8.8, 9.9.9.9).
- Un DNS mal configurado o manipulado puede impedir el acceso a servicios o redirigir a destinos no deseados (privacidad / phishing).

Herramientas de comprobación: `nslookup`, `dig`, o la pestaña DNS del navegador / del sistema.

### HTTP, HTTPS y FTP

- **HTTP**: protocolo de la Web. **HTTPS** añade cifrado (TLS) y autenticación del servidor.
- **FTP**: transferencia de archivos (en producción se prefiere SFTP/FTPS; en el aula a menudo se simula FTP clásico).
- **TFTP**: variante simple (sin autenticación fuerte); típica en arranque de equipos de red o laboratorios.

En Packet Tracer puedes montar servidores DNS/HTTP/DHCP y comprobar el acceso por **nombre**, no solo por IP.

---

## Resolución de conflictos e incidencias

Cuando “la red no va”, el técnico necesita un **método**, no solo intuición.

### Incidencias habituales

| Tipo | Síntoma típico | Primera comprobación |
| --- | --- | --- |
| **IP duplicada** | Cortes intermitentes en dos hosts | `ipconfig` / `ip a`; escaneo de la LAN |
| **DNS** | “No carga la web” pero el ping a IP sí | `nslookup` / cambiar DNS de prueba |
| **Cableado / enlace** | LED apagado, sin enlace | cable, puerto, latiguillo, panel |
| **Saturación** | Todo va lento | quién consume ancho de banda; QoS |
| **Configuración** | Solo un VLAN / solo un segmento falla | gateway, ruta, ACL, firewall |

### Método de trabajo (RA5)

1. **Identificar** la incidencia y el comportamiento anómalo (CE5a).
2. Decidir si parece **hardware o software** (CE5b); mirar **LEDs** y estado de interfaces (CE5c).
3. **Verificar protocolos** y servicios implicados (CE5d): ¿IP? ¿DNS? ¿HTTP? ¿DHCP?
4. **Aislar** el alcance (un PC, un switch, toda la LAN) y **localizar la causa** (CE5e).
5. **Restituir**: cambiar cable/equipo o reconfigurar/reinstalar (CE5f, CE5g).
6. **Documentar** en un informe de incidencias (CE5h).

### Herramientas de diagnóstico (visión SMR)

**Windows (ejemplos):** `ipconfig`, `ping`, `tracert`, `nslookup`, `netstat`, `arp`, `route`, `netsh`.  
**GNU/Linux (ejemplos):** `ip`, `ping`, `traceroute`, `dig`/`nslookup`, `ss`/`netstat`, `nmap` (solo con autorización), captura con `tcpdump` / Wireshark.

!!! warning "Ética y autorización"
    Escaneos (`nmap`) y capturas de tráfico solo en redes del **aula / laboratorio** y con permiso del profesor. No se escanean redes ajenas.

---

## Protección, vigilancia y soporte

### Filtrado y control de acceso

- **Firewall / cortafuegos**: permite o bloquea tráfico según políticas (IP, puerto, protocolo; a veces por aplicación).
- **Filtros de contenido** y de correo: reducen acceso a sitios no deseados o spam/phishing.
- **Filtrado por MAC**: útil en entornos pequeños; no sustituye una política de seguridad completa (las MAC se pueden falsificar).

### Vigilancia y mantenimiento

- Observar tráfico y señales de los equipos (LEDs, cargas, errores de interfaz).
- Revisar **logs** de routers/switches/servicios.
- Mantener **firmware** y software al día (parches de seguridad).
- **Copias de seguridad** de configuraciones y de datos críticos.
- Acceso remoto controlado (RDP, VNC, SSH…): solo con cuentas y políticas adecuadas.

### Documentación de la red

Sin documentación, cada incidencia se reinventa. Como mínimo conviene:

- Diagrama lógico/físico (Excalidraw / draw.io / Dia).
- Inventario (equipo, IP, MAC, ubicación, rol).
- Parámetros clave (VLANs, gateways, DHCP pools, DNS).
- Políticas básicas de seguridad.
- **Historial de incidencias** (qué pasó, causa, solución, tiempo).

---

## Prevención de riesgos y protección ambiental (RA6)

El mantenimiento de redes se hace en **taller y en racks**: hay riesgos eléctricos, cortes, caídas de equipos y residuos.

| Ámbito | Qué debes aplicar |
| --- | --- |
| Riesgos | Electricidad, herramientas de crimpado, peso de equipos, cableado suelto (CE6a, CE6c) |
| Normas de trabajo | Desconectar antes de abrir; no forzar conectores; avisar ante humo/olor/calor (CE6b, CE6e) |
| EPI / protecciones | Guantes ESD cuando proceda, protección ocular si hay corte de cable, calzado adecuado (CE6d) |
| Ambiente | No tirar electrónica a la basura; **RAEE** al contenedor indicado (CE6f, CE6g) |
| Orden | Puesto limpio, cables recogidos, herramientas en su caja (CE6h) |

Lee y aplica las [Normas del taller](../00-normas/normas_taller.md): son el marco práctico de este apartado en el centro.

---

## Actividades

!!! tip "Formato de entrega"
    Las entregas en **Aules** son **obligatorias en Markdown** (`.md`). No se aceptan PDF.  
    Nombre del archivo: `AC9XX.md`, `PR9XX.md` o `PY9XX.md` (sustituye XX por el número). Respeta la fecha de vencimiento.  
    Escribiremos los `.md` con **Visual Studio Code**.

    !!! note "Cómo empezar"
        - Guía de Markdown: [tutorialmarkdown.com/guia](https://tutorialmarkdown.com/guia)
        - Documentación de Visual Studio Code: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)

### AC901 — Servicio DHCP

* :simple-readdotcv: **AC901**. (RA5 // CE5d // **AC 0–1**). Explica con tus palabras qué es DHCP, los tres modos de asignación y dos ventajas + un riesgo si falla el servidor. Indica un ejemplo de dispositivo que convenga reservar por MAC.

### AC902 — Servicio DNS

* :simple-readdotcv: **AC902**. (RA5 // CE5d // **AC 0–1**). Describe el proceso “escribo un nombre en el navegador → llega el contenido”. Incluye el papel del DNS y qué probarías si la web no resuelve pero el `ping` a una IP pública sí funciona.

### AC903 — HTTP/HTTPS y FTP

* :simple-readdotcv: **AC903**. (RA5 // CE5d // **AC 0–1**). Tabla comparativa HTTP / HTTPS / FTP: para qué sirven, puerto orientativo y un riesgo de seguridad de cada uno (o de usarlo sin cifrado).

### AC904 — Tipos de incidencias

* :simple-readdotcv: **AC904**. (RA5 // CE5a, CE5b, CE5e // **AC 0–1**). Para cada caso, indica causa probable (HW/SW), primer comando o comprobación y siguiente paso:

    1. Dos portátiles pierden Internet a ratos; el resto de la clase no.
    2. Nadie resuelve nombres; el ping a `8.8.8.8` funciona.
    3. Un único PC no tiene enlace (LED apagado en el switch).

### AC905 — Caja de herramientas de diagnóstico

* :simple-readdotcv: **AC905**. (RA5 // CE5c, CE5d, CE5e // **AC 0–1**). Elige **Windows o Linux**. Lista 6 comandos de diagnóstico, qué muestra cada uno y en qué tipo de incidencia lo usarías. Incluye al menos uno de resolución de nombres y uno de ruta (`tracert`/`traceroute`).

### AC906 — Filtrado y firewall

* :simple-readdotcv: **AC906**. (RA5 // CE5a, CE5d // **AC 0–1**). Propón una política **restrictiva** mínima para un aula: qué se permite salir (DNS, HTTP/HTTPS, …) y qué bloquearías. Justifica dos bloqueos.

### AC907 — Documentar la red

* :simple-readdotcv: **AC907**. (RA5 // CE5h // **AC 0–1**). Plantilla en `.md` de documentación mínima: inventario (4 equipos inventados), parámetros IP/DNS/gateway y un historial con **una** incidencia ficticia ya resuelta.

### AC908 — PRL en el taller de redes

* :simple-readdotcv: **AC908**. (RA6 // CE6a, CE6b, CE6c, CE6d, CE6e, CE6f, CE6g, CE6h // **AC 0–1**). Partiendo de las [Normas del taller](../00-normas/normas_taller.md), elabora una ficha con: 4 riesgos, cómo operas las herramientas/máquinas con seguridad, EPI/medidas asociadas, 2 causas frecuentes de accidente, fuentes de contaminación del entorno y qué haces con residuos de cableado/electrónica (**RAEE**).

### PR901 — Servicios de aplicación en Packet Tracer

* :simple-cisco: **PR901**. (RA5 // CE5d, CE5e, CE5h // **PR 0–10**). Simulación: topología propia (no copies un esquema ajeno al pie de la letra) con DHCP, DNS y HTTP. Debes poder abrir la web **por nombre** desde un PC cliente. Documenta direccionamiento, capturas y comprobaciones en `PR901.md`. El guion detallado se facilitará en clase / Aules.

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Topología coherente | Dispositivos y enlaces correctos | 0–2 |
| DHCP operativo | Cliente obtiene IP y parámetros | 0–2 |
| DNS + HTTP | Acceso por nombre verificado | 0–3 |
| Documentación `.md` | Clara, con evidencias | 0–3 |
| **Total** | | **/10** |

### PR902 — Laboratorio de diagnóstico

* :simple-neutralinojs: **PR902**. (RA5 // CE5a–CE5h // **PR 0–10**). El profesor introduce **una o varias fallas** en el escenario de aula/PT. Debéis: identificar síntomas, clasificar HW/SW, localizar causa, corregir y entregar informe `PR902.md` (pasos, comandos, evidencia, solución).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Identificación | Síntomas y alcance | 0–2 |
| Método | Orden lógico de pruebas | 0–2 |
| Causa | Localización correcta | 0–3 |
| Resolución + informe | Arreglo y CE5h | 0–3 |
| **Total** | | **/10** |

### PY901 — Incidente completo (cierre del tema)

* :material-calendar: **PY901**. (RA5 // CE5a–CE5h // RA6 // CE6a, CE6d, CE6e, CE6h // **PY 0–30**). En grupo pequeño: escenario de incidencia (suministrado o acordado). Entregables en Markdown + diagrama (Excalidraw / draw.io / Dia):

    1. Descripción del incidente y impacto.
    2. Hipótesis HW/SW y plan de pruebas.
    3. Resolución aplicada y verificación.
    4. Informe de incidencia (plantilla).
    5. Apartado PRL: riesgos del procedimiento, EPI y orden del puesto.

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Análisis del incidente | Claridad y alcance | 0–6 |
| Diagnóstico técnico | Método y evidencias | 0–8 |
| Resolución y verificación | Solución coherente | 0–6 |
| Informe y diagrama | Documentación usable | 0–6 |
| PRL | Riesgos, EPI, orden | 0–4 |
| **Total** | | **/30** |

### PO901 — Prueba objetiva (cuando toque)

* :material-pen: **PO901**. (RA5, RA6 // **PO 0–100**). Examen escrito o en ordenador sobre servicios de aplicación, diagnóstico y PRL. Fecha y formato se anuncian en Aules.

---

## Referencias y fuentes

- Inspiración didáctica (reesrito; no es copia literal): Marcos Ruiz — [Capa de aplicación](https://marcosruiz.github.io/posts/capa-aplicacion/), [Resolución de conflictos en una red local](https://marcosruiz.github.io/posts/resolucion-conflictos-lan/), [Protección, vigilancia y soporte de redes](https://marcosruiz.github.io/posts/proteccion-vigilancia-soporte-redes/), índice [Redes Locales 22‑23](https://marcosruiz.github.io/posts/redes-locales-22-23/) (UD16–UD18).
- Criterios de evaluación: [RD 1691/2007](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2008-819), módulo **0225**.
- Diagramas: [Excalidraw](https://excalidraw.com/), [draw.io](https://app.diagrams.net/), [Dia](https://wiki.gnome.org/Apps/Dia)
- Simulación: [Cisco Packet Tracer](https://www.netacad.com/es/cisco-packet-tracer)
- Entregas: [Visual Studio Code](https://code.visualstudio.com/docs) + [Markdown](https://tutorialmarkdown.com/guia)
- Normas: [Normas del taller](../00-normas/normas_taller.md)
- Tema previo (puertos/TCP-UDP): [Tema 7](../07-capa-transporte/tema7.md)

*[RA]: Resultado de aprendizaje  
*[CE]: Criterio de evaluación  
*[AC]: Actividad de clase  
*[PR]: Práctica  
*[PY]: Proyecto  
*[PO]: Prueba objetiva  
*[DHCP]: Dynamic Host Configuration Protocol  
*[DNS]: Domain Name System  
*[HTTP]: Hypertext Transfer Protocol  
*[FTP]: File Transfer Protocol  
*[PRL]: Prevención de riesgos laborales  
*[RAEE]: Residuos de Aparatos Eléctricos y Electrónicos  
*[EPI]: Equipo de protección individual
