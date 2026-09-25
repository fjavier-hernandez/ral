---
title: PR103 — Mi primera red en Packet Tracer
description: Guion de práctica — montar una LAN con switch y cuatro PC, IP y ping.
---

# PR103 — Mi primera red en Packet Tracer

Enunciado corto y rúbrica en el [Tema 1](../01-introduccion-arquitectura/tema1.md#pr103-mi-primera-red-en-packet-tracer).

Vas a montar tu primera red local: un **switch** y **cuatro ordenadores**, les das dirección IP y compruebas que se comunican. No partimos de un archivo `.pkt` del profesor: lo construyes tú desde cero. Antes necesitas Packet Tracer con la sesión iniciada; si aún no lo tienes listo, sigue la [guía inicial](packet-tracer.md).

## Vídeo 1 — Paso a paso

Mira del **1:23 al 10:04**. Él monta dos PC; tú montarás **cuatro**, con el mismo método.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/9xWQGuoVhPM?start=83&end=604"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="Curso Cisco Packet Tracer #1 · Conecta 2 PCs con un Switch y Haz Ping (Escuela de Informática)"></iframe>
</div>

!!! tip "Avisos sobre el vídeo"
    En el vídeo pone la IP en **Config > FastEthernet0**. Aquí lo haces en **Desktop > IP Configuration**; el resultado es el mismo.

    Deja **puerta de enlace** y **DNS** en blanco: sin router no hacen falta.

    Si Packet Tracer o NetAcad te pide iniciar sesión, usa tu cuenta **`@alu.edu.gva.es`**, no Google.

## Pasos

1. Coloca un **switch 2960** y **cuatro PC** (*End Devices*).
2. Conéctalos con cable **automático** o **directo**: PC1 a **Fa0/1**, PC2 a **Fa0/2**, PC3 a **Fa0/3**, PC4 a **Fa0/4**.
3. Cambia los nombres a **PC1**, **PC2**, **PC3**, **PC4** y **SW1** (pestaña *Config* > *Display Name*).
4. Pon las IP en **Desktop > IP Configuration**, modo **Static**, según esta tabla:

| Equipo | Dirección IP | Máscara | Puerta de enlace |
| --- | --- | --- | --- |
| PC1 | 192.168.1.10 | 255.255.255.0 | (vacía) |
| PC2 | 192.168.1.11 | 255.255.255.0 | (vacía) |
| PC3 | 192.168.1.12 | 255.255.255.0 | (vacía) |
| PC4 | 192.168.1.13 | 255.255.255.0 | (vacía) |

5. Espera a que los enlaces se pongan en **verde**. En PC1, *Desktop* > *Command Prompt*: escribe `ipconfig` y después `ping 192.168.1.11`, `ping 192.168.1.12` y `ping 192.168.1.13`.
6. Pasa a modo **Simulación**. Mira solo del **9:50 al 14:00** del vídeo siguiente (lo de antes usa otro cableado y no lo necesitas). Deja el filtro solo en **ICMP**, envía una **PDU simple** de PC1 a PC4 y avanza paso a paso hasta que vuelva la respuesta.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/XYiPkNtEo5s?start=590&end=840"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="Cómo crear tu primera red en Cisco Packet Tracer — modo Simulación (Redes Plus)"></iframe>
</div>

7. Guarda el archivo como **`PR103.pkt`** (*Archivo > Guardar como* / *File > Save As*). Si dudas del menú, mira el apartado de [abrir y guardar](packet-tracer.md#6-abrir-guardar-y-entregar-un-pkt) en la guía inicial.

## Entrega en Aules

Sube **`PR103.pkt`** y **`PR103.md`** con:

- Captura del ping de PC1 a PC4 (solo la ventana *Command Prompt*).
- Captura del modo Simulación con la *Event List*.
- Respuestas a:
  1. ¿Qué topología forman los equipos y qué hace el switch?
  2. ¿Qué cable has usado y por qué?
  3. *(Opcional)* Cambia la IP de PC4 a `192.168.2.13` y vuelve a hacer ping desde PC1. ¿Qué pasa? ¿Por qué crees que ocurre?

## Antes de entregar

- [ ] Packet Tracer con sesión iniciada
- [ ] Switch y cuatro PC cableados, enlaces en verde, nombres PC1–PC4 y SW1
- [ ] IP según la tabla (sin puerta de enlace)
- [ ] Ping de PC1 al resto
- [ ] PDU ICMP en Simulación de PC1 a PC4 (ida y vuelta)
- [ ] `PR103.pkt` y `PR103.md` listos para Aules
