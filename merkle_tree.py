# merkle_tree.py
# Implémentation d'un arbre de Merkle pour ZK-Audit

from hash_utils import sha3_hash

class MerkleTree:
    """Classe représentant un arbre de Merkle."""

    def __init__(self, leaves):
        """Initialise l'arbre à partir d'une liste de feuilles."""
        # Hache chaque feuille pour former la base de l'arbre
        self.leaves = [sha3_hash(leaf) for leaf in leaves]
        # Construit l'arbre et stocke la racine
        self.root = self.build_tree(self.leaves)

    def build_tree(self, nodes):
        """Construit récursivement l'arbre de Merkle et retourne la racine."""
        # Cas de base : un seul nœud = racine
        if len(nodes) == 1:
            return nodes[0]
        # Si nombre impair de nœuds, duplique le dernier
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])
        # Concatène et hache les paires de nœuds
        parent_level = []
        for i in range(0, len(nodes), 2):
            combined = nodes[i] + nodes[i+1]
            parent_hash = sha3_hash(combined)
            parent_level.append(parent_hash)
        # Appel récursif sur le niveau parent
        return self.build_tree(parent_level)

    def get_root(self):
        """Retourne la racine de l'arbre de Merkle."""
        return self.root
