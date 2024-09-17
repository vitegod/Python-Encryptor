# Python-Encryptor
A Python-based AES encryption/decryption application with a user-friendly Tkinter GUI. Allows users to encrypt and decrypt messages, generate random keys, and save keys for future use.

# Python Encryptor

This is a simple Python application that provides AES encryption and decryption capabilities through an intuitive graphical user interface built with Tkinter.

## Features

* **Encrypt and Decrypt:** Securely encrypt and decrypt messages using the AES algorithm.
* **Key Management:** 
    * Generate strong random keys.
    * Option to enter your own keys.
    * Save keys for convenient reuse.
* **User-Friendly Interface:** Easy-to-use Tkinter GUI for seamless interaction.

## Requirements

* Python 3.x
* PyCryptodome (`pip install pycryptodome`)

## How to Use

1. **Clone the repository:**

  ```bash
  git clone

2. **Install dependencies:**

  ```bash
  pip install -r requirements.txt

3. **Run the application:**

  ```bash
  python main.py

4. **Building into an Executable:**
  ```bash
  pip install pyinstaller
  pyinstaller --onefile --windowed main.py
