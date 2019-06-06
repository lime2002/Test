def tulosta(nimi_funktiossa, kertaa):
    for i in range(kertaa):
        print("terve", nimi_funktiossa)
    print("tässä tervedykset")
    



def main():
    nimi =input("kerro nimesi: \n")
    lkm = int(input("kuinka monta kertaa tervehditään? \n"))
    
    tulosta(nimi, lkm)
    
    print("main-funktio suoaritettu")

main()