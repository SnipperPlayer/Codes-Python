#!/usr/bin/env python
# coding: utf-8

# # Métodos de las cadenas

# Una cadena en Python es una secuencia de caracteres enmarcadas por comillas dobles o simples.

# In[1]:


var_tipo_cadena = "Esto es una cadena en Python"
var_tipo_cadena


# Una cadena puede contener cualquier caracter válido. Las cadenas en Python son INMUTABLES, es decir, no pueden modificarse una vez que han sido asignados los valores.

# Si quieres acceder a un caracter en especial de la cadena, deberás usar el operador [] e indicar la posición del caracter en la cadena. La primera posición de una cadena es la cero.

# In[2]:


var_tipo_cadena[0] # caracter en la posición cero de var_tipo_cadena


# Una cadena en varios renglones:

# In[3]:


cadena = """esta es una cadena
escrita
en varios renglones
"""
print(cadena)


# ### Secuencias de escape
# https://www.w3schools.com/python/python_strings.asp

# In[4]:


cadena = "esta es una cadena con salto de linea aqui,\nun tabulador aqui\t, y uso de comillas \"dentro\" de la misma cadena"
print(cadena)


# ### operador *: repite la cadena el número de veces que se indica

# In[5]:


print("Hola" * 3) # imprime 3 veces la cadena "Hola"


# ### operador +: realiza la suma o concatenación de cadenas

# In[6]:


suma_cadenas = "sumo" + "cadenas"
suma_cadenas


# ### operador +=: realiza la suma o cancatenación

# In[7]:


mas_igual = 'Hola'
mas_igual += ' '
mas_igual += 'Mundo'
print(mas_igual)


# ### operador %: permite incorporar valores a una cadena que se imprime

# In[8]:


texto = "La ecuacion %d tiene una %s y una variable con valor decimal %f" % (1, 'descripcion',5.567)
print(texto)


# ### len(): calcula la extensión de una cadena (el número de carcateres de la cadena)

# In[9]:


cadena = "la extension de una cadena es la cantidad de caracteres que tiene"
print("cadena tiene {} caracteres".format(len(cadena)))


# ### upper(): devuelve la cadena con todos sus caracteres en mayúscula

# In[10]:


"Hola Mundo".upper()


# ### lower(): devuelve la cadena con todos sus caracteres en minúscula

# In[11]:


"Hola Mundo".lower()


# ### capitalize(): devuelve la cadena con su primer carácter en mayúscula

# In[12]:


"hola mundo".capitalize()


# ### title(): devuelve la cadena con el primer carácter de cada palabra en mayúscula

# In[13]:


"hola mundo".title()


# ### count(): devuelve la cuenta de las veces que aparece una subcadena en la cadena

# In[14]:


"Hola mundo".count('mundo')


# ### find(): devuelve el índice en el que aparece la subcadena (-1 si no aparece)

# In[15]:


"Hola mundo".find('mundo')


# In[16]:


"Hola mundo".find('mundoz')


# In[17]:


mensaje = "Hola Mundo"
print(mensaje[:5].find("d"))


# ### rfind():  devuelve el índice en el que aparece la subcadena, empezando por el final

# In[18]:


"Hola mundo mundo mundo".rfind('mundo')


# ### isdigit(): devuelve True si todos los caracteres de la cadena son dígitos (False en caso contrario)

# In[19]:


c = "100"


# In[20]:


c.isdigit()


# ### isdecimal(): determina si todos los caracteres de la cadena son números decimales

# In[21]:


decimal = "1234.7"
decimal.isdecimal()


# ### isalnum(): devuelve True si todos los caracteres de la cadena son letras o dígitos

# In[22]:


c2 = "ABC10034po"


# In[23]:


c2.isalnum()


# ### isalpha(): devuelve True si en la cadena sólo hay carácteres alfabéticos

# In[24]:


c2.isalpha()


# In[25]:


"Holamundo".isalpha()


# ### islower(): devuelve True si toda la cadena está en minúsculas

# In[26]:


"Hola mundo".islower()


# ### isupper(): devuelve True si toda la cadena está en mayúsculas

# In[27]:


"Hola mundo".isupper()


# ### istitle(): devuelve True si la primera letra de cada palabra es mayúscula

# In[28]:


"Hola Mundo".istitle()


# ### isspace(): devuelve True si todos los caracteres de la la cadena son espacios

# In[29]:


"  -  ".isspace()


# ### startswith(): devuelve True si la cadena empieza con una subcadena

# In[30]:


"Hola mundo".startswith("Mola")


# ### endswith(): devuelve True si la cadena acaba con una subcadena

# In[31]:


"Hola mundo".endswith('mundo')


# ### split(): separa la cadena en subcadenas a partir de sus espacios y devuelve una lista

# In[32]:


"Hola mundo mundo".split()[0]


# In[33]:


"Hola mundo mundo".split()


# #### Con split(), podemos indicar el carácter a partir del que se separa:

# In[34]:


"Hola,mundo,mundo,otra,palabra".split(',')


# ### join(): une todos los caracteres de una cadena utilizando un caracter de unión

# In[35]:


",".join("Hola mundo")


# In[36]:


" ".join("Hola")


# ### strip(): borra todos los espacios por delante y detrás de una cadena y la devuelve

# In[37]:


"   Hola mundo     ".strip()


# #### con strip puedes indicar el carácter a borrar:

# In[38]:


"-----Hola mundo---".strip('-')


# ### replace(): reemplaza una subcadena de una cadena por otra y la devuelve

# In[39]:


"Hola mundo".replace('o','0')


# #### con replace() puedes indicar un límite de veces a reemplazar:

# In[40]:


"Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)


# ### Recorro todos los caracteres de una cadena

# In[41]:


cadena = "la cadena"
for caracter in cadena:
    print(caracter)


# ### Slicing, segmentos de las cadenas [inicio:end]
# Si j es un entero no negativo, se puede usar la notación a[ : j ] para representar al segmento a[ 0 : j ]; también se puede usar la notación a[ j : ] para representar al segmento a[ j : len(a) ]; a[ : : ] representa el segmento de 0 a len(a)

# In[42]:


cadena = "esto es una cadena"
print(cadena[-1]) # ultimo caracter de la cadena
print(cadena[::]) # desde el primero hasta el ultimo carcater por omision
print(cadena[0::]) # desde el caracter en la posicion 0 hasta el ultimo por omision
print(cadena[1:3]) # caracteres de las posiciones en el rango 1, 2 sin incluir el 3
print(cadena[-2]) # penultimo caracter
print(cadena[-5:-2]) # carcater de la posicion 5 de derecha a izquierda hasta la posicion -3 de derecha a izquierda

otra_cadena = ""
print(otra_cadena[0:0])


# ### Verificar contenidos en cadena

# In[43]:


texto = "La lluvia de los últimos días ha generado inundaciones en Cuernavaca"
x = "una" not in texto
print(x)
y = "La" in texto
print(y)

