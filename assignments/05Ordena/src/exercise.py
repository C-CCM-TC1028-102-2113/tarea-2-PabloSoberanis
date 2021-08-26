def main():
    # Escribe el código adecuado para completar el programa
    print("Ingresa el primer número")
    x = int(input())
    print("Ingresa el segundo número")
    y = int(input())
    print("Ingresa el tercer número")
    z = int(input())

    if(x<y and y<z):
        print(x,"-",y,"-",z)
    elif(y<x and x<z):
        print(y,"-",x,"-",z)
    elif(z<x and x<y):
        print(z,"-",x,"-",y)
    elif(z<y and y<x):
        print(z,"-",y,"-",x) 
    elif(x<z and z<y):
        print(x,"-",z,"-",y)
    elif(y<z and z<x):
        print(y,"-",z,"-",x)
    pass


if __name__=='__main__':
    main()
