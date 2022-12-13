from random import sample, choice


class Single_trans:
    """Звичайний та блоковий одинарні шифри перестановки."""
    def __init__(self, alphabet: str, message: str) -> None:
        """Ініціалізація атрибутів."""
        self.alphabet = alphabet
        self.message = message

        self.key = {}
        self.res = []

        self.encrypted_message = ''
        self.decrypted_message = ''
    

    def simple_encrypt(self):
        """Зашифрувати повідомлення методом одинарної простої перестановки."""
        from random import sample
        indexes = sample(range(len(self.message)), len(self.message))

        while indexes == sorted(indexes):
            indexes = sample(range(len(self.message)), len(self.message))

        for i in indexes:
            self.key[i] = self.message[i]
        
        for i in self.key:
            self.encrypted_message += self.key[i]
        
        return self.encrypted_message
    

    def simple_decrypt(self):
        """Розшифрувати повідомлення методом одинарної простої перестановки."""
        count = 0

        while count != len(self.message):
            self.decrypted_message += self.key[count]
            count += 1
        
        return self.decrypted_message

    
    def chunkify(self, items, chunk_size):
        """Розбиття матриці."""
        matrix = []

        for i in range(0, len(items), chunk_size):
            matrix.append(items[i:i + chunk_size])
        
        while len(matrix[-1]) != chunk_size:
            matrix[-1].append(choice(self.alphabet))
        
        return matrix


    def block_encrypt(self):
        """Зашифрувати повідомлення методом одинарної блокової перестановки."""
        self.encrypted_message = ''
        chunk_size = 7

        self.new_message = self.chunkify(list(self.message), chunk_size)

        indexes = sample(range(len(self.new_message[0])), len(self.new_message[0]))

        while indexes == sorted(indexes):
            indexes = sample(range(len(self.new_message[0])), len(self.new_message[0]))
        
        for block in self.new_message:
            for index in indexes:
                self.key[index] = block[index]
                self.res.append(self.key)
                self.key = {}
                self.encrypted_message += block[index]
        
        return self.encrypted_message


    def block_decrypt(self):
        """Розшифрувати повідомлення методом одинарної блокової перестановки."""
        self.decrypted_message = ''

        for block in self.res:
            for key in sorted(block):
                self.decrypted_message += block[key]
        
        return self.decrypted_message[:len(self.message)]


def main():
    """Головна функція."""
    alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,.'
    initial_message = 'Я, КІРІЧЕНКО НІКІТА ІЛЛІЧ, СТУДЕНТ УНІВЕРСИТЕТУ'

    data = Single_trans(alphabet, initial_message)
    print("--__Звичайний метод перестановки__--")
    print("Зашифроване повідомлення: " + data.simple_encrypt())
    print("Розшифроване повідомлення: " + data.simple_decrypt())
    print("--__Блоковий метод перестановки__--")
    print("Зашифроване повідомлення: " + data.block_encrypt())
    print("Розшифроване повідомлення: " + data.block_decrypt())


if __name__ == "__main__":
    main()