'''
"""
-------SOLUCION AL EJERCICIO 6-----------------------------
0.Mensaje inicial🆗
1.Pedir total consumido.🆗
2.Pedir total personas.🆗
3.Pedir propina.🆗
4.Realizar operaciones:
    totalConsumido + propina = total🆗
    total/numPersonas = pagoxpersona🆗
5.Imprimir en pantalla cantidad a pagar x persona.🆗
"""

print("Sistema de calculos del restaurante EL FAVORITO 🍲")
totalConsumido = float(input("Ingresa el total consumido:"))
personas = int(input("Ingresa la cantidad de personas en la mesa:"))
propina = float(input("Ingresa la cantidad de propina:"))

total = totalConsumido + propina
pagoxpersona = total / personas

print(f"La cantidad a pagar por cada persona es de ${pagoxpersona}.")
-------SOLUCION AL EJERCICIO 6-----------------------------
'''

"""Pedir al usuario su edad y arrojar si es mayor de edad o es menor de edad.
edad < 18 -> Menor de edad 
edad >= 18 ->Mayor de edad"""
edad = int(input("Ingresa tu edad:"))
if edad < 18:
    #bloque cuando cond -> v
    print("Eres menor de edad.")
else:
    #bloque cuando cond -> f
    print("Eres mayor de edad.")