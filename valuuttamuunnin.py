#testiAnna dollarin kurssi euroina: 0.75
#Anna rahan määrä euroina: 10
#Rahan arvo on dollareina: 13.33
#Valuuttamuunnin
valuuttavalitsin = input("minkä kurssin haluat (d,j,p):")

if valuuttavalitsin == "d":
    dollarinkurssi = float(input("anna dollarin kurssi euroina:"))
    arvo = float(input("anna rahan määrä euroina:"))
    oikeaarvo_d = dollarinkurssi * arvo
    print (f"Rahan arvo on dollareina {oikeaarvo_d}")


if valuuttavalitsin == "j":
    jeninkurssi = float(input("anna jenin kurssi euroina:"))
    arvo = float(input("anna rahan määrä euroina:"))
    oikeaarvo_j = jeninkurssi * arvo
    print (f"Rahan arvo on jeneinä {oikeaarvo_j}")


if valuuttavalitsin == "p":
    punnankurssi = float(input("anna punnan kurssi euroina:"))
    arvo = float(input("anna rahan määrä euroina:"))
    oikeaarvo_p = punnankurssi * arvo
    print (f"Rahan arvo on puntina {oikearvo_p}")