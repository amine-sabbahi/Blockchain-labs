from polynomial_crypto import PolynomialCrypto

def test_crypto_system():
    """Test function to verify the cryptographic system works correctly."""
    # Initialize with larger parameters for better security
    crypto = PolynomialCrypto(degree=8, field_size=257)  # Using 257 as it's prime and just larger than 256 (ASCII)
    
    # Generate keys
    public_key, private_key = crypto.generate_keypair()
    print(f"Public Key (polynomial, base): {public_key}")
    print(f"Private Key (polynomials): {private_key}")
    
    # Test messages
    test_messages = [
        "Hello World!",
        "Testing 123",
        "SABBAHI",
        "!@#$%^&*()"
    ]
    
    for message in test_messages:
        print(f"\nOriginal message: {message}")
        
        try:
            # Encrypt
            cipher = crypto.encrypt(message, public_key)
            print(f"Encrypted message: {cipher}")
            
            # Decrypt
            decrypted = crypto.decrypt(cipher, private_key, public_key[1])
            print(f"Decrypted message: {decrypted}")
            
            # Verify
            assert message == decrypted, "Decryption failed!"
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_crypto_system()