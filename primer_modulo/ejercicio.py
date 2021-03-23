'''
    crear variable que contenga un texto y mostrar el tipo de la variable,
    crear otra variable que almacene la longitud de la variable anterior,
    crear otra variable que almacene la primera variable pero en mayusculas.
    crear otra variable que concatene la variable mayusculas y la variable de longitud
'''

def main():

    nombre = 'yuletsy pabon'
    print(nombre)
    print(type(nombre))

    longitud = len(nombre)
    print(longitud)


    mayusculas = nombre.upper()
    print(mayusculas)

    concatenar = "Mi nombre es " + mayusculas + " - " + repr(longitud)
    print(concatenar)

main()