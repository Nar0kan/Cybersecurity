from string import ascii_letters

class MonoalphabetEncryptor:
    def __init__(self, alphabet: str=ascii_letters, offset: int=20, message: str='Hello') -> None:
        self.alphabet = alphabet
        self.offset = offset
        self.message = message
    

    def encrypt(self) -> str:
        return 'Encrypt function'
    

    def decrypt(self) -> str:
        return 'Decrypt function'