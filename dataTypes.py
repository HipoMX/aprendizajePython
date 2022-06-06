# Defino si las variables son falsas o verdaderas
x = True
y = False

# Indico que si alguna de esas variables es verdadera, retornará un True
print(x or y) #True

# Indico que ambas tienen que ser verdaderas para que sea verdadero
print(x and y) #False

# Devuelve lo contrario a lo que es la variable
print(not x)  #False

# Lo mismo que el anterior solo es para probar
print(not y) #True

# De python 2.x a python 3.x, un boleano también es un int. El tipo boleano
# es una subclase del tipo int, y True y Falso solo son sus instancias
print(issubclass(bool, int)) #True

print(isinstance(True, bool)) #True
print(isinstance(False, bool)) #True

#También es importante mencionar que para cuestiones aritméticas
#El True funciona como un uno y el False como un 0

print(x * y) #0
print(x + y) #1