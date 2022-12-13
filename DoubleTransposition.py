class Double_transportational_cipher:
    def __init__(self, alphabet: str, message: str, key_1: str, key_2):
        self.alphabet = alphabet
        self.message = message
        
        self.k1 = key_1
        self.k2 = key_2

        self.translate_keys()
    

    def translate_keys(self):
        """Сформувати пару позиція - ключ."""
        self.x = {int(val): num for num, val in enumerate(self.k1)}
        self.y = {int(val): num for num, val in enumerate(self.k2)}

        while len(self.message) != len(self.x) * len(self.y):
            self.message += '_'
    

    def separate_lenght(self, line, length):
        return [line[i:i + length] for i in range(0, len(line), length)]


    def encrypt(self):
        """Зашифрувати повідомлення методом подвійної перестановки."""
        self.encrypted_message = ''
        self.ciphertext_x = ''
        self.ciphertext_y = ''
        count = 0

        for index in sorted(self.x.keys()):
            for part in self.separate_lenght(self.message, len(self.x)):
                self.ciphertext_x += part[self.x[index]]
        
        for index in sorted(self.y.keys()):
            for path in self.separate_lenght(self.ciphertext_x, len(self.y)):
                self.ciphertext_y += path[self.y[index]]
        
        while count != (len(self.x)):
            for block in self.separate_lenght(self.ciphertext_y, len(self.x)):
                self.encrypted_message += block[count]
            count += 1
        
        return self.encrypted_message[:len(self.message)]


    def decrypt(self):
        """Розшифрувати зашифроване повідомлення методои подвійної перестановки."""
        self.decrypted_message = ''

        for y in self.y:
            for x in self.x:
                self.decrypted_message += self.separate_lenght(self.ciphertext_y, len(self.x))[y - 1][x - 1]
        
        return self.decrypted_message[:len(self.message)]


def main():
    """Головна функція, що запускається при старті файлу."""

    message = 'Я, КІРІЧЕНКО НІКІТА ІЛЛІЧ, СТУДЕНТ УНІВЕРСИТЕТУ'
    alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,.'

    key_1 = (4, 1, 3, 2, 5, 6)
    key_2 = (3, 1, 4, 2, 6, 9, 7, 11, 8, 10, 5)

    data = Double_transportational_cipher(alphabet, message, key_1, key_2)

    print('Зашифроване повідомлення: ' + data.encrypt())
    print('Розшифроване повідомлення: ' + data.decrypt())


if __name__ == "__main__":
    main()