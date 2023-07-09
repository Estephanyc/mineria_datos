def createObject(row):

    object = {
    'n_boleta': row[0],
    'fecha_venta':	row[1],
    'codigo_medicamento': row[2],
    'nombre_medicamento': row[3],
    'clasificacion_de_origen': row[4],
    'tipo_venta': row[5],
    'unidades_vendidas': row[6],
    'n_local': row[7],
    'direccion': row[8],
    'rut_cliente': row[9],
    'clasificacion': row[10],
    'nombre_cliente': row[11]
   }
    return object