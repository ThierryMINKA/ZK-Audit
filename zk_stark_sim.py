# zk_stark_sim.py
# Simulation simplifiée de génération et vérification de preuve zk-STARK

from hash_utils import sha3_hash

def zk_stark_prove(merkle_root, metadata):
    """Génère une preuve simulée à partir d'une racine Merkle et de métadonnées."""
    # Concatène la racine et les métadonnées
    input_data = merkle_root + '|' + metadata
    # Simule une preuve en hashant les données d'entrée
    proof = sha3_hash(input_data)
    # Retourne la structure simulée de preuve
    return {
        'root': merkle_root,
        'metadata': metadata,
        'proof': proof
    }

def zk_stark_verify(proof_object, expected_root, expected_metadata):
    """Vérifie la preuve simulée en recalculant le hash attendu."""
    # Recalcule la preuve à partir des données attendues
    recomputed_input = expected_root + '|' + expected_metadata
    recomputed_proof = sha3_hash(recomputed_input)
    # Compare la preuve fournie à la preuve attendue
    return recomputed_proof == proof_object['proof']
