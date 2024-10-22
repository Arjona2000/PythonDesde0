### Funciones ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(7, 23)
sum_two_values(1, 2)
sum_two_values(70, 30)
sum_two_values("7", "2") # Las cadenas de texto las concatena

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values(10,5)
print(my_result)

def print_name(name, surname, genero = "No contesta"):
    print(f"{name} {surname} {genero}") # La f es para acceder a los valores de name y surname

print_name(surname = "Arjona", name = "Alex")
print_name(surname = "Arjona", name = "Alex", genero = "Hombre")

def print_texts(*text):
    print(text)

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "Alex", "Arjona")
print_texts("Hola")

print_upper_texts("Hola", "Python", "Alex", "Arjona")
print_upper_texts("Hola")