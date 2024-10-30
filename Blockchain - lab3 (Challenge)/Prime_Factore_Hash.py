from sympy import primerange, factorint

def generate_primes(n):
    # Generate a list of the first `n` primes
    return list(primerange(2, n * 10))[:n]

def prime_factor_encode(ascii_value, primes):
    # Factorize the ASCII value into prime factors and use the custom primes as encoding
    factors = factorint(ascii_value)
    encoded_factors = []
    for prime, exponent in factors.items():
        # Find index in our custom primes, fall back to the prime itself if not in list
        if prime in primes:
            index = primes.index(prime)
            encoded_factors.append(f"{index:02d}{exponent}")
        else:
            # For any non-matching primes, encode directly (fallback option)
            encoded_factors.append(f"{prime}{exponent}")
    return ''.join(encoded_factors)

def prime_factor_encoding_hash(input_string):
    # Convert input string to ASCII values
    ascii_values = [ord(char) for char in input_string]
    length = len(ascii_values)

    # Step 1: Generate a custom set of primes based on input length
    custom_primes = generate_primes(length)

    # Step 2: Encode each ASCII value as a string of prime factors
    encoded_string = ""
    for value in ascii_values:
        encoded_string += prime_factor_encode(value, custom_primes)

    # Step 3: Hash reduction to fixed size by modulo operation
    # Convert encoded string to a big integer and apply modulo for fixed length
    hash_value = int(encoded_string) % (2**256)

    # Step 4: Convert hash value to fixed-length hexadecimal
    hash_hex = f"{hash_value:032x}"
    return hash_hex

# Testing with examples
input_1 = "hash"
input_2 = "prime"
print("Hash of 'hash':", prime_factor_encoding_hash(input_1))
print("Hash of 'prime':", prime_factor_encoding_hash(input_2))
