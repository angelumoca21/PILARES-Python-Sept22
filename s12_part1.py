def principal():
    nombre = input("Ingresa tu nombre:")
    edad = int(input("Ingresa tu edad:"))
    direccion = input("Ingresa tu direccion:")
    numTelefono = input("Ingresa tu telefono:")

    persona = {'nombre':nombre,'edad':edad,"direccion":direccion,"telefono":numTelefono}
    print(type(persona))

    print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y numero de telefono es {persona['telefono']}")
    print(persona.items())

    for llave, valor in persona.items():
        print(f"{llave}=>{valor}")

    print(persona.keys())
    print(persona.values())

if __name__ == '__main__':
    principal()