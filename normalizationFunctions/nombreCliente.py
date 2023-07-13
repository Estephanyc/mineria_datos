def nombreCliente(object):
    
    currentNombre = object['nombre_cliente']
    
    # Dividir nombre
    nombreApellido = currentNombre.split()
    
    if len(nombreApellido) > 1:

        if  len(nombreApellido) < 3:
                nombreCliente = nombreApellido[0]
                apellidoCliente = nombreApellido[1]
        else: 
                apellidoCliente = "".join(nombreApellido[-1])
                nombreCliente = " ".join(nombreApellido[:-1])
    else:
        nombreCliente = ' '
        apellidoCliente = ' '
          
    object['nombre_cliente'] = nombreCliente
    object['apellido_cliente'] = apellidoCliente