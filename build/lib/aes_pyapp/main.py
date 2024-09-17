import base64
import os
import tkinter as tk
from tkinter import messagebox

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

KEY_FILE = "saved_key.txt"


def encrypt_message():
    try:
        key = key_entry.get().encode('utf-8')
        message = message_entry.get('1.0', 'end-1c').encode('utf-8')

        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')

        result = iv + ":" + ct
        result_entry.delete('1.0', tk.END)
        result_entry.insert('1.0', result)

        if key:
            with open(KEY_FILE, "wb") as f:
                f.write(key)

    except (ValueError, KeyError) as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")


def decrypt_message():
    try:
        key = key_entry.get().encode('utf-8')
        encrypted_message = result_entry.get('1.0', 'end-1c')

        iv, ct = encrypted_message.split(":")
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        result_entry.delete('1.0', tk.END)
        result_entry.insert('1.0', pt.decode('utf-8'))

        if key:
            with open(KEY_FILE, "wb") as f:
                f.write(key)

    except (ValueError, KeyError) as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")


def generate_random_key():
    key = get_random_bytes(16)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.hex())

    with open(KEY_FILE, "wb") as f:
        f.write(key)


def load_saved_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            key = f.read()
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key.hex())

# Create the main window
window = tk.Tk()
window.title("AES Encryption/Decryption")

key_label = tk.Label(window, text="Key:")
key_label.grid(row=0, column=0, padx=10, pady=10)

key_entry = tk.Entry(window, width=50, font=("Arial", 14))

key_entry.grid(row=0, column=1, padx=10, pady=10)
message_label = tk.Label(window, text="Message:")
message_label.grid(row=1, column=0, padx=10, pady=10)

message_entry = tk.Text(window, width=50, height=10)  # Adjust width and height as needed
message_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

result_label = tk.Label(window, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=10)

result_entry = tk.Text(window, width=50, height=10)  # Adjust width and height as needed
result_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=3, column=2, padx=10, pady=10)

generate_key_button = tk.Button(window, text="Generate Random Key", command=generate_random_key)
generate_key_button.grid(row=3, column=1, padx=10, pady=10)

load_saved_key()

window.mainloop()