def arbolDecisiones(object):
    
    variableTipoVenta = object['variable_tipo_venta']
    variableClasificacion = object['variable_clasificacion']
    variableComuna = object['variable_comuna']

    # Evaluvar las variables en orden de prioridad para dar un indicador al registro
    if(variableTipoVenta == 'si'):
        if(variableClasificacion == 'si'):
            if(variableComuna == 'si'):
                object['indicador'] = 'A++'
            else:
                object['indicador'] = 'A+'
        else:
            object['indicador'] = 'D'
    else:
        object['indicador'] = 'D'


