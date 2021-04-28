def main():

    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))

    if (edad > 5):
        print("Bienvenido al programa de operaciones basicas")
        
        num1 = int(input("\n Ingrese el 1er numero: "))
        num2 = int(input("Ingrese el 2do numero: "))

        opcion = (str(input("Elija una opcion siendo 1 suma, 2 resta, 3 multiplicacion, 4 division: ")))
    
        if(opcion ==  "1"):
            print(f"El resultado de la suma es: {(num1 + num2)}")
        elif(opcion ==  "2"):
            print(f"El resultado de la resta es: {(num1 - num2)}")
        elif(opcion ==  "3"):
            print(f"El resultado de la multiplicacion es: {(num1 * num2)}")
        elif(opcion ==  "4"):
            print(f"El resultado de la division es: {(num1 / num2)}")
        else:
            print("ingrese otra funcion\n")

        print(f"Tu nombre es: {(nombre)}")
        print(f"Tienes: {(edad)} años")
    else:
        print("No puede usar el programa porque es menor de 5 años")
main()


