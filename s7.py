######################################EXPLICACION ELIF#################################################
"""Pedir al usuario su edad y arrojar si es mayor de edad o es menor de edad.
En caso de que la edad sea entre 12 y 18 -> Eres menor de edad y eres un adolescente
En caso de que la edad sea mayor a 60 -> Eres un adulto mayor.
edad < 18 -> Menor de edad 
edad >= 18 ->Mayor de edad"""
"""
edad = int(input("Ingresa tu edad:"))
if (edad >= 12) and (edad < 19):
    print("Eres menor de edad y eres un adolescente.")
elif edad >= 60:
    print("Eres un adulto mayor.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
"""
######################################EJERCICIO7#################################################
"""
1.Mostrar al usuario tipos de pizzas:
    a.Vegetarianas
    b.No vegetariana
2.Pedir al usuario que indique el tipo tipo de pizza que quiere.
3.Mostrar ingredientes en funcion a la opcion escogida:
    Si vegetariana:
        a.Pimiento
        b.Tofu
    Si no vegetariana:
        a.peperoni
        b.jamon
        c.salmon
4.Pedir al usuario el ingrediente que desea.
5.Mostrar en pantalla la pizza ordenada.
****Nota: todas las pizzas llevan salsa tomate y queso.******
"""

print("""Bienvenido a la pizzeria Bella Napoli 🍕
        Tipos de pizza:
        a.Vegetariana
        b.No vegetariana""")

tipoPizza = input("¿Que tipo de pizza quieres? ")

if tipoPizza == 'a':
    print("""Los ingredientes disponibles son:
            1.Pimiento
            2.Tofu""")
    ingrediente = input("Escoge tu ingrediente:")
    if ingrediente == '1':
        print("La pizza que ordenaste es: pimiento, salsa de tomate y queso.")
    else:
        print("La pizza que ordenaste es: tofu, salsa de tomate y queso.")
else:
    print("""Los ingredientes disponibles son:
            1.Pepperoni
            2.Jamon
            3.Salmon""")
    ingrediente = input("Escoge tu ingrediente:")
