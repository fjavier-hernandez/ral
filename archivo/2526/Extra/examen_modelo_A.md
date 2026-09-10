# EXAMEN MODELO A – Capa de Enlace y Capa de Red

**Módulo:** Redes de Área Local (RAL)  
**Temas:** Capa de Enlace de Datos y Capa de Red  
**Curso:** Sistemas Microinformáticos y Redes (SMR)

---

**Nombre y apellidos:** _________________________________________________

**Fecha:** _______________________

---

## PARTE 1: PREGUNTAS DE DESARROLLO (5 preguntas)

**1.** Explica las funciones principales de la capa de enlace de datos en el modelo OSI. Indica al menos cuatro funciones.

---

**2.** Describe los campos principales de una trama Ethernet IEEE 802.3 (Preámbulo, SDF, direcciones MAC, Longitud/Tipo, Datos+Relleno, FCS). Indica el tamaño en bytes de al menos cuatro de ellos.

---

**3.** Explica la diferencia entre direcciones IP públicas y privadas. Indica los tres rangos de direcciones IP privadas más utilizados.

---

**4.** Describe el proceso del protocolo ARP paso a paso. Indica qué ocurre cuando un host necesita enviar datos a otro en la misma red y no conoce su dirección MAC.

---

**5.** ¿Qué es el protocolo DHCP y para qué sirve? Indica qué parámetros asigna a los clientes y qué ventajas ofrece frente a la configuración manual. Nombra al menos tres comprobaciones básicas que se realizan para verificar la configuración de red (comandos como ping) y explica qué verifica cada una.

---

## PARTE 2: EJERCICIOS DE CÁLCULO (5 ejercicios)

**1.** Una trama Ethernet tiene 64 bytes de datos útiles. Calcula el tamaño total de la trama en bytes, sabiendo que: Preámbulo = 7 bytes, SDF = 1 byte, MAC destino = 6 bytes, MAC origen = 6 bytes, Longitud/Tipo = 2 bytes, FCS = 4 bytes. (El campo Datos+Relleno debe tener al menos 46 bytes).

---

**2.** En Ethernet, la trama mínima es de 64 bytes. Si el campo de cabecera (desde MAC destino hasta FCS) ocupa 26 bytes, ¿cuál es el tamaño mínimo del campo Datos+Relleno?

---

**3.** Dada la dirección IP 172.16.50.25 con máscara 255.255.0.0, calcula:
   - Dirección de red
   - Dirección de broadcast
   - Número de hosts disponibles en esa red

---

**4.** Indica cuáles de las siguientes direcciones IP son inválidas y explica por qué:
   - 192.168.1.1
   - 256.10.10.10
   - 192.168.1.255
   - 10.0.0.300
   - 172.16.0.1

---

**5.** Un aula de informática tiene la red 192.168.1.0/24. El router usa la IP 192.168.1.1. Se quieren configurar 30 ordenadores y 2 impresoras. Indica:
   - ¿Hay suficientes direcciones IP disponibles?
   - Proporciona un ejemplo de configuración para el primer ordenador (IP, máscara, puerta de enlace)
   - ¿Cuál sería la última IP válida que podrías asignar a un equipo en esa red?

---

## CRITERIOS DE CALIFICACIÓN

- **Parte 1 (Desarrollo):** 1 punto por pregunta (5 puntos total)
- **Parte 2 (Cálculos):** 1 punto por ejercicio (5 puntos total)
- **Total:** 10 puntos
