# PR201 — Guía de taller: crimpado de latiguillos UTP

Esta guía desarrolla paso a paso la práctica **PR201** del [Tema 2](../02-medios-capa-fisica/tema2.md#pr201-crimpado-utp-t568ab-comprobador-etiquetado). Se trabaja en pareja en el aula-taller. La ficha de la práctica (RA, CE y sesiones) y la rúbrica están en el tema. Antes de empezar, repasad las [normas del taller](../00-normas/normas_taller.md).

## Vídeo de referencia

Antes de crimpar, mirad una vez el procedimiento completo (corte, orden de hilos, crimpado y comprobación) para no improvisar en el primer conector.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/x7cJAv9Buhc"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          title="Joaquín Cantero — Práctica de cableado de red (Normas T568A y T568B)"></iframe>
</div>

## Material por pareja

- Cable UTP (*Unshielded Twisted Pair*, par trenzado sin apantallar) de la categoría que indique el profesor.
- Dos conectores RJ‑45 por latiguillo, con su capuchón si los hay.
- Pelacables, crimpadora, cúter o tijeras de electricista y comprobador de cables.
- Etiquetas y rotulador.
- Gafas de protección si el taller lo exige: al cortar los hilos pueden saltar trozos de cobre.

## Fase 1. Preparar el cable

1. Cortad el tramo de cable a la longitud que indique el profesor. Si el conector lleva capuchón, metedlo ahora en el cable, antes de crimpar.
2. Pelad la cubierta exterior unos 2–2,5 cm con el pelacables, sin cortar el aislante de los hilos.
3. Destrenzad los pares solo lo necesario y estirad los hilos para que queden rectos.

## Fase 2. Ordenar los hilos según la norma

Por defecto se usa **T568B** en los dos extremos, que da un latiguillo **directo**. Mirando el conector con la pestaña hacia abajo y los contactos hacia vosotros, del pin 1 al 8:

| Pin | T568B | T568A |
| --- | --- | --- |
| 1 | Blanco‑naranja | Blanco‑verde |
| 2 | Naranja | Verde |
| 3 | Blanco‑verde | Blanco‑naranja |
| 4 | Azul | Azul |
| 5 | Blanco‑azul | Blanco‑azul |
| 6 | Verde | Naranja |
| 7 | Blanco‑marrón | Blanco‑marrón |
| 8 | Marrón | Marrón |

Si el profesor lo pide, haced además un latiguillo **cruzado**, con T568A en un extremo y T568B en el otro, para comparar las dos normas. La diferencia entre ambas está explicada en el [Tema 2](../02-medios-capa-fisica/tema2.md).

1. Colocad los hilos en el orden de la tabla, bien juntos y planos.
2. Cortadlos rectos, todos a la misma longitud, dejando aproximadamente 1,2 cm de hilo fuera de la cubierta.

## Fase 3. Crimpar

1. Introducid los hilos en el conector sin perder el orden, hasta que **todos lleguen al fondo**. Comprobadlo mirando la punta del conector.
2. La **cubierta exterior tiene que entrar en el conector**, para que la pestaña de presión la sujete y el cable no se suelte al tirar.
3. Meted el conector en la crimpadora y apretad **de un solo golpe**, firme y hasta el final.
4. Repetid las fases 1 a 3 en el otro extremo.

## Fase 4. Comprobar

1. Conectad los dos extremos al comprobador y ejecutad la prueba de continuidad.
2. En un latiguillo directo, los LED tienen que encenderse en el mismo orden en los dos lados (1‑1, 2‑2… 8‑8). En uno cruzado, se intercambian el 1 con el 3 y el 2 con el 6.
3. Si falla, no lo deis por bueno: cortad el conector, identificad el error, anotadlo y rehacedlo.
4. Haced una foto o una captura del resultado del comprobador.

## Fase 5. Etiquetar y entregar

1. Etiquetad el cable en los dos extremos con el código que indique el profesor, por ejemplo `PR201-Gx-nn`.
2. Haced una foto de cada extremo en la que se vean bien los colores.
3. Entregad el **cable físico** al profesor y recoged el puesto según las [normas del taller](../00-normas/normas_taller.md).

## Errores típicos

Anotad en el informe cualquiera de estos errores si os ocurre y cómo lo habéis resuelto:

- Pares cruzados o invertidos.
- Hilos que no llegan al fondo del conector.
- Cubierta que no entra en el conector.
- Crimpado doble o incompleto.
- Cable sin etiquetar.
- No usar las gafas cuando el taller lo exige.

## Entrega

Un fichero `PR201.md` por pareja, subido a Aules, con las fotos de los dos extremos, el resultado del comprobador, la checklist firmada y los errores que hayáis tenido con su corrección. La calificación sigue la rúbrica de la [PR201 en el Tema 2](../02-medios-capa-fisica/tema2.md#pr201-crimpado-utp-t568ab-comprobador-etiquetado).
