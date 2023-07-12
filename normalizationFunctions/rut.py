def rut(object):
    currentRut = object['rut_cliente']
    
    #Eliminar puntos
    currentRut  = currentRut.replace('.', '')
    
    #Dividr Rut
    if(currentRut):
        if '-' in currentRut:
            splitRut = currentRut.rsplit('-', 1)
            rut = splitRut[0]
            dv = splitRut[1]
        else:
            lenCurrentRut = len(currentRut)
            rut = currentRut[0 :lenCurrentRut - 1]
            dv = currentRut[lenCurrentRut - 1]
    else:
        rut = ''
        dv = ''
    
    object['rut_cliente'] = rut
    object['dv'] = dv
    