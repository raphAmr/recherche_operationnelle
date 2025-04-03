# -*- coding: utf-8 -*-
import fonctions as fct
from graphe import Graphe, Sommet


print ("-----------------Bienvenu sur le projet de recherche opérationnelle.---------------------------------")

running = True

while running:
    fichier = -1
    while not(0 <= fichier and fichier <= 20):
        fichier = int(input("Veuillez entre le numéro du problème à traiter : "))
    if fichier == 0:
        running = False
        
    else:
        fichier = "data/prop_test.txt"
        graphe = fct.lecture(fichier)
        """
        fct.affichage_matrices_capacités(matrice)
        fct.affichage_matrices_couts(matrice)
        if fct.probleme_flot_min(matrice):
            methode = "min"
        else :
            methode = "max"
            
        if methode == "min":
            pass
        else:
            pass
        """
        while graphe.sommets["T"].predecesseurs:
            fct.afficher_matrice(graphe)
            chaine_graph_amelio = fct.detect_chaine_amelio(graphe)
            value_arc_minimum = fct.find_value_min(chaine_graph_amelio, graphe)
            fct.update_graphe(graphe, chaine_graph_amelio, value_arc_minimum)
        fct.afficher_matrice(graphe)
        
        #print ("Valeur du flot " + methode + " = ")
