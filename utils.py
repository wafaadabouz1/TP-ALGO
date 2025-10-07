import matplotlib.pyplot as plt
import networkx as nx


def dessiner_arbre(G, node, pos=None, x=0, y=0, layer=1):
    """
    Fonction récursive pour positionner les nœuds de manière hiérarchique.
    Correction : on utilise (-1)**(i+1) pour que le 1er voisin soit placé à gauche,
    et le 2e à droite (au lieu de l'inverse).
    """
    if pos is None:
        pos = {}
    pos[node] = (x, y)
    voisins = list(G.neighbors(node))
    if len(voisins) != 0:
        dx = 1 / (2 ** layer)
        for i, v in enumerate(voisins):
            # i=0 -> (-1)**(1) = -1 (gauche)
            # i=1 -> (-1)**(2) = +1 (droite)
            offset = (-1) ** (i + 1)
            pos.update(dessiner_arbre(G, v, pos=pos, x=x + offset * dx, y=y - 1, layer=layer + 1))
    return pos


def afficher_arbre(abr):
    G = nx.DiGraph()

    def ajouter_noeuds_et_aretes(noeud):
        if noeud:
            G.add_node(noeud.valeur)
            if noeud.gauche:
                G.add_edge(noeud.valeur, noeud.gauche.valeur)
                ajouter_noeuds_et_aretes(noeud.gauche)
            if noeud.droite:
                G.add_edge(noeud.valeur, noeud.droite.valeur)
                ajouter_noeuds_et_aretes(noeud.droite)

    if abr.racine is None:
        print("Arbre vide : rien à afficher.")
        return

    ajouter_noeuds_et_aretes(abr.racine)
    pos = dessiner_arbre(G, abr.racine.valeur)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, arrows=False)
    plt.title("Affichage de l'Arbre Binaire de Recherche")
    plt.axis('off')
    plt.show()


def compter_noeuds(noeud):
    """Compte le nombre total de nœuds dans l’arbre"""
    if noeud is None:
        return 0
    return 1 + compter_noeuds(noeud.gauche) + compter_noeuds(noeud.droite)


def densite(arbre):
    """Calcule la densité de l’arbre = nb_noeuds / hauteur"""
    nb_noeuds = compter_noeuds(arbre.racine)
    h = arbre.hauteur()
    return round(nb_noeuds / h, 2) if h > 0 else 0
