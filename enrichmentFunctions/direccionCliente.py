from api.getDirectionByRut import getDirectionByRut

def direccionCliente(object):
    
    # Consultar api que trae la dirección del usuario por su rut
    direccionCliente = getDirectionByRut(object['rut_cliente'])
    
    if(direccionCliente):
        object['direccion_cliente'] = direccionCliente['direccion']
        object['comuna_cliente'] = direccionCliente['comuna']
        object['ciudad_cliente'] = direccionCliente['ciudad']
    else:
        object['direccion_cliente'] = ''
        object['comuna_cliente'] = ''
        object['ciudad_cliente'] = ''
