print("Bienvenue dans le Quiz !")
nom = input("Quel est ton prénom ? ")
print(f"Bonjour {nom}, bonne chance !")

print("🎓 Bienenue dans le Quiz Super Sérieux sur... toi même !")
score=0

# Question 1
rep1 = input("1. Tu préfères travaillé le soir tard ou bien le matin tôt ? (matin/nuit) : ").lower()
if rep1 == "nuit":
    score += 1

# Question 2
rep2 = input("2. Plutôt OM ⚪️🔵 ou PSG 🔵🔴 ? (OM/PSG) : ").lower()
if rep2 == "psg" :
    score += 1
elif rep2 == "om" :
    print("🤦😅 t'abuse frro qui à la dernière étoile haha 😂")
  
# Question 3etahn
rep3 = input("3. Question pour un futur Millionaire : Plutôt Lamborghini ou Ferrari ? AHAH pas facile (Lamborghini/Ferrari) : ").lower()
if rep3 == "Lamborghini" :
    score += 1

print(f"\n👉 Ton score final : {score}/3")

# Analyse finale
if score == 3:
    print("🧠 T'es clairement dans la matrice. Bienvenue.")
elif score== 2:
    print("PAS MAL ! A un point du score maximal 👏 ")
elif score == 1:
    print("😅 Bon... On en pense quoi 🤣, On va dire t'as un style à toi.")
else :
    print("🤯🙄 Bon On va réprendre les bases hein. Mais oklm t'es là pour ça.")
          