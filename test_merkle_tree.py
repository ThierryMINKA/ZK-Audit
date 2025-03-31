# test_merkle_tree.py
# Tests unitaires pour le module MerkleTree de ZK-Audit

import pytest
from merkle_tree import MerkleTree
from hash_utils import sha3_hash

def test_merkle_root_single_leaf():
    # Test avec une seule feuille : la racine est le hash de cette feuille
    data = ["log1"]
    tree = MerkleTree(data)
    expected_root = sha3_hash(data[0])
    assert tree.get_root() == expected_root

def test_merkle_root_multiple_leaves_even():
    # Test avec un nombre pair de feuilles
    data = ["log1", "log2"]
    tree = MerkleTree(data)
    root = tree.get_root()
    assert isinstance(root, str)
    assert len(root) == 64  # SHA3-256 hash length

def test_merkle_root_multiple_leaves_odd():
    # Test avec un nombre impair de feuilles (doit dupliquer la dernière)
    data = ["log1", "log2", "log3"]
    tree = MerkleTree(data)
    root = tree.get_root()
    assert isinstance(root, str)
    assert len(root) == 64

def test_merkle_root_determinism():
    # Vérifie que deux arbres avec les mêmes données donnent la même racine
    data = ["A", "B", "C", "D"]
    tree1 = MerkleTree(data)
    tree2 = MerkleTree(data)
    assert tree1.get_root() == tree2.get_root()
