num1= int(input("digite el primer numero entero: "))
num2= int(input("digite el segundo numero entero: "))

for i in range(num1,num2+1):
    if i % 2 == 0:
        print(i)