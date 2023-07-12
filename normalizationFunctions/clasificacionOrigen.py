def clasificacionOrigen(object):
    
    # Acá debe quedar la clasificacuión de origen normalizada
    if object['clasificacion_de_origen'] == 'Marca Registrada':
        object['clasificacion_de_origen'] = '1'
    elif object['clasificacion_de_origen'] == 'Generico':
        object['clasificacion_de_origen'] = '2'
    elif object['clasificacion_de_origen'] == 'Bioequivalente':
        object['clasificacion_de_origen'] = '3'
    else:
        pass
     
    return object