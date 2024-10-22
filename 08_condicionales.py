### Condicionales ###

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5*5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condición del tercer if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")

elif my_condition == 1: # elif == else if()
    print("Es igual a 1")
else:
    print("Es mayor que 10 o menor o igual que 20")

print("La ejecución continúa")

my_string = ""

if not my_string: # Si está vacía
    print("Mi cadena de texto está vacía")

if my_string: # Si no está vacía
    print("Mi cadena de texto no es vacía")

if my_string == "Mi cadena de textooooooooo":
    print("Estas cadenas de texto coinciden")

