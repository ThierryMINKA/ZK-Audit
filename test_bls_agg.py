# test_bls_agg.py
# Tests pour les fonctions simulées d'agrégation BLS

import pytest
from bls_agg import aggregate_signatures, verify_aggregated_signature

def test_aggregate_signatures_format():
    # Vérifie que la signature agrégée est bien formatée
    sigs = ["sig1", "sig2", "sig3"]
    agg = aggregate_signatures(sigs)
    assert agg.startswith("AGG_SIG(")
    assert "sig1" not in agg  # doit être hashé, pas concaténé lisiblement

def test_verify_aggregated_signature_valid():
    # Vérifie que la signature agrégée est reconnue comme valide
    agg = aggregate_signatures(["s1", "s2"])
    assert verify_aggregated_signature(agg, 2)

def test_verify_aggregated_signature_invalid():
    # Vérifie que les entrées invalides sont rejetées
    assert not verify_aggregated_signature("INVALID", 2)
