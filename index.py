import csv

from normalizationFunctions.tipoVenta import tipoVenta
from normalizationFunctions.nombreCliente import nombreCliente
from normalizationFunctions.clasificacion import clasificacion
from normalizationFunctions.clasificacionOrigen import clasificacionOrigen
from normalizationFunctions.direccion import direccion
from normalizationFunctions.rut import rut
from enrichmentFunctions.direccionCliente import direccionCliente
from enrichmentFunctions.correo import correo
from arbolDecisiones import arbolDecisiones
from exportResults import exportResults
from createObject import createObject
from variables import variables

def processData():

    # Open data
    with open('data/data.csv', newline='') as File:  
        
        items = []
        
        reader = csv.reader(File, delimiter=';')
        for row in reader:

            object = createObject(row) 
            
            # 1. Normalización
            
            #Tipo de venta  //Fran
            tipoVenta(object)

            #Clasificacion del medicamento //Cynthia ok
            clasificacion(object)
            
            #Clasificacion del medicamento segun origen //Cynthia ok
            clasificacionOrigen(object)

            #Nombre cliente //Fran
            nombreCliente(object)
            
            #Rut // Estephany ok
            rut(object) 
            
            #Direccion // Estephany ok
            direccion(object)
            
            # 2. Enriquecimiento
            
            # Correo cliente
            correo(object)

            #Direccion del cliente
            direccionCliente(object)
            
            # 3. Analisis de variables
            variables(object)

            # 4.Arbol de decisiones
            arbolDecisiones(object)
            
            #Objecto final
            #print(object)
            
            items.append(object)
            
        #Create file
        exportResults(items)
        
        
processData();