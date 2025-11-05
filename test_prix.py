import pytest
from prix import calculer_prix_ttc


def test_calculer_prix_ttc_standard():
    # Arrange
    prix_ht, tva = 100, 0.2
    # Act
    expected = calculer_prix_ttc(prix_ht, tva)
    # Assert
    assert expected == 120

def test_calculer_prix_ttc_with_negative_price():
    # Arrange
    prix_ht, tva = -50, 0.2
    # Aact + Assert
    with pytest.raises(ValueError):
        calculer_prix_ttc(prix_ht, tva)

def test_calculer_prix_ttc_with_negative_tva():
    # Arrange
    prix_ht, tva = 50, -0.2
    # Act + Assert
    with pytest.raises(ValueError):
        calculer_prix_ttc(prix_ht, tva)

def test_calculer_prix_ttc_with_0():
    # Arrange
    prix_ht, tva = 0, 0.2
    # Act
    expected = calculer_prix_ttc(prix_ht, tva)
    # Assert
    assert expected == 0

def test_calculer_prix_ttc_invalid_type():
    # Arrange
    prix_ht, tva = "cent", 0.2
    # Act + Assert
    with pytest.raises(TypeError):
        calculer_prix_ttc(prix_ht, tva)