def variables(object):
    
    tipoVenta = object['tipo_venta']
    clasificacion = object['clasificacion']
    comunaLocal = object['comuna_local']
    comunaCliente = object['comuna_cliente']

    # Tipo de venta
    if(tipoVenta in ['1', '3']):
        object['variable_tipo_venta'] = 'si'
    else:
        object['variable_tipo_venta'] = 'no'
        
    # Clasificación
    if(clasificacion in ['1', '2', '3', '4', '5']):
        object['variable_clasificacion'] = 'si'
    else:
        object['variable_clasificacion'] = 'no'
        
    # Comuna
    if(comunaLocal.lower() == comunaCliente.lower()):
        object['variable_comuna'] = 'si'
    else:
        object['variable_comuna'] = 'no'
