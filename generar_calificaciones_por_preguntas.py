#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
from collections import defaultdict
from datetime import datetime

# Leer el CSV
csv_file = "/Users/javih/Downloads/Xarxes locals-1CFMSMIR L   1756975370-Examen desarrollo UT1 y UT2-respostes.csv"

# Puntos máximos por pregunta
puntos_maximos = {
    "1": 3,  # Tipos de redes
    "2": 3,  # Red pública vs privada
    "3": 3,  # Switch
    "4": 3,  # Fibra óptica
    "5": 3,  # Topología estrella
    "6": 3,  # Nodos finales e intermedios
    "7": 3,  # Transmisión serie vs paralela
    "8": 3,  # Modelo OSI vs TCP/IP
    "9": 3,  # Conmutación vs difusión
}

# Textos de las preguntas
textos_preguntas = {
    "1": "¿Qué tipos de redes conoces según su extensión?",
    "2": "¿Qué diferencia hay entre una red pública y una privada?",
    "3": "¿Qué función tiene un switch en una red local?",
    "4": "¿Qué ventajas ofrece la fibra óptica frente al par trenzado?",
    "5": "¿Qué es una topología en estrella? ¿Dónde se suele usar?",
    "6": "¿Qué relación existe entre los nodos finales e intermedios?",
    "7": "¿Qué diferencia hay entre transmisión serie y paralela?",
    "8": "¿Cuáles son las principales diferencias entre el modelo OSI y el modelo TCP/IP?",
    "9": "¿Qué diferencias hay entre conmutación y difusión en el uso del medio?",
}

