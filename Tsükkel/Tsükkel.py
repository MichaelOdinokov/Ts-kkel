from random import *

#0
while True:
    print("Tere Tulemast!")
    print("Latte, 2.50 euro.")
    print("Espresso, 2 euro.")
    print("Cappuccino, 3 euro.")
    print("Kakao, 2.20 euro.")
    try:
        s=float(input("Sisestage summa:"))
        if s<2 and s>3: break
        m=input("Valige makseviis:")
        while m.lower()=="kaardiga":
            n=int(input("Sisestage kaardi number:"))
            print(n,"selle kaardiga on tehtud makse")
            continue
        if m.lower()=="sulraha": continue
                
    except:
        print("!!")


while True:
        print("Latte")
        print("Espresso")
        print("Cappuccino")
        print("Kakao")
        try:
            j=int("Valige jook:")
            latte="Latte"
            espresso="Espresso"
            cappuccino="Cappuccino"
            kakao="Kakao"
            if j==latte:
                print("soojenemine")
                print("lisa 1/4 vahustatud piima")
                print("lisage 2/4 piima")
                print("lisa 1/4 kohvi")
                print("Teie Latte on valmis!")

            elif j==espresso:
                print("soojenemine")
                print("lisage vett")
                print("lisa kohvi")
                print("Teie espresso on valmis!")

            elif j==cappuccino:
                print("soojenemine")
                print("lisage 2/4 vahustatud piimast")
                print("lisada 1/4 piima")
                print("lisa 1/4 kohvi")
                print("Teie Cappuccino on valmis!")

            elif j==kakao:
                print("soojenemine")
                print("lisage 3/4 piima")
                print("lisa 1/4 kakaod")
                print("Teie kakao on valmis!")
            else:
                break
        except:
            print("Kirjuta kohvi nimed!!!")






















#1
while True:
    try:
        nimi=input("Palun sisesta oma nimi:")
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: ")) # n=korda
            for i in range(1, n+1): # i=katsete arv
                print(f"Ole tervitatud, {nimi}, {i}. korda.")
        else:
            break
    except:
        print("!!!")





#22
print("Ma than kommi")
katsed=0
while True:
    answer=input("Tahan kommi!")
    katsed+=1
    if answer.lower()=="komm":
        print(f"Teil kommid kirjitakse kulus {katsed}, katse")
       
    katsed=0
    answer=""
    while answer!="komm":
        answer=input("Tahan kommi!")
        katsed+=1
        if answer.upper()=="JÄH":
            katsed=0
            continue
        else:
            break
print(f"Katsed: {katsed}")
       



#
p=0
while True:
    number= int(input("Sisetage number suurem kui 10: "))
    p+=1
    if number >=10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")
print("katsed", p)





#
print("Arvuti mõistatab numbrit 1-10 ja sina üriitad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõisttanud arvuti?:"))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!:")
    vastus=int(input("Sisesta vastus:"))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud")
        b=input("Kas proovi veel kord:")
        if b.upper()=="JÄH":          
            k=0
            continue
        else:
            break
if vastus==a:
    print("Palju õnne, sa arvasid ära!", p)

print()
#0



       


print()

#1