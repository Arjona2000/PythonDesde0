### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Alex", "Apellido":"Arjona", "Edad": 24, 1:"Python"}

my_dict = {
    "Nombre":"Alex", 
    "Apellido":"Arjona",
    "Edad": 24,
    "Lenguajes": {"Python", "Java", "C#"},
    1:1.65
    }

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"

my_dict["Calle"] = "Calle Oslo"

print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Alex" in my_dict)
print("Alejandro" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]


my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Alex", "Arjona"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Alex")
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))