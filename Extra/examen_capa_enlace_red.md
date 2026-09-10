# EXAMEN: Capa de Enlace y Capa de Red

**Módulo:** Redes de Área Local (RAL)  
**Temas:** Capa de Enlace de Datos y Capa de Red  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

---

**Nombre y apellidos:** _________________________________________________

**Fecha:** _______________________

---

## PARTE 1: PREGUNTAS DE DESARROLLO (10 preguntas)

### Tema: Capa de Enlace de Datos (5 preguntas)

**1.** Explica las funciones principales de la capa de enlace de datos en el modelo OSI. Indica al menos cuatro funciones.

---

**2.** ¿Qué son las subcapas LLC y MAC? Indica la norma que define cada una y cuál es la función principal de cada subcapa.

---

**3.** Describe los campos principales de una trama Ethernet IEEE 802.3 (Preámbulo, SDF, direcciones MAC, Longitud/Tipo, Datos+Relleno, FCS). Indica el tamaño en bytes de al menos cuatro de ellos.

---

**4.** Explica cómo funciona el protocolo CSMA/CD. Indica los cuatro pasos del algoritmo y por qué los switches modernos eliminan las colisiones.

---

**5.** ¿Qué son el dominio de colisión y el dominio de difusión? Explica qué dispositivos (hub, switch, router) extienden o limitan cada uno.

---

### Tema: Capa de Red (5 preguntas)

**6.** Explica la diferencia entre direcciones IP públicas y privadas. Indica los tres rangos de direcciones IP privadas más utilizados.

---

**7.** ¿Qué es una máscara de red y para qué sirve? Explica cómo se utiliza para determinar si dos hosts pertenecen a la misma red.

---

**8.** Describe el proceso del protocolo ARP paso a paso. Indica qué ocurre cuando un host necesita enviar datos a otro en la misma red y no conoce su dirección MAC.

---

**9.** ¿Qué es el protocolo ICMP y para qué se utiliza? Nombra al menos dos herramientas que lo utilicen y explica brevemente su función.

---

**10.** ¿Qué es el protocolo DHCP y para qué sirve? Indica qué parámetros asigna a los clientes y qué ventajas ofrece frente a la configuración manual. Nombra al menos tres comprobaciones básicas que se realizan para verificar la configuración de red (comandos como ping) y explica qué verifica cada una.

---

## PARTE 2: EJERCICIOS DE CÁLCULO (10 ejercicios)

### Tema: Capa de Enlace (5 ejercicios)

**1.** Una trama Ethernet tiene 64 bytes de datos útiles. Calcula el tamaño total de la trama en bytes, sabiendo que: Preámbulo = 7 bytes, SDF = 1 byte, MAC destino = 6 bytes, MAC origen = 6 bytes, Longitud/Tipo = 2 bytes, FCS = 4 bytes. (El campo Datos+Relleno debe tener al menos 46 bytes).

---

**2.** ¿Cuántos bytes ocupa en total una trama Ethernet que transporta 1200 bytes de datos? (Incluye Preámbulo, SDF, direcciones MAC, Longitud/Tipo, Datos y FCS. No incluyas IFG).

---

**3.** En Ethernet, la trama mínima es de 64 bytes. Si el campo de cabecera (desde MAC destino hasta FCS) ocupa 26 bytes, ¿cuál es el tamaño mínimo del campo Datos+Relleno?

---

**4.** Una red Ethernet transmite tramas de 1518 bytes (trama máxima estándar con cabecera VLAN). Si se envían 100 tramas de ese tamaño, ¿cuántos bytes se transmiten en total por el medio?

---

**5.** El campo FCS de una trama Ethernet ocupa 4 bytes. ¿Cuántos bits son? Si el CRC detecta un error en la trama, ¿qué hace el receptor con esa trama?

---

### Tema: Capa de Red (5 ejercicios)

**6.** Dada la dirección IP 192.168.5.100 con máscara 255.255.255.0, calcula:
   - Dirección de red
   - Dirección de broadcast
   - Primera IP válida para hosts
   - Última IP válida para hosts
   - Número de hosts que se pueden conectar

---

**7.** Dada la dirección IP 172.16.50.25 con máscara 255.255.0.0, calcula:
   - Dirección de red
   - Dirección de broadcast
   - Número de hosts disponibles en esa red

---

**8.** Dada la dirección 192.168.10.75 con prefijo /26:
   - ¿Cuál es la máscara de subred?
   - Calcula la dirección de red
   - Calcula la dirección de broadcast
   - ¿Cuántos hosts se pueden conectar?

---

**9.** Indica cuáles de las siguientes direcciones IP son inválidas y explica por qué:
   - 192.168.1.1
   - 256.10.10.10
   - 192.168.1.255
   - 10.0.0.300
   - 172.16.0.1

---

**10.** Un aula de informática tiene la red 192.168.1.0/24. El router usa la IP 192.168.1.1. Se quieren configurar 30 ordenadores y 2 impresoras. Indica:
   - ¿Hay suficientes direcciones IP disponibles?
   - Proporciona un ejemplo de configuración para el primer ordenador (IP, máscara, puerta de enlace)
   - ¿Cuál sería la última IP válida que podrías asignar a un equipo en esa red?

---

## CRITERIOS DE CALIFICACIÓN

- **Parte 1 (Desarrollo):** 1 punto por pregunta (10 puntos total)
- **Parte 2 (Cálculos):** 1 punto por ejercicio (10 puntos total)
- **Total:** 20 puntos

---

*Documento para imprimir. Sin enlaces externos.*
