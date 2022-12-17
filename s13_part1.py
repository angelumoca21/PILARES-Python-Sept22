def promedio(mate=0,espanol=0,ciencias=0,progra=0):
    suma = mate + espanol + ciencias + progra
    resultado = suma / 4
    return suma,resultado

SUMA,RESULTADO = promedio(10,8,9,7)
print("PromV1",SUMA,RESULTADO)
SUMA,RESULTADO = promedio()
print("PromV2",SUMA,RESULTADO)
SUMA,RESULTADO = promedio(progra=10,mate=8)
print("PromV3",SUMA,RESULTADO)

