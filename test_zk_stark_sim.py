# test_zk_stark_sim.py
# Tests pour les fonctions simulées de preuve zk-STARK

import pytest
from zk_stark_sim import zk_stark_prove, zk_stark_verify
from hash_utils import sha3_hash

def test_zk_stark_proof_structure():
    # Vérifie la structure retournée par la fonction de preuve
    root = sha3_hash("dummy_root")
    metadata = "2025-03-31T12:00:00Z"
    proof = zk_stark_prove(root, metadata)
    assert isinstance(proof, dict)
    assert 'proof' in proof
    assert proof['root'] == root
    assert proof['metadata'] == metadata

def test_zk_stark_verify_success():
    # Vérifie que la preuve est acceptée si les entrées sont correctes
    root = sha3_hash("root_data")
    metadata = "timestamp"
    proof = zk_stark_prove(root, metadata)
    assert zk_stark_verify(proof, root, metadata)

def test_zk_stark_verify_failure():
    # Vérifie que la preuve est rejetée si on modifie l'entrée
    root = sha3_hash("original")
    wrong_root = sha3_hash("fake")
    metadata = "time"
    proof = zk_stark_prove(root, metadata)
    assert not zk_stark_verify(proof, wrong_root, metadata)
