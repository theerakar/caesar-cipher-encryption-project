# 🔐 Caesar Cipher – Python Encryption Project

This project is a simple implementation of the **Caesar Cipher**, one of the oldest and most well-known encryption techniques. It demonstrates the core concept of **substitution ciphers**, where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

---

## 🧠 What Is Caesar Cipher?

The Caesar Cipher shifts each letter in the input text by a fixed number of positions (called the **key**). 

- For **encryption**, letters are shifted **forward**
- For **decryption**, letters are shifted **backward**
- Non-alphabetic characters (like numbers, spaces, and symbols) remain unchanged

**Example** (Key = 7):  
Plaintext : Hello World!
Encrypted : OLSSV DVYSK!

---

## 🚀 How to Use This Script

### ✅ Step 1: Run the script
Open your terminal and run the Python file:

```bash
python caesar_cipher.py
✅ Step 2: Enter your message and key
Follow the prompts:

bash
Copy
Edit
Enter your message: Hello World!
Enter the shift key (1-25): 7
Encrypted message: OLSSV DVYSK!

⚙️ Features
Encrypt and decrypt messages

Supports both uppercase and lowercase letters

Leaves non-alphabetic characters (spaces, punctuation) unchanged

Works fully in the terminal

No external libraries used (just core Python)

📁 Project Files
bash
Copy
Edit
caesar-cipher/
│
├── caesar_cipher.py    # Main Python script
└── README.md           # Project documentation

🛠️ Future Enhancements
Add brute-force mode (try all 25 shifts to crack a message)
Auto-detect English words in decrypted text to guess the key
Add a simple GUI using Tkinter
Log encryption/decryption history to a file

🧰 Tech Used
Python 3.13.5

No external libraries

📝 License
This project is licensed under the MIT License. Feel free to use and modify it.

⭐ Like this project?
Give it a ⭐ on GitHub or fork it to start experimenting with cryptography yourself!

---

Once added, commit it:

```bash
git add README.md
git commit -m "Add README for Caesar Cipher project"
git push
