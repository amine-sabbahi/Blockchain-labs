import hashlib

class MerkleTree:
    def __init__(self):
        self.leaves = []
        self.tree = []

    def hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def add_leaf(self, data):
        self.leaves.append(self.hash(data))

    def build_tree(self):
        self.tree = self.leaves.copy()
        while len(self.tree) > 1:
            new_level = []
            for i in range(0, len(self.tree), 2):
                if i + 1 < len(self.tree):
                    new_level.append(self.hash(self.tree[i] + self.tree[i + 1]))
                else:
                    new_level.append(self.tree[i])
            self.tree = new_level

    def get_root(self):
        if not self.tree:
            self.build_tree()
        return self.tree[0]

    def get_proof(self, leaf_index):
        proof = []
        tree_index = leaf_index
        tree_level = self.leaves.copy()
        
        while len(tree_level) > 1:
            is_right = tree_index % 2 == 1
            if is_right:
                proof.append(("left", tree_level[tree_index - 1]))
            elif tree_index + 1 < len(tree_level):
                proof.append(("right", tree_level[tree_index + 1]))
            
            tree_level = [self.hash(tree_level[i] + tree_level[i + 1]) if i + 1 < len(tree_level) else tree_level[i] for i in range(0, len(tree_level), 2)]
            tree_index //= 2
        
        return proof

    def verify_proof(self, leaf, proof, root):
        current = leaf
        for direction, node in proof:
            if direction == "left":
                current = self.hash(node + current)
            else:
                current = self.hash(current + node)
        return current == root
