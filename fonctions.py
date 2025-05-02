# -*- coding: utf-8 -*-
from graphe import Graphe, Sommet


#input le chemin exacte
#selectionne le fichier et le retranscrit dans une objet graphe
#output : le graphe contenant la matrice
def lecture_maximal(path):
    graphe = Graphe()
    with open(path, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            source = ligne[0]
            capacite = int(ligne[1:-1])
            destination = ligne[-1]

            graphe.ajouter_sommet(source)
            graphe.ajouter_sommet(destination)
            graphe.ajouter_arete(source, destination, capacite)
    return graphe


#input notre objet graphe
#parcours le graphe pour afficher chaque point 
#No output
def afficher_matrice(graphe):
    sommets = list(graphe.sommets.keys())
    print ("     ", end="")
    for elem in sommets:
        print (elem + "   ", end="")
    print ()
    for s1 in sommets:
        print(s1 + "  ", end="")
        for s2 in sommets:
            val = graphe.sommets[s1].successeurs.get(graphe.sommets[s2], (0, 0))[0]
            print(f"{val:3} ", end="")
        print()


#input le Graphe sur lequel on veut chercher la chaine améliorante
#parcours en alrgeur + detection de chaine améliorante
#return une liste contenant les noms des sommets de la chaine améliorante
def detect_chaine_amelio(graphe):
    print ("------------detection chaine amméliorante------------")
    file, visite = ["S"], ["S"]
    while "T" not in file:
        if not file:
            print ("Sortie demandée")
            return None
        
        sommet = file[0]
        for voisin in graphe.sommets[sommet].successeurs:
            if voisin.nom not in visite:
                file.append(voisin.nom)
                visite.append(voisin.nom)
        file.remove(sommet)

    chaine_ameliore = ["T"]
    chaine_ameliore.insert(0, sommet)

    while chaine_ameliore[0] != "S":
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
                arc_value = sommet.successeurs[voisin][0]
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
            if sommet.nom == "T":
                pass
            elif voisin.nom == chaine_ameliore[0]:

                ancienne_capacite = sommet.successeurs[voisin][0]
                new_arc = ancienne_capacite - mini
                sommet_nom, voisin_nom = sommet.nom, voisin.nom
                print(f"nouvelle branche de {sommet.nom} vers {voisin.nom} vaut : {new_arc}")
                find = False
                for elem in voisin.successeurs:
                    if elem.nom == sommet.nom:
                        find = True
                        break
                """ Ancien code ? 
                for elem in voisin.successeurs:
                    if elem.nom == sommet.nom:
                        #print("already a branch before")
                        find = True
                        break
                    else:
                        #print("not find")
                        find = False"""

                if not find:
                    print(f"nouvelle branche de {voisin.nom} vers {sommet.nom} vaut : {mini}")
                    graphe.ajouter_arete(voisin_nom, sommet_nom, mini)
                else:
                    print(f"branche de {voisin.nom} vers {sommet.nom} update et vaut : {mini} + {voisin.successeurs[sommet][0]}")
                    arc_update = mini+voisin.successeurs[sommet][0]
                    graphe.update_arete(voisin.nom, sommet.nom, arc_update)

                if new_arc == 0:
                    graphe.supprimer_arete(sommet_nom, voisin_nom)
                else:
                    graphe.update_arete(sommet_nom, voisin_nom, new_arc)

                sommet = graphe.sommets[chaine_ameliore[0]]
                print("\ntestint value of sommet",sommet.nom)
                break



#WIP fctionne mais pour un premier cas, a tester sur d'autres
def afficher_flux_utilise(graphe_initial, graphe_modifie):
    print("\nFlux utilisé / Capacité initiale:\n")
    sommets = list(graphe_initial.sommets.keys())
    largeur_colonne = 8
    little_largeur = 4
    intermediaire_largeur = 6
    flot_max = 0
    
    print(" " * (little_largeur+1), end="")
    for elem in sommets:
        print(f"{elem}", end="")
        print(" " * largeur_colonne, end = "")
    print()
    
    for s1 in sommets:
        print(f"{s1}", end="")
        print("   ", end="")
        for s2 in sommets:
            capacite_initiale = graphe_initial.sommets[s1].successeurs.get(graphe_initial.sommets[s2], (0, 0))[0]
            capacite_modifiee = graphe_modifie.sommets[s1].successeurs.get(graphe_modifie.sommets[s2], (0, 0))[0]
            flux_utilise = capacite_initiale - capacite_modifiee
            if capacite_initiale > 0:
                print(f"{flux_utilise}/{capacite_initiale}", end="")
                print(" "*intermediaire_largeur, end="")
                if s1 == "S":
                    flot_max += flux_utilise
            else:
                print(" 0", end="")
                print(" "*(largeur_colonne-1), end = "")
        print()
    print (f"La valeur du flot maximal vaut {flot_max}")


"""def afficher_flux_utilise(graphe_initial, graphe_modifie):
    print("\nFlux utilisé / Capacité initiale:\n")
    sommets = list(graphe_initial.sommets.keys())
    largeur_colonne = 8
    little_largeur = 4
    intermediaire_largeur = 6
    flot_max = 0

    print(" " * little_largeur, end="")
    for elem in sommets:
        print(f"{elem:>{largeur_colonne}}", end="")
    print()

    for s1 in sommets:
        print(f"{s1:<{largeur_colonne}}", end="")
        for s2 in sommets:
            capacite_initiale = graphe_initial.sommets[s1].successeurs.get(graphe_initial.sommets[s2], (0, 0))[0]
            capacite_modifiee = graphe_modifie.sommets[s1].successeurs.get(graphe_modifie.sommets[s2], (0, 0))[0]
            flux_utilise = capacite_initiale - capacite_modifiee
            if capacite_initiale > 0:
                print(f"{flux_utilise:>2}/{capacite_initiale:<2}", end=" " * (largeur_colonne - 4))
            else:
                print(f"{'0':>{largeur_colonne}}", end="")
        print()"""

#FLOT MINIMAL

def lecture_minimal(path):
    graphe = Graphe()
    with open(path, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            source = ligne[0]
            destination = ligne[-1]
            capacite, cout = map(int, ligne[1:-1].split(','))  # <- ligne critique

            graphe.ajouter_sommet(source)
            graphe.ajouter_sommet(destination)
            graphe.ajouter_arete(source, destination, capacite, cout)
    return graphe


def bellman_ford(graphe, source, puits):
    sommets = list(graphe.sommets.keys())
    dist = {s: float('inf') for s in sommets}
    pred = {s: None for s in sommets}
    dist[source] = 0

    distances_par_etape = [dist.copy()]
    pred_par_etape = [pred.copy()]

    for _ in range(len(sommets) - 1):
        maj = False
        new_dist = dist.copy()
        new_pred = pred.copy()

        for u in sommets:
            sommet_u = graphe.sommets[u]
            for v_sommet, (cap, cost) in sommet_u.successeurs.items():
                v = v_sommet.nom
                if cap > 0 and dist[u] + cost < new_dist[v]:
                    new_dist[v] = dist[u] + cost
                    new_pred[v] = u
                    maj = True

        dist = new_dist
        pred = new_pred
        distances_par_etape.append(dist.copy())
        pred_par_etape.append(pred.copy())

        if not maj:
            break

    # Affichage du tableau complet
    afficher_tableau_bellman(distances_par_etape, pred_par_etape, sommets)

    # Construction du chemin de t à s
    chemin = []
    curr = puits
    while pred[curr] is not None:
        chemin.insert(0, (pred[curr], curr))
        curr = pred[curr]

    if curr != source:
        return None
    return chemin



def flot_minimal(graphe, source="s", puits="t", flot_requis=4):
    flot_total = 0
    cout_total = 0
    iteration = 1

    while flot_total < flot_requis:
        chemin = bellman_ford(graphe, source, puits)
        if not chemin:
            print("Aucun chemin de coût minimal trouvé.")
            break

        capacites = []
        for u, v in chemin:
            u_sommet = graphe.sommets[u]
            v_sommet = graphe.sommets[v]
            if v_sommet in u_sommet.successeurs:
                cap, _ = u_sommet.successeurs[v_sommet]
                capacites.append(int(cap))  # FORCEMENT int

        if not capacites:
            print("⚠ Aucun arc utilisable dans le chemin.")
            break

        flot_possible = min(capacites + [flot_requis - flot_total])  # Tous sont des int

        cout_chemin = sum(
            graphe.sommets[u].successeurs[graphe.sommets[v]][1]
            for u, v in chemin
            if graphe.sommets[v] in graphe.sommets[u].successeurs
        )

        print(f"\nItération {iteration}")
        print(f"   ➤ Chemin : {' → '.join([u for u, v in chemin] + [chemin[-1][1]])}")
        print(f"   ➤ Flot envoyé : {flot_possible}")
        print(f"   ➤ Coût chemin : {cout_chemin} (total = {flot_possible * cout_chemin})")

        for u, v in chemin:
            u_sommet = graphe.sommets[u]
            v_sommet = graphe.sommets[v]
            cap, cout = u_sommet.successeurs[v_sommet]

            if cap == flot_possible:
                graphe.supprimer_arete(u, v)
            else:
                graphe.update_arete(u, v, cap - flot_possible, cout)

            # Arc retour
            if u_sommet not in v_sommet.successeurs:
                v_sommet.ajouter_successeur(u_sommet, flot_possible, -cout)
            else:
                cap_retour, cout_retour = v_sommet.successeurs[u_sommet]
                v_sommet.successeurs[u_sommet] = (cap_retour + flot_possible, cout_retour)

        flot_total += flot_possible
        cout_total += flot_possible * cout_chemin
        iteration += 1

    print(f"\nFlot total envoyé : {flot_total}")
    print(f"Coût total du flot : {cout_total}")
    return flot_total, cout_total

def afficher_tableau_bellman(distances_par_etape, pred_par_etape, sommets):
    print("\nTableau Bellman-Ford (k = nb d'itérations)\n")

    en_tete = ["k"] + sommets
    largeur = 8
    print("".join(f"{col:>{largeur}}" for col in en_tete))

    for k, (dist, pred) in enumerate(zip(distances_par_etape, pred_par_etape)):
        ligne = [str(k)]
        for s in sommets:
            d = dist.get(s, float('inf'))
            p = pred.get(s, None)
            if d == float('inf'):
                ligne.append("+∞")
            elif p is None:
                ligne.append(str(d))
            else:
                ligne.append(f"{d}_{p}")
        print("".join(f"{val:>{largeur}}" for val in ligne))

