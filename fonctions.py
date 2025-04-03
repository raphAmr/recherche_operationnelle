# -*- coding: utf-8 -*-
from graphe import Graphe, Sommet


#input le chemin exacte
#selectionne le fichier et le retranscrit dans une variable
#output : la variable contenant la matrice
def lecture(path):
    graphe = Graphe()
    with open(path, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()  # Enlève les espaces et \n
            print(f"notre ligne est {ligne} \
                  \nNotre source est {ligne[0]}\
                  \nNotre capacité est {ligne[1:-1]}\
                  \nNotre destination est {ligne[-1]}\n")
            
            source = ligne[0]
            capacite = int(ligne[1:-1])  # Correction ici
            destination = ligne[-1]  # Correction ici
            
            graphe.ajouter_sommet(source)
            graphe.ajouter_sommet(destination)
            graphe.ajouter_arete(source, destination, capacite)
    return graphe


def afficher_matrice(graphe):
    sommets = list(graphe.sommets.keys())
    print ("     ", end="")
    for elem in sommets:
        print (elem + "   ", end="")
    print ()
    for s1 in sommets:
        print(s1 + "  ", end="")
        for s2 in sommets:
            val = graphe.sommets[s1].successeurs.get(graphe.sommets[s2], 0)
            print(f"{val:3} ", end="")
        print()

#input le Graphe sur lequel on veut chercher la chaine améliorante
#parcours en alrgeur + detection de chaine améliorante
#return une liste contenant les noms des sommets de la chaine améliorante
def detect_chaine_amelio(graphe):
    file, visite = ["S"], ["S"]
    liste_sommets = list(graphe.sommets.keys())
    #--------------------------------PARCOURS EN LARGEUR-------------------------------------------
    while "T" not in file:
        sommet = file[0]
        for voisin in graphe.sommets[sommet].successeurs:
            print(voisin.nom)
            if voisin.nom not in visite:
                file.append(voisin.nom)
                visite.append(voisin.nom)
        file.remove(sommet)
    print (f"Parcours en largeur : {visite} \nDernier point parcouru : {sommet}")
    
    chaine_ameliore = ["T"]
    chaine_ameliore.insert(0, sommet)
    #if graphe.sommets["A"] in graphe.sommets["C"].predecesseurs:
    #    print("success")

    #--------------------------------CHAINE AMELIORANTE--------------------------------------------
    while chaine_ameliore[0] != "S":
        #print (chaine_ameliore)
        for elem in visite:
            if graphe.sommets[elem] in graphe.sommets[sommet].predecesseurs:
                chaine_ameliore.insert(0, elem)
                sommet = elem
                break
    print (f"Chaine améliorante : {chaine_ameliore}")
    return chaine_ameliore
            
#input une liste contenant les noms des sommets de la chaine améliorante
#parcours le chemin amélioré pour detecter l'arc le plus faible
#
def find_value_min(ca, graphe):
    chaine_ameliore = ca.copy()
    sommet = graphe.sommets[chaine_ameliore[0]]
    mini = 0
    while sommet.nom != "T":
        #compare la prochaine valeur et prend le mini
        del chaine_ameliore[0]
        for voisin in sommet.successeurs:
            if voisin.nom == chaine_ameliore[0]:
                arc_value = sommet.successeurs[voisin]
                if mini < 1 or arc_value < mini :
                    mini = arc_value
                sommet = graphe.sommets[chaine_ameliore[0]]
    print("mini : ", mini)
    return (mini)


def update_graphe(graphe, ca, mini):
    chaine_ameliore = ca.copy()
    sommet = graphe.sommets[chaine_ameliore[0]]
    while sommet.nom != "T":
        del chaine_ameliore[0]
        for voisin in sommet.successeurs:
            #print(chaine_ameliore)
            #print(sommet.nom)
            if sommet.nom == "T":
                pass
            elif voisin.nom == chaine_ameliore[0]:
                print(f"nouvelle branche de {sommet.nom} vers {voisin.nom} vaut : {sommet.successeurs[voisin]-mini}")
                sommet_nom, voisin_nom, new_arc = sommet.nom, voisin.nom, sommet.successeurs[voisin]-mini
                for elem in voisin.successeurs:
                    if elem.nom == sommet.nom:
                        #print("already a branch before")
                        find = True
                        break
                    else:
                        #print("not find")
                        find = False
                if not find:
                    print(f"nouvelle branche de {voisin.nom} vers {sommet.nom} vaut : {mini}")
                    graphe.ajouter_arete(voisin_nom, sommet_nom, mini)
                else:
                    print(f"branche de {voisin.nom} vers {sommet.nom} update et vaut : {mini} + {voisin.successeurs[sommet]} = {mini+voisin.successeurs[sommet]}")
                    arc_update = mini+voisin.successeurs[sommet]
                    graphe.update_arete(voisin.nom, sommet.nom, arc_update)
                #verify if need to delete or just to update
                if new_arc == 0:
                    graphe.supprimer_arete(sommet_nom, voisin_nom)
                else:
                    graphe.update_arete(sommet_nom, voisin_nom, new_arc)
                sommet = graphe.sommets[chaine_ameliore[0]]
                print("\ntestint value of sommet",sommet.nom)
                break

graphe = lecture("data/prop_test.txt")
afficher_matrice(graphe)