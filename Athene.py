from encrypt import MonoalphabetEncryptor

class Athene(MonoalphabetEncryptor):
    def __init__(self, message: str, offset: int, alphabet: str):
        if alphabet:
            super().__init__(alphabet=alphabet, message=message, offset=offset)
        else:
            raise ValueError("Error. Please, check if values you've given are correct.")

    
    def encode(self) -> str:
        self.__encrypted_message = ''

        for element in self.message:
            index = (self.__alphabet.find(element)*self.__offset[0] + self.__offset[1])%len(self.__alphabet)
            self.__encrypted_message += self.__alphabet[index]
        
        return self.__encrypted_message
    

    def decode(self) -> str:
        self.__decrypted_message = ''

        alpLen = len(self.__alphabet)
        k = self.__offset[0]**(alpLen*(alpLen-1) - 1)
        t = (-k*self.offset[1])%alpLen

        for element in self.message:
            index = (self.__alphabet.find(element)*k + t)%alpLen
            self.__decrypted_message += self.__alphabet[index]
        
        return self.__decrypted_message


def main() -> None:
    return None


if __name__ == "__main__":
    main()