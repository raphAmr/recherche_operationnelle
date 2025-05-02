import fonctions as fct
from graphe import Graphe

print("\n========= Projet de Recherche Opérationnelle =========")

running = True

while running:
    try:
        fichier_num = int(input("Veuillez entrer le numéro du problème à traiter (1 à 10, 0 pour quitter) : "))
        if fichier_num == 0:
            print("Fermeture du programme.")
            running = False
            break

        fichier = f"data/prop_{fichier_num}.txt"

        if 1 <= fichier_num <= 5:
            graphe = fct.lecture_maximal(fichier)
            graphe_initial = fct.lecture_maximal(fichier)

            while graphe.sommets["T"].predecesseurs:
                fct.afficher_matrice(graphe)
                chaine_graph_amelio = fct.detect_chaine_amelio(graphe)
                if chaine_graph_amelio is None:
                    print("Aucune chaîne améliorante.")
                    break
                value_arc_minimum = fct.find_value_min(chaine_graph_amelio, graphe)
                fct.update_graphe(graphe, chaine_graph_amelio, value_arc_minimum)

            fct.afficher_matrice(graphe)
            fct.afficher_flux_utilise(graphe_initial, graphe)

        elif fichier_num >= 6:
            graphe = fct.lecture_minimal(fichier)

            print("\nMatrice initiale :")
            fct.afficher_matrice(graphe)

            fct.flot_minimal(graphe, source="s", puits="t", flot_requis=4)

        else:
            print("Numéro invalide.")

    except Exception as e:
        print(f"Erreur : {e}")
