class Cardano_cipher:
    def __init__(self, phrase: str, keys: str):
        """Ініціалізація ключової фрази і ключа."""
        self.phrase = phrase
        self.keys = keys

        # Кількість ротацій
        from math import sqrt
        self.n = int(sqrt(len(self.phrase)))

        # Заповнення первинної матриці
        self.matrix = []
        for i in range(0, self.n):
            temp_matrix = []
            for j in range(0, self.n):
                temp_matrix.append('_')
            self.matrix.append(temp_matrix)
    

    def rotate_matrix_90(self) -> list:
        """Повернути матрицю на 90 градусів."""
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0])-1,-1,-1)]
    

    def rotate_matrix_180(self):
        for i in range(0, self.n):
            for j in range(i, self.n):
                t = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][i]
                self.matrix[j][i] = t
        for i in range(self.n):
            j = 0
            k = self.n-1
            while j < k:
                t = self.matrix[j][i]
                self.matrix[j][i] = self.matrix[k][i]
                self.matrix[k][i] = t
                j += 1
                k -= 1
        return self.matrix
#

    def iterate_phrase(self) -> list:
        """Ітерація для запису в матрицю значень з ключової фрази (зашифрування)."""
        global k
        for key in self.keys:
            
            if key < self.n:
                self.matrix[0][key] = self.phrase[k]
            elif key < self.n*2:
                self.matrix[1][key-self.n] = self.phrase[k]
            elif key < self.n*3:
                self.matrix[2][key-self.n*2] = self.phrase[k]
            elif key < self.n*4:
                self.matrix[3][key-self.n*3] = self.phrase[k]
            elif key < self.n*5:
                self.matrix[4][key-self.n*4] = self.phrase[k]
            elif key < self.n*6:
                self.matrix[5][key-self.n*5] = self.phrase[k]
            elif key < self.n*7:
                self.matrix[6][key-self.n*6] = self.phrase[k]
            else:
                self.matrix[7][key-self.n*7] = self.phrase[k]
            k+=1

        return self.matrix
    

    def encrypt(self) -> list:
        global k
        k = 0
        self.matrix = self.iterate_phrase()
        self.matrix = self.rotate_matrix_90()
        self.matrix = self.iterate_phrase()
        self.matrix = self.rotate_matrix_180()
        
        self.matrix = self.iterate_phrase()
        self.matrix = self.rotate_matrix_90()
        self.matrix = self.iterate_phrase()
        self.matrix = self.rotate_matrix_180()

        return self.matrix
        
            

    def decrypt(self) -> list:
        self.phrase = ''
        k = 0

        for i in range(4):
            for key in self.keys:
                if key < 8:
                    self.phrase += self.matrix[0][key]
                elif 8 <= key < 16:
                    self.phrase += self.matrix[1][key-8]
                elif 16 <= key < 24:
                    self.phrase += self.matrix[2][key-16]
                elif 24 <= key < 32:
                    self.phrase += self.matrix[3][key-24]
                elif 32 <= key < 40:
                    self.phrase += self.matrix[4][key-32]
                elif 40 <= key < 48:
                    self.phrase += self.matrix[5][key-40]
                elif 48 <= key < 56:
                    self.phrase += self.matrix[6][key-48]
                elif 56 <= key < 64:
                    self.phrase += self.matrix[7][key-56]
            self.matrix = self.rotate_matrix_90()
        self.matrix = self.matrix[::-1]
        return self.phrase
    

def main():
    phrase = "Я, Кіріченко Нікіта Ілліч, студент університету навчаюсь у Києві"
    keys = [3, 7, 11, 15, 16, 17, 21, 29, 35, 39, 43, 49, 51, 53, 55, 61]

    cipher_2 = Cardano_cipher(phrase, keys)
    
    print("Зашифроване повідомлення: \n", '\n'.join(["|".join(j) for j in cipher_2.encrypt()]))
    print("Розшифроване повідомлення: ", cipher_2.decrypt())

if __name__ == "__main__":
    main()