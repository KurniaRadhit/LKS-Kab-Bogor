#!/bin/bash

ENC_FILE="file.jpg.enc"
WORDLIST="/usr/share/wordlists/rockyou.txt"

if [[ ! -f "$ENC_FILE" ]]; then
    echo "File terenkripsi tidak ditemukan: $ENC_FILE"
    exit 1
fi

if [[ ! -f "$WORDLIST" ]]; then
    echo "Wordlist tidak ditemukan: $WORDLIST"
    exit 1
fi

head -n 100 "$WORDLIST" | while read -r password; do

    count=$(ls flag*.jpg 2>/dev/null | wc -l)
    output_file="flag$((count + 1)).jpg"

    echo "[+] Mencoba password: $password -> $output_file"
    openssl enc -d -aes-256-cbc -salt -pbkdf2 -in "$ENC_FILE" -out "$output_file" -pass pass:"$password" 2>/dev/null
done

echo "[+] Brute force selesai. Cek file flag*.jpg untuk hasilnya."
