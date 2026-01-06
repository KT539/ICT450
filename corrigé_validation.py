# validation.py

import re

def valider_mot_de_passe(mdp: str) -> bool:
    if not isinstance(mdp, str):
        return False
    if len(mdp) < 8:
        return False
    if not re.search(r"[A-Z]", mdp):
        return False
    if not re.search(r"[a-z]", mdp):
        return False
    if not re.search(r"\d", mdp):
        return False
    return True
