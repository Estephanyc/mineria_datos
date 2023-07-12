def clasificacion(object):
    
    if object['clasificacion'] == 'Ansiolitico':
        object['clasificacion'] = '1'
    elif object['clasificacion'] == 'Antidepresivo':
        object['clasificacion'] = '2'
    elif object['clasificacion'] == 'Sedantes hipnóticos':
        object['clasificacion'] = '3'
    elif object['clasificacion'] == 'Antipsicóticos y neurolépticos':
        object['clasificacion'] = '4'
    elif object['clasificacion'] == 'Estabilizadores del animo':
        object['clasificacion'] = '5'
    elif object['clasificacion'] == 'Analgesico':
        object['clasificacion'] = '6'
    elif object['clasificacion'] == 'Antigripal':
        object['clasificacion'] = '7'
    elif object['clasificacion'] == 'Antinflamatorio':
        object['clasificacion'] = '8'
    else:
        pass
