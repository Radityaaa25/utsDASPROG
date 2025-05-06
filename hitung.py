from wrap import wrap_text

def kalkulator_bmi(berat, tinggi):
    # Menghitung BMI (Body Mass Index) berdasarkan berat (kg) dan tinggi (cm)
    # BMI = berat / (tinggi dalam meter)^2
    tinggi_in_meters = tinggi / 100
    bmi = berat / (tinggi_in_meters ** 2)
    return round(bmi, 2)

def kalkulator_berat_ideal(tinggi, gender):
    # Menghitung berat badan ideal berdasarkan tinggi dan jenis kelamin
    # Menggunakan rumus Broca yang dimodifikasi:
    # - Untuk pria: (tinggi - 100) - ((tinggi - 100) * 0.1)
    # - Untuk wanita: (tinggi - 100) - ((tinggi - 100) * 0.15)
    if gender.lower() == "pria" or gender.lower() == "laki-laki" or gender.lower() == "l":
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.1)
    else:  # wanita
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.15)
    return round(berat_ideal, 1)

def get_bmi_status(bmi):
    # Menentukan status BMI berdasarkan nilai BMI
    if bmi < 18.5:
        return "kurang"
    elif 18.5 <= bmi < 25:
        return "normal"
    else:
        return "kelebihan"

def get_recommendation(status, gender, age):
    # Memberikan rekomendasi kesehatan berdasarkan status BMI, jenis kelamin, dan umur
    gender_term = "Anda" if gender.lower() in ["pria", "laki-laki", "l"] else "Anda"
    
    if status == "kurang":
        if age < 18:
            return wrap_text(f"Berat badan {gender_term} kurang dari ideal. Pada usia pertumbuhan, disarankan untuk mengonsumsi makanan bergizi seimbang, protein yang cukup, dan konsultasikan dengan dokter atau ahli gizi untuk memastikan tumbuh kembang yang optimal.")
        elif age >= 60:
            return wrap_text(f"Berat badan {gender_term} kurang dari ideal. Pada usia lanjut, hal ini dapat meningkatkan risiko beberapa penyakit. Disarankan untuk mengonsumsi makanan bergizi, tingkatkan asupan protein, dan konsultasikan dengan dokter.")
        else:
            return wrap_text(f"Berat badan {gender_term} kurang dari ideal. Disarankan untuk menambah asupan makanan bergizi, konsumsi protein yang cukup (0.8-1g per kg berat badan), dan rutin berolahraga untuk membangun massa otot.")
    
    elif status == "normal":
        if age < 18:
            return wrap_text(f"Berat badan {gender_term} ideal. Tetap pertahankan pola makan sehat dan aktivitas fisik yang cukup untuk mendukung masa pertumbuhan.")
        elif age >= 60:
            return wrap_text(f"Berat badan {gender_term} ideal. Tetap jaga pola makan seimbang dan lakukan aktivitas fisik yang sesuai dengan kondisi tubuh untuk menjaga kesehatan di usia lanjut.")
        else:
            return wrap_text(f"Berat badan {gender_term} ideal. Pertahankan pola makan sehat dan tetap aktif secara fisik untuk menjaga kondisi tubuh optimal.")
    
    else:  # kelebihan
        if age < 18:
            return wrap_text(f"Berat badan {gender_term} melebihi ideal. Pada masa pertumbuhan, disarankan untuk mengatur pola makan dan meningkatkan aktivitas fisik, namun tetap memperhatikan asupan nutrisi yang cukup. Konsultasikan dengan dokter atau ahli gizi.")
        elif age >= 60:
            return wrap_text(f"Berat badan {gender_term} melebihi ideal. Pada usia lanjut, penurunan berat badan sebaiknya dilakukan secara perlahan. Disarankan untuk konsultasi dengan dokter sebelum memulai program diet.")
        else:
            return wrap_text(f"Berat badan {gender_term} melebihi ideal. Disarankan untuk mengatur pola makan, mengurangi makanan tinggi kalori dan lemak, serta rutin berolahraga minimal 30 menit setiap hari dengan intensitas sedang.")