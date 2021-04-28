''' escriba un programa que pida numeros decimales 
mientras el ususario escrba numero que el primero.

'''
num1= float(input("digite el primer numero: "))
num2= float(input("digite el segundo numero: "))


while num2 < num1:
    num2 = float(input("digite un numero mayor al primero: "))
print(num2)