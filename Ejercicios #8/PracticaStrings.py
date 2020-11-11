#Emmanuel Galeana
#25/09/2020
#AAAAAAAAAAAAAA

def practica():
    frase = input('Ingresa frase: ').lower()
    nuevafrase = ""
    for caracter in frase:                   #Para que observe cada letra de la palabra 
        if caracter == "a":
            nuevafrase += "a"
    if nuevafrase == "":
        print("no hay a")
    else:
        print(nuevafrase)
    
practica()
    
            
            
        
        
    
    