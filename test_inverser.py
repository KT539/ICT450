import pytest
from inverser import inverserTexte

def test_inverser_chaine_classique():
    assert inverserTexte("chat") == "tahc"

def test_inverser_chaine_vide():
    assert inverserTexte("") == ""

def test_inverser_chaine_un_caractere():
    assert inverserTexte("a") == "a"

def test_inverser_chaine_avec_espaces():
    assert inverserTexte("salut tout le monde") == "ednom el tuot tulas"
