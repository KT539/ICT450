# test_code_bug.py
import pytest
from code_bug import ajouter, est_adulte, division

def test_ajouter():
    assert ajouter(2, 3) == 5

def test_est_adulte_vrai():
    assert est_adulte(18) is True

def test_est_adulte_faux():
    assert est_adulte(17) is False

def test_division():
    assert division(10, 2) == 5

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

