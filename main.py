def count_word(chaine):
        mots = chaine.split()
        nb_de_mots = len(mots)
        return nb_de_mots


# Demander à l'utilisateur de saisir une chaîne 
chaine = input("Entrez une chaine de caractères : \n")
nb_de_mots = count_word(chaine)
print("Le nombre de mots dans la chaîne est : \n", nb_de_mots)

