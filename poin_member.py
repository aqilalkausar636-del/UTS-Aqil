print("=== Sistem Poin Member ===")

total_belanja = 0
total_poin = 0

while True:
    belanja = float(input("Masukkan total belanja (Rp): "))

    total_belanja += belanja  # Tambah ke akumulasi total

    # Hitung poin (1 poin per Rp 10.000)
    poin = int(belanja // 10000)
    total_poin += poin

    print(f"Poin dari transaksi ini: {poin} poin")

    lanjut = input("Apakah ingin input transaksi lagi? (iya/tidak): ").lower()
    if lanjut == 'tidak':
        break

print("\n=== RINGKASAN ===")
print(f"Total Belanja: Rp {total_belanja}")
print(f"Total Poin Didapat: {total_poin} poin")
print("Terima kasih sudah menjadi member!")
