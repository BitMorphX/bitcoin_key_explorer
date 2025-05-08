# 🔍 Bitcoin Key Explorer

## 🧠 Description

**bitcoin_key_explorer.py** is a Python-based tool that allows you to:
- generate a private key from an integer,
- convert it to WIF (compressed & uncompressed),
- output public keys (HEX),
- generate Bitcoin addresses,
- and decode any Base58 Bitcoin address.

Designed for learning, analysis, and understanding how Bitcoin keys are derived from raw numbers.

---

## 📦 Features

- ✅ Converts integer to private key (HEX)
- 🔐 Generates WIF format (compressed & uncompressed)
- 🔎 Public keys (HEX): compressed & uncompressed
- 🏷️ Generates Bitcoin addresses (Base58Check)
- 🧮 Base58 decoder: shows version, payload and checksum
- 🌈 Colored CLI output (white, yellow, green, cyan, red)
- 🧹 Clears terminal on startup (Linux + Windows compatible)

---

## 🛠️ Usage

```bash
python3 bitcoin_key_explorer.py
```

You will be prompted to:

1. Enter any integer (used as a private key), for example:
   ```
   Enter an integer (used as a private key): 12345
   ```

2. View output including:
   - Private key in HEX
   - WIF (compressed & uncompressed)
   - Public keys (compressed & uncompressed)
   - Bitcoin addresses (Base58Check)

3. Optionally decode a Base58 Bitcoin address:
   ```
   Enter a Bitcoin address (or press Enter to skip):
   ```

Which will show:
   - Version byte
   - RIPEMD-160 payload
   - Checksum

---

## 📋 Requirements

```bash
pip install base58 ecdsa termcolor pycryptodome
```

---

## 📄 License

MIT License. Free to use for educational and research purposes.

---

## ⚠️ Disclaimer

This tool is **not intended for use with real cryptocurrencies**.  
Use at your own risk. The author assumes no liability for misuse or losses.

---


## 💰 Donations

**Bitcoin (BTC)**  
1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7

**Monero (XMR)**  
86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu

**Dash (DASH)**  
XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX

**Bytecoin (BCN)**  
bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR

🙏 Thank you for supporting independent projects and open education.


## 👤 Author

*“From the number comes the key – from the key comes the structure.”*  
— **BitMorphX**
