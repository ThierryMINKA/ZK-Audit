# demo_zk_audit.py
# Script de démonstration du flux ZK-Audit complet

from hash_utils import generate_nonce, forgettable_commitment
from merkle_tree import MerkleTree
from zk_stark_sim import zk_stark_prove, zk_stark_verify
from bls_agg import aggregate_signatures, verify_aggregated_signature

def main():
    # Étape 1 : Génération de logs d'exemple avec engagement
    print("Étape 1: Génération des engagements oubliables")
    logs = ["User A accessed File X", "User B deleted File Y", "Admin modified Policy Z"]
    nonces = [generate_nonce() for _ in logs]
    commitments = [forgettable_commitment(log, nonce) for log, nonce in zip(logs, nonces)]
    for i, c in enumerate(commitments):
        print(f"Log {i+1}: {c}")

    # Étape 2 : Construction de l’arbre de Merkle
    print("\nÉtape 2: Construction de l'arbre de Merkle")
    tree = MerkleTree(commitments)
    merkle_root = tree.get_root()
    print(f"Merkle Root: {merkle_root}")

    # Étape 3 : Génération de la preuve zk-STARK simulée
    print("\nÉtape 3: Génération de la preuve zk-STARK simulée")
    metadata = "2025-03-31T12:00:00Z"  # Ex: timestamp
    proof_obj = zk_stark_prove(merkle_root, metadata)
    print(f"Proof: {proof_obj['proof']}")
    
    # Étape 4 : Vérification de la preuve
    print("\nÉtape 4: Vérification de la preuve")
    verified = zk_stark_verify(proof_obj, merkle_root, metadata)
    print(f"Proof valid: {verified}")

    # Étape 5 : Agrégation et vérification de signatures BLS simulées
    print("\nÉtape 5: Signature distribuée (BLS simulée)")
    partial_signatures = [f"SIG_from_node_{i}" for i in range(3)]
    agg_sig = aggregate_signatures(partial_signatures)
    print(f"Aggregated Signature: {agg_sig}")
    valid_agg = verify_aggregated_signature(agg_sig, len(partial_signatures))
    print(f"Aggregated Signature Valid: {valid_agg}")

if __name__ == "__main__":
    main()
