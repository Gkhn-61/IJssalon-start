from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs} euro voor {prijs_na_korting:.2} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2} euro btw betaald dienst te worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    gemiddelde_waarde = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten van deze week zijn {gemiddelde_waarde:.2} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinaties(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

