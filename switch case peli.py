
#switch case peli
#looppi:

while True: 
    print("***************************")
    print ("* 1 – Käynnistä auto")
    print ("* 2 – Aja autoa")
    print ("* 3 – Sammuta auto")
    print ("* 4 – Lopeta peli")
    print ("***************************")
    valinta1 = input("valitse mitä haluat tehdä (1,2,3,4):")
#jos valitaan 1:
    if valinta1 == "1":
        print ("auto käynnistetty wruum wruum")
    if valinta1 == "2":
        print ("ajat autolla, oo tarkkana prkl")
    if valinta1 == "3":
        print ("auto sammutettu, wrumph...")
    if valinta1 == "4":
        print ("peli lopetettu")
