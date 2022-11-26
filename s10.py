"""lista1 = [5,"Hola",True,5.22,[1,2,3,4,5]]
print(type(lista1))
print("original:",lista1)
lista1[0]="adios"
print("mutada:",lista1)
lista1.append(456)
print("mutada2:",lista1)
lista1.insert(3,"Angel")
print("mutada3:",lista1)
lista1.reverse()
print("mutada4:",lista1)
lista1.pop(1)
print("mutada5:",lista1)
lista1.remove("Angel")
print("mutada6:",lista1)
print("indexBusqueda",lista1.index("adios"))
longitud = len(lista1)
print(f"La lista1 contine:{longitud} elementos")
lista2 = [5,456,741,5.22,1000,5263,789]
print("original2:",lista2)
lista2.sort()
print("lista2Mutada:",lista2)
lista2.sort(reverse=True)
print("lista2MutadaReverse:",lista2)
lista3 = ["a","z","r","p"]
print("original3:",lista3)
lista3.sort()
print("lista3Mutada:",lista3)

lista2 = [5,456,741,5.22,1000,5263,789]
for elemento in lista2:
    print(elemento)

tuplaEjemplo = (5,456,741,5.22,1000,5263,789)
print(tuplaEjemplo)
print(type(tuplaEjemplo))
tuplaEjemplo = list(tuplaEjemplo)
print(type(tuplaEjemplo))
tuplaEjemplo[0]=45
print(tuplaEjemplo)
tuplaEjemplo =tuple(tuplaEjemplo)
print(type(tuplaEjemplo))
print(tuplaEjemplo)
"""
lista1 = [5,"Hola",True,5.22,[1,2,3,4,5]]
print(lista1)
lista1[-1].append(6)
print(lista1)
print(lista1[-1][-1])