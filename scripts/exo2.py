# nbLignes, nbMots = map(int, input().split())

# # Initialisation du dictionnaire pour stocker le nombre de mots pour chaque longueur
# longueurs_mots = {}

# # Traitement des données
# for _ in range(nbLignes):
#     mots = input().split()
#     for mot in mots:
#         longueur = len(mot)
#         if longueur in longueurs_mots:
#             longueurs_mots[longueur] += 1
#         else:
#             longueurs_mots[longueur] = 1

# # Affichage du résultat
# for longueur, nombre in sorted(longueurs_mots.items()):
#     print(f"{longueur} : {nombre}")


# nb_lignes = int(input())
# chaine_de_caracteres_inversee = ""
# for i in range (nb_lignes):
#     chaine_de_caracteres = input()
#     for j in range (len(chaine_de_caracteres) -1, -1, -1):
#         chaine_de_caracteres_inversee += chaine_de_caracteres[j]
#     print(chaine_de_caracteres_inversee)
#     chaine_de_caracteres_inversee = ""
# print()


# nom_du_livre = input()
# titre_auteur = input()
# nomlivre =""
# titreauteur =""
# for i in  (nom_du_livre):
#     if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y" or i == " ":
#         i=""
#         nomlivre += i
#     else:
#         nomlivre += i
# for j in  (titre_auteur):
#     if j == "A" or j == "E" or j == "I" or j == "O" or j == "U" or j == "Y" or j == " ":
#         j = ""
#         titreauteur += j
#     else:
#         titreauteur += j
# print(nomlivre, end=" ")
# print()
# print(titreauteur)
        


# if joueur_1 < joueur_2:
    # for i in (joueur_1):
#         if joueur_1[i] < joueur_2[i]:
#             point_j1 += 1
#         elif joueur_2[i] < joueur_1[i]:
#             point_j2 += 1
#         elif joueur_1[i] == joueur_2[i]:
#             nombre_egalite += 1
#             print("2")
#             print(nombre_egalite)
# elif joueur_2 > joueur_1:
#     for j in joueur_2:
#         if joueur_2[j] < joueur_1[j]:
#             point_j2 += 1
#         elif joueur_2[j] > joueur_1[j]:
#             point_j1 += 1
#         elif joueur_2[j] == joueur_1[j]:
#             nombre_egalite +=1
#             print("1")
#             print(nombre_egalite)
# elif joueur_2 == joueur_1:
#     for k in joueur_1:
#         if joueur_1[k] < joueur_2[k]:
#             point_j1 += 1
#         elif joueur_2[k] < joueur_1[k]:
#             point_j2 += 1
#         elif joueur_1[k] == joueur_2[k]:
#             nombre_egalite += 1
#             print("=")
#             print(nombre_egalite)
        



# joueur_1 = input()
# joueur_2 = input()

# nombre_egalite = 0

# if joueur_1 > joueur_2:
#     for i in (joueur_2):
#         while joueur_1[i] == joueur_2[i]:
            
#             nombre_egalite += 1
                
#             if joueur_1[i] < joueur_2[i]:
#                 print(nombre_egalite)
#                 print()
#                 print("1")
#             elif joueur_2[i] < joueur_1[i]:
#                 print(nombre_egalite)
#                 print()
#                 print("2")
#             else:
#                 print(nombre_egalite)
#                 print()
#                 print("=")

# elif joueur_2 < joueur_1:
#     for j in (joueur_1):
#         while joueur_1[j] == joueur_2[j]:
            
#             nombre_egalite +=1
#             if joueur_1[j] < joueur_2[j]:
#                 print(nombre_egalite)
#                 print()
#                 print("1")
#             elif joueur_2[j] < joueur_1[j]:
#                 print(nombre_egalite)
#                 print()
#                 print("2")
#             elif joueur_1[j] == joueur_2[k]:
#                 print(nombre_egalite)
#                 print()
#                 print("=")

# elif joueur_2 == joueur_1:
#     for k in joueur_1:
#         while joueur_1[k] == joueur_2[k]:
#             nombre_egalite += 1
#             if joueur_1[k] < joueur_2[k]:
#                 print(nombre_egalite)
#                 print()
#                 print("1")
#             elif joueur_2[k] < joueur_1[k]:
#                 print(nombre_egalite)
#                 print()
#                 print("2")
#             elif joueur_1[k] == joueur_2[k]:
#                 print(nombre_egalite)
#                 print()
#                 print("=")





# joueur_1 = input()
# joueur_2 = input()

# nombre_egalite = 0

# min_length = min(len(joueur_1), len(joueur_2))

# for i in range(min_length):
#     if joueur_1[i] == joueur_2[i]:
#         nombre_egalite += 1
#     else:
#         break  

# if nombre_egalite == min_length:
#     if len(joueur_1) < len(joueur_2):
#         print("1")
#         print(nombre_egalite)
#     elif len(joueur_2) < len(joueur_1):
#         print("2")
#         print(nombre_egalite)
#     else:
#         print("=")
#         print(nombre_egalite)
# else:
#     if joueur_1[nombre_egalite] < joueur_2[nombre_egalite]:
#         print("1")
#         print(nombre_egalite)
#     elif joueur_2[nombre_egalite] < joueur_1[nombre_egalite]:
#         print("2")
#         print(nombre_egalite)
#     else:
#         print("=")
#         print(nombre_egalite)



# j1 = str(input())
# j2 = str(input())
 
# jeu = j1 + j2
 
# i = 0
# t = 0
 
# if len(jeu) == 52:
 
#     if len(j1) < len(j2):
#         n = len(j1)
#     else:
#         n = len(j2)
         
#     while i < n:
        
#         if j1[i] == j2[i]:
#             t += 1
#             i += 1
          
#         else:
#             break
 
#     if j1 == j2:
#         print("=")
#         print(len(j1))
#     elif t == n and len(j1) > n:
#         print("1")
#         print(t)
#     elif t == n and len(j2) > n:
#         print("2")
#         print(t)
#     elif j1[i] > j2[i]:
#         print("2")
#         print(t)
#     else:
#         print("1")
#         print(t)


# lettre = (input())
# nb_lignes = int(input())
# nombre_lettre = 0
# for i in range (nb_lignes):
#     texte = input()
    
#     for j in texte :
#         if j == lettre :
#             nombre_lettre += 1
# print(nombre_lettre)


# ligne_de_texte = str(input())
# chaine_a_modifiee = list(ligne_de_texte)

# for i in range (len(chaine_a_modifiee)):
#     if chaine_a_modifiee[i] == " ":
#         chaine_a_modifiee[i] = "_"
# ligne_de_texte = "".join(chaine_a_modifiee)
# print(ligne_de_texte)


# def fonction(longueur_dentelle):
#     for i in range(longueur_dentelle):
#         print("X", end ="")
#     print()
#     for i in range(longueur_dentelle):
#         print("#", end ="")
#     print()
#     for i in range(longueur_dentelle):
#         print("i", end = "")
#     print()
# fonction(5)


# def min2(nombre1,  nombre2):
#     if nombre1 < nombre2:
#         return nombre1
#     else:
#          nombre2 
# plus_petit = int(input())
# for i in range(10):
#     entier1=int(input())
    
#     plus_petit = min2(entier1, plus_petit)

    

# print(plus_petit)



# def pair_ou_impair(terme):
#     if terme % 2 != 0:
#         terme = terme * 3 + 1
#         return terme
#     else:
#         terme = terme // 2
#         return terme
    

# def calcul_de_la_suite(terme_initial):
#     terme_actuel = terme_initial
#     while terme_actuel !=1 :
#         print(terme_actuel, end = " ")
#         terme_actuel = pair_ou_impair(terme_actuel)
#     print("1")

# terme_initial = int(input())

# calcul_de_la_suite(terme_initial)



# from math import *

# def calcul_de_la_distance(x1, y1, x2, y2):
#     valeur = 0
#     valeur = ((x2 - x1)**2 + (y2 - y1)**2) 
#     valeur = sqrt(valeur)
#     return valeur

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())


# resultat = calcul_de_la_distance(x1, y1, x2, y2)
# print(resultat)




# def ligne_x(nombre_de_x):
#     for i in range(nombre_de_x):
#         print("X", end = "")
#     print()



# def dessin_rectange(lignes, colonnes):
#     for i in range(lignes):
#         for j in range(colonnes):
#             if i == 0 or i == lignes - 1 or j == 0 or j == colonnes - 1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()




# def dessin_triangle_rectangle(taille):
#     for i in range(taille):
#         for j in range(i + 1):
#             if i == taille - 1 or j == 0 or j == i:
#                 print("@", end="")
#             else:
#                 print(" ", end=" ")
#         print()

                
# nombre_de_x = int(input())
# lignes = int(input())
# colonnes = int(input())
# taille = int(input())


# ligne_x(nombre_de_x)
# print()
# dessin_rectange(lignes, colonnes)
# print()
# dessin_triangle_rectangle(taille)



# pied_en_metre = 0.3048
# gramme_en_livres = 0.002205

# nb_conversions = int(input())


# for i in range(nb_conversions):
#     valeur, unite = input().split()
#     valeur = float(valeur)
#     if unite == "m" :
#         valeur = valeur * pied_en_metre
#         print(valeur,end=" p")
#     elif unite == "g" :
#         valeur = valeur * gramme_en_livres
#         print(valeur,end=" l")
#     elif unite == "c" :
#         valeur = valeur * 1.8 + 32
#         print(valeur,end=" f")
#     else:
#         print("Veuillez rentrez une autre unite")


# def imprimer_cible(nbLettres):
#     for i in range(nbLettres):
#         ligne = "a" * (nbLettres - i)
#         if i > 0:
#             ligne += "b" * (2 * i - 1)
#             ligne += "a"
#         print(ligne)

#     for i in range(nbLettres - 2, -1, -1):
#         ligne = "a" * (nbLettres - i)
#         if i > 0:
#             ligne += "b" * (2 * i - 1)
#             ligne += "a"
#         print(ligne)

# # Lecture de l'entrée
# nbLettres = int(input())

# # Impression de la cible
# imprimer_cible(nbLettres)








# x = 0
# depense = 0
# while depense != -1 :
#     entier = int(input())
#     if entier != -1 :
#         depense += entier
#     else:
#         print(depense)
       



# nombre_secret = int(input())
# proposition_enfant =  0
# nombre_d_essai = 1
# while nombre_secret != proposition_enfant :
#     proposition_enfant = int(input())
#     if proposition_enfant < nombre_secret :
#         nombre_d_essai += 1
#         print("C'est plus")
#     elif proposition_enfant > nombre_secret :
#         nombre_d_essai += 1
#         print("C'est moins")
#     elif proposition_enfant == nombre_secret :
#         print(f"Nombres d'essais necessaires : {nombre_d_essai}")


# nombre_de_charettes = int(input())
# poids_a_modifier = 0
# nouveau_poids_charette = 0
# poids_moyen = 0
# poids_total_caravane = 0
# liste = []
# liste_poids_moyen = []
# for i in range(nombre_de_charettes):
#     poids_charettes = float(input())
#     poids_total_caravane += poids_charettes
#     liste.append(poids_charettes)
# poids_moyen = poids_total_caravane / nombre_de_charettes
# for j in liste:
#     nouveau_poids_charette = poids_moyen - j   
#     liste_poids_moyen.append(nouveau_poids_charette)
# for k in liste_poids_moyen:
#     print(k)

    
nbMesures = int(input())
diffMax = float(input())
diff_totale = 0
nombre_dessai = 0
L = []
M = []
while diffMax < doff_moyenne:
    for i in range(nbMesures) :
        entier = float(input())
        L.append(entier)
    for indice, j in enumerate(L):
        if indice == 0 or indice == -1 :
            M.append(L[indice])
        elif indice !=0 and indice != nbMesures -1 :
            m = (L[indice-1] + L[indice+1]) / 2
            M.append(m)
        elif indice == -1 :
            M.append(m)
    L.pop
    for indice, k in enumerate(M):
        diff_actuelle = k - L[indice]
        diff_totale += diff_actuelle
        doff_moyenne = diff_totale / nbMesures
        L , M = M , L 
        L.clear()
        nombre_dessai +=1
print(nombre_dessai)

    
