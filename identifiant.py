def creer_identifiant_utilisateur(prenom, nom):
    """
    Génère un identifiant utilisateur sous forme : prénom.nom en minuscules.
    Supprime les espaces et accents.

    Ex : "Jean", "Dupont" → "jean.dupont"
    """
    import unicodedata
    def nettoyer(texte):
        texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode('utf-8')
        return texte.strip().lower().replace(" ", "")

    return f"{nettoyer(prenom)}.{nettoyer(nom)}"