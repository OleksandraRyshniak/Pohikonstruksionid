# 1
print("Tere mailm!")
nimi=input("Mis on sinu nimi?").capitalize()
print(f"Tere maailm!, Tervitan sind {nimi}")
vanus=int(input("Kui vana sa oled?"))
print(f"Tere maailm!, Tervitan sind {nimi}! Sa oled {vanus} aasta vana. ")

# 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuj {kas_käib_koolis} on {type(kas_käib_koolis)}")

# 3
from random import randint
kommide_arv=randint(10,100)
print(f"Laua peal on {kommide_arv}")
mitu=int(input("Mitu tahad süüja"))
print(f"Laua peal on jäänud {kommide_arv-mitu}")

# 4
import math

ümbermõõt=float(input("Mis on puu ümbermõõt?"))
vastus=round(ümbermõõt/math.pi)
print(f"Puu läbimõõt on {vastus}")

# 5
import math

N=float(input("Milline on maatüki pikkus?"))
M=float(input("Milline on maatüki laius?"))
D=N**2+M**2
vastus=math.sqrt(D)
print(f"Diagonaal on võrdne: {vastus}")

#6
aeg = float(input("Mitu tundi kulus sõiduks? "))  
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))  
kiirus = teepikkus/aeg 
print("Sinu kiirus oli " + str(kiirus) + " km/h")  

# 7
print("Sisesta 5 täisarvu: ")
arv1=int(input("arv1: " ))
arv2=int(input("arv2: " ))
arv3=int(input("arv3: " ))
arv4=int(input("arv4: " ))
arv5=int(input("arv5: " ))
vastus=(arv1+arv2+arv3+arv4+arv5)/5
print(f"Aritmeetiline keskmine: {vastus}")

# 8
print("  @..@\n (----)\n (\__/)\n ^^ "" ^^\n")

#9
a=int(input("Sisesta külje a pikkus: "))
b=int(input("Sisesta külje b pikkus: "))
c=int(input("Sisesta külje c pikkus: "))
P=a+b+c
print(f"Kolmnurga ümbermõõt on võrdne: {P}")

# 10
pitsa=12.90
jootraha=pitsa*10/100
summ=pitsa+jootraha
vastus=summ/2
print(f"Kõik peavad maksma:{vastus}")

