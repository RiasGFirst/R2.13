def ex1():
    print("Calcul d'un prêt immobilier ou d'un crédit à la consommation")
    montant = float(input("Entrez le montant du prêt ou du crédit: "))
    taux = float(input("Entrez le taux d'intérêt annuel (%): "))
    duree = int(input("Entrez la durée du prêt ou du crédit (en années): "))

    taux_mensuel = taux/12/100
    mensualite = (montant * taux_mensuel) / (1 - (1 + taux_mensuel) ** (-duree*12))
    interet_global = (mensualite*duree*12)-montant

    print(f"La mensualité avec intérêt est de {round(mensualite, 2)}€")
    print(f"Le montant des interêts remboursés sont de {round(interet_global, 2)}€")
    print(f"Le taux mensuel est de {taux_mensuel}")

    # faire un tableau: mois, mensualité, intérêts, capital remboursé, capital restant dû, intérêts cumulés
    capital_restant = montant
    interets_cumules = 0
    print("Mois | Mensualité | Intérêts | Capital remboursé | Capital restant dû | Intérêts cumulés")
    for i in range(duree*12):
        interets = capital_restant * taux_mensuel
        capital_rembourse = mensualite - interets
        capital_restant -= capital_rembourse
        interets_cumules += interets
        print(f"{i+1} | {round(mensualite, 2)} | {round(interets, 2)} | {round(capital_rembourse, 2)} | {round(capital_restant, 2)} | {round(interets_cumules, 2)}")

    print("Fin du tableau")


def ex2():
    capital_depart = float(input("Entrez le capital de départ: "))
    versement_mensuel = float(input("Entrez le versement mensuel: "))
    taux = float(input("Entrez le taux d'intérêt annuel (%): "))
    annees = int(input("Entrez le nombre d'années: "))

    capital = capital_depart
    capital2 = capital_depart
    for i in range(annees):
        capital = (capital + 12*versement_mensuel)*(1+taux/100)

    for j in range(annees*12):
        capital2 = (capital2 + versement_mensuel)*(1+taux/12/100)

    interet_global = capital - capital_depart - annees*12*versement_mensuel
    interet_global2 = capital2 - capital_depart - annees*12*versement_mensuel
    print("=====================================")
    print(f"Le capital aquis avec intérêt est de {round(capital, 2)}€ au bout de {annees} ans avec versement mensuel de {versement_mensuel}€")
    print(f"Les interêts gagnés sur un taux annuel de {taux}% sont de {round(interet_global, 2)}€")
    print(f"Sans placement avec intérêt, le capital serait de {capital_depart + annees*12*versement_mensuel}€")
    print("=====================================")
    print(f"Le capital aquis avec intérêt est de {round(capital2, 2)}€ au bout de {annees} ans avec versement mensuel de {versement_mensuel}€")
    print(f"Les interêts gagnés sur un taux annuel de {taux}% sont de {round(interet_global2, 2)}€")
    print(f"Sans placement avec intérêt, le capital serait de {capital_depart + annees * 12 * versement_mensuel}€")


def ex3():
    diametre = float(input("Entrez le diamètre de l'axe en mm: "))
    tours = float(input("Entrez le nombre de tours: "))

    


if __name__ == '__main__':
    ex2()