import os
import math

def tampilkan_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=" * 45)
    print("   KALKULATOR SUPER (SCIENTIFIC VIBE EDITION)   ")
    print("=" * 45)

def main():
    riwayat = []
    while True:
        tampilkan_banner()
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Persen (%)")
        print("6. Pangkat (x^y)")
        print("7. Akar Kuadrat (√x)")
        print("8. Sinus, Kosinus, Tangen (Sin/Cos/Tan)")
        print("9. Lihat Riwayat")
        print("10. Keluar")
        
        pilihan = input("\nPilih menu (1-10): ").strip()
        
        if pilihan == '10':
            print("\nTerima kasih! Sampai jumpa.")
            break
            
        if pilihan == '9':
            print("\n--- RIWAYAT PERHITUNGAN ---")
            if not riwayat:
                print("Belum ada riwayat.")
            else:
                for r in riwayat:
                    print(f"- {r}")
            input("\nTekan Enter untuk kembali...")
            continue

        try:
            if pilihan in ['1', '2', '3', '4', '5', '6']:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1': hasil, ops = a + b, '+'
                elif pilihan == '2': hasil, ops = a - b, '-'
                elif pilihan == '3': hasil, ops = a * b, '*'
                elif pilihan == '4':
                    if b == 0:
                        print("\n[Error] Nggak bisa bagi dengan angka 0!")
                        input("Tekan Enter...")
                        continue
                    hasil, ops = a / b, '/'
                elif pilihan == '5': hasil, ops = (a * b) / 100, '% dari'
                elif pilihan == '6': hasil, ops = math.pow(a, b), '^'

                teks_hasil = f"{a} {ops} {b} = {hasil}"

            elif pilihan == '7':
                a = float(input("Masukkan angka: "))
                if a < 0:
                    print("\n[Error] Tidak bisa menghitung akar angka negatif!")
                    input("Tekan Enter...")
                    continue
                hasil = math.sqrt(a)
                teks_hasil = f"√{a} = {hasil}"

            elif pilihan == '8':
                sudut = float(input("Masukkan sudut (derajat): "))
                rad = math.radians(sudut)
                sin_val = math.sin(rad)
                cos_val = math.cos(rad)
                tan_val = math.tan(rad)
                print(f"\nHasil untuk {sudut}°:")
                print(f"- Sin: {sin_val:.4f}")
                print(f"- Cos: {cos_val:.4f}")
                print(f"- Tan: {tan_val:.4f}")
                teks_hasil = f"Trigonometri({sudut}°) -> Sin:{sin_val:.2f}, Cos:{cos_val:.2f}, Tan:{tan_val:.2f}"
                hasil = "Selesai"

            else:
                print("\n[Error] Pilihan menu tidak valid!")
                input("Tekan Enter...")
                continue

            if pilihan != '8':
                print(f"\nHasil: {hasil}")
            
            riwayat.append(teks_hasil)
                
        except ValueError:
            print("\n[Error] Masukkan angka yang valid!")
            
        input("\nTekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()

