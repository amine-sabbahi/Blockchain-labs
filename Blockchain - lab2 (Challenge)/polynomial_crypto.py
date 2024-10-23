import secrets
from typing import List, Tuple

class PolynomialCrypto:
    def __init__(self, degree: int = 8, field_size: int = 257):
        """
        Initialize the cryptosystem with specified polynomial degree and field size.
        
        Args:
            degree (int): Degree of the polynomials used in the system. Higher means more security but slower.
            field_size (int): Prime number to be used as field size. Should be larger than 256 to accommodate ASCII.
        
        Note:
            field_size must be prime for security and proper modular arithmetic
            degree should be even for the key generation to work properly
        """
        if degree % 2 != 0:
            raise ValueError("Degree must be even")
        if field_size <= 256:
            raise ValueError("Field size must be greater than 256 to accommodate ASCII characters")
        
        self.degree = degree
        self.field_size = field_size
        
    def generate_random_polynomial(self, degree: int) -> List[int]:
        """
        Generate a random polynomial of specified degree with coefficients in the finite field.
        
        Args:
            degree (int): Degree of the polynomial to generate
            
        Returns:
            List[int]: Coefficients of the random polynomial
        """
        # Use cryptographically secure random numbers
        return [secrets.randbelow(self.field_size) or 1 for _ in range(degree + 1)]
    
    def polynomial_multiplication(self, poly1: List[int], poly2: List[int]) -> List[int]:
        """
        Multiply two polynomials in the finite field.
        
        Args:
            poly1 (List[int]): First polynomial coefficients
            poly2 (List[int]): Second polynomial coefficients
            
        Returns:
            List[int]: Coefficients of the product polynomial
        """
        result = [0] * (len(poly1) + len(poly2) - 1)
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                result[i + j] = (result[i + j] + poly1[i] * poly2[j]) % self.field_size
        return result
    
    def evaluate_polynomial(self, poly: List[int], x: int) -> int:
        """
        Evaluate polynomial at point x in the finite field using Horner's method.
        
        Args:
            poly (List[int]): Polynomial coefficients
            x (int): Point at which to evaluate
            
        Returns:
            int: Result of polynomial evaluation
        """
        result = 0
        for coef in reversed(poly):
            result = (result * x + coef) % self.field_size
        return result
    
    def generate_keypair(self) -> Tuple[Tuple[List[int], int], Tuple[List[int], List[int]]]:
        """
        Generate public and private keys.
        
        Returns:
            Tuple[Tuple[List[int], int], Tuple[List[int], List[int]]]: 
                ((public_poly, base), (poly1, poly2)) representing public and private keys
        """
        # Generate two random polynomials for private key
        poly1 = self.generate_random_polynomial(self.degree // 2)
        poly2 = self.generate_random_polynomial(self.degree // 2)
        
        # Generate base point using cryptographically secure random number
        base = secrets.randbelow(self.field_size-2) + 2  # Ensures base is between 2 and field_size-1
        
        # Create public polynomial through multiplication
        public_poly = self.polynomial_multiplication(poly1, poly2)
        
        return ((public_poly, base), (poly1, poly2))
    
    def validate_message(self, message: str) -> bool:
        """
        Validate that the message contains only supported characters.
        
        Args:
            message (str): Message to validate
            
        Returns:
            bool: True if message is valid, False otherwise
        """
        return all(ord(c) < self.field_size for c in message)
    
    def encrypt(self, message: str, public_key: Tuple[List[int], int]) -> List[int]:
        """
        Encrypt a message using the public key.
        
        Args:
            message (str): Message to encrypt
            public_key: Tuple of (public polynomial coefficients, base point)
            
        Returns:
            List[int]: Encrypted message values
            
        Raises:
            ValueError: If message contains unsupported characters
        """
        if not self.validate_message(message):
            raise ValueError("Message contains unsupported characters")
            
        public_poly, base = public_key
        # Convert message to numbers using direct ASCII values
        message_nums = [ord(c) for c in message]
        
        # Calculate encryption factor once
        encryption_factor = self.evaluate_polynomial(public_poly, base)
        
        # Encrypt each character
        cipher = []
        for m in message_nums:
            cipher_value = (m * encryption_factor) % self.field_size
            cipher.append(cipher_value)
            
        return cipher
    
    def decrypt(self, cipher: List[int], private_key: Tuple[List[int], List[int]], base: int) -> str:
        """
        Decrypt a message using the private key.
        
        Args:
            cipher (List[int]): Encrypted message values
            private_key: Tuple of (poly1 coefficients, poly2 coefficients)
            base (int): Base point used in encryption
            
        Returns:
            str: Decrypted message
        """
        poly1, poly2 = private_key
        
        # Calculate decryption factor once
        factor1 = self.evaluate_polynomial(poly1, base)
        factor2 = self.evaluate_polynomial(poly2, base)
        decryption_factor = pow(factor1 * factor2, -1, self.field_size)
        
        # Decrypt each character
        message = ""
        for c in cipher:
            # Recover the original ASCII value
            m = (c * decryption_factor) % self.field_size
            message += chr(m)
            
        return message

