
print("Tere tulemast! 1","Tere tulemast! 2",end="...", sep="---") #selgitus
#kommentaar end- что написано в конце sõne. sep - что между текстом
# andmetüüpid täisarv- int, ujukomaarv - float, sõne - str, tõevärtused - bool
# astendamine **
print( )
a=5
aste=2
tulemus=a**aste
print(a,"**",aste,"=",tulemus)
# korrutamine *
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Teine korrutaja: "))
tulemus=arv1*arv2
print(arv1,"*",arv2,"=",tulemus)
#jagamine /
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Jagaja: "))
tulemus=arv1/arv2
print(arv1,"/",arv2,"=",tulemus)
print(type(tulemus))
#jagamisjääk %
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Jagaja: "))
tulemus=arv1%arv2
print(arv1,"%",arv2,"=",tulemus)
print(type(tulemus))
#liitmine +
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Teine korrutaja: "))
tulemus=arv1+arv2
print(arv1,"+",arv2,"=",tulemus)
print(type(tulemus))
#lahutamine -
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Teine korrutaja: "))
tulemus=arv1-arv2
print(arv1,"-",arv2,"=",tulemus)
# jagamise täisarvulise osa leidmine //
arv1=int(input("Esimene korrutaja: "))
arv2=int(input("Jagaja: "))
tulemus=arv1//arv2
print(arv1,"//",arv2,"=",tulemus)
