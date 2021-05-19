'''
las listas son estructuras de datos que se usan para almacenar valores.
Se asemejan a los vectores

Append(<obj>)
    Este método nos permite agregar nuevos elementos a una lista/vector.

Remove(<indice>)
    El método remove va a remover un elemento que se le pase como
    parámentro de la lista a donde se le esté aplicando.

Index(<dato>)
    Index devuelve el número de indice del elemento que le pasemos por parámetro.

Count(<dato>)
    Para saber cuántas veces un elemento de una lista
    se repite podemos utilizar el metodo count().

Reverse()
    También podemos invertir los elementos  de una lista.
'''

''' Escriba un programa que pida dos números enteros y escriba qué
    números son pares y cuáles impares desde el primero hasta el segundo.
'''

'''
Una tupla es una colección de elementos ordenada pero que no se puede modificar, es inalterable

se pueden recorrer y consultar mas no modificar

count()    Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la tupla.

 index()    Comparte el mismo método index() del tipo lista. Este método recibe un elemento como argumento, y devuelve
 el índice de su primera aparición en la tupla.

'''

'''
Un diccionario es una colección de elementos que están
indexados, no están ordenados y se pueden
modificar. Son escritos entre llaves
y están formados por pares de elementos, clave valor.

diccionario = {
    calve1:valor1,
    clave2:valor2,
     ...
}

keys()    Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.

items()    Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo,
    su valor.

values()     Retorna una lista de elementos, que serán los valores de nuestro diccionario.

clear()    Elimina todos los ítems del diccionario dejándolo vacío.

copy()    Retorna una copia del diccionario original.

get(<clave>)    Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un
    objeto none.

pop(<clave>)   Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.

setdefault():    Funciona de dos formas.
        En la primera como get: dic.setdefault(<clave>)
        Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.:
            dic.setdefault(<clave>,<valor>)

'''

'''
Las matrices se pueden definir de dos formas:
    Un vector bidimensional que ya no posee un solo indice sino que ahora posee subindices

    Una estructura de control que almacena datos y accede a ellos mediante filas y coljumnas

En este tipo de estructuras de datos ya no tendremos solo una posicion del array, sino que tendremos una posicion
definida por otras 2. En Python, estas se definen como listas dentro de listas... Las listas externas son las filas de
la matriz y las listas internas son las columnas de la misma. Esto puede variar segun el criterio de cada persona.

Supongamos que tenemos una matriz A

Sintaxis:
    A= [[a, b, c],[1, 2, 3],[True, False, 24.9]]

    Aquí estamos definiendo que la matriz tendrá 3 fila y  3 columnas quedando así

    [a,     b,     c]
    [1,     2,     3]
    [True, False, 24.9]

'''

'''
Escribir una función que reciba dos matrices y devuelva la suma.
'''
'''
Escriba un programa que pida la cantidad de números que se tienen que escribir
 y a continuación pida números hasta que la cantidad de elementos especificada. Mostrar la cantidad de numeros
positivos, negativos, pares e impares.
'''

'''
Crea un array de 10 posiciones de números aleatorios.  Muestra por consola el indice y el valor al que corresponde.
'''

'''Crea un array de números de un tamaño pasado por teclado, 
el array contendrá números aleatorios impares entre los números deseados, 
por último nos indica cual es el mayor de todos.'''

'''
Crea un array de números de 100 posiciones, que contendrá los números del 
1 al 100. Obtén la suma de todos ellos y el promedio. 

    promedio = suma(elementos)/elementos
'''

'''Realizar un programa que muestre por pantalla la traspuesta de una matriz'''
'''
