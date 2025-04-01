# -*- coding: utf-8 -*-
import fonctions as fct



print ("-----------------Bienvenu sur le projet de recherche opérationnelle.---------------------------------")

running = True

while running:
    fichier = -1
    while not(0 <= fichier and fichier <= 20):
        fichier = int(input("Veuillez entre le numéro du problème à traiter : "))
    if fichier == 0:
        running = False
        
    else:
        matrice = fct.lecture(fichier)
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
        
        print ("Valeur du flot " + methode + " = ")
