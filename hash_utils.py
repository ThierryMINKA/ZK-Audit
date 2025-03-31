# hash_utils.py
# Fonctions de hachage et d'engagement oubliable pour ZK-Audit

import hashlib
import os

def sha3_hash(data):
    """Calcule un hash SHA3-256 sur une chaîne de caractères."""
    # Encodage en bytes de la chaîne
    data_bytes = data.encode('utf-8')
    # Application du hachage SHA3-256
    return hashlib.sha3_256(data_bytes).hexdigest()

def generate_nonce(length=16):
    """Génère un nonce aléatoire sous forme hexadécimale."""
    # Génère une chaîne de bytes aléatoires
    nonce = os.urandom(length)
    # Retourne sa représentation hexadécimale
    return nonce.hex()

def forgettable_commitment(entry, nonce):
    """Crée un engagement oubliable à partir d'une entrée de log et d'un nonce."""
    # Concatène l'entrée avec le nonce
    combined = f"{entry}|{nonce}"
    # Calcule le hash SHA3-256 de la combinaison
    return sha3_hash(combined)
