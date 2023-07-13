import json

def getDirectionByRut(rut):    
   
    if(rut):
        #Abrir json
        file = open('data/direcciones.json')
        data = json.load(file)
        
         #Cerrar json
        file.close()
        
        #Obtener dirección por el rut
        if rut in data:
            direccion = data[rut]
            return direccion
        else:
            return ''
    else:
        return ''
        