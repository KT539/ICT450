from identifiant import creer_identifiant_utilisateur
import pytest

def test_identifiant_sans_accent():
    # Arrange
    prenom = "Jean"
    nom = "Dupont"

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "jean.dupont"


def test_identifiant_avec_accent_et_espaces():
    # Arrange
    prenom = "Élodie"
    nom = "  Le Bris  "

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "elodie.lebris"


def test_identifiant_avec_espaces_autour():
    # Arrange
    prenom = "  Jean  "
    nom = "   Valjean"

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "jean.valjean"


def test_identifiant_tout_en_majuscules_et_accent():
    # Arrange
    prenom = "Sébastien"
    nom = "  MARTIN  "

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "sebastien.martin"


def test_identifiant_avec_nom_compose():
    # Arrange
    prenom = "Jean-Pierre"
    nom = " De La Tour "

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "jean-pierre.delatour"


def test_identifiant_avec_prenom_accentue():
    # Arrange
    prenom = "Zoé"
    nom = "Durand"

    # Act
    resultat = creer_identifiant_utilisateur(prenom, nom)

    # Assert
    assert resultat == "zoe.durand"


def test_identifiant_vide():
    # Arrange
    prenom = ""
    nom = ""

    # Act / Assert
    with pytest.raises(IndexError):
        creer_identifiant_utilisateur(prenom, nom)
