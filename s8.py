"""for contador in range(2,7,2):
    print(f"Hola, {contador}")
"""

"""
1.Pedir frase al usuario.
2.Pedir numero.
3.Generar ciclo que repetirá la frase.
"""
#erick
phrase = input("Ingresa una frase: ")
num = int(input("Ingresa un numero: "))
for i in range(num):
    print(f"{i} {phrase}")

#santiago
frase = input("\nIngresa una frase: ")
numero = int(input("Ingresa un numero: "))
print("\n")
for i in range(numero):
    print(f"{i+1} --> {frase}\n")

#ariel
rep = 0
frase = input("Ingresa la frase que deseas repetir")
rep = int(input("Indica el numero de veces que deseas repetir la frase"))
for rep in range (0,rep,1):
    print(f"{frase}")
