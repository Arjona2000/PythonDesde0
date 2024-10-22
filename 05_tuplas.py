### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.65, "Alex", "Arjona")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Alex"))
print(my_tuple.index("Arjona")) # Devuelve el primer índice del valor que encuentre, si hubiera dos "Arjona" en la tupla, devolvería el índice del primero.

# my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment
#print(my_tuple)

print(my_tuple + my_other_tuple)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) 

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[1] = 1.80
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))

my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined 