from hitung import kalkulator_bmi, kalkulator_berat_ideal, get_bmi_status, get_recommendation
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main(): 
    continue_program = True
    
    while continue_program:
        print("=" * 80)
        print("PROGRAM PENGECEK KESEHATAN".center (80))
        print("=" * 80)
        print("Program ini akan memeriksa kondisi kesehatan berdasarkan BMI".center (80))
        print("=" * 80)
        print("-" * 80)
        # Input data pengguna
        nama = input("Masukkan nama Anda                        : ")
        
        # Validasi umur
        while True:
            try:
                umur = int(input("Masukkan umur Anda (tahun)                : "))
                if umur <= 0:
                    print("Umur harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("Masukan angka untuk umur yang valid!")
        # Input jenis kelamin
        while True:
            jenis_kelamin = input("Masukkan jenis kelamin Anda (pria/wanita) : ").lower()
            if jenis_kelamin in ["pria", "wanita", "laki-laki", "perempuan", "l", "p"]:
                if jenis_kelamin in ["laki-laki", "l"]:
                    jenis_kelamin = "pria"
                elif jenis_kelamin in ["perempuan", "p"]:
                    jenis_kelamin = "wanita"
                break
            else:
                print("Masukkan jenis kelamin yang valid (pria/wanita)!")
        
        # Validasi tinggi
        while True:
            try:
                tinggi = float(input("Masukkan tinggi badan Anda (cm)           : "))
                if tinggi <= 0:
                    print("Tinggi harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("Masukkan angka yang valid untuk tinggi badan!")
        
        # Validasi berat
        while True:
            try:
                berat = float(input("Masukkan berat badan Anda (kg)            : "))
                if berat <= 0:
                    print("Berat harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("Masukkan angka yang valid untuk berat badan!")
        
        # Hitung BMI dan berat ideal
        bmi = kalkulator_bmi(berat, tinggi)
        berat_ideal = kalkulator_berat_ideal(tinggi, jenis_kelamin)
        
        # Tentukan status dan rekomendasi
        status = get_bmi_status(bmi)
        rekomendasi = get_recommendation(status, jenis_kelamin, umur)
        
        # Menampilkan hasil
        print("-" * 80)
        print("=" * 80)
        print("HASIL PEMERIKSAAN".center (80))
        print("=" * 80)
        print("-" * 80)
        print(f"Nama          : {nama}")
        print(f"Umur          : {umur} tahun")
        print(f"Jenis Kelamin : {jenis_kelamin.capitalize()}")
        print(f"Tinggi        : {tinggi:.0f} cm")
        print(f"Berat         : {berat} kg")
        print(f"Berat Ideal   : {berat_ideal} kg")
        print(f"BMI           : {bmi}")
        print("-" * 80)
        
        if status == "normal":
            print("Status        : Berat badan NORMAL")
        elif status == "kurang":
            print("Status        : Berat badan KURANG (perlu ditambah lagi)")
        else:
            print("Status        : Berat badan KELEBIHAN (perlu diet)")
        print("=" * 80)
        
        print(f"\nRekomendasi:\n {rekomendasi}")
        print(" ")
        print("=" * 80)
        # Tanya apakah ingin melanjutkan
        lanjut = input("\nApakah ingin mencoba lagi? (y/n) : ").lower()
        if lanjut != 'y':
            continue_program = False
    
    print("\nTerima kasih telah menggunakan Program Pengecek Kesehatan!\nTetap Jaga Pola Hidup Yang Sehat Karena Sehat Itu MAHALL!!!")
    print("=" * 80)

if __name__ == "__main__":
    clear_terminal()
    main()