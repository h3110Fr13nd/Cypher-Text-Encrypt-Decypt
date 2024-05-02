# RSA Algorithm Implementation in Python

This repository contains a Python implementation of the RSA algorithm for encryption and decryption. The script `rsaalgo.py` provides a simple command line interface for generating RSA keys, encrypting and decrypting messages.

## How to Use

The script provides a menu with the following options:

1. Generate Key Pair
2. Encrypt message from file
3. Decrypt message from file
4. Encrypt message in terminal
5. Decrypt message in terminal

### Generate Key Pair

This option will ask for two prime numbers and generate a pair of public and private keys. The public key consists of `N` and `e`, and the private key consists of `N` and `d`.

Example:

```
Enter the first prime number: 17
Enter the second prime number: 11
```

Output:

```
Public key:
N: 187
e: 7

Private key:
N: 187
d: 23
```

### Encrypt Message from File

This option will ask for a public key and a file name, then encrypt the content of the file and save it to `data/encrypted.txt`.

Example:

```
Enter public key N: 187
Enter public key e: 7
Enter file name to encrypt (default is 'data/input.txt') or press enter to use default:
```

### Decrypt Message from File

This option will ask for a private key and a file name, then decrypt the content of the file and save it to `data/decrypted.txt`.

Example:

```
Enter private key N: 187
Enter private key d: 23
Enter file name to decrypt (default is 'data/encrypted.txt') or press enter to use default:
```

### Encrypt Message in Terminal

This option will ask for a public key and a message, then encrypt the message and print it to the terminal.

Example:

```
Enter public key N: 187
Enter public key e: 7
Enter message to encrypt: Hello World
```

Output:

```
Encrypted message:
072 101 108 108 111 032 087 111 114 108 100
```

### Decrypt Message in Terminal

This option will ask for a private key and a message, then decrypt the message and print it to the terminal.

Example:

```
Enter private key N: 187
Enter private key d: 23
Enter message to decrypt: 072 101 108 108 111 032 087 111 114 108 100
```

Output:

```
Decrypted message:
Hello World
```

## Note

The script uses a simple ASCII-based encryption, so it can only handle ASCII characters (0-127). It is intended for educational purposes and not for serious cryptographic use.