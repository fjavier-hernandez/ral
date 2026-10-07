---
title: PR202 — Conectar la capa física
description: Guion de práctica — puertos, módulos y cableado de la capa física en Packet Tracer.
---

# PR202 — Conectar la capa física

Enunciado corto y rúbrica en el [Tema 2](../02-medios-capa-fisica/tema2.md#pr202-packet-tracer-capa-fisica).

En esta práctica abres una actividad oficial de Packet Tracer y trabajas la **capa física**: identificas puertos y módulos de un router y de varios switches, añades los módulos que faltan (con el equipo apagado), eliges el cable correcto para cada enlace (cobre directo, cobre cruzado o fibra) y compruebas que todo queda bien conectado. La comprobación la haces con el estado de las interfaces (`show ip interface brief`), con el navegador del portátil y con la puntuación de la actividad (sobre 55 puntos).

!!! tip "Esta práctica es del CCNA"
    Es una actividad del curso oficial *Introduction to Networks* del **CCNA** (Cisco Certified Network Associate). Lo que trabajas aquí (puertos, módulos y tipos de cable) entra también en las certificaciones **CCST** (Cisco Certified Support Technician) Networking y CCNA.

## Qué necesitas

- Packet Tracer con la sesión iniciada. Si aún no lo tienes listo, sigue la [guía inicial](packet-tracer.md).
- El fichero **`PR202.pka`** de Aules (actividad Packet Tracer con puntuación).

!!! warning "Sesión iniciada"
    Si abres el `.pka` **sin** sesión iniciada en Packet Tracer, la puntuación de la actividad **no se guarda**. Entra primero con tu cuenta `@alu.edu.gva.es` y después abre el archivo.

---

Puedes ver el vídeo siguiente como apoyo, pero las respuestas del informe las sacas tú del equipo en Packet Tracer.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/HU9otfUeZBE"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="Packet Tracer — Conectar la capa física (Leimer Sebastian Baez)"></iframe>
</div>

!!! tip "Avisos sobre el vídeo"
    La versión del vídeo puede diferir un poco de tu `.pka`. Para cableado e interfaces, manda la **tabla de esta guía**.

    Si Packet Tracer o NetAcad te pide iniciar sesión, usa tu cuenta **`@alu.edu.gva.es`**, no Google.

## Parte 1 — Identificar las características físicas

1. Abre `PR202.pka`. En la topología verás los routers **Este** y **West**, los switches **Switch1–Switch4**, los PC **PC1–PC9**, un punto de acceso, un portátil y una **TabletPC**. **West** queda al otro extremo del enlace serie que conectarás con **Este**.
2. Haz clic en el router **Este**. La pestaña **Physical** (Capa física) debe estar activa. Amplía la ventana para ver el chasis completo.
3. Localiza los **puertos de administración** (consola, AUX…) y las interfaces **LAN** (red de área local, *Local Area Network*) y **WAN** (red de área amplia, *Wide Area Network*) que trae de fábrica. Anota cuántas hay de cada tipo.
4. Abre la pestaña **CLI** (interfaz de línea de comandos, *Command Line Interface*). Es la primera vez que usas la consola del equipo en RAL: escribes comandos y lees la respuesta del dispositivo. Pulsa Intro para llegar al modo usuario y escribe:

```text
Este> show ip interface brief
```

   Este comando lista las interfaces del equipo, su dirección IP (si la tiene) y si están activas (*up*) o no (*down*). Lo usas para comprobar cuántas interfaces físicas aparecen y su estado.

5. Anota cuántas **interfaces físicas** enumera (la interfaz `Vlan1` es virtual: solo existe en software).
6. Escribe:

```text
Este> show interface gigabitethernet 0/0
```

   Este comando muestra el detalle de una interfaz concreta (estado, ancho de banda, etc.). Busca el **ancho de banda predeterminado** de `GigabitEthernet0/0`.

7. Repite con la interfaz serie:

```text
Este> show interface serial 0/0/0
```

   Anota el ancho de banda predeterminado de `Serial0/0/0`. En las interfaces serie ese valor lo usan los protocolos de enrutamiento para elegir rutas; **no** es el caudal real del enlace (ese lo negocia el proveedor).

8. Sigue en la pestaña Physical del router **Este** y cuenta las **ranuras de expansión** vacías donde se pueden insertar módulos.
9. Abre **Switch2** (pestaña Physical) y cuenta también sus ranuras de expansión.

---

## Parte 2 — Seleccionar e insertar módulos

1. En el router **Este**, pestaña **Physical**, revisa la lista de **Módulos** a la izquierda. Haz clic en cada uno y lee la descripción de abajo: así sabes qué conectividad aporta (puertos FastEthernet, fibra, etc.).
2. Necesitas conectar **PC1, PC2 y PC3** al router **Este** sin comprar un switch nuevo. Elige el módulo que te permite conectar esos tres PC y anota cuántos hosts admite.
3. En **Switch2**, identifica el módulo que permite una conexión **óptica Gigabit** hacia **Switch3** (módulo de fibra / **SFP**, transceptor enchufable, *Small Form-factor Pluggable*, según lo que ofrezca el equipo en Packet Tracer).

!!! warning "Apaga el equipo antes de insertar módulos"
    En este modelo de router (y en los switches de la actividad) los módulos **no** se pueden cambiar en caliente. Si intentas insertar uno con el equipo encendido, Packet Tracer no lo acepta. Apaga el dispositivo con el interruptor de la pestaña Physical, inserta el módulo y vuelve a encenderlo.

4. Apaga el router **Este**, arrastra el módulo elegido a una ranura vacía y enciéndelo de nuevo. Si te equivocas de módulo, arrástralo otra vez hasta su imagen en la esquina inferior derecha para quitarlo.
5. Con el mismo procedimiento, inserta en **Switch2** el módulo de fibra en la ranura vacía más a la derecha.
6. En la CLI de **Switch2**, vuelve a usar `show ip interface brief` para ver en **qué ranura** ha quedado el módulo (aparecen las nuevas interfaces).

---

## Parte 3 — Conectar los dispositivos

Para cada fila de la tabla: elige el tipo de cable, haz clic en el primer dispositivo y su interfaz, y después en el segundo dispositivo y su interfaz. Si el enlace es correcto, sube la puntuación de la actividad.

**Regla de cable (cobre):** entre dispositivos de **tipos distintos** (PC–switch, PC–router, router–switch) se usa cable **directo**. Entre dispositivos del **mismo tipo** (switch–switch, router–router) se usa cable **cruzado**. Los equipos actuales suelen detectar el cruce solos (**Auto-MDIX**, *Automatic Medium-Dependent Interface Crossover*), pero esta actividad **puntúa el cable que pide la tabla**: pon exactamente el que indica cada fila.

!!! note "Luces de enlace"
    En esta actividad de Cisco las luces de enlace **no están habilitadas**. No te guíes por el color del enlace en el lienzo: comprueba con la puntuación y, en la Parte 4, con los comandos.

| Dispositivo | Interfaz | Cable | Dispositivo | Interfaz |
| --- | --- | --- | --- | --- |
| Este | GigabitEthernet0/0 | Cobre directo | Switch1 | GigabitEthernet0/1 |
| Este | GigabitEthernet0/1 | Cobre directo | Switch4 | GigabitEthernet0/1 |
| Este | FastEthernet0/1/0 | Cobre directo | PC1 | FastEthernet0 |
| Este | FastEthernet0/1/1 | Cobre directo | PC2 | FastEthernet0 |
| Este | FastEthernet0/1/2 | Cobre directo | PC3 | FastEthernet0 |
| Switch1 | FastEthernet0/1 | Cobre directo | PC4 | FastEthernet0 |
| Switch1 | FastEthernet0/2 | Cobre directo | PC5 | FastEthernet0 |
| Switch1 | FastEthernet0/3 | Cobre directo | PC6 | FastEthernet0 |
| Switch4 | GigabitEthernet0/2 | Cobre cruzado | Switch3 | GigabitEthernet3/1 |
| Switch3 | GigabitEthernet5/1 | Fibra | Switch2 | GigabitEthernet5/1 |
| Switch2 | FastEthernet0/1 | Cobre directo | PC7 | FastEthernet0 |
| Switch2 | FastEthernet1/1 | Cobre directo | PC8 | FastEthernet0 |
| Switch2 | FastEthernet2/1 | Cobre directo | PC9 | FastEthernet0 |
| Switch2 | GigabitEthernet3/1 | Cobre directo | AccessPoint | Port 0 |
| Este | Serial0/0/0 | DCE serial (conectar primero a Este) | West | Serial0/0/0 |

Ejemplo: para unir **Este** con **Switch1**, elige cable de cobre directo, en Este la interfaz `GigabitEthernet0/0` y en Switch1 `GigabitEthernet0/1`. La puntuación debería subir (por ejemplo a 4/55 en ese primer enlace).

---

## Parte 4 — Comprobar la conectividad

1. En la CLI del router **Este**, ejecuta otra vez `show ip interface brief`. Si el cableado es correcto, el estado debe coincidir con esta referencia (Status y Protocol en *up* donde corresponda):

| Interface | IP-Address | OK? | Method | Status | Protocol |
| --- | --- | --- | --- | --- | --- |
| GigabitEthernet0/0 | 172.30.1.1 | YES | manual | up | up |
| GigabitEthernet0/1 | 172.31.1.1 | YES | manual | up | up |
| Serial0/0/0 | 10.10.10.1 | YES | manual | up | up |
| Serial0/0/1 | unassigned | YES | unset | down | down |
| FastEthernet0/1/0 | unassigned | YES | unset | up | up |
| FastEthernet0/1/1 | unassigned | YES | unset | up | up |
| FastEthernet0/1/2 | unassigned | YES | unset | up | up |
| FastEthernet0/1/3 | unassigned | YES | unset | down | down |
| Vlan1 | 172.29.1.1 | YES | manual | up | up |

2. Abre el **portátil** → pestaña **Config** → interfaz **Wireless0** → marca **On** en el estado del puerto. Espera a que aparezca la conexión inalámbrica.
3. En **Desktop** del portátil, abre el **navegador web**, escribe `www.cisco.pka` y pulsa Ir. Debe mostrarse la página **Cisco Packet Tracer**.
4. Repite el encendido de **Wireless0** en la **TabletPC** y comprueba también `www.cisco.pka` en su navegador.
5. *(Opcional de la actividad)* En la TabletPC puedes apagar **Wireless0** y activar **3G/4G Cell1** para probar acceso por red celular. No dejes las dos interfaces activas a la vez: solo debe haber una interfaz de red activa; si WiFi y celular compiten, el equipo puede usar una ruta de salida distinta y el navegador dejar de resolver bien el acceso.
6. Pulsa **Check Results**. La puntuación debe llegar al **100 %** (55/55). Guarda el `.pka` con *Archivo > Guardar como* / *File > Save As* como **`PR202.pka`**.

---

## Preguntas para `PR202.md`

Responde en tu informe (frases completas):

1. ¿Qué puertos de administración tiene el router **Este**?
2. ¿Qué interfaces LAN y WAN trae el router **Este** y cuántas hay de cada tipo?
3. Según `show ip interface brief`, ¿cuántas interfaces **físicas** enumera el router **Este**?
4. ¿Cuál es el ancho de banda predeterminado de `GigabitEthernet0/0`? ¿Y el de `Serial0/0/0`?
5. ¿Cuántas ranuras de expansión tiene el router **Este**? ¿Y el **Switch2**?
6. ¿Qué módulo usas para conectar PC1, PC2 y PC3 al router **Este** sin un switch nuevo? ¿Cuántos hosts permite ese módulo?
7. ¿Qué módulo insertas en **Switch2** para la conexión óptica Gigabit hacia **Switch3**? ¿En qué ranura queda?
8. Resume con tus palabras cuándo usas cable directo, cuándo cruzado y cuándo fibra en esta actividad.

---

## Entrega en Aules

Sube **`PR202.pka`** (guardado con la puntuación) y **`PR202.md`** con:

- Captura de la pestaña **Physical** del router **Este** (o de Switch2) con los módulos ya insertados.
- Captura de la salida de `show ip interface brief` en **Este** y en **Switch2**.
- Captura del navegador del portátil mostrando `www.cisco.pka`.
- Captura de la ventana **Check Results** (puntuación completa).
- Las respuestas a las preguntas de arriba.

Sin nombres, correos ni datos personales en capturas ni en el `.md`.

## Antes de entregar

- [ ] Sesión iniciada en Packet Tracer
- [ ] Módulos insertados con el equipo apagado
- [ ] Cableado según la tabla
- [ ] `show ip interface brief` coherente en Este
- [ ] Portátil (y TabletPC) llegan a `www.cisco.pka`
- [ ] Check Results al 100 %
- [ ] `PR202.pka` y `PR202.md` listos para Aules

## Rúbrica

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Identificación de puertos y módulos | Respuestas correctas sobre administración, LAN/WAN, ranuras y comandos `show` | 2 |
| Módulos insertados correctamente | Módulos adecuados en Este y Switch2, insertados con el equipo apagado | 2 |
| Cableado según la tabla | Todos los enlaces con el tipo de cable e interfaces indicados | 2 |
| Verificación | Comandos, navegador a `www.cisco.pka`, Check Results al 100 % | 2 |
| Entrega | `.pka` que abre bien y `.md` claro, respuestas correctas, sin datos personales | 2 |
| **Total** | | **/10** |
