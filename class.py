# -*- coding: utf-8 -*-

class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.successeurs = {}  # Dictionnaire {sommet: capacité}
        self.predecesseurs = {}  # Dictionnaire {sommet: capacité}
        
    
    def ajouter_successeur(self, sommet, capacite):
        self.successeurs[sommet] = capacite
        sommet.predecesseurs[self] = capacite  # Lier bidirectionnellement
        
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

"""
# Exemple d'utilisation
graphe = Graphe()
graphe.ajouter_sommet("A")
graphe.ajouter_sommet("B")
graphe.ajouter_sommet("C")

graphe.ajouter_arete("A", "B", 10)
graphe.ajouter_arete("B", "C", 5)

graphe.afficher()
"""

def afficher_matrice(graphe):
    sommets = list(graphe.sommets.keys())
    
    #print("    " + " ".join(f"{s}  " for s in sommets))
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

# Création du graphe
graphe = Graphe()
for sommet in ["A", "B", "C", "D", "E", "F"]:
    graphe.ajouter_sommet(sommet)

graphe.ajouter_arete("A", "B", 10)
graphe.ajouter_arete("A", "C", 5)
graphe.ajouter_arete("B", "C", 2)
graphe.ajouter_arete("B", "D", 8)
graphe.ajouter_arete("C", "D", 3)

# Affichage de la matrice
afficher_matrice(graphe)
