#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import base58
from ecdsa import SigningKey, SECP256k1
import binascii
import os
import platform
from termcolor import colored
from Crypto.Hash import RIPEMD160  # <-- pridėtas importas

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def print_colored(text, color="white"):
    try:
        print(colored(text, color))
    except:
        print(text)

def int_to_hex(number: int) -> str:
    return f"{number:064x}"

def hex_to_wif_private_key(hex_key: str, compressed: bool = True) -> str:
    prefix = b"\x80"
    key_bytes = binascii.unhexlify(hex_key)
    if compressed:
        key_bytes += b"\x01"
    payload = prefix + key_bytes
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return base58.b58encode(payload + checksum).decode()

def public_key_to_address(public_key: bytes, compressed: bool = True) -> str:
    if compressed:
        prefix = b"\x02" if public_key[-1] % 2 == 0 else b"\x03"
        public_key = prefix + public_key[:32]
    else:
        public_key = b"\x04" + public_key

    sha256_digest = hashlib.sha256(public_key).digest()
    ripemd160 = RIPEMD160.new(sha256_digest).digest()  # <-- naudota pycryptodome
    payload = b"\x00" + ripemd160
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    address = base58.b58encode(payload + checksum).decode()
    return address

def get_bitcoin_info_from_number(number: int):
    print_colored(f"Processing number: {number}\n", "cyan")

    private_key_hex = int_to_hex(number)
    print_colored(f"Private Key (HEX): {private_key_hex}", "yellow")

    wif_compressed = hex_to_wif_private_key(private_key_hex, compressed=True)
    wif_uncompressed = hex_to_wif_private_key(private_key_hex, compressed=False)
    print_colored(f"WIF (Compressed):   {wif_compressed}", "cyan")
    print_colored(f"WIF (Uncompressed): {wif_uncompressed}", "cyan")

    sk = SigningKey.from_string(binascii.unhexlify(private_key_hex), curve=SECP256k1)
    vk = sk.get_verifying_key()

    public_key_uncompressed = b"\x04" + vk.to_string()
    public_key_compressed = (
        b"\x02" + vk.to_string()[:32]
        if vk.to_string()[32] % 2 == 0
        else b"\x03" + vk.to_string()[:32]
    )

    print_colored(f"Public Key (Uncompressed HEX): {public_key_uncompressed.hex()}", "white")
    print_colored(f"Public Key (Compressed HEX):   {public_key_compressed.hex()}", "white")

    address_compressed = public_key_to_address(vk.to_string(), compressed=True)
    address_uncompressed = public_key_to_address(vk.to_string(), compressed=False)
    print_colored(f"Bitcoin Address (Compressed):   {address_compressed}", "green")
    print_colored(f"Bitcoin Address (Uncompressed): {address_uncompressed}", "green")

def decode_base58(address: str):
    try:
        decoded = base58.b58decode(address)
        hex_representation = decoded.hex()
        print_colored(f"Base58 Decoded (HEX): {hex_representation}", "yellow")

        version = decoded[0:1].hex()
        checksum = decoded[-4:].hex()
        payload = decoded[1:-4].hex()
        print_colored(f"Version Byte: {version}", "cyan")
        print_colored(f"Payload (RIPEMD-160): {payload}", "white")
        print_colored(f"Checksum: {checksum}", "cyan")
    except Exception as e:
        print_colored(f"Invalid Base58 address or decode error: {e}", "red")

def main():
    clear_screen()
    try:
        number = int(input("Enter an integer (used as a private key): "))
        get_bitcoin_info_from_number(number)

        print_colored("\nOptionally, decode a Base58 address:", "cyan")
        address = input("Enter a Bitcoin address (or press Enter to skip): ").strip()
        if address:
            decode_base58(address)
    except Exception as e:
        print_colored(f"Error: {e}", "red")

if __name__ == "__main__":
    main()
