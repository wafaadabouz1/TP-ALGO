class Node:
    """Classe représentant un nœud dans un Arbre Binaire de Recherche (ABR)"""
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None


class ABR:
    """Classe représentant un Arbre Binaire de Recherche"""
    def __init__(self):
        self.racine = None

    # ---------- Insertion ----------
    def inserer(self, valeur):
        """Insère une nouvelle valeur dans l’arbre"""
        if self.racine is None:
            self.racine = Node(valeur)
        else:
            self._inserer_rec(self.racine, valeur)

    def _inserer_rec(self, noeud, valeur):
        """Méthode récursive d’insertion"""
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Node(valeur)
            else:
                self._inserer_rec(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            if noeud.droite is None:
                noeud.droite = Node(valeur)
            else:
                self._inserer_rec(noeud.droite, valeur)
        # Si la valeur existe déjà, on ne fait rien

    # ---------- Parcours ----------
    def parcours_infixe(self):
        """Retourne les valeurs en ordre croissant (gauche - racine - droite)"""
        valeurs = []
        self._infixe_rec(self.racine, valeurs)
        return valeurs

    def _infixe_rec(self, noeud, valeurs):
        if noeud:
            self._infixe_rec(noeud.gauche, valeurs)
            valeurs.append(noeud.valeur)
            self._infixe_rec(noeud.droite, valeurs)

    def parcours_preordre(self):
        """Retourne le parcours préordre (racine - gauche - droite)"""
        valeurs = []
        self._preordre_rec(self.racine, valeurs)
        return valeurs

    def _preordre_rec(self, noeud, valeurs):
        if noeud:
            valeurs.append(noeud.valeur)
            self._preordre_rec(noeud.gauche, valeurs)
            self._preordre_rec(noeud.droite, valeurs)

    def parcours_postordre(self):
        """Retourne le parcours postordre (gauche - droite - racine)"""
        valeurs = []
        self._postordre_rec(self.racine, valeurs)
        return valeurs

    def _postordre_rec(self, noeud, valeurs):
        if noeud:
            self._postordre_rec(noeud.gauche, valeurs)
            self._postordre_rec(noeud.droite, valeurs)
            valeurs.append(noeud.valeur)

    # ---------- Hauteur ----------
    def hauteur(self):
        """Calcule la hauteur de l’arbre"""
        return self._hauteur_rec(self.racine)

    def _hauteur_rec(self, noeud):
        if noeud is None:
            return 0
        return 1 + max(self._hauteur_rec(noeud.gauche), self._hauteur_rec(noeud.droite))

    # ---------- Degré ----------
    def degre_max(self):
        """Calcule le degré maximal de l’arbre (max de fils d’un nœud)"""
        return self._degre_max_rec(self.racine)

    def _degre_max_rec(self, noeud):
        if noeud is None:
            return 0
        degre = 0
        if noeud.gauche:
            degre += 1
        if noeud.droite:
            degre += 1
        return max(degre, self._degre_max_rec(noeud.gauche), self._degre_max_rec(noeud.droite))
