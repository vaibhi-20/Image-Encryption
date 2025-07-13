import os
from cryptography.fernet import Fernet

# ====== Generate Key ======
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to 'secret.key'")

# ====== Load Key ======
def load_key():
    if not os.path.exists("secret.key"):
        print("[-] Key file not found. Run 'generate_key()' first.")
        exit()
    return open("secret.key", "rb").read()

# ====== Encrypt Image ======
def encrypt_image(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"[+] Encrypted file saved as: {encrypted_path}")

# ====== Decrypt Image ======
def decrypt_image(enc_path, output_path):
    key = load_key()
    fernet = Fernet(key)

    with open(enc_path, "rb") as enc_file:
        encrypted_data = enc_file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("[-] Decryption failed:", e)
        return

    with open(output_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"[+] Decrypted file saved as: {output_path}")

# ====== Main Menu ======
def main():
    print("=== Image Encryptor Tool ===")
    print("1. Generate Key")
    print("2. Encrypt Image")
    print("3. Decrypt Image")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        path = input("Enter image file path to encrypt: ")
        if os.path.exists(path):
            encrypt_image(path)
        else:
            print("[-] File not found.")
    elif choice == "3":
        enc_path = input("Enter path of encrypted file: ")
        out_path = input("Enter output path for decrypted image: ")
        decrypt_image(enc_path, out_path)
    elif choice == "4":
        print("Goodbye!")
    else:
        print("[-] Invalid option.")

if __name__ == "__main__":
    main()