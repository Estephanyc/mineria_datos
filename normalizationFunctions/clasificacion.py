def clasificacion(object):
    
    # Eliminar espacios
    clasificacion = object['clasificacion'].strip()

    # Convertir a minuscula
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
    
    if clasificacion == 'ansiolitico':
        object['clasificacion'] = '1'
    elif clasificacion == 'antidepresivo':
        object['clasificacion'] = '2'
    elif clasificacion == 'sedantes hipnoticos':
        object['clasificacion'] = '3'
    elif clasificacion == 'antipsicoticos y neurolepticos':
        object['clasificacion'] = '4'
    elif clasificacion == 'estabilizadores del animo':
        object['clasificacion'] = '5'
    elif clasificacion == 'analgesico':
        object['clasificacion'] = '6'
    elif clasificacion == 'antigripal':
        object['clasificacion'] = '7'
    elif clasificacion == 'antinflamatorio':
        object['clasificacion'] = '8'
    else:
        pass
