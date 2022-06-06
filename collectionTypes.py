from collections import defaultdict

# Lo que tiene que ver con listas y similares
# solo repasaré los elementos que sean neuvos para mi

a = [1, 1, 1, 2, 4, 3]

# Cuenta la cantidad de veces que se repite en la lista
print(a.count(1))  # 3

# Para reversear la lista
a.reverse()
print(a)  # [3, 4, 2, 1, 1, 1]

# Para nombrar cada elemento con un iterador

for element in a:
    print(element)

# Tuplas

# Las tuplas son similares a las listas, solo que estas son inmutables
# entonces sus valores no puede ser cambiados ni removidos, son usadas para pequeñas
# colecciones de valores que no cambiaran, como una dirección IP y un puerto.

ip_address = ('10.20.30.40', 8080)

# si queremos definir una tupla con un solo elemento, se coloca una coma al final
one_member_tuple = ('Only member',)
# o sin usar parentesis, pero colocando la coma
one_member_tuple_2 = 'Only member',
# o usando la sintaxis de tupla
one_member_tuple_3 = tuple(['Only member'])

# Diccionarios

# https://devcode.la/tutoriales/diccionarios-en-python/

# Un diccionario es una colección de pares Clave - Valor
# separados con llave y cada par es separado por coma, y cada
# llave - valor es separado por dos puntos

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

# Para obtener el valor debemos referirnos a su llave
ca_capital = state_capitals['California']
print(ca_capital)  # Sacramento

# También se puede iterar para obtener todas las llaves

llaves = state_capitals.keys()
print(llaves)

for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))

# Set

# Es una colección de elementos que no se repiten sin algún tipo de orden
# Se usan en situaciones  donde es importante que algunas cosas sean agrupadas
# juntas sin importar su orden

# Se define muy parecido al diccionario

first_names = {'Adam', 'Beth', 'Charlie'}
print(first_names)

# O se puede hacer con una lista ya existente

my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)

# Se puede verificar la pertenencia al conjunto usando in
if 'Adam' in first_names:
    print('Adam')

# y se puede iterar como una lista normal, solo hay que recordar que no hay un orden

# defaultdict

# Es un diccionario con un valor por defecto para las llaves
# por ejemplo, si mandamos a llamar una llave que no existe, aparecerá un error
# entonces esta librería lo que nos permite es que si colocamos una llave no existente
# por defecto nos arrojará un resultado, sin tener algún error
# en la primera linea de este archivo se encuentra lo que hay que importar

state_capitals = defaultdict(lambda: 'Boston')
print(state_capitals['Alabama'])
