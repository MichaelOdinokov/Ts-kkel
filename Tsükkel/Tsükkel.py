

#0
while True:
    try:
        print("Latte, 2.50 euro.")
        print("Espresso, 2 euro.")
        print("Cappuccino, 3 euro.")
        print("Kakao, 2.20 euro.")
        s=float(input("Sisestage summa:"))
        if s<2 and s>3: break
        if s<3 and s>2: 
            m=int("Valige makseviis:")
            if m.upper()=="sulraha":
                if m.upper=="kaardiga":
                    n=int(input("Sisestage kaardi number:"))
                    print(n,"selle kaardiga on tehtud makse.")

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
        except:
            print("Kirjuta kohvi nimed!!!")
    except:
        print("Suur summa!!!")
       





print()

#1
while True:
    try:
        nimi=input("Palun sisesta oma nimi: ")
        n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: ")) # n=korda
        for i in range(1, n+1): # i=katsete arv
            print(f"Ole tervitatud, {nimi}, {i}. korda.")
    except:
        print("!!!")



