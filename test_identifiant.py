from identifiant import creer_identifiant_utilisateur

def test_full():
    assert creer_identifiant_utilisateur("Jean", "Dupont") == "jean.dupont"
    assert creer_identifiant_utilisateur("Élodie", "  Le Bris  ") == "elodie.lebris"
    assert creer_identifiant_utilisateur("  Jean  ", "   Valjean") == "jean.valjean"
    assert creer_identifiant_utilisateur("Sébastien", "  MARTIN  ") == "sebastien.martin"
    assert creer_identifiant_utilisateur("Zoé", "Durand") == "zoe.durand"
    assert creer_identifiant_utilisateur("Jean-Pierre", " De La Tour ") == "jean-pierre.delatour"
