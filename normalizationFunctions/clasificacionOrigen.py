def clasificacionOrigen(object):
    
    # Eliminar espacios
    clasificacion = object['clasificacion_de_origen'].strip()
    
    # Eliminar puntos
    clasificacion = clasificacion.replace('.', '')
    
    # Convertir a minúscula
    clasificacion = clasificacion.lower()

    # Reemplazar letras con tildes
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

    for a, b in replacements:
        clasificacion = clasificacion.replace(a, b)
    
    if clasificacion == 'marca registrada':
        object['clasificacion_de_origen'] = '1'
    elif clasificacion == 'generico':
        object['clasificacion_de_origen'] = '2'
    elif clasificacion == 'bioequivalente':
        object['clasificacion_de_origen'] = '3'
    else:
        pass
     
