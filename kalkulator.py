import os

def tampilkan_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=" * 40)
    print("      KALKULATOR SUPER (VIBE EDITION)    ")
    print("=" * 40)

def main():
    riwayat = []
    while True:
        tampilkan_banner()
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Persen (%)")
        print("6. Lihat Riwayat")
        print("7. Keluar")
        
        pilihan = input("\nPilih menu (1-7): ").strip()
        
        if pilihan == '7':
            print("\nTerima kasih! Sampai jumpa.")
            break
            
        if pilihan == '6':
            print("\n--- RIWAYAT PERHITUNGAN ---")
            if not riwayat:
                print("Belum ada riwayat.")
            else:
                for r in riwayat:
                    print(f"- {r}")
            input("\nTekan Enter untuk kembali...")
            continue

        if pilihan in ['1', '2', '3', '4', '5']:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil = a + b
                    ops = '+'
                elif pilihan == '2':
                    hasil = a - b
                    ops = '-'
                elif pilihan == '3':
                    hasil = a * b
                    ops = '*'
                elif pilihan == '4':
                    if b == 0:
                        print("\n[Error] Nggak bisa bagi dengan angka 0!")
                        input("Tekan Enter...")
                        continue
                    hasil = a / b
                    ops = '/'
                elif pilihan == '5':
                    hasil = (a * b) / 100
                    ops = '% dari'

                teks_hasil = f"{a} {ops} {b} = {hasil}"
                riwayat.append(teks_hasil)
                print(f"\nHasil: {hasil}")
                
            except ValueError:
                print("\n[Error] Masukkan angka yang valid!")
                
            input("\nTekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()
