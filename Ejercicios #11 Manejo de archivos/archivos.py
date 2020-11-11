# MLBC
# manejo de archivo de texto en Python

# Archivos de texto

# Crear archivo y escribir texto
texto = "Una línea con texto\ny esta es otra línea con texto"
archivo = open('archivo.txt','w')  # archivo.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)
archivo.write(texto) # escribimos el texto
archivo.close()  # cerramos el archivo

# Lectura de un archivo de texto
archivo = open('archivo.txt','r')  # modo lectura read, por omision r, no es necesario
texto = archivo.read() # lectura completa
archivo.close()
print('\ntexto leido con read')
print(texto)
archivo = open('archivo.txt','r')
texto = archivo.readlines() # leer creando una lista de líneas
archivo.close()
print('\ntexto leido con readlines')
print(texto)
print(texto[-1]) # Última línea

# Extensión de un archivo de texto
archivo = open('archivo.txt','a')  # modo a, append, añadir - extender (puntero al final)
archivo.write('\nOtra línea más abajo del todo')
archivo.close()

# Lectura de un archivo no existente
#archivo = open('archivo_inventado.txt','r')
archivo = open('archivo_inventado.txt','a+')  # Extensión con escritura simultánea, crea archivo si no existe

# Lectura línea a línea
archivo = open('archivo.txt','r')
archivo.readline()   # Línea a línea
archivo.readline()
texto = archivo.readline()
print('\n tercera linea leida')
print(texto)
archivo.close()

# Lectura línea a línea secuencial
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

# Manejando el puntero
print('\nPunteros')
archivo = open('archivo.txt','r')
archivo.seek(0) # Puntero al principio
texto = archivo.read(10) # Leemos 10 carácteres
print('texto read(10)',texto)
archivo.read(10) # Leemos 10 carácteres más, a partir del 10 donde está el puntero
archivo.seek(0)
linea = archivo.seek( len(archivo.readline()) ) # Leemos la primera línea y situamos el puntero al principio de la segunda
texto = archivo.read() # Leemos todo lo que queda del puntero hasta el final
print('el resto',texto)
# ## Lectura y escritura a la vez
archivo2 = open('archivo2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
archivo2.write(texto)
archivo2.close()
archivo2 = open('archivo2.txt','r+')  # + escritura simultánea, puntero al principio por defecto
archivo2.write('asdfgh')
archivo2.close()

## Modificar una línea específica
archivo2 = open('archivo2.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
texto = archivo2.readlines() # leemos todas las líneas
print(texto)
texto[2] = "Esta es la línea 3 modificada\n"  # indice menos 1
print(texto)
archivo2.seek(0) # Ponemos el puntero al principio
archivo2.writelines(texto)
archivo2.close()

