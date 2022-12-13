class Hash_function():
    """Клас для функцій гешування."""
    def __init__(self, message: str) -> None:
        """Ініціалізація атрибутів класу."""
        self.message = message
        self.__hash_message = ''
    

    @staticmethod
    def chunkify(a, b):
            return [a[i:i + b] for i in range(0, len(a), b)]


    @staticmethod
    def rol(a, b):
        return ((a << b) | (a >> (32 - b))) & 0xffffffff


    def update(self, new_message: str) -> None:
        """Оновити дані для повідомлення."""
        if not self.__hash_message:
            self.message = self.message + new_message
        else:
            print("Неможливо оновити дані вже хешованого повідомлення!")
    

    def check_sha1(self, message) -> bool:
        """Перевірити повідомлення на співпадіння з загешованим повідомленням."""
        return "Повідомлення збігається!" if message == self.__hash_message else "Помилка доступу!"


    def sha1(self, salt: str="") -> str:
        """Створити геш-послідовність у вигляді рядку з ініціалізованого \
        повідомлення та можливим застосуванням 'солі'."""
        if salt: self.salt = salt; self.message += self.salt

        self.bytes = ''
        h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
        self.bytes += ''.join(['{0:08b}'.format(ord(self.message[i])) for i in range(len(self.message))])
        bits = self.bytes + "1"
        t_bits = bits

        while len(t_bits) % 512 != 448:
            t_bits += "0"
        t_bits += '{0:064b}'.format(len(bits) - 1)

        for c in Hash_function.chunkify(t_bits, 512):
            words = Hash_function.chunkify(c, 32)
            w = [0] * 80

            for i in range(0, 16):
                w[i] = int(words[i], 2)
            
            for i in range(16, 80):
                w[i] = Hash_function.rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

            a, b, c, d, e = h0, h1, h2, h3, h4

            for i in range(0, 80):

                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = Hash_function.rol(a, 5) + f + e + k + w[i] & 0xffffffff

                e, d, b, a = d, c, a, temp
                c = Hash_function.rol(b, 30)

            h0 = h0 + a & 0xffffffff
            h1 = h1 + b & 0xffffffff
            h2 = h2 + c & 0xffffffff
            h3 = h3 + d & 0xffffffff
            h4 = h4 + e & 0xffffffff

        self.__hash_message = str('%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4))
        return self.__hash_message


def main():
    """Головна функція."""
    initial_message = "Я, Кіріченко Нікіта Ілліч"
    data = Hash_function(initial_message)
    print("Повідомлення: ", initial_message)
    
    data.update(", студент університету.")
    print("Оновлене повідомлення: ", data.message)

    hash_message = data.sha1()
    print("Хеш повідомлення: ", hash_message)

    check_message = "Я, Кіріченко Нікіта Ілліч"
    data_2 = Hash_function(check_message)
    print("Повідомлення для перевірки: ", data_2.sha1())
    print(data.check_sha1(data_2._Hash_function__hash_message))


if __name__ == "__main__":
    main()