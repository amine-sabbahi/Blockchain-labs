# Proof of Work Blockchain Implementation

This project implements a basic blockchain with a Proof of Work (PoW) consensus mechanism in Python. It demonstrates the core concepts of blockchain technology and the PoW algorithm.

## Concept: Proof of Work

Proof of Work is a consensus mechanism used in many blockchain systems, including Bitcoin. The main ideas behind PoW are:

1. **Difficulty in Creating Blocks**: Miners must solve a computationally intensive problem to create a new block.
2. **Ease of Verification**: While creating a valid block is difficult, verifying its validity is easy for other nodes.
3. **Adjustable Difficulty**: The difficulty of the problem can be adjusted to maintain a consistent block creation rate.

In this implementation, the PoW algorithm requires finding a block hash that starts with a specific number of zeros. The number of required zeros determines the difficulty.

## Implementation

The project consists of two main Python files:

1. `blockchain.py`: Contains the `Block` and `Blockchain` classes.
2. `pow_verification.py`: Demonstrates the usage of the blockchain and tests different difficulty levels.

### Key Components

- **Block**: Represents a single block in the blockchain, containing:
  - Index
  - Timestamp
  - Data
  - Previous block's hash
  - Nonce (used for PoW)
  - Current block's hash

- **Blockchain**: Manages the chain of blocks and implements PoW:
  - Adds new blocks to the chain
  - Performs the PoW algorithm
  - Validates the entire chain
  - Allows adjusting the mining difficulty

- **Proof of Work**: Implemented in the `proof_of_work` method, which adjusts the nonce until a hash with the required number of leading zeros is found.

## Results

The `pow_verification.py` script tests the PoW implementation with different difficulty levels (4, 5, and 6). Here's an example of the output:

```
Difficulty: 4
Time taken: 0.01 seconds
Chain valid: True
Blocks in the chain:
Block #0 - Hash: ...
Block #1 - Hash: 0000...
Block #2 - Hash: 0000...
Block #3 - Hash: 0000...

Difficulty: 5
Time taken: 0.15 seconds
Chain valid: True
Blocks in the chain:
Block #0 - Hash: ...
Block #1 - Hash: 00000...
Block #2 - Hash: 00000...
Block #3 - Hash: 00000...

Difficulty: 6
Time taken: 3.25 seconds
Chain valid: True
Blocks in the chain:
Block #0 - Hash: ...
Block #1 - Hash: 000000...
Block #2 - Hash: 000000...
Block #3 - Hash: 000000...
```

### Observations

1. **Increasing Difficulty**: As the difficulty increases (more leading zeros required), the time to mine blocks increases exponentially.
2. **Hash Patterns**: The block hashes show the required number of leading zeros, demonstrating successful PoW.
3. **Chain Validity**: The blockchain remains valid after each difficulty level, showing the integrity of the chain.

## Running the Code

To run this implementation:

1. Ensure you have Python installed on your system.
2. Save `blockchain.py` and `pow_verification.py` in the same directory.
3. Run the following command:
   ```
   python pow_verification.py
   ```

## Potential Extensions

- Implement a more complex data structure for transactions within blocks.
- Add networking capabilities to simulate a distributed blockchain network.
- Implement additional consensus mechanisms for comparison (e.g., Proof of Stake).

This implementation provides a foundation for understanding blockchain technology and the Proof of Work concept. It demonstrates how difficulty affects mining time and how the blockchain maintains its integrity through cryptographic links between blocks.