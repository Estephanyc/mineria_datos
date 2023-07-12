def clasificacionOrigen(object):
    
    #Eliminar espacios
    clasificacion = object['clasificacion_de_origen'].strip()
    
    if clasificacion == 'Marca Registrada':
        object['clasificacion_de_origen'] = '1'
    elif clasificacion == 'Generico':
        object['clasificacion_de_origen'] = '2'
    elif clasificacion == 'Bioequivalente':
        object['clasificacion_de_origen'] = '3'
    else:
        pass
     
