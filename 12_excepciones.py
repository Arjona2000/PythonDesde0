### Manejo de Excepciones ###

numberOne, numberTwo = 5, 1

numberTwo = "1"

try: 
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as e:
    # Se ejecuta si se produce una excepción de tipo ValueError
    print(e)
except TypeError as e:
     # Se ejecuta si se produce una excepción de tipo TypeError
    print(e)
except Exception as e:
    print(e)
else:
    # Se ejecuta si no se produce una excepción
    print("Continuamos con la ejecución sin errores")

finally: 
    #Se ejecuta siempre
    print("La ejecución continúa")