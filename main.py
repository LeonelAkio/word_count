#créé par leonel akio briones

#définit la fonction count_word
def count_word(chaine):
        mots = chaine.split()
        nb_de_mots = len(mots)
        return nb_de_mots


# Demander à l'utilisateur de saisir une chaîne 
chaine = input("Entrez une chaine de caractères : \n")
#définit le nombre de mots
nb_de_mots = count_word(chaine)
#retourne le nombre de mots dans la chaine
print("Le nombre de mots dans la chaîne est : \n", nb_de_mots)

