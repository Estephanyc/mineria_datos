import csv

def exportResults(items):
    rowCsv = []

    headers = [
                'N Boleta', 'Fecha venta','Tipo venta', 'Unidades',
                'Código medicamento', 'Clasificación de origen', 'Nombre medicamento', 'Clasificación',
                'N local', 'Direccion', 'Comuna', 'Ciudad', 
                'Rut cliente', 'Dv', 'Nombre cliente',	'Apellido cliente', 'Dirección','Comuna', 'Ciudad',
                'Variabale: Tipo de venta', 'Variable: Clasificación',	'Variable: Comuna',	'Indicador'
            ]
 
    rowCsv.append(headers)

 
    for item in items:
        objectCsv  = [ 
                    item['n_boleta'], item['fecha_venta'], item['tipo_venta'], item['unidades_vendidas'],
                    item['codigo_medicamento'], item['clasificacion_de_origen'], item['nombre_medicamento'], item['clasificacion'],
                    item['n_local'], item['direccion_local'], item['comuna_local'], item['ciudad_local'],
                    item['rut_cliente'], item['dv'], item['nombre_cliente'], item['apellido_cliente'], item['direccion_cliente'], item['comuna_cliente'], item['ciudad_cliente'],
                    item['variable_tipo_venta'], item ['variable_clasificacion'], item['variable_comuna'], item['indicador']                                                                                                                     
                ]
        
        rowCsv.append(objectCsv)
        
    with open('data/finalData.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rowCsv)
      
      
      
