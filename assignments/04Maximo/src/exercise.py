def main():
    #escribe tu código abajo de esta línea
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if( y < x > z):
        print(x)
    if( x < y > z):
        print(y)
    if( y < z > x):
        print(z)
    pass


if __name__=='__main__':
    main()
