def direccion(object):
    
    #Dividir dirección
    currentAddress = object['direccion']
    currentAddressSplit = currentAddress.rsplit(',')

    #Eliminar espacios
    direccion_local = currentAddressSplit[0].strip()
    comuna_local =currentAddressSplit[1].strip()
    ciudad_local = currentAddressSplit[2].strip()
    
    #Eliminar puntos
    if '.' in comuna_local:
        comuna_local = comuna_local.replace('.', '')
        
    if '.' in ciudad_local:
        ciudad_local = ciudad_local.replace('.', '')

    object['direccion_local'] = direccion_local
    object['comuna_local'] = comuna_local
    object['ciudad_local'] = ciudad_local

    

