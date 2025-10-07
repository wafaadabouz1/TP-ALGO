from abr import ABR
from utils import afficher_arbre, densite, compter_noeuds


if __name__ == "__main__":
    print("=== TP1 : Arbre Binaire de Recherche (ABR) ===\n")

    arbre = ABR()

    # 🔹 Saisie utilisateur
    print("Entrez les valeurs à insérer dans l'arbre (séparées par des espaces) :")
    valeurs_str = input("")
    valeurs = [int(v) for v in valeurs_str.split()]

    for v in valeurs:
        arbre.inserer(v)

    # 🔹 Parcours
    print("\n Parcours infixe (ordre croissant) :", arbre.parcours_infixe())
    print("Parcours préordre :", arbre.parcours_preordre())
    print(" Parcours postordre :", arbre.parcours_postordre())

    # 🔹 Calculs
    nb_noeuds = compter_noeuds(arbre.racine)
    h = arbre.hauteur()
    d = densite(arbre)
    degre = arbre.degre_max()

    print(f"\n Hauteur de l’arbre : {h}")
    print(f" Nombre total de nœuds : {nb_noeuds}")
    print(f" Degré maximal : {degre}")
    print(f" Densité : {d}")

    # 🔹 Affichage graphique
    print("\nAffichage graphique de l’arbre...")
    afficher_arbre(arbre)

 