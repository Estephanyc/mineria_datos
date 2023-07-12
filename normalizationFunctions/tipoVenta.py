def tipoVenta(object):
     # Eliminar espacios
    tipoVenta = object['tipo_venta'].strip()
        # Convertir a minuscula
    tipoVenta = tipoVenta.lower()
    # Reemplazar letras con tildes
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

    for a, b in replacements:
        tipoVenta = tipoVenta.replace(a, b)

    if tipoVenta == 'receta obligatoria':
        object['tipo_venta'] = '3'
    elif tipoVenta == 'receta retenida':
        object['tipo_venta'] = '1'
    elif tipoVenta == 'libre':
        object['tipo_venta'] = '2'
    else:
        pass
     

    