palabra = input("Ingresa la palabra a codificar:")
vocales = "aeiou"

if palabra[0] in vocales:
    print(f"{palabra} => {palabra}way")
else:
    print(f"{palabra} => {palabra[1:]}{palabra[0]}ay")