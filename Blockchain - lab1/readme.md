
# Blockchain Lab1

This repository contains implementations of three fundamental concepts in blockchain technology:

- **Arbre de Merkle (Merkle Tree)**
- **Proof of Work (PoW)**
- **Proof of Stake (PoS)**

These implementations are designed to demonstrate the core principles of these concepts and provide a hands-on understanding of how they work.

## Project Structure

The repository is organized as follows:

```
Blockchain - lab1/
│
├── Arbre de Merkle/
│   ├── Merkle_Tree.py
│   ├── Tree_Verification.py
│   └── readme.md
│
├── Proof of work/
│   ├── blockchain.py
│   ├── pow_verification.py
│   └── readme.md
│
└── Proof of Stake/
    ├── pos_blockchain.py
    ├── test_pos.py
    ├── comparison.py
    └── readme.md
```

### 1. Arbre de Merkle (Merkle Tree)
- **Located in the `Arbre de Merkle/` folder.**
- A Merkle tree, also known as a hash tree, is a fundamental data structure used in blockchain technology for efficiently verifying the integrity of large datasets.

**Key features:**
- Efficient verification of data integrity
- Widely used in peer-to-peer networks and blockchain systems
- Allows for quick detection of data tampering

For more details on the implementation and usage, please refer to the `readme.md` file in the `Arbre de Merkle/` folder.

### 2. Proof of Work (PoW)
- **Located in the `Proof of work/` folder.**
- Proof of Work is a consensus mechanism used in many blockchain systems, including Bitcoin. It demonstrates the core concepts of blockchain technology and the PoW algorithm.

**Key concepts:**
- Difficulty in creating blocks
- Ease of verification
- Adjustable difficulty to maintain consistent block creation rate

For more details on the implementation, usage, and results of different difficulty levels, please refer to the `readme.md` file in the `Proof of work/` folder.

### 3. Proof of Stake (PoS)
- **Located in the `Proof of Stake/` folder.**
- Proof of Stake is an alternative consensus mechanism used in some blockchain systems. It relies on the validators' stake (cryptocurrency holdings) to validate transactions and add blocks to the blockchain.

**Key features:**
- Validators' chance of being selected is proportional to their stake
- Less energy-intensive compared to Proof of Work
- Includes methods for adding blocks, updating validator stakes, and validating the blockchain

For more details on the implementation and comparison with Proof of Work, please refer to the `readme.md` file in the `Proof of Stake/` folder.

## Running the Implementations

Each implementation has its own set of Python files and a dedicated readme with specific instructions. To run any of the implementations:

1. Navigate to the respective folder (`Arbre de Merkle/`, `Proof of work/`, or `Proof of Stake/`)
2. Follow the instructions in the folder's `readme.md` file

## Prerequisites

- Python 3.x
- No additional libraries required; all implementations use Python's standard library

## Learning Objectives

By exploring these implementations, you will gain insights into:

- How Merkle trees provide efficient data verification in blockchain systems
- The mechanics of Proof of Work and its role in securing blockchain networks
- The principles of Proof of Stake and how it differs from Proof of Work
- The relationship between mining difficulty and block creation time in PoW systems
- The impact of validator stakes on the PoS blockchain validation process

Feel free to explore each implementation, run the code, and experiment with different parameters to deepen your understanding of these blockchain concepts.

---

**Abdelmalek Essaadi University** Faculty of Sciences and Techniques
   - Department : Computer Engineering
   - Master : AI & DS
   - Module : Blockchain
   - Prof : Ikram ben abdel ouahab