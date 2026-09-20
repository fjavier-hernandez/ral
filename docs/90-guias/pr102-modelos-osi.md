---
title: PR102 — Modelos OSI/TCP en Packet Tracer
description: Guion de práctica — encapsulación HTTP/TCP/IP/Ethernet en simulación.
---

# PR102 — Modelos OSI y TCP/IP en Packet Tracer

Guion de aula / Aules. Enunciado corto y rúbrica también en el [Tema 1](../01-introduccion-arquitectura/tema1.md#pr102-modelos-en-packet-tracer).

## Objetivos

- Relacionar capas **OSI** y **TCP/IP** con lo que muestra Packet Tracer.
- Observar **encapsulación** en una petición web (HTTP sobre TCP/IP/Ethernet).
- Identificar tráfico **DNS**, **ARP** y **TCP** además de HTTP.

## Requisitos

- [Guía inicial Packet Tracer](packet-tracer.md) (instalación e interfaz).
- Cisco Packet Tracer instalado.
- Topología del profesor (archivo `.pkt` / `.pka` en **Aules**) **o** la mini-topología de la sección «Si aún no hay archivo».

## Si aún no hay archivo NetAcad

Monta una LAN mínima:

1. 1× **PC** (cliente), 1× **Server-PT**, 1× **Switch** 2960.
2. Cables rectos PC—switch y server—switch.
3. En el servidor: IP `192.168.1.254/24`, servicio **HTTP** y **DNS** activos; registro A `www.osi.local` → `192.168.1.254`.
4. En el PC: IP `192.168.1.10/24`, DNS `192.168.1.254`, puerta de enlace la que indique el guion (o ninguna si solo hay LAN).

(Cuando NetAcad esté activo, sustituid esto por el lab oficial que indiquemos.)

---

## Parte 1 — Tráfico HTTP

1. Abre la topología. Pasa a modo **Simulación**.
2. **Editar filtros** → desactiva todo y deja solo **HTTP**.
3. En el **PC** → Escritorio → **Navegador web** → URL `www.osi.local` → Ir.
4. Pulsa **Capturar/Avanzar** varias veces hasta ver eventos HTTP.
5. Abre el primer evento HTTP → pestaña **Modelo OSI**:
   - Capa 7: petición HTTP al servidor.
   - Capa 4: puerto destino **80**.
   - Capa 3: IP destino del servidor.
   - Capa 2: MAC origen/destino.
6. En **Detalles PDU**: anota IP origen/destino, puertos TCP y host HTTP.

## Parte 2 — DNS, ARP y TCP

1. En filtros, **Mostrar todo** (o activa DNS, ARP, TCP, HTTP).
2. Localiza un evento **DNS** (consulta del nombre) y la **respuesta** (IP resuelta).
3. Localiza **ARP** si aparece (resolución MAC).
4. Localiza eventos **TCP** (apertura / ESTABLISHED / cierre).

## Qué entregar (`PR102.md` + capturas)

En el `.md` (plantilla Aules):

1. Captura modo Simulación con eventos visibles (HTTP y al menos DNS o TCP).
2. Tabla breve: capa (OSI o TCP/IP) | qué viste en esa capa en la PDU HTTP.
3. Respuestas (una o dos frases cada una):
   - ¿Qué puerto escucha el servidor web para HTTP?
   - ¿Qué puerto usa DNS?
   - En la respuesta del servidor, ¿qué se intercambia respecto a IP/MAC/puertos?
4. (Opcional) Archivo `.pkt` si lo modificasteis.

**Escala:** PR 0–10 según rúbrica del Tema 1 / Aules.

## Nota NetAcad

Esta semana se activa la plataforma del centro. Los labs `.pka` oficiales se enlazarán en Aules; PR102 con topología propia **cuenta** igual mientras tanto.
