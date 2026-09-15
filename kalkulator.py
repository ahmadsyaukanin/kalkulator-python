print("=== KALKULATOR SAYA ===")
print("1. Tambah (+)")
print("2. Kurang (-)")

pilihan = input("Pilih menu (1/2): ")
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))

if pilihan == "1":
    print("Hasil:", a + b)
elif pilihan == "2":
    print("Hasil:", a - b)
else:
    print("Pilihan tidak valid!")
