def main():
    # Escribe el código adecuado para completar el programa
    print("Ingresa el primer número:")
    x = int(input())
    print("Ingresa el segundo número:")
    y = int(input())
    print("Ingresa el tercer número")
    z = int(input())

    if(x<y and y<z):
        print("\n", x,"\n",y,"\n",z)
    elif(y<x and x<z):
        print("\n",y,"\n",x,"\n",z)
    elif(z<x and x<y):
        print("\n",z,"\n",x,"\n",y)
    elif(z<y and y<x): 
        print("\n",z,"\n",y,"\n",x) 
    elif(x<z and z<y):
        print("\n",x,"\n",z,"\n",y)
    elif(y<z and z<x):
        print("\n",y,"\n",z,"\n",x)
    pass


if __name__=='__main__':
    main()
