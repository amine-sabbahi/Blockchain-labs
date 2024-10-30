# Prime Factor Hash (PFH)

## Introduction
Hashing algorithms play an essential role in data security, integrity, and cryptography, creating unique and fixed-length representations (hashes) of input data. The **Prime Factor Encoding (PFE) Hash** is a novel hashing approach based on prime factorization, which uniquely represents input data by breaking down each byte into prime factors and encoding them. Unlike standard hashing algorithms, PFE Hash leverages mathematical properties of prime numbers, ensuring that even the slightest input change results in a significantly different hash.

## Concept
The PFE Hash algorithm is structured around dynamic prime generation, byte prime factorization, and unique prime factor encoding:
- **Dynamic Prime Generation**: Generates a custom prime set based on input length to ensure unique mappings.
- **Byte Prime Factorization**: Converts each byte in the input to its ASCII value and factorizes it into primes.
- **Unique Factor Encoding**: Each prime factor is encoded and concatenated to create a unique, intermediate representation of the input.

The final hash is then reduced to a fixed-length using a modulo operation, ensuring the output fits a predefined size (e.g., 256 bits).

## Algorithm Steps
1. **Prime Generation**: Create a custom list of prime numbers based on the input’s length.
2. **ASCII Conversion and Factorization**:
   - Convert each character in the input to its ASCII value.
   - Factorize each ASCII value into prime factors.
3. **Prime Factor Encoding**:
   - Encode each factor uniquely, using an index in the custom primes list or directly if unmatched.
   - Concatenate all encoded factors into a single string.
4. **Hash Reduction**:
   - Convert the concatenated result to an integer.
   - Reduce the integer to a fixed bit-length (e.g., 256 bits) using modulo.
   - Convert to hexadecimal for the final hash output.

## Example Explanation
For the input `"hash"`:
1. **ASCII Conversion**: The ASCII values for `"h"`, `"a"`, `"s"`, and `"h"` are `[104, 97, 115, 104]`.
2. **Prime Factorization**:
   - `104` factorizes to \(2^3 \times 13\).
   - `97` is prime, so it remains `97`.
   - `115` factorizes to \(5 \times 23\).
3. **Prime Factor Encoding**:
   - Assume custom primes include `2`, `3`, `5`, `7`, etc. Encoding might be:
     - `104` as `203` for `2^3` and `13`.
     - `97` directly as `97`.
     - `115` as `10` (for `5`) and `23`.
4. **Concatenation**: The encoded result is `203971023203`.
5. **Hash Reduction**:
   - Convert `203971023203` to an integer and reduce it using modulo \(2^{256}\).
   - The final hash is converted to hexadecimal, resulting in a fixed-length hash.

## Conclusion
The **Prime Factor Encoding (PFE) Hash** introduces a unique one-way hashing function, leveraging the distinct properties of prime numbers to generate sensitive and non-reversible hashes. Although PFE Hash may not match cryptographic standards like SHA-256, it provides an innovative alternative for use cases requiring unique and non-traditional hashing mechanisms.

## Usage
```python
# Example usage of PFE Hash algorithm
input_string = "hash"
hash_value = prime_factor_encoding_hash(input_string)
print(f"Hash of '{input_string}': {hash_value}")
