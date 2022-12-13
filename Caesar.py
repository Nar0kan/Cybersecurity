from encrypt import MonoalphabetEncryptor

class Caesar(MonoalphabetEncryptor):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
    

    def encode(self) -> str:
        self.__encrypted_message = ''

        for element in self.message:
            index = (self.alphabet.find(element)+self.offset)%len(self.alphabet)
            self.__encrypted_message += self.alphabet[index]
        
        return self.__encrypted_message
    

    def decode(self) -> str:
        self.__decrypted_message = ''

        for element in self.message:
            index = (self.alphabet.find(element) + len(self.alphabet) - self.offset)%len(self.alphabet)
            self.__decrypted_message += self.alphabet[index]
        
        return self.__decrypted_message


def main() -> None:
    return None


if __name__ == "__main__":
    main()