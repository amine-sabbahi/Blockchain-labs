# Merkle Tree Implementation

This project implements a basic Merkle tree in Python, demonstrating the concept, structure, and verification process of Merkle trees.

## What is a Merkle Tree?

A Merkle tree, also known as a hash tree, is a data structure used for efficiently summarizing and verifying the integrity of large sets of data. It is a tree in which every leaf node is labelled with the hash of a data block, and every non-leaf node is labelled with the cryptographic hash of the labels of its child nodes.

Key features of Merkle trees:
- Efficient verification of large data structures
- Widely used in peer-to-peer networks and blockchain technologies
- Allows for quick detection of data tampering

## Implementation

This project consists of two main Python files:

1. `Merkle_Tree.py`: Contains the `MerkleTree` class implementation
2. `Tree_Verification.py`: Demonstrates the usage of the `MerkleTree` class and includes test cases

### Merkle_Tree.py

This file implements the `MerkleTree` class with the following main methods:
- `add_leaf(data)`: Adds a new leaf to the tree
- `build_tree()`: Constructs the Merkle tree from the leaves
- `get_root()`: Returns the Merkle root
- `get_proof(leaf_index)`: Generates a proof for a specific leaf
- `verify_proof(leaf, proof, root)`: Verifies a proof against the Merkle root

### Tree_Verification.py

This file demonstrates how to use the `MerkleTree` class and includes a basic test scenario.

## Example Usage

The example in `Tree_Verification.py` creates a Merkle tree with four transactions, generates a proof for one of the transactions, and verifies the proof.

## Results

When running `Tree_Verification.py`, you should see output similar to the following:

```
Merkle Root: 7e1182c5c00e379261503e757487cfa16cda7010f1ca3ae0115d5b78cfc07509
Leaf: 2b8fd91deadf550d81682717104df059adc0addd006a0c7b99297e88769b30e5
Proof: [('right', 'b99ca09efe93055ad86acb5bfc964e16393d8e4672c3a4c5fa08ffabc85065b3'), ('left', 'a31d3187c179a847bc0fbe729e06a0770147ad58b45995ac945032df15ba38e3')]
Proof is valid: True
Invalid proof is valid: False

All leaves:
Leaf 0: dff3b30655dc240deca00ed22fae68fdf8cf465bbe99bb2b2e24259cc1daac3a
Leaf 1: 4ae0e48b754a046b0f08e50e91708ddff4bac4daee30b786dbd67c30d8e00df8
Leaf 2: 2b8fd91deadf550d81682717104df059adc0addd006a0c7b99297e88769b30e5
Leaf 3: b99ca09efe93055ad86acb5bfc964e16393d8e4672c3a4c5fa08ffabc85065b3

Tree levels:
Level 0: ['dff3b30655dc240deca00ed22fae68fdf8cf465bbe99bb2b2e24259cc1daac3a', '4ae0e48b754a046b0f08e50e91708ddff4bac4daee30b786dbd67c30d8e00df8', '2b8fd91deadf550d81682717104df059adc0addd006a0c7b99297e88769b30e5', 'b99ca09efe93055ad86acb5bfc964e16393d8e4672c3a4c5fa08ffabc85065b3']
Level 1: ['a31d3187c179a847bc0fbe729e06a0770147ad58b45995ac945032df15ba38e3', 'c6dadc3fe8fde36887f07ed12e0bb073b4165d0921749b98b2ae237f3aed3e07']
Level 2 (Root): ['7e1182c5c00e379261503e757487cfa16cda7010f1ca3ae0115d5b78cfc07509']
```

This output shows:
1. The Merkle root of the tree
2. A leaf (transaction) hash
3. The proof for that leaf
4. Verification results for both valid and invalid proofs
5. The structure of the Merkle tree, including all leaves and intermediate levels