class Column_cipher:
    """Клас для шифрування методом вертикальної перестановки."""
    def __init__(self, key: str, message: str) -> None:
        """Ініціалізація аргументів."""
        self.key = key
        self.message = message

        self.lenght = float(len(self.message))
        self.message_list = list(self.message)

        self.key_list = sorted(list(self.key))
        self.columns = len(self.key)


    def encrypt(self):
        """Зашифрувати повідомлення методом вертикальної перестановки."""
        self.encrypted_message = ""
        count_index, temp_matrix = 0, []

        from math import ceil as round_to_bigger
        row = int(round_to_bigger(self.lenght/self.columns))
        fill_null = int((row * self.columns) - self.lenght)
        self.message_list.extend('_' * fill_null)

        for i in range(0, len(self.message_list), self.columns):
            temp_matrix.append(self.message_list[i: i + self.columns])

        for i in range(self.columns):
            current_index = self.key.index(self.key_list[count_index])
            for row in temp_matrix:
                self.encrypted_message += ''.join(row[current_index])
            count_index += 1

        return self.encrypted_message


    def decrypt(self):
        """Розшфрувати повідомлення методом вертикальної перестановки."""
        count_index = 0
        message_index = 0
        self.message_list = list(self.encrypted_message)

        from math import ceil as round_to_bigger
        row = int(round_to_bigger(self.lenght/self.columns))

        key_lst = sorted(list(self.key))

        temp_cipher = []
        for i in range(row):
            temp_cipher += [[None] * self.columns]

        for i in range(self.columns):
            current_index = self.key.index(key_lst[count_index])
    
            for j in range(row):
                temp_cipher[j][current_index] = self.message_list[message_index]
                message_index += 1
            count_index += 1

        try:
            self.decrypted_message = ''.join(sum(temp_cipher, []))
        except TypeError:
            print("Ключ і повідомлення не може містити повторів у буквах.")
        
        null_count = self.decrypted_message.count('_')
    
        if null_count > 0:
            return self.decrypted_message[:-null_count]
        return self.decrypted_message


def main():
    """Головна функція."""
    key = "Я, Кіра".upper()
    message = "Я, Кіріченко Нікіта Ілліч, студент університету".upper()
    data = Column_cipher(key, message)

    print(f"Encrypted Message: {data.encrypt()}")
    print(f"Decryped Message: {data.decrypt()}")


if __name__ == "__main__":
    main()