"""
funcion input():

    funcion utilizada para pedir datos al usuario por teclado
        (similar a un read en pseudocodigo)

    -se le puede pasar un mensaje al usuario
    -para mayor explicitud de datos, se puede encerrar en un casting (str, int, float, bool)
    -se pueden pasar variables en sus parametros
    -devuelve el dato que pasó el usuario por teclado así que este debe
        ser asignado en una variable

"""

def main():

    num1 = int(input("ingrese el primer numero:"))
    num2 = int(input("ingrese el segundo numero:"))
    print(num1 + num2)

main()
'''
    #mensaje = "ingrese el monto: "
    #nombre = int(input("Escriba su nombre: " + mensaje))
    #print(type(nombre))

    # variable = int("123")
    # print(type(variable))

    #var = bool("true")
    #print(type(var))
'''