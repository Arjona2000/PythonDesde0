# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)

# Algunas funciones del sistema
print(len(my_int_to_str_variable))
print(len(my_string_variable))

# Variables en una sola línea

name, surname, age = 'Alejandro', 'Arjona', 24
print('Me llamo:', name, surname,'y tengo:', age,'años.')

# Inputs

#name = input('¿Cómo te llamas? ')
#age = input('¿Cuántos años tienes? ')

print(name)
print(age)

name = 24
age = 'Alejandro'
print(name)
print(age)

# Probamos a forzar el tipo
address: str = 'Mi dirección'
address = 32
print(address)
print(type(address))

