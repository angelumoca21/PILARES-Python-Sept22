"Uso de funciones sin parametros y sin retorno de datos"
def areaCuadrado():
    l = float(input("Ingresa el lado del cuadrado:"))
    area = l * l
    print(f"El area del cuadrado es {area} usando v1.")

"Uso de funciones con parametros y sin retorno de datos"
def areaCuadrado2(lado):
    area = lado * lado
    print(f"El area del cuadrado es {area} usando v2.")

"Uso de funciones sin parametros y con retorno de datos"
def areaCuadrado3():
    LADO = float(input("Ingresa el lado del cuadrado:"))
    area = LADO * LADO
    return area

"Uso de funciones con parametros y con retorno de datos"
def areaCuadrado4(LADO):
    area = LADO * LADO
    return area

#Inicia programa principal
def main():
    areaCuadrado() #llamado de la funcion sin parametros y sin retorno de dato
    areaCuadrado2(8) #llamado de la funcion con parametros y sin retorno de datos
    AREA = areaCuadrado3()#llamado de la funcion sin parametros y con retorno de datos
    print(f"El area del cuadrado es {AREA} usando v3.")

    Area = areaCuadrado4(10)#llamado de la funcion con parametros y con retorno de datos
    print(f"El area del cuadrado es {Area} usando v4.")

if __name__ == '__main__':
    main()