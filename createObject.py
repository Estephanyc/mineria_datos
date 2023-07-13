def createObject(row):

    object = {
        'n_boleta': row[0].strip(),
        'fecha_venta':	row[1].strip(),
        'codigo_medicamento': row[2].strip(),
        'nombre_medicamento': row[3].strip(),
        'clasificacion_de_origen': row[4].strip(),
        'tipo_venta': row[5].strip(),
        'unidades_vendidas': row[6].strip(),
        'n_local': row[7].strip(),
        'direccion': row[8].strip(),
        'rut_cliente': row[9].strip(),
        'clasificacion': row[10].strip(),
        'nombre_cliente': row[11].strip()
    }
    
    return object