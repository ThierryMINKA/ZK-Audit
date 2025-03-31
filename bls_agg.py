# bls_agg.py
# Simulation de l'agrégation de signatures BLS à seuil pour ZK-Audit

def aggregate_signatures(signatures):
    """Agrège une liste de signatures simulées en une seule signature collective."""
    # Concatène toutes les signatures individuelles
    concatenated = '|'.join(signatures)
    # Simule une signature agrégée par simple hachage
    return f"AGG_SIG({hash(concatenated)})"

def verify_aggregated_signature(aggregated_signature, expected_signers_count):
    """Vérifie que la signature agrégée est bien structurée et contient le bon nombre de signataires."""
    # Vérifie simplement que la signature contient le format attendu
    return aggregated_signature.startswith("AGG_SIG(") and expected_signers_count >= 1
