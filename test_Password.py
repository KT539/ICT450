# test_motdepasse.py

import pytest
from validation import valider_mot_de_passe

# --- Tests valides ---

def test_mot_de_passe_valide_classique():
    assert valider_mot_de_passe("MotDePasse1") is True

# --- Tests invalides ---

def test_mot_de_passe_trop_court():
    assert valider_mot_de_passe("Ab1") is False

def test_mot_de_passe_sans_majuscule():
    assert valider_mot_de_passe("motdepasse1") is False

def test_mot_de_passe_sans_minuscule():
    assert valider_mot_de_passe("MOTDEPASSE1") is False

def test_mot_de_passe_sans_chiffre():
    assert valider_mot_de_passe("MotDePasse") is False

def test_mot_de_passe_vide():
    assert valider_mot_de_passe("") is False

def test_mot_de_passe_non_string():
    assert valider_mot_de_passe(12345678) is False
