# 🔐 Image Encryption Tool (Python)

This project provides a simple tool to encrypt and decrypt image files using symmetric encryption with the cryptography library.

## 📦 Features

- AES-based encryption via Fernet (symmetric encryption)
- Key generation and secure storage
- Encrypt and decrypt any binary file (images, etc.)
- Simple command-line interface

---

## 🗂️ Project Structure

image-encryption/
├── encryptor.py          # Main script with menu and encryption logic
├── secret.key            # Generated encryption key (created at runtime)
├── sample_image.jpg      # (Optional) Image used for testing
├── sample_image.jpg.enc  # Encrypted version of the image
├── decrypted_image.jpg   # Decrypted output
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
