vuos = int(input("anna vuosi: "))
if vuos % 400 == 0:
    print ("on karakausvuos")
elif vuos % 4 == 0:
    if vuos %100 != 0:
        print ("oli kauravuos")
else: 
    print (" ei ollut :3 ")