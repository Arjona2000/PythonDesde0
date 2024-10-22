### Clases ### 

class MyEmptyPerson:
    #def __init__(self) -> None: # Constructor vacío
    pass # Es para que no de error al crear una clase vacía

#print(MyEmptyPerson)
#print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, edad = 0):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname} ({edad})"

    def get_name(self):
        return self.name
    
    def walk(self):
        print(f"{self.full_name} Está caminando")
    

my_person = Person("Alex", "Arjona")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("Alex", "Arjona", 24)

print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Héctor De León, 35"
print(my_other_person.full_name)