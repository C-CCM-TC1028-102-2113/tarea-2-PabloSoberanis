
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if (edad >= 18):
        identificacion = str(input("¿Tienes identifiación oficial? (s/n): "))
        if(identificacion == "s" ):
            print("Trámite de licencia concedido")
        elif(identificacion == "n"):
            print("No cumple requisitos")
        else:
            print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")
    pass


if __name__ == '__main__':
    main()
