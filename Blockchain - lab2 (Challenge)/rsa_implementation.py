import math
from random import randrange

def letter_to_number(letter):
    """Convert letter to number (A/a=1, B/b=2, etc)"""
    letter = letter.lower()
    if letter.isalpha():
        return ord(letter) - ord('a') + 1
    elif letter.isspace():
        return 27  # Space character
    elif letter.isdigit():
        return 28 + int(letter)  # Digits 0-9 map to 28-37
    return ord(letter)

def number_to_letter(number):
    """Convert number back to letter"""
    if 1 <= number <= 26:
        return chr(number + ord('a') - 1)
    elif number == 27:
        return ' '  # Space character
    elif 28 <= number <= 37:
        return str(number - 28)  # Convert back to digit
    return chr(number)

def is_prime(n, k=5):
    """Miller-Rabin primality test"""
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        a = randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1: continue
        for r in range(s-1):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

def generate_prime(min_val=100, max_val=1000):
    """Generate a prime number within specified range"""
    attempts = 0
    while attempts < 1000:  # Prevent infinite loop
        n = randrange(min_val, max_val)
        if is_prime(n): 
            return n
        attempts += 1
    raise ValueError("Could not find prime number in range after 1000 attempts")

def mod_inverse(e, phi):
    """Calculate the modular multiplicative inverse using extended Euclidean algorithm"""
    def extended_gcd(a, b):
        if a == 0: return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def choose_e(phi):
    """Choose public exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1"""
    candidates = [3, 5, 17, 257, 65537]  # Common choices for e
    for e in candidates:
        if e < phi and math.gcd(e, phi) == 1:
            return e
    
    # If no common value works, find the smallest valid e
    e = 3
    while e < phi:
        if math.gcd(e, phi) == 1:
            return e
        e += 2
    raise ValueError("Could not find suitable public exponent")

def generate_keypair(min_prime=100, max_prime=1000):
    """Generate public and private key pairs"""
    while True:
        try:
            p = generate_prime(min_prime, max_prime)
            q = generate_prime(min_prime, max_prime)
            if p == q:  # Ensure p and q are different
                continue
                
            n = p * q
            phi = (p - 1) * (q - 1)
            e = choose_e(phi)
            d = mod_inverse(e, phi)
            
            # Basic test to ensure the key pair works
            test_value = 42
            if pow(pow(test_value, e, n), d, n) == test_value:
                return ((e, n), (d, n))
        except ValueError:
            continue

def encrypt(public_key, message):
    """Encrypt a message using public key"""
    e, n = public_key
    try:
        numbers = [letter_to_number(char) for char in message]
        cipher = [pow(num, e, n) for num in numbers]
        return cipher
    except Exception as err:
        raise ValueError(f"Encryption failed: {str(err)}")

def decrypt(private_key, cipher):
    """Decrypt a message using private key"""
    d, n = private_key
    try:
        numbers = [pow(num, d, n) for num in cipher]
        message = ''.join(number_to_letter(num) for num in numbers)
        return message
    except Exception as err:
        raise ValueError(f"Decryption failed: {str(err)}")

# Example usage
if __name__ == "__main__":
    # Generate key pair
    public_key, private_key = generate_keypair()
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    # Test encryption and decryption
    message = "Hello World 123"
    print(f"\nOriginal message: {message}")
    
    # Encrypt
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message (numbers): {encrypted_msg}")
    
    # Decrypt
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")