print(" Bem vindo a calculadora python, digite umas das operações abaixo:")
print("A= adição")
print("S= subtração")
print("D= divisão")
print("M=multiplicação")

n1=int(input("digite um numero:" ))
n2=int(input("digite um numero:" ))

operação=input("digite uma operação: ")


if operação== "A":
    print(n1+n2)
if operação == "S":
     print(n1 - n2)
if operação== "D":
    if n2==0:
        print("erro")
    if n2!= 0:
        print(n1/n2)
if operação== "M":
    print(n1*n2)
