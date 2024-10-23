# Polynomial-Based Cryptographic System

A Python implementation of a custom cryptographic system based on polynomial operations in finite fields. This project demonstrates the use of polynomial arithmetic for encryption and decryption of messages.

## Overview

This cryptographic system uses polynomial multiplication in finite fields to create a public-key cryptography scheme. The implementation includes:
- Key generation using random polynomials
- Message encryption using public key
- Message decryption using private key
- Support for full ASCII character set
- Cryptographically secure random number generation

## Features

- Custom polynomial-based encryption/decryption
- Public-key cryptography implementation
- Finite field arithmetic operations
- Configurable security parameters (field size and polynomial degree)
- Comprehensive input validation
- Testing suite included

## Requirements

- Python 3.7+
- Standard Python libraries:
  - `secrets` (for secure random number generation)
  - `typing` (for type hints)

## Installation

Clone the repository:
```bash
git clone https://github.com/amine-sabbahi/Blockchain-labs.git
cd "Blockchain-labs/Blockchain - labs2 (Challenge)"
```

No additional dependencies are required as the implementation uses only Python standard libraries.

## Usage

Basic usage example:

```python
from polynomial_crypto import PolynomialCrypto

# Initialize the cryptosystem
crypto = PolynomialCrypto(degree=8, field_size=257)

# Generate key pair
public_key, private_key = crypto.generate_keypair()

# Encrypt a message
message = "Hello World!"
cipher = crypto.encrypt(message, public_key)

# Decrypt the message
decrypted = crypto.decrypt(cipher, private_key, public_key[1])

print(f"Original: {message}")
print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypted}")
```

## Security Parameters

- `degree`: Polynomial degree (default=8)
  - Higher degrees provide more security but increase computation time
  - Must be even number
  
- `field_size`: Prime number for finite field (default=257)
  - Must be prime
  - Must be larger than 256 to support ASCII characters
  - Larger field size increases security

## Example Output

```python
Original message: SABBAHI
Encrypted message: [203, 224, 180, 180, 224, 173, 129]
Decrypted message: SABBAHI
```

## Security Considerations

This implementation is primarily for educational purposes and should not be used in production environments. For production use, please use established cryptographic libraries and standards.

Key security aspects:
- Uses `secrets` module for cryptographically secure random numbers
- Implements proper parameter validation
- Supports full ASCII character set
- Includes basic security checks

## Implementation Details

The system consists of three main components:

1. **Key Generation**
   - Creates two random polynomials for private key
   - Generates public key through polynomial multiplication
   - Selects secure random base point

2. **Encryption**
   - Converts message to ASCII values
   - Uses public polynomial evaluation for encryption
   - Performs operations in finite field

3. **Decryption**
   - Uses private polynomials to compute decryption factor
   - Recovers original message through modular arithmetic
   - Converts numbers back to characters


## Author

[SABBAHI]

## Acknowledgments

- Inspired by RSA cryptographiE method
- Built for educational purposes to demonstrate finite field arithmetic
- Based on fundamental concepts of public-key cryptography