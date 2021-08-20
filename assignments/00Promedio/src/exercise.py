def main():
    #escribe tu código abajo de esta línea
    print("Promedio de 10 números")

    s = 0 #Acumulador
    cp = 0 #Contador de pares
    ci = 0 #Contador de impares

    for i in range (10):
        n = int(input("Ingrese un valor: "))

        if n % 2 == 0:
            cp = cp +1
        else:
            ci = ci + 1
        s = s + n

    promedio = s / 10
    
    print(f"El promedio de los valores capturados es: {promedio}")
    print(f"El total de valores pares fue: {cp}")
    print(f"El total de valores impares fue: {ci}")

if __name__=='__main__':
    main()
