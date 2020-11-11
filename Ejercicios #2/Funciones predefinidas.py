#Emmanuel Galeana
#17/08/2020
#Programas que utilizan funciones predefinidas

#import math, help(math)
import math
radio = int(input())
area = (4*math.pi)*(math.pow(radio,2))
volumen = (4*math.pi)*(math.pow(radio,3))/3

print("El area es: {0:.2f}".format(area))
print("El volumen es: {0:.2f}".format(volumen))