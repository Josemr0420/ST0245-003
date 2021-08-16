#Por: Mauricio Correa y Jose Muñoz
archivo = open ("Nombre del archivo.csv" , "r")
lineas = archivo.readlines()

registros = []
for linea in lineas:
    actual = linea.split(",")
    registros.append(actual)

print(registros[1][1])
