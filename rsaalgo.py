# Encryption alphabet
alphabet_e = {chr(i): str(i).zfill(3) for i in range(128)}

# Decryption alphabet
alphabet_d = {n: c for c, n in alphabet_e.items()}

# Euclidian Algorithm: Find GCD of two numbers
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


# Generate encryption keys, e, and d
def generate_keys(p, q):

    # Part of public key
    n = p * q

    # Part of private key
    N0 = (p-1) * (q-1)

    # Part of public key
    # Find e: first integer relatively prime to N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break
    
    # Part of private key
    # Find d: multiplicative inverse of e % N0
    for i in range(0, N0):
        if ((e * i) % N0) == 1:
            d = i
            break

    return n, e, d


# Encrypt character
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(3)


# Decrypt character
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(3)


# Split word into characters
def split(word):
    return [char for char in word]


# Encrypt message
def encrypt_message(msg, N, e):

    # Messages
    plaintext = msg.split()
    encrypted = []

    # Exncrypt message
    for word in plaintext:

        # Split word into characters
        chars = split(word)
        # Create list of encrypted characters
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]

        # Add encrypted word to list
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Join encrypted words with space characters
    encrypted  = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)

    return encrypted


# Decrypt message
def decrypt_message(msg, N, d):

    # Messages
    encrypted = msg.split()
    decrypted = []
    plaintext = []

    # Decrypt
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Decipher message
    for char in decrypted:

        plaintext.append(alphabet_d[char])
    
    plaintext = "".join(plaintext)

    return plaintext

# Option Menu
def options():
    print("Options:\n\
        0 - Generate Key Pair\n\n\
        1 - Encrypt message from file\n\
        2 - Decrypt message from file\n\
        3 - Encrypt message in terminal\n\
        4 - Decrypt message in terminal\n")


# User interface
while True:

    # Show options
    options()

    # Get selection from user
    selection = input()

    # Generate key pair
    if selection == "0":

        # Get prime numbers
        p = int(input("Enter the first prime number: "))
        q = int(input("Enter the second prime number: "))
        print()

        try:
            # Generate values for encryption / decryption
            N, e, d = generate_keys(p, q)
            
            # Show keys
            print(f"Public key:\nN: {N}\ne: {e}\n")
            print(f"Private key:\nN: {N}\nd: {d}\n")

        except:
            print("Error: Invalid Primes\n")

    # Encrypt message from file
    elif selection == "1":

        # Get public key
        N = int(input("Enter public key N: "))
        e = int(input("Enter public key e: "))
        print()

        input_file = input("Enter file name to encrypt (default is 'data/input.txt') or press enter to use default:\n")

        if input_file == "":
            input_file = "data/input.txt"

        with open(input_file, "r") as fin:
            message = fin.read()

        # Write encrypted message
        with open("data/encrypted.txt", "w") as fout:
            fout.write(encrypt_message(message, N, e))
        
        # Success message
        print("File encrypted! Encrypted message saved to 'data/encrypted.txt'\n")

    # Decrypt message from file
    elif selection == "2":

        # Get private key
        N = int(input("Enter private key N: "))
        d = int(input("Enter private key d: "))
        print()

        input_file = input("Enter file name to decrypt (default is 'data/encrypted.txt') or press enter to use default:\n")
        if input_file == "":
            input_file = "data/encrypted.txt"
        with open(input_file, "r") as fin:
            message = fin.read()

        # Write encrypted message

        with open("data/decrypted.txt", "w") as fout:
            fout.write(decrypt_message(message, N, d))

        print("Decrypted message saved to 'data/decrypted.txt'\n")

        print("File decrypted!\n")

    # Encrypt message in terminal
    elif selection == "3":
        
        # Get public key
        N = int(input("Enter public key N: "))
        e = int(input("Enter public key e: "))
        print()

        # Get message from user
        message = input("Enter message to encrypt:\n")

        # Print encrypted message
        print(f"\nEncrypted message:\n{encrypt_message(message, N, e)}\n")

    # Decrypt message in terminal
    elif selection == "4":

        # Get private key
        N = int(input("Enter private key N: "))
        d = int(input("Enter private key d: "))
        print()

        # Get encrypted message from user
        message = input("Enter message to decrypt:\n")

        # Print decrypted message
        try:
            print(f"\nDecrypted message:\n{decrypt_message(message, N, d)}\n")
        except:
            print("Error: Invalid Private Key\n")

    # Input validation
    else:
        print("Invalid choice\n")

    # Option to exit
    exit = input("Make another selection?\n\
        'Y' to continue\n\
        any other key to exit\n").upper()

    print()

    # Make another selection
    if exit == "Y":
        continue
    
    # Exit
    else:
        break