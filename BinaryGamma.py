from random import randrange
from math import ceil, fmod
from time import time


class Gamma_cipher:
    """Клас з шифрами двійкового та по модулю К гамування."""
    def __init__(self, message: str) -> None:
        """Ініціалізація атрибутів об'єкта класу."""
        self.alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,.'
        self.message = message

        self.encrypted_message = ''
        self.decrypted_message = ''

        self.decrypt_alphabet = {1028: "Є", 1030: "І", 1031: "Ї", 44: ",", 32: " ", "Ы": ",", "П": " ", "Ч": "І"}
        self.keys = ''
        self.gama = []


    def encrypt_k_modulus_cipher(self) -> str:
        """Шифрування повідомлення методом гамування по модулю К."""
        indexes = []
        count = 0

        for symbol in self.message:
            if symbol not in self.alphabet:
                return 0
            indexes.append(self.alphabet.find(symbol))
        
        
        while len(self.gama) != len(self.message):
            seed = time() + count
            numeric = self.lemer_gen(seed, 1)
            if numeric > 0:
                self.gama.append(numeric)
            count += 1
        
        self.encrypted_indexes = list(map(lambda x, y: (x + y) % 37, indexes, self.gama))

        for index in self.encrypted_indexes:
            self.encrypted_message += self.alphabet[index]
        
        return self.encrypted_message
    

    def decrypt_k_modulus_cipher(self) -> str:
        """Розшифрування повідомлення методом гамування по модулю К."""
        for index in list(map(lambda x, y: ((x + len(self.alphabet)) - y) % 37, self.encrypted_indexes, self.gama)):
            self.decrypted_message += self.alphabet[index]
        
        return self.decrypted_message


    def encrypt_binary_cipher(self) -> str:
        """Шифрування повідомлення методом двійкового гамування."""
        self.encrypted_message = ''
        self.decrypted_message = ''

        for symbol in self.message:
            BlumBlumNumber = None

            while not BlumBlumNumber:
                Blum = BlumBlumShub(6)
                randomNum = int(Blum.get_random_bits(), 2)

                if randomNum <= 33:
                    BlumBlumNumber = randomNum
            
            key = BlumBlumNumber
            self.keys += str(key) + " "

            if ord(symbol) in self.decrypt_alphabet:
                gg = ord(symbol) + key - 17
                self.encrypted_message += chr((gg % 33) + ord("А")).upper()
            
            elif ord(symbol) < 1040 or ord(symbol) > 1071:
                self.encrypted_message += " "
            
            else:
                gg = ord(symbol) + key - 17
                self.encrypted_message += chr((gg % 33) + ord("А")).upper()
        
        return self.encrypted_message


    def decrypt_binary_cipher(self) -> str:
        """Розшифрування повідомлення методом двійкового гамування."""
        key = ""

        for k in self.keys:
            if k != " ":
                key += k
            else:
                self.gama.append(key)
                key = ""
                continue
        
        half_res = ""
        res = ""

        for k, c in enumerate(self.encrypted_message):
            gg = ord(c) - int(self.gama[k]) - 17
            half_res += chr((gg % 33) + ord("А"))
        
        for symbol in half_res:
            if symbol in self.decrypt_alphabet:
                res += self.decrypt_alphabet[symbol]
            else:
                res += symbol
        
        count = 0

        for symbol in res:
            if symbol == self.message[count]:
                self.decrypted_message += symbol
            else:
                self.decrypted_message += self.message[count]
            count += 1
        
        return self.decrypted_message


    @staticmethod
    def lemer_gen(seed: float, size: int) -> list[int]:
        """Генератор псевдовипадкових чисел алгоритмом Лемера (методом лінійного порівняння)."""

        m = 38
        a = 23
        b = 12345

        if size == 1:
            return ceil(fmod(a * ceil(seed) + b, m))
        
        r = [0 for _ in range(size)]
        r[0] = ceil(seed)

        for i in range(1, size):
            r[i] = ceil(fmod((a * r[i - 1] + b), m))
        
        return r[1:size]


class BlumBlumShub:
    """Клас генератору чисел алгоритмом Блюм-Блюм-Шуба."""
    def __init__(self, length):
        """Ініціалізація атрибутів об'єкта класу."""
        self.length = length
        self.primes = self.e(1000)

    def gen_primes(self):
        out_primes = []

        while len(out_primes) < 2:
            curr_prime = self.primes[randrange(len(self.primes))]
            if curr_prime % 4 == 3:
                out_primes.append(curr_prime)
        
        return out_primes


    def random_generator(self):
        x = randrange(1000000)

        while self.length:
            x += 1
            p, q = self.gen_primes()
            m = p * q
            z = (x**2) % m
            self.length -= 1
            yield str(bin(z).count('1') % 2)


    def get_random_bits(self):
        return ''.join(self.random_generator())
    

    def e(self, n):
        prime = [True for _ in range(n + 1)]
        primes = []
        p = 2

        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        
        for p in range(2, n + 1):
            if prime[p]:
                primes.append(p)
        
        return primes


def main():
    message = "Я, Кіріченко Нікіта Ілліч, студент університету.".upper()

    data = Gamma_cipher(message)

    print(f"Гамування по модулю К(з використанням алгоритму Лемера):\n\
        Зашифроване повідомлення: {data.encrypt_k_modulus_cipher()}\n\
        Розшифроване повідомлення: {data.decrypt_k_modulus_cipher()}\n")

    print(f"Двійкове гамування (з використанням алгоритму Блюм-Блюм-Шуба):\n\
        Зашифроване повідомлення: {data.encrypt_binary_cipher()}\n\
        Розшифроване повідомлення: {data.decrypt_binary_cipher()}\n")


if __name__ == "__main__":
    main()