'''
crear un programa que le pida al usuario su edad, nombre, dos números y muestre por pantalla:
    - suma
    - resta
    - multiplicación
    - o división (dependiendo de la opcion)
    - de ambos números seguidos de su nombre y edad
    NOTA: si el usuario no es mayor de 5 años, no puede usar el programa

    ingrese su nombre
    ingrese su edad
    ingrese el primer numero 
    ingrese el segundo numero 

    1. suma
    2. resta
    3. multi
    4. division
    resultado de la operación : X 
    Nombre: 
    Edad: 
    
'''

def main():

    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))

    if (edad > 5):
        print("bienvenido al programa")
        
        num1 = int(input("\n Ingrese el 1er numero: "))
        num2 = int(input("Ingrese el 2do numero: "))

        opcion = (str(input("Elija una opcion siendo 1 suma, 2 resta, 3 multiplicacion, 4 division: ")))
    
        op_suma = "1"
        op_resta = "2"
        op_multi = "3"
        op_divi = "4"

        if(opcion == op_suma):
            print(f"El resultado de la suma es: {(num1 + num2)}")
        elif(opcion == op_resta):
            print(f"El resultado de la resta es: {(num1 - num2)}")
        elif(opcion == op_multi):
            print(f"El resultado de la multiplicacion es: {(num1 * num2)}")
        elif(opcion == op_divi):
            print(f"El resultado de la division es: {(num1 / num2)}")
        else:
            print("ingrese otra funcion\n")

        print(f"nombre: {(nombre)}")
        print(f"edad: {(edad)}")

    else:
        print("No puede usar el programa")
    
   








main()


