"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

from numpy import double
import pandas as pd
import re

def ingest_data():
    with open("clusters_report.txt") as f:
        lineas = f.readlines()
    columns = []
    newcolums =[]
    columns.append(lineas[0].split('  ',5))
    columns.append(lineas[1].split('  ',5))
    columns[0] = list(filter(None,columns[0]))
    columns[1] = list(filter(None,columns[1]))
    columns[0].remove("   \n")
    newcolums.append(columns[0][0].strip().lower())
    newcolums.append(columns[0][1].strip().lower() + " " + columns[1][0].strip().lower())
    newcolums.append(columns[0][2].strip().lower() + " " + columns[1][1].strip().lower())
    newcolums.append(columns[0][3].strip().lower())
    
    for y in range(len(newcolums)):
        newcolums[y] = newcolums[y].replace(" ","_")
    listagrande =[]
    for x in range(len(lineas)):
        cluster = lineas[x][3:5]
        resultregex = re.search("[0-9]",cluster)
        if resultregex:
            inicluster = lineas[x].split('    ',5)
            inicluster = list(filter(None,inicluster))
            for elemento in range(len(inicluster)):
                inicluster[elemento]= inicluster[elemento].strip().lower()
                inicluster[elemento] = inicluster[elemento].replace(" %","")
            inicluster[0]= int(inicluster[0])
            inicluster[1]= int(inicluster[1])
            inicluster[2] = float(inicluster[2].replace(",","."))
            inicluster[3]= " ".join(inicluster[3].split())
            listagrande.append(inicluster)
        else:
            if len(listagrande) > 0:
                continuecluster = lineas[x].strip().lower()
                continuecluster = " ".join(continuecluster.split())
                listagrande[len(listagrande)-1][3] = listagrande[len(listagrande)-1][3] + " " + continuecluster

    for elementos in listagrande:
        elementos[3] = elementos[3].replace(". ", "")
        elementos[3] = elementos[3].strip()
    df = pd.DataFrame(listagrande, columns =newcolums) 

    return df

