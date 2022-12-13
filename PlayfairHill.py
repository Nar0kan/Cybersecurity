import numpy as np
from numpy import linalg as LA


class Poligram_cipher:
    """Клас для полігамного шифрування, що містить шифр Playfair і шифр Хілла."""
    def __init__(self, message: str, keys: tuple()) -> None:
        self.alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,."
        self.message = message
        self.__init_keys = keys
        self.make_keys_matrix()


    def playfair_encrypt(self) -> str: # битмейкер
        """Шифрування методом Playfair."""
        
        self.__init_message = self.message
        key = self.keys[0]
        message = list(self.message)

        for k in range(0, len(message), 2):
            x1, x2, y1, y2 = -1, -1, -1, -1
            for i in range(6):
                for j in range(6):
                    if x1 == -1:
                        if message[k] == key[i][j]:
                            x1 = i   
                            y1 = j
                    if x2 == -1:
                        if message[k+1] == key[i][j]:
                            x2 = i
                            y2 = j
            if x1 == x2:
                if y1 == 5:
                    y1 = 0
                    y2 += 1
                elif y2 == 5:
                    y1 += 1
                    y2 = 0
                else:
                    y1 += 1
                    y2 += 1
            elif y1 == y2:
                if  x1 == 5 and x2 == 5:
                    x1 = 0   
                    x2 = 0
                elif x1 == 5:
                    x1 = 0
                    x2 += 1
                elif x2 == 5:
                    x2 = 0
                    x1 += 1
                else:
                    x2 += 1
                    x1 += 1
            else:
                temp = 0
                temp = y1
                y1 = y2
                y2 = temp
            message += key[x1][y1]
            message += key[x2][y2]
        self.message = ''.join(message[int(len(message)/2):])
        print("Зашифроване повідомлення: {0}".format(self.message))
        return self.message


    def playfair_decrypt(self) -> str:
        """Дешифрування методом Playfair."""

        i = 0
        key = self.keys[0]
        message = ''

        # Знайти місцезнаходження кожного символу
        def locindex(key, c):
            for i in range(6):
                for j in range(6):
                    if key[i][j] == c:
                        return [i, j]
            return [-1, -1]
            
        while i < len(self.message):
            loc = locindex(key, self.message[i])
            loc1 = locindex(key, self.message[i+1])

            if loc[1] == loc1[1]:
                message += key[(loc[0]-1)%6][loc[1]]
                message += key[(loc1[0]-1)%6][loc1[1]]
            elif loc[0]==loc1[0]:
                message += key[loc[0]][(loc[1]-1)%6]
                message += key[loc1[0]][(loc1[1]-1)%6]
            else:
                message += key[loc[0]][loc1[1]]
                message += key[loc1[0]][loc[1]]
            i = i + 2
        print("Розшифроване повідомлення: {0}".format(message))
        return message


    def hill_encrypt(self) -> str: 
        """Шифрування методом Хілла."""

        self.key = self.keys[1] # багатоукладність
        self.text_numbers = []
        self.key_code = []
        self.result = []
        encrypted_message = ''

        # Заповнення списку відповідними індексами повідомлення
        for symbol in self.message:
            if symbol in self.alphabet:
                self.text_numbers.append(self.alphabet.find(symbol))
            else:
                print(f'Не допустимий символ для шифрування - {symbol}')
                return 0
        for symbol in self.key:
            if symbol in self.alphabet:
                self.key_code.append(self.alphabet.find(symbol))
        
        # Створення ключової матриці
        self.key_matrix = np.array(self.chunkify(self.key_code, 4))
        self.text_matrix = self.chunkify(self.text_numbers, 4)

        for text_block in self.text_matrix:
            self.result.append((np.array(text_block).dot(self.key_matrix))%37)
        
        for block in self.result:
            for number in block:
                encrypted_message += self.alphabet[number]
        
        print('Зашифроване повідомлення: {0}'.format(encrypted_message))
        self.encrypted_message = encrypted_message
        return encrypted_message

    
    def hill_decrypt(self) -> str:
        """Розшифрування методом Хілла."""

        self.text_numbers.clear()
        for symbol in self.encrypted_message:
            if symbol in self.alphabet:
                self.text_numbers.append(self.alphabet.find(symbol))
        text_matrix = self.chunkify(self.text_numbers, 4)

        # Детермінант матриці ключа
        det_matrix_key = int(LA.det(self.key_matrix))
        determinant = self.evklid_alg(det_matrix_key, len(self.alphabet))

        # Обрахунок оберненого детермінанту елементу
        key_matrix_inverse_determinant = self.get_inverse_determinant_element(det_matrix_key, determinant[1])
        temp_result = []
        alliance_matrix = np.array(self.chunkify(self.make_algebraic_additions(self.key_matrix), 4))
        for i in alliance_matrix:
            for j in i:
                if j < 0:
                    j = abs(j)%37
                    temp_result.append(-j)
                else:
                    j = j%37
                    temp_result.append(j)
        
        temp_result = np.array(self.chunkify(temp_result, 4))
        result = []

        for i in temp_result:
            for j in i:
                if j < 0:
                    j = (abs(j) * key_matrix_inverse_determinant)%37
                    result.append(-j)
                else:
                    j = (j * key_matrix_inverse_determinant)%37
                    result.append(j)
        
        inverse_module_to_the_key_matrix = []
        result = np.array(self.chunkify(result, 4))
        result_transpose = result.transpose()
        
        for i in result_transpose:
            for j in i:
                if j < 0:
                    j = 37 + j
                    inverse_module_to_the_key_matrix.append(j)
                else:
                    inverse_module_to_the_key_matrix.append(j)
        inverse_module_to_the_key_matrix = np.array(self.chunkify(inverse_module_to_the_key_matrix, 4))

        message_decryption = []
        for i in text_matrix:
            message_decryption.append((np.array(i).dot(inverse_module_to_the_key_matrix))%37)
        message_decryption = [x for l in message_decryption for x in l]

        decrypted_message = ''
        for number in message_decryption:
            decrypted_message += self.alphabet[number]
        
        print('Розшифроване повідомлення:', decrypted_message)
        return decrypted_message
        

    @staticmethod
    def is_number_prime(number: int=0) -> bool:
        """Перевірка числа на простоту."""
        return False if any([True for iter in range(2, number) if number%iter == 0]) else True
    

    @classmethod
    def make_int(self, number: float) -> int:
        """Округлення числа"""
        number = int(number + (0.5 if number > 0 else -0.5))
        return number
    

    @classmethod
    def evklid_alg(self, a, b) -> set:
        """Розширений алгоритм Евкліда"""

        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.evklid_alg(b, a%b)
            return d, y, x - y * (a // b)
    

    @classmethod
    def make_keys_matrix(self) -> None:
        """Функція, що виводить в змінну self.keys відповідні значення позицій кожного символу (з self.init_keys) у алфавіті."""
        
        pf_alphabet = [
                ['Б', 'И', 'Т', 'М', 'Е', 'Й'], 
                ['К', 'Р', 'А', 'В', 'Г', 'Ґ'], 
                ['Д', 'Є', 'Ж', 'З', 'І', 'Ї'], 
                ['Л', 'Н', 'О', 'П', 'С', 'У'], 
                ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ'], 
                ['Ь', 'Ю', 'Я', ' ', ',', '.']
            ]
        
        self.keys = (pf_alphabet, "БАГАТОУКЛАДНІСТЬ")
    

    @classmethod
    def chunkify(self, items, chunk_size) -> list:
        """Блоки по 4 символи"""

        matrix = []
        for i in range(0, len(items), chunk_size):
            matrix.append(items[i:i + chunk_size])
        while len(matrix[-1]) != 4:
            matrix[-1].append(33)
        return matrix


    @classmethod
    def get_inverse_determinant_element(self, determinant, x) -> int:
        """Обернений детермінанту елемент"""

        if determinant < 0 and x > 0:
            return x
        elif determinant > 0 and x < 0:
            return 37 + x
        elif determinant > 0 and x > 0:
            return x
        elif determinant < 0 and x < 0:
            return -x


    @classmethod
    def make_algebraic_additions(self, key_matrix) -> list:
        """Алгебраїчні доповнення"""

        result = []
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                Mi = np.delete(key_matrix, [i], axis=0)
                Mij = np.delete(Mi, [j], 1)
                if (i + j) % 2 == 0:
                    result.append((self.make_int(LA.det(Mij))))
                else:
                    result.append(-(self.make_int(LA.det(Mij))))
        return result


def main() -> None:
    initial_message = str(input("Введіть повідомлення для шифрування: ")).upper()
    initial_keys = ("БИТМЕЙКЕР", "БАГАТОУКЛАДНІСТЬ")

    if not initial_message:
        initial_message = "Я, КІРІЧЕНКО НІКІТА ІЛЛІЧ, СТУДЕНТ УНІВЕРСИТЕТУ."
    
    data = Poligram_cipher(message=initial_message, keys=initial_keys)

    print(" \nШифрування Playfair: ")
    data.message = data.playfair_encrypt()
    print(" \nРозшифрування Playfair: ")
    data.message = data.playfair_decrypt()
    
    print(" \nШифрування Хілл: ")
    data.message = data.hill_encrypt()
    print(" \nРозшифрування Хілл: ")
    data.message = data.hill_decrypt()


if __name__ == "__main__":
    main()