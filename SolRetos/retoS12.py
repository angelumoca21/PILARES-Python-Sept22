def primoONo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True


if __name__ == '__main__':
    if primoONo(53):
        print("Primo")
    else:
        print("No Primo")
    if primoONo(78):
        print("Primo")
    else:
        print("No Primo")