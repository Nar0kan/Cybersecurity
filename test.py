def main():
    from string import ascii_letters
    initial_alphabet = ascii_letters
    initial_message = 'Hello, world!'

    method = str(input("""Select encryption method:\n
        1 - Caesar;\n
        2 - Linear;\n
        3 - Athena;\n
        Your choice: """))
    
    if method == "1":
        from Caesar import Caesar

        data = Caesar(alphabet=initial_alphabet, message=initial_message, offset=24)

        print("Encrypted message: ", data.encode())
        print("Decrypted message: ", data.decode())

    elif method == "2":
        from Linear import Linear

        data = Linear(alphabet=initial_alphabet, message=initial_message, offset=23)

        print("Encrypted message: ", data.encode())
        print("Decrypted message: ", data.decode())
    
    elif method == "3":
        from Athene import Athene

        data = Athene(message=initial_message, offset=(27, 7))

        print("Encrypted message: ", data.encode())
        print("Decrypted messageя: ", data.decode())


if __name__ == "__main__":
    main()