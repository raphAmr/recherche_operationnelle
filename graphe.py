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

    def supprimer_arete(self, source, destination):
        if source in self.sommets and destination in self.sommets:
            if self.sommets[destination] in self.sommets[source].successeurs:
                del self.sommets[source].successeurs[self.sommets[destination]]
            if self.sommets[source] in self.sommets[destination].predecesseurs:
                del self.sommets[destination].predecesseurs[self.sommets[source]]
    
    def update_arete(self, source, destination, nouvelle_capacite):
        if source in self.sommets and destination in self.sommets:
            if self.sommets[destination] in self.sommets[source].successeurs:
                self.sommets[source].successeurs[self.sommets[destination]] = nouvelle_capacite
    
    def afficher(self):
        for sommet in self.sommets.values():
            print(f"Sommet {sommet.nom}:")
            print(f"  Successeurs: {[(s.nom, c) for s, c in sommet.successeurs.items()]}")
            print(f"  Prédécesseurs: {[(s.nom, c) for s, c in sommet.predecesseurs.items()]}")
            print()

"""
#input le Graphe que l'on veut afficher
#parcours et affiche
#no output
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
"""                
            
"""-------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------GRAPHE NUMERO 1---------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------"""
"""
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
graphe.afficher()
afficher_matrice(graphe)
chaine_graph_1 = detect_chaine_amelio(graphe)
minimum = find_value_min(chaine_graph_1, graphe)
update_graphe(graphe, chaine_graph_1, minimum)
afficher_matrice(graphe)
print("affichage 2eme tour\n\n")"""

"""-------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------GRAPHE NUMERO 2---------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------"""
"""
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
graphe_round_2.ajouter_arete("T", "C", 1)


# Affichage de la matrice
graphe_round_2.afficher()
afficher_matrice(graphe_round_2)"""

"""

chaine_graph_2 = detect_chaine_amelio(graphe)
mininini = find_value_min(chaine_graph_2, graphe)
update_graphe(graphe, chaine_graph_2, mininini)
afficher_matrice(graphe)
print("affichage 3eme tour\n\n")

chaine_graph_3 = detect_chaine_amelio(graphe)
minininini = find_value_min(chaine_graph_3, graphe)
update_graphe(graphe, chaine_graph_3, minininini)
afficher_matrice(graphe)
graphe.afficher()"""