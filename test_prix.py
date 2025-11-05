import pytest
from prix import calculer_prix_ttc

def test_calculer_prix_ttc_invalid_type():
    with pytest.raises(TypeError):
        calculer_prix_ttc