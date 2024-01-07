# # Lecture de l'entrée
# nbLivres = int(input())
# titres = [input().strip() for _ in range(nbLivres)]

# # Sélection des livres à lire
# livres_a_lire = []
# titre_max_lu = ""

# for i in range(nbLivres):
#     titre_actuel = titres[i]

#     # Vérifie si le titre actuel est strictement plus long que tous les titres lus précédemment
#     if all(len(t) < len(titre_actuel) for t in livres_a_lire):
#         livres_a_lire.append(titre_actuel)
#         titre_max_lu = max(titre_max_lu, titre_actuel, key=len)

# # Affichage du résultat
# for livre in livres_a_lire:
#     print(livre)




