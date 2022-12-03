"""diccionario = {
    "llave1":1235,
    "llave2":True,
    "llave3":[1,2,3,4,5],
    "llave4":"Angel",
    "llave5":('a','b','c'),
    "llave6":3.1415
}

print("Diccionario original:",diccionario)
print(type(diccionario))
print("Valor de la llave 6:",diccionario["llave6"])
print("Valor de la llave 5 usando get:",diccionario.get("llave5"))
print("Valor de la llave 56 usando get:",diccionario.get("llave56"))
print(f"La cantidad de pares llaver-valor son:{len(diccionario)}")
diccionario["llave2"]=False
print("Diccionario modificado:",diccionario)
print("Comprobando que la llave4 existe en el diccionario:","llave4" in diccionario)
print("ELIMINANDO LLAVE4")
diccionario.pop("llave4")
print("Comprobando que la llave4 existe en el diccionario:","llave4" in diccionario)
print("Diccionario modificadoV2:",diccionario)
print("ELIMINANDO LLAVE1")
del diccionario["llave1"]
print("Diccionario modificadoV3:",diccionario)"""

miCarro = {
    "Marca":"Honda",
    "Modelo":"Civic",
    "Año":2010,
    "Gasolina":True
}

print("Valores de miCarro:",miCarro.values())
print("Llaves de miCarro:",miCarro.keys())
print("Llaves de miCarro:",miCarro.items())

for valor, llave in miCarro.items():
    print(f"{valor}=>{llave}")