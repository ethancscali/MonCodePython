print(" Bienvenu dans ce test de logique (de tête) bonne chance 😉")
nom = input("Quel est ton prénom ?").strip().capitalize()
print(f"Salut {nom} j'espère que tu es prêt concentre toi bien")
score=0

#Question 1 
rep1 = input("1. Un ami à toi possède 3 000 eur sur un compte il en perd 2/3 combien lui en reste t-il ?").strip().lower()
if rep1 in ["1000", "1000 euros"]:
    score += 1
    print("Bien joué pas mal mais c'étais la question la plus facil haha")
#Question 2 
rep2 = input("""2.Paul a deux fois l’âge de sa sœur.
Dans 10 ans, il aura 1,5 fois son âge. 
Quel âge a Paul aujourd’hui ?""").strip().lower()
if rep2 in ["20" ,"2O ans"]:
    score+= 1
    print("T'es un malin toi bien joué 💪")

#Question 3
rep3= input("""3.Dans une classe, la moyenne des notes de 4 élèves est de 15.
Un 5ᵉ élève rejoint le groupe, et la moyenne passe à 14.
🧠 Quelle est la note du 5ᵉ élève ?""").strip().lower() 
if rep3== "10" :
    score+= 1
    print("OKOK très fort c'était pas simple de tête !")

# Résultat final
print("\n🎯 Résultat final :")
if score == 3 :
   print("Monstrueux ça tu as un score de 3/3 🤯 ")
elif score==2 : 
    print("Pas mal, pas mal c'est bien joué tente le perfect la prochaine fois")
elif score==1 :
    print("Bon... c'est pas fameux hein 🤣 va falloir que tu t'exerces")
else :
    print( "Bon tu as tout raté mdrr retourne à l'ecole quelque annnée encore 😅")
