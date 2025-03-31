# test_hash_utils.py
# Tests pour les fonctions de hachage et d'engagement oubliable de ZK-Audit

import pytest
from hash_utils import sha3_hash, generate_nonce, forgettable_commitment

def test_sha3_hash_deterministic():
    # Vérifie que le hash est déterministe
    input_str = "test_input"
    h1 = sha3_hash(input_str)
    h2 = sha3_hash(input_str)
    assert h1 == h2
    assert len(h1) == 64  # SHA3-256 donne 64 caractères hexadécimaux

def test_generate_nonce_length():
    # Vérifie que le nonce généré a bien la longueur attendue
    nonce = generate_nonce(16)
    assert isinstance(nonce, str)
    assert len(nonce) == 32  # 16 octets -> 32 caractères hexadécimaux

def test_forgettable_commitment_uniqueness():
    # Vérifie que le même message avec des nonces différents produit des engagements différents
    log = "user access log"
    c1 = forgettable_commitment(log, generate_nonce())
    c2 = forgettable_commitment(log, generate_nonce())
    assert c1 != c2