def evaluar_respuesta(pregunta_num, respuesta):
    """Evalúa una respuesta comparándola con los criterios de las soluciones"""
    if not respuesta or respuesta.strip() == "" or respuesta == "-" or "PDF" in respuesta or "Adjunts" in respuesta:
        return 0, "Sin respuesta o respuesta en PDF"
    
    respuesta_lower = respuesta.lower()
    puntos = 0
    observaciones = []
    
    if pregunta_num == "1":  # Tipos de redes: PAN, LAN, MAN, WAN
        conceptos = ["pan", "lan", "man", "wan"]
        encontrados = sum(1 for c in conceptos if c in respuesta_lower)
        if encontrados == 4:
            puntos = puntos_maximos[pregunta_num]
            observaciones.append("Todos los tipos mencionados correctamente")
        elif encontrados == 3:
            puntos = puntos_maximos[pregunta_num] * 0.8
            observaciones.append("Falta un tipo")
        elif encontrados == 2:
            puntos = puntos_maximos[pregunta_num] * 0.5
            observaciones.append("Solo menciona 2 tipos")
        elif encontrados == 1:
            puntos = puntos_maximos[pregunta_num] * 0.3
            observaciones.append("Solo menciona 1 tipo")
        else:
            puntos = 0
            observaciones.append("No menciona tipos correctos")
    
    elif pregunta_num == "2":  # Red pública vs privada
        tiene_publica = "pública" in respuesta_lower or "publica" in respuesta_lower
        tiene_privada = "privada" in respuesta_lower or "privada" in respuesta_lower
        tiene_acceso = "acceso" in respuesta_lower or "usuario" in respuesta_lower or "autorizado" in respuesta_lower
        tiene_titularidad = "propiedad" in respuesta_lower or "titularidad" in respuesta_lower or "empresa" in respuesta_lower
        
        if tiene_publica and tiene_privada:
            puntos = puntos_maximos[pregunta_num] * 0.6
            observaciones.append("Menciona ambas")
            if tiene_acceso:
                puntos = puntos_maximos[pregunta_num] * 0.9
                observaciones.append("Explica diferencia de acceso")
            if tiene_titularidad:
                puntos = puntos_maximos[pregunta_num]
                observaciones.append("Explica diferencia de titularidad/control")
        elif tiene_publica or tiene_privada:
            puntos = puntos_maximos[pregunta_num] * 0.3
            observaciones.append("Solo menciona una")
        else:
            puntos = 0
            observaciones.append("No distingue correctamente")
    
    elif pregunta_num == "3":  # Switch
        tiene_capa = "capa 2" in respuesta_lower or "enlace" in respuesta_lower or "capa de enlace" in respuesta_lower
        tiene_mac = "mac" in respuesta_lower or "dirección física" in respuesta_lower
        tiene_hub = "hub" in respuesta_lower
        tiene_colision = "colisión" in respuesta_lower or "dominio" in respuesta_lower or "colision" in respuesta_lower
        tiene_funcion = "interconectar" in respuesta_lower or "conectar" in respuesta_lower or "dirigir" in respuesta_lower
        
        if tiene_funcion:
            puntos += 0.5
            observaciones.append("Menciona función básica")
        if tiene_capa:
            puntos += 0.5
            observaciones.append("Menciona capa OSI")
        if tiene_mac:
            puntos += 0.5
            observaciones.append("Menciona direcciones MAC")
        if tiene_hub:
            puntos += 0.5
            observaciones.append("Compara con hub")
        if tiene_colision:
            puntos += 0.5
            observaciones.append("Menciona dominios de colisión")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("Respuesta muy básica o incorrecta")
    
    elif pregunta_num == "4":  # Fibra óptica
        conceptos = {
            "ancho de banda": 0.8,
            "atenuación": 0.6,
            "interferencia": 0.6,
            "seguridad": 0.5,
            "velocidad": 0.5,
            "distancia": 0.5
        }
        puntos = 0
        for concepto, peso in conceptos.items():
            if concepto in respuesta_lower:
                puntos += peso
                observaciones.append(f"Menciona {concepto}")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("No menciona ventajas principales")
    
    elif pregunta_num == "5":  # Topología estrella
        tiene_central = "central" in respuesta_lower or "switch" in respuesta_lower or "hub" in respuesta_lower or "nodo central" in respuesta_lower
        tiene_ventajas = "ventaja" in respuesta_lower
        tiene_desventajas = "desventaja" in respuesta_lower or "dependencia" in respuesta_lower
        tiene_uso = "lan" in respuesta_lower or "oficina" in respuesta_lower or "empresa" in respuesta_lower or "doméstica" in respuesta_lower
        
        if tiene_central:
            puntos += 1
            observaciones.append("Menciona dispositivo central")
        if tiene_ventajas or tiene_desventajas:
            puntos += 1
            observaciones.append("Menciona ventajas/desventajas")
        if tiene_uso:
            puntos += 1
            observaciones.append("Menciona uso en LAN/oficinas")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("Respuesta muy básica")
    
    elif pregunta_num == "6":  # Nodos finales e intermedios
        tiene_dte = "dte" in respuesta_lower or "final" in respuesta_lower or "terminal" in respuesta_lower
        tiene_dce = "dce" in respuesta_lower or "intermedio" in respuesta_lower
        tiene_relacion = "relación" in respuesta_lower or "comunicación" in respuesta_lower or "intermediario" in respuesta_lower or "permiten" in respuesta_lower
        tiene_ejemplos = ("repetidor" in respuesta_lower or "switch" in respuesta_lower or "router" in respuesta_lower) and ("servidor" in respuesta_lower or "estación" in respuesta_lower or "impresora" in respuesta_lower)
        
        if tiene_dte:
            puntos += 1
            observaciones.append("Menciona nodos finales (DTE)")
        if tiene_dce:
            puntos += 1
            observaciones.append("Menciona nodos intermedios (DCE)")
        if tiene_relacion:
            puntos += 1
            observaciones.append("Explica relación funcional")
        if tiene_ejemplos:
            puntos += 0.3
            observaciones.append("Incluye ejemplos")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("No distingue correctamente")
    
    elif pregunta_num == "7":  # Transmisión serie vs paralela
        tiene_serie = "serie" in respuesta_lower
        tiene_paralela = "paralela" in respuesta_lower or "paralelo" in respuesta_lower
        tiene_distancia = "distancia" in respuesta_lower or "larga" in respuesta_lower or "corta" in respuesta_lower
        tiene_cableado = "cableado" in respuesta_lower or "complejidad" in respuesta_lower or "canal" in respuesta_lower
        tiene_sincronizacion = "sincronización" in respuesta_lower or "sincronizacion" in respuesta_lower or "diafonía" in respuesta_lower or "diafonia" in respuesta_lower
        
        if tiene_serie and tiene_paralela:
            puntos += 1
            observaciones.append("Distingue ambos tipos")
        if tiene_distancia:
            puntos += 1
            observaciones.append("Menciona diferencia de distancia")
        if tiene_cableado:
            puntos += 0.5
            observaciones.append("Menciona complejidad de cableado")
        if tiene_sincronizacion:
            puntos += 0.5
            observaciones.append("Menciona problemas de sincronización")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("Respuesta muy básica")
    
    elif pregunta_num == "8":  # Modelo OSI vs TCP/IP
        tiene_osi = "osi" in respuesta_lower
        tiene_tcp = "tcp" in respuesta_lower or "tcp/ip" in respuesta_lower
        tiene_capas = "7" in respuesta and "4" in respuesta
        tiene_teorico = "teórico" in respuesta_lower or "teorico" in respuesta_lower or "iure" in respuesta_lower
        tiene_practico = "práctico" in respuesta_lower or "practico" in respuesta_lower or "facto" in respuesta_lower
        
        capas_osi = ["física", "enlace", "red", "transporte", "sesión", "presentación", "aplicación"]
        capas_encontradas = sum(1 for c in capas_osi if c in respuesta_lower)
        
        if tiene_osi and tiene_tcp:
            puntos += 0.5
            observaciones.append("Menciona ambos modelos")
        if tiene_capas:
            puntos += 0.5
            observaciones.append("Menciona número de capas (7 vs 4)")
        if capas_encontradas >= 4:
            puntos += 1
            observaciones.append(f"Menciona {capas_encontradas} capas OSI")
        elif capas_encontradas >= 2:
            puntos += 0.5
            observaciones.append(f"Menciona {capas_encontradas} capas")
        if tiene_teorico and tiene_practico:
            puntos += 1
            observaciones.append("Menciona diferencia teórico/práctico")
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("Respuesta muy básica")
    
    elif pregunta_num == "9":  # Conmutación vs difusión
        tiene_conmutacion = "conmutación" in respuesta_lower or "conmutacion" in respuesta_lower or "conmuta" in respuesta_lower
        tiene_difusion = "difusión" in respuesta_lower or "difusion" in respuesta_lower
        tiene_medio = "medio" in respuesta_lower or "compartido" in respuesta_lower or "dedicado" in respuesta_lower
        tiene_nodos = "nodo" in respuesta_lower or "intermedio" in respuesta_lower
        
        if tiene_conmutacion:
            puntos += 1
            observaciones.append("Menciona conmutación")
        if tiene_difusion:
            puntos += 1
            observaciones.append("Menciona difusión")
        if tiene_medio:
            puntos += 1
            observaciones.append("Explica diferencia en uso del medio")
        if tiene_nodos and tiene_medio:
            puntos += 0.2
        if puntos > puntos_maximos[pregunta_num]:
            puntos = puntos_maximos[pregunta_num]
        if puntos == 0:
            observaciones.append("Respuesta muy básica o incorrecta")
    
    return round(puntos, 1), "; ".join(observaciones) if observaciones else "Respuesta básica"

# Leer datos del CSV
alumnos = []
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nombre_completo = f"{row['Nom']} {row['Cognoms']}"
        alumnos.append({
            'nombre': nombre_completo,
            'email': row['Adreça electrònica'],
            'tiempo': row.get('Temps emprat', ''),
            'respuestas': {
                '1': row.get('Resposta 1', ''),
                '2': row.get('Resposta 2', ''),
                '3': row.get('Resposta 3', ''),
                '4': row.get('Resposta 4', ''),
                '5': row.get('Resposta 5', ''),
                '6': row.get('Resposta 6', ''),
                '7': row.get('Resposta 7', ''),
                '8': row.get('Resposta 8', ''),
                '9': row.get('Resposta 9', ''),
            }
        })

# Organizar por preguntas y evaluar
preguntas_data = defaultdict(list)
totales_alumnos = defaultdict(float)

for alumno in alumnos:
    total_alumno = 0
    for num_preg in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        respuesta = alumno['respuestas'][num_preg]
        puntos, obs = evaluar_respuesta(num_preg, respuesta)
        total_alumno += puntos
        preguntas_data[num_preg].append({
            'alumno': alumno['nombre'],
            'email': alumno['email'],
            'tiempo': alumno['tiempo'],
            'respuesta': respuesta[:500] + "..." if len(respuesta) > 500 else respuesta,  # Limitar longitud
            'puntos': puntos,
            'observaciones': obs
        })
    totales_alumnos[alumno['nombre']] = total_alumno

# Generar Markdown
output_file = "/Users/javih/Library/CloudStorage/OneDrive-Conselleriad'Educació/[MKDOCS]/ral/Correccion UT1y2/Calificaciones_Examen_Redes.md"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Calificaciones - Examen Desarrollo UT1 y UT2\n")
    f.write("## Redes de Área Local\n\n")
    f.write(f"**Fecha:** {datetime.now().strftime('%d de %B %Y')}\n")
    f.write("**Total:** 27 puntos (9 preguntas × 3 puntos)\n\n")
    f.write("---\n\n")
    
    f.write("## Criterios de Evaluación\n\n")
    for num, texto in textos_preguntas.items():
        f.write(f"* **Pregunta {num}:** {puntos_maximos[num]} puntos - {texto}\n")
    f.write("\n---\n\n")
    
    # Organizar por preguntas
    for num_preg in sorted(preguntas_data.keys()):
        f.write(f"## Pregunta {num_preg}: {textos_preguntas[num_preg]}\n\n")
        f.write(f"**Puntos máximos:** {puntos_maximos[num_preg]}/3\n\n")
        
        # Ordenar por puntos (de mayor a menor)
        respuestas_ordenadas = sorted(preguntas_data[num_preg], key=lambda x: x['puntos'], reverse=True)
        
        f.write("| Alumno | Email | Puntos | Observaciones |\n")
        f.write("|:-------|:------|:-------|:--------------|\n")
        
        for item in respuestas_ordenadas:
            nombre_corto = item['alumno'][:30] + "..." if len(item['alumno']) > 30 else item['alumno']
            email_corto = item['email'][:25] + "..." if len(item['email']) > 25 else item['email']
            f.write(f"| {nombre_corto} | {email_corto} | {item['puntos']}/{puntos_maximos[num_preg]} | {item['observaciones']} |\n")
        
        f.write("\n### Respuestas Detalladas\n\n")
        for item in respuestas_ordenadas:
            f.write(f"#### {item['alumno']} ({item['puntos']}/{puntos_maximos[num_preg]} puntos)\n\n")
            f.write(f"**Email:** {item['email']}\n\n")
            f.write(f"**Respuesta:**\n\n{item['respuesta']}\n\n")
            f.write(f"**Observaciones:** {item['observaciones']}\n\n")
            f.write("---\n\n")
    
    # Resumen por alumno
    f.write("## Resumen por Alumno\n\n")
    f.write("| Alumno | Total | Porcentaje |\n")
    f.write("|:-------|:-----|:-----------|\n")
    
    total_maximo = sum(puntos_maximos.values())
    for alumno_nombre, total in sorted(totales_alumnos.items(), key=lambda x: x[1], reverse=True):
        porcentaje = round((total / total_maximo) * 100, 1)
        f.write(f"| {alumno_nombre} | {total}/{total_maximo} | {porcentaje}% |\n")
    
    # Estadísticas
    f.write("\n## Estadísticas\n\n")
    f.write(f"* **Total de alumnos:** {len(alumnos)}\n")
    f.write(f"* **Media de la clase:** {round(sum(totales_alumnos.values()) / len(totales_alumnos), 1)}/{total_maximo}\n")
    f.write(f"* **Nota media:** {round((sum(totales_alumnos.values()) / len(totales_alumnos) / total_maximo) * 10, 1)}/10\n")

print(f"✓ Archivo generado: {output_file}")
print(f"✓ Procesados {len(alumnos)} alumnos")
print(f"✓ Organizadas {len(preguntas_data)} preguntas")

