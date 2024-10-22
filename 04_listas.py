### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [24, 35, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.65, "Alex", "Arjona"]
print(my_other_list)

print(my_other_list[0])

age, height, name, surname = my_other_list

my_other_list.append("Molina")

my_other_list.insert(1, "Azul")

my_other_list.remove("Azul")

my_list.remove(30)

print(my_list.pop())

my_pop_element = my_list.pop(2)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.sort() # Ordena de menor a mayor
print(my_new_list)
print(my_new_list[1:3]) # Devuelve una sub lista con los elementos entre la posición 1 y 3