# 🔐 Caesar Cipher Encryption & Decryption Tool

## 📌 Project Overview
This project was built as part of my **Week 2 Cybersecurity Internship at DecodeLabs**.  

The goal of this project was to implement a basic encryption and decryption system using the **Caesar Cipher** technique. The project focuses on understanding the fundamentals of cryptography, data confidentiality, and logical transformations in programming.

---

## 🚀 Features
- Encrypt plaintext messages  
- Decrypt encrypted messages  
- Supports:
  - Uppercase letters
  - Lowercase letters
  - Spaces and punctuation
- User-defined shift key
- ASCII-based encryption logic using:
  - `ord()`
  - `chr()`
- Modular arithmetic (`% 26`) for alphabet wrapping

---

## 🧠 How the Caesar Cipher Works

### Encryption Formula
E(x) = (x + n) % 26

### Decryption Formula
D(x) = (x - n) % 26

Where:
- `x` = letter position
- `n` = shift value/key

---

## 💻 Technologies Used
- Python 3

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/caesar-cipher-tool.git
cd caesar-cipher-tool
python main.py

## 📚What I Learned

Through this project I learned:

Core cryptography concepts
Encryption and decryption logic
ASCII character manipulation
Modular arithmetic
String handling in Python
Data confidentiality fundamentals

## 🔥 Future Improvements
GUI version using Tkinter
File encryption support
Randomized encryption keys
Vigenère Cipher implementation
Advanced encryption concepts


# This project was completed as part of the DecodeLabs Cybersecurity Internship Program.

# ⭐ Feel free to fork, improve, or star the repository!
