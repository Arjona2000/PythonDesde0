### Bucles ###

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # No existe my_condition++ en python, tenemos que hacer += 1

if my_condition == 10:
    print("Mi condición es igual a 10")
else:
    print("Mi condición es mayor que 10")

print("La ejecución continúa")

while my_condition < 20:
    print("Mi condición es menor que 20")
    my_condition += 2 

    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print("Mi condición es menor que 20")


# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (24, 1.65, "Alex", "Arjona")

for element in my_tuple:
    print(element)

my_set = {"Alex", "Arjona", 24}

for element in my_set:
    print(element)


my_dict = {"Nombre":"Alex", "Apellido":"Arjona", "Edad": 24, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta") # Si el elemento es "Edad", el print no se ejecuta, pero el for sigue su curso, si ponemos un break, forzamos el fin del bucle
else:
    print("El bucle for para el diccionario ha finalizado.")

