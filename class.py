# -*- coding: utf-8 -*-

class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.successeurs = {}  # Dictionnaire {sommet: capacité}
        self.predecesseurs = {}  # Dictionnaire {sommet: capacité}
    
    def ajouter_successeur(self, sommet, capacite):
        self.successeurs[sommet] = capacite
        sommet.predecesseurs[self] = capacite  # Lier bidirectionnellement
        


class Graphe:
    def __init__(self):
        self.sommets = {}

    def ajouter_sommet(self, nom):
        if nom not in self.sommets:
            self.sommets[nom] = Sommet(nom)
    
    def ajouter_arete(self, source, destination, capacite):
        if source in self.sommets and destination in self.sommets:
            self.sommets[source].ajouter_successeur(self.sommets[destination], capacite)

    def afficher(self):
        for sommet in self.sommets.values():
            print(f"Sommet {sommet.nom}:")
            print(f"  Successeurs: {[(s.nom, c) for s, c in sommet.successeurs.items()]}")
            print(f"  Prédécesseurs: {[(s.nom, c) for s, c in sommet.predecesseurs.items()]}\n")


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


def parcours_largeur(graphe):
    file, visite = ["S"], ["S"]
    liste_sommets = list(graphe.sommets.keys())
    #--------------------------------PARCOURS EN LARGEUR-------------------------------------------
    while "T" not in file:
        sommet = file[0]
        for voisin in graphe.sommets[sommet].successeurs:
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
            

            
"""-------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------GRAPHE NUMERO 1---------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------"""
# Création du graphe
graphe = Graphe()
for sommet in ["S", "A", "B", "C", "D", "T"]:
    graphe.ajouter_sommet(sommet)

graphe.ajouter_arete("S", "A", 7)
graphe.ajouter_arete("S", "B", 4)
graphe.ajouter_arete("A", "C", 1)
graphe.ajouter_arete("A", "D", 8)
graphe.ajouter_arete("B", "D", 4)
graphe.ajouter_arete("C", "T", 1)
graphe.ajouter_arete("D", "T", 8)


# Affichage de la matrice
afficher_matrice(graphe)
parcours_largeur(graphe)

"""-------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------GRAPHE NUMERO 2---------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------"""

graphe_round_2 = Graphe()
for sommet in ["S", "A", "B", "C", "D", "T"]:
    graphe_round_2.ajouter_sommet(sommet)

graphe_round_2.ajouter_arete("S", "A", 6)
graphe_round_2.ajouter_arete("S", "B", 4)
graphe_round_2.ajouter_arete("A", "S", 1)
graphe_round_2.ajouter_arete("A", "D", 8)
graphe_round_2.ajouter_arete("B", "D", 4)
graphe_round_2.ajouter_arete("C", "A", 1)
graphe_round_2.ajouter_arete("D", "T", 8)


# Affichage de la matrice
afficher_matrice(graphe_round_2)
parcours_largeur(graphe_round_2)
