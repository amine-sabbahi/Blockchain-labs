from Merkle_Tree import MerkleTree
merkle_tree = MerkleTree()

# Add some leaves
transactions = ["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4"]
for tx in transactions:
    merkle_tree.add_leaf(tx)

# Build the tree and get the root
merkle_tree.build_tree()
root = merkle_tree.get_root()
print(f"Merkle Root: {root}")

# Generate and verify a proof
leaf_index = 2  # We'll verify "Transaction 3"
leaf = merkle_tree.hash(transactions[leaf_index])
proof = merkle_tree.get_proof(leaf_index)

print(f"Leaf: {leaf}")
print(f"Proof: {proof}")

is_valid = merkle_tree.verify_proof(leaf, proof, root)
print(f"Proof is valid: {is_valid}")

# Try an invalid proof
invalid_leaf = merkle_tree.hash("Invalid Transaction")
is_invalid = merkle_tree.verify_proof(invalid_leaf, proof, root)
print(f"Invalid proof is valid: {is_invalid}")

# Debug: print all leaves and tree levels
print("\nAll leaves:")
for i, leaf in enumerate(merkle_tree.leaves):
    print(f"Leaf {i}: {leaf}")

print("\nTree levels:")
tree_level = merkle_tree.leaves.copy()
level = 0
while len(tree_level) > 1:
    print(f"Level {level}: {tree_level}")
    tree_level = [merkle_tree.hash(tree_level[i] + tree_level[i + 1]) if i + 1 < len(tree_level) else tree_level[i] for i in range(0, len(tree_level), 2)]
    level += 1
print(f"Level {level} (Root): {tree_level}")