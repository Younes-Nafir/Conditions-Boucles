mht = float(input("Saisir montant HT : "))
tva = float(input("Saisir tva: "))
print(f"montant HT: {mht} Taux de TVA: {tva}")
mtva= ((tva/100)*mht)
print(f"Le montant de la TVA est de: {mtva}")
print (f"Le montant TTC est: {mtva+mht}")