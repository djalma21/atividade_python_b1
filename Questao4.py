l1=int(input("informe o lado do triangulo: "))
l2=int(input("informe o lado do triangulo: "))
l3=int(input("informe o lado do triangulo: "))

if l1+l2<l3:
    print("essas medidas não forma um triangulo")
    exit()
if l1==l2 and l2==l3:
    print("é um triangulo equilatero!")
elif l1==l2 or l1==l2 or l2==l3:
    print("é um triangulo isóceles!")
else:
    print("é um triangulo escaleno")
