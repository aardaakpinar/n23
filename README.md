# N²³ Cryptography 🔐

**N²³** is a custom cryptography experiment.  
It uses a unique key-based shifting mechanism combined with **square (n²)** and **cube (n³)** transformations.

This project includes:
- Explanation of how N²³ works
- A Bootstrap-based demo site
- An interactive playground (encrypt & decrypt your own text)

---

## 🚀 Live Demo
👉 [Demo Page](https://aardaakpinar.github.io/n23/)

---

## ⚡ How It Works

### Encryption
1. Take the **first character** of each word → this is the **key**.
2. Convert the key to its Unicode code point value.
3. For the rest of the word:
   - **Letters (A–Z, a–z, Unicode letters):**
     - Shift by key value
     - Square the result → `n²`
   - **Digits (0–9):**
     - Shift by key value (mod 10)
     - Cube the result → `n³`
   - **Others (punctuation, symbols, spaces):**
     - Remain unchanged
     
### Decryption
1. Take square root (√) or cube root (∛) of the encrypted numbers.
2. Reverse the key-based shift.
3. Reconstruct the original text.

---

## 🛠️ Example

**Input:**  
```

Hello 123

```

**Encrypted Output (example):**  
```

H 29929 30976 31329 31329 32400  1 1728 2744

```

**Decrypted Back:**  
```

Hello 123

```

---

## 🧪 Try It Yourself

The demo page includes:

* A text area to enter plain/encrypted text
* **Encrypt** button → converts plain text to encrypted form
* **Decrypt** button → restores the original message

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
It is **not a secure cryptographic algorithm** and should not be used for real-world security.

---

## 📜 License

GNU General Public License v3.0 License © 2025
