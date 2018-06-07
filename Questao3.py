resp_sim=0


R1=input("telefonou para a vitima? ")
if R1== "sim":
    resp_sim =resp_sim+1
R2=input("esteve no local do crime? ")
if R2== "sim":
    resp_sim =resp_sim+1
R3=input("mora perto da vitima? ")
if R3== "sim":
    resp_sim =resp_sim+1
R4=input(" devia para a vitima? ")
if R4== "sim":
    resp_sim =resp_sim+1
R5=input("ja trabalhou com a vitima? ")
if R5== "sim":
    resp_sim =resp_sim+1

if resp_sim==1:
    print("Você é inocente")
if resp_sim==2:
    print("Você é suspeito")

if resp_sim==3 or resp_sim==4:
    print("Você e cumplice")

if resp_sim==5:
    print("Você é o assassino")
