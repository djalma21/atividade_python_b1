resp_sim=0


r1=input("telefonou para a vitima? ")
if r1== "sim":
    resp_sim =resp_sim+1
r2=input("esteve no local do crime? ")
if r2== "sim":
    resp_sim =resp_sim+1
r3=input("mora perto da vitima? ")
if r3== "sim":
    resp_sim =resp_sim+1
r4=input(" devia para a vitima? ")
if r4== "sim":
    resp_sim =resp_sim+1
r5=input("ja trabalhou com a vitima? ")
if r5== "sim":
    resp_sim =resp_sim+1

if resp_sim<=1:
    print("Você é inocente")
if resp_sim==2:
    print("Você é suspeito")
if resp_sim==3 or resp_sim==4:
    print("Você e cumplice")
if resp_sim==5:
    print("Você é o assassino")
