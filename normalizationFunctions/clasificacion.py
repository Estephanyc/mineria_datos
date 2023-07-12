def clasificacion(object):
    
    #Eliminar espacios
    clasificacion = object['clasificacion'].strip()

    if clasificacion == 'Ansiolitico':
        object['clasificacion'] = '1'
    elif clasificacion == 'Antidepresivo':
        object['clasificacion'] = '2'
    elif clasificacion == 'Sedantes hipnóticos':
        object['clasificacion'] = '3'
    elif clasificacion == 'Antipsicóticos y neurolépticos':
        object['clasificacion'] = '4'
    elif clasificacion == 'Estabilizadores del animo':
        object['clasificacion'] = '5'
    elif clasificacion == 'Analgesico':
        object['clasificacion'] = '6'
    elif clasificacion == 'Antigripal':
        object['clasificacion'] = '7'
    elif clasificacion == 'Antinflamatorio':
        object['clasificacion'] = '8'
    else:
        pass
