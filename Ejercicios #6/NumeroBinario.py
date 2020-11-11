#Emmanuel Galeana
#27/08/2020
#numeros binarios

def decimales_binarios(num):
    dividendo = num
    divisor = 2
    while True:
        cociente = dividendo//divisor
        residuo = dividendo%divisor
        print("construir el numero binario",residuo)
        dividendo = cociente
        if cociente == 0:
            break
            
decimales_binarios(8)
        
        
        