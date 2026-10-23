---
title: PR303 — WLAN en Packet Tracer
description: Guion de práctica — montar una WLAN (red de área local inalámbrica) con AP, SSID, canal y WPA2 en Packet Tracer.
---

# PR303 — WLAN en Packet Tracer

Enunciado corto en el [Tema 3](../03-cableado-estructurado/tema3.md#pr303-pasa-a-certificacion-trabajo-para-casa). El montaje real del aula es **PR305**; esta práctica no lo sustituye.

Vas a montar en Packet Tracer una **WLAN** (*Wireless Local Area Network*, red de área local inalámbrica) mínima: un **AP** (*Access Point*, punto de acceso) unido a un switch, dos PC por cable y dos clientes Wi‑Fi. Configuras el **SSID** (*Service Set Identifier*, nombre de la red), el canal y **WPA2** (*Wi‑Fi Protected Access 2*, acceso Wi‑Fi protegido versión 2), asocias los clientes y compruebas con `ping`. No partimos de un archivo `.pka` ni `.pkt` del profesor: lo construyes tú desde cero, como en [PR103](pr103-primera-red.md).

!!! tip "Cuenta solo para el +1"
    PR303 se hace **en casa**, se entrega en Aules y se defiende en la auditoría. **No puntúa** en la nota de los RA (resultados de aprendizaje). **No sustituye** a [PR305](../03-cableado-estructurado/tema3.md#pr305-taller-wlan-real) (taller: NIC, AP o router Wi‑Fi del centro y WLAN usable).

Antes de empezar, Packet Tracer con la sesión iniciada. Si aún no lo tienes listo, sigue la [guía inicial](packet-tracer.md). Entra con tu cuenta **`@alu.edu.gva.es`**, no con Google.

Los modos del AP, el SSID, el canal y WPA2/WPA3 ya están en el [Tema 3, punto de acceso](../03-cableado-estructurado/tema3.md#ap). El medio Wi‑Fi (bandas 2,4 GHz y 5 GHz, interferencia) está en el [Tema 2](../02-medios-capa-fisica/tema2.md#medios-no-guiados-y-wifi-basico). Aquí solo montas y compruebas.

## Vídeo de apoyo

Las lecciones de Wi‑Fi del curso **CCNA Recargado 2.0** de Pablo Hidalgo que están abiertas sin membresía son la [15](https://www.youtube.com/watch?v=ESquFnfym7Q) y la [16](https://www.youtube.com/watch?v=MeGor4SxCCM). Sirven para el concepto (SSID, canal, seguridad). El laboratorio de Packet Tracer de ese curso (lección 14 y, en el curso v1.1, las lecciones 34–38) es de **pago**: no lo necesitas. El guion de esta página es el que cuentas en la auditoría.

Puedes ver la lección 15 como repaso; los clics de Packet Tracer los haces con los pasos de abajo.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/ESquFnfym7Q"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="CCNA Recargado 2.0 — lección 15, Wi‑Fi (Pablo Hidalgo)"></iframe>
</div>

!!! tip "Avisos sobre el vídeo"
    El vídeo nombra ideas del CCNA que el módulo trata más adelante. Para esta práctica basta con SSID, canal y WPA2.

    Si Packet Tracer o NetAcad te pide iniciar sesión, usa tu cuenta **`@alu.edu.gva.es`**, no Google.

## Qué necesitas

- Packet Tracer con la sesión iniciada ([guía inicial](packet-tracer.md)).
- Un archivo nuevo, vacío: no hay `PR303.pka` en Aules. Montas la topología y la guardas como **`PR303.pkt`**.

## Parámetros de laboratorio

Usa **estos** valores, no el SSID ni la clave del centro.

| Parámetro | Valor de laboratorio |
| --- | --- |
| SSID | `RAL-LAB-WLAN` |
| Banda / canal | 2,4 GHz · canal **6** |
| Seguridad | **WPA2-PSK** (clave precompartida), cifrado **AES** si el equipo lo deja elegir |
| Frase de paso | `LabNet-2026!` |
| Red | `192.168.10.0` / máscara `255.255.255.0` |
| Puerta de enlace | vacía (no hay router) |

| Equipo | Dirección IP | Máscara |
| --- | --- | --- |
| PC1 (cable) | 192.168.10.10 | 255.255.255.0 |
| PC2 (cable) | 192.168.10.11 | 255.255.255.0 |
| LT1 (Wi‑Fi) | 192.168.10.20 | 255.255.255.0 |
| LT2 (Wi‑Fi) | 192.168.10.21 | 255.255.255.0 |

El AP de Packet Tracer (*Access Point-PT*) es un puente de capa 2: no le pongas IP. Une el aire con el cable, igual que el AP del taller cuando trabaja en modo infraestructura.

## Pasos

### 1. Colocar los equipos

1. En *Network Devices > Switches*, un **switch 2960**. Nombre **SW1** (*Config > Display Name*).
2. En *Wireless Devices*, un **Access Point-PT**. Nombre **AP1**.
3. En *End Devices*, **dos PC** (**PC1**, **PC2**) y **dos portátiles** (**LT1**, **LT2**).

### 2. Cablear el tramo de cobre

Con cable **automático** o **directo**:

- AP1, interfaz **Port 0**, a SW1 **Fa0/1**.
- PC1 a SW1 **Fa0/2**.
- PC2 a SW1 **Fa0/3**.

Espera a que los tres enlaces queden en **verde**. El AP se alimenta en Packet Tracer al conectarlo: no hace falta simular PoE (*Power over Ethernet*, alimentación por Ethernet) para esta práctica.

### 3. Módulo Wi‑Fi en los portátiles

El portátil de Packet Tracer sale de fábrica con tarjeta **Ethernet**. Para asociarse al AP hay que ponerle una NIC inalámbrica, con el equipo **apagado** (la misma precaución que al insertar módulos en [PR202](pr202-capa-fisica.md)).

En **LT1**:

1. Pestaña **Physical**. Apaga el portátil con el interruptor.
2. Arrastra el módulo **FastEthernet** (el de la ranura lateral) hasta la lista de módulos, para quitarlo.
3. Arrastra el módulo **WPC300N** (o el adaptador inalámbrico que ofrezca tu versión) a esa ranura.
4. Enciende el portátil.

Repite en **LT2**. Si dejas Ethernet y Wi‑Fi a la vez, el `ping` puede salir por el cable y la práctica no demuestra la WLAN.

### 4. Configurar el AP

Clic en **AP1** → pestaña **Config** → interfaz inalámbrica (**Port 1** en *Access Point-PT*):

1. **SSID:** `RAL-LAB-WLAN`.
2. **Channel:** `6`.
3. **Authentication:** `WPA2-PSK`. Si aparece el tipo de cifrado, elige **AES**.
4. **PSK Pass Phrase** (o equivalente): `LabNet-2026!`.

No dejes el AP abierto ni uses WEP: en el módulo la seguridad de aula es WPA2 o WPA3, como se indica en el [Tema 3](../03-cableado-estructurado/tema3.md#ap). Si tu versión de Packet Tracer ofrece **WPA3**, puedes usarlo con la misma frase; en el informe anota cuál has dejado.

### 5. Direcciones IP en los PC de cable

En PC1 y PC2: *Desktop > IP Configuration*, modo **Static**, según la tabla. **Gateway** y **DNS** en blanco.

Comprueba primero el tramo cableado: en PC1, *Command Prompt*:

```text
ping 192.168.10.11
```

Si ese ping falla, no pases al Wi‑Fi: el fallo está en el switch, en el cable o en las IP.

### 6. Asociar los portátiles

En **LT1**: *Desktop > PC Wireless* (o *Config > Wireless0*, según la versión).

1. Pestaña **Connect**. Pulsa **Refresh** / Actualizar.
2. Elige la red **`RAL-LAB-WLAN`**.
3. Introduce la frase `LabNet-2026!` y conéctate.
4. Cuando el estado sea asociado (*Connected* / conectado), ve a *Desktop > IP Configuration* y pon **192.168.10.20** / **255.255.255.0**, puerta de enlace vacía.

Repite en **LT2** con **192.168.10.21**.

Si no aparece el SSID: revisa el módulo WPC300N, que el portátil esté encendido y que el SSID del AP coincida carácter a carácter (mayúsculas incluidas).

### 7. Comprobar la WLAN

Desde **LT1**, *Command Prompt*:

```text
ping 192.168.10.10
ping 192.168.10.11
ping 192.168.10.21
```

Los tres deben responder. El primero demuestra que el cliente Wi‑Fi llega al PC de cable a través del AP y del switch. El último, que los dos clientes inalámbricos se ven entre sí.

Opcional: modo **Simulación**, filtro **ICMP**, PDU simple de LT1 a PC1, y avanza hasta la respuesta. No es obligatorio para la entrega.

### 8. Guardar

*Archivo > Guardar como* / *File > Save As* → **`PR303.pkt`**. Si dudas del menú, mira [abrir y guardar](packet-tracer.md#6-abrir-guardar-y-entregar-un-pkt).

## Entrega en Aules

Sube **`PR303.pkt`** y **`PR303.md`** con:

- Captura de la config del AP (SSID, canal, WPA2 o WPA3; **sin** la frase de paso del centro: aquí solo la de laboratorio).
- Captura de un portátil asociado a `RAL-LAB-WLAN`.
- Captura del `ping` de LT1 a PC1 (solo la ventana *Command Prompt*).
- Respuestas a:
  1. ¿Qué hace el AP en esta topología respecto al switch y a los clientes Wi‑Fi?
  2. ¿Por qué el AP no lleva dirección IP en esta práctica?
  3. ¿Qué ocurriría si el portátil se asociara al SSID pero tuviera una IP de otra red (por ejemplo `192.168.20.20`)?

Sin nombres, correos ni SSID reales del centro en capturas ni en el `.md`.

## Antes de entregar

- [ ] Packet Tracer con sesión iniciada (`@alu.edu.gva.es`)
- [ ] SW1, AP1, PC1, PC2, LT1 y LT2; enlaces de cobre en verde
- [ ] Módulo inalámbrico en LT1 y LT2 (Ethernet quitado)
- [ ] SSID `RAL-LAB-WLAN`, canal 6, WPA2-PSK (o WPA3), frase de laboratorio
- [ ] IP según la tabla; ping de LT1 a PC1 y a LT2
- [ ] `PR303.pkt` y `PR303.md` listos para Aules
