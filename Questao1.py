n1 = int(input('digite um número'))
n2 = int(input('digite um número'))
n3 = int(input('digite um número'))
if n1 < n2 < n3:
    print('ordem crescente',n1,n2,n3)
if n1 < n3 < n2:
    print('ordem crescente',n1,n3,n2)
if n2 < n1 < n3:
    print('ordem crescente',n2,n1,n3)
if n2 < n3 < n1:
    print('ordem crescente',n2,n3,n1)
if n3 < n1 < n2:
    print('ordem crescente',n3,n1,n2)
if n3 < n2 < n1:
    print('ordem crescentes',n3,n2,n1)
if n1 > n2 > n3:
    print('ordem decrescente', n1, n2,n3)
if n1 > n3 > n2:
    print('ordem decrescente',n1,n3,n2)
if n2 > n1 > n3:
    print('ordem decrescente',n2,n1,n3)
if n2 > n3 > n1:
    print('ordem decrescente',n2,n3,n1)
if n3 > n1 > n2:
    print('ordem decrescente',n3,n1,n2)
if n3 > n2 > n1:
    print('ordem decrescentes',n3,n2,n1)
