### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Alex", "Arjona", 24}
print(type(my_other_set))

my_other_set.add(1.65)

print(my_other_set)

print("Alex" in my_other_set)
print("Alejandro" in my_other_set)

my_other_set.remove("Alex")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(len(my_other_set)) NameError: name 'my_other_set' is not defined

my_set = {"Alex", "Arjona", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java", "Python", "C#"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C++"}))

print(my_new_set.difference(my_set))