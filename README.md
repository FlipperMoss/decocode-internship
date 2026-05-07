# 🔐 Password Strength Checker

## 📌 Project Overview
This project is part of my **Week 1 Cybersecurity Internship at DecodeLabs**.  

The goal was to build a program that evaluates the strength of a password using fundamental **security validation techniques**. This project focuses on understanding how simple logic can help improve user security.

---

## 🚀 Features
- Checks password length  
- Detects:
  - Uppercase letters  
  - Numbers  
  - Symbols  
- Classifies password strength:
  - ❌ Weak  
  - ⚠️ Medium  
  - 💪 Strong  
- Provides feedback on how to improve weak passwords  

---

## 🧠 How It Works
The program uses:
- String handling  
- Conditional statements  
- A scoring system based on character variety  

### Strength Criteria:
- **Strong Password**
  - Length > 10  
  - Contains uppercase, number, and symbol  

- **Medium Password**
  - Length ≥ 6  
  - Contains at least 2 of the following:
    - Uppercase  
    - Number  
    - Symbol  

- **Weak Password**
  - Does not meet the above conditions  

---

## 💻 How to Run

1. Make sure you have Python installed  
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
