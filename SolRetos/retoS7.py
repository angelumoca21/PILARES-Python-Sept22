numElefantes = 0
contador = 1

numElefantes = int(input("Ingresa la cantidad de elefantes para cantarte:"))
if (numElefantes >  0) and (numElefantes < 11):
    while contador <= numElefantes:
        if (contador == 1):
            print(f"{contador} elefante se columpiaba")
            print("sobre la tela de una araña")
            print("como veia que resistia") 
            print("fue a llamar a otro elefante")
        else:
            print(f"{contador} elefantes se columpiaban")
            print("sobre la tela de una araña")
            print("como veian que resistia") 
            print("fueron a llamar a otro elefante")
        contador = contador + 1
elif numElefantes > 10:
    print("La telaraña no aguanta tantos elefantes.")
elif numElefantes == 0:
    print("OK aguafiestas")
else:
    print("El numero que ingresaste no es valido")