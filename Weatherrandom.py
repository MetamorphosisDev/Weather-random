import random
import datetime


hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
cuaca_list = ["Cerah", "Hujan", "Berawan", "Badai"]
aktivitas_disarankan = {
    "Cerah": "Baik untuk olahraga di luar ruangan.",
    "Hujan": "Bawa payung dan hindari aktivitas luar.",
    "Berawan": "Cuaca tenang, cocok untuk jalan santai.",
    "Badai": "Tetap di dalam rumah dan pantau berita."
}


def generate_uv_index():
    return round(random.uniform(0, 11), 1)

def get_uv_keterangan(index):
    if index <= 2:
        return "Rendah"
    elif index <= 5:
        return "Sedang"
    elif index <= 7:
        return "Tinggi"
    elif index <= 10:
        return "Sangat Tinggi"
    else:
        return "Ekstrem"


def simulasi_cuaca(nama_hari):
    suhu_cel = random.randint(25, 35)
    kelembapan = random.randint(60, 90)
    suhu_fahrenheit = (suhu_cel * 9 / 5) + 32
    kecepatan_angin = random.randint(0, 20)
    cuaca_hari_ini = random.choice(cuaca_list)
    indeks_uv = generate_uv_index()

    data_cuaca = {
        "Hari": nama_hari,
        "Cuaca": cuaca_hari_ini,
        "Suhu (Celsius)": suhu_cel,
        "Suhu (Fahrenheit)": suhu_fahrenheit,
        "Kelembapan (%)": kelembapan,
        "Kecepatan Angin (km/jam)": kecepatan_angin,
        "Indeks UV": indeks_uv,
        "Keterangan UV": get_uv_keterangan(indeks_uv),
        "Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return data_cuaca

def tampil_cuaca(data_cuaca):
    print("\n========= Simulasi Cuaca =========")
    print(f"Hari\t\t\t: {data_cuaca['Hari']}")
    print(f"Cuaca\t\t\t: {data_cuaca['Cuaca']}")
    print(f"Suhu\t\t\t: {data_cuaca['Suhu (Celsius)']} °C / {data_cuaca['Suhu (Fahrenheit)']:.2f} °F")
    print(f"Kelembapan\t\t: {data_cuaca['Kelembapan (%)']} %")
    print(f"Kecepatan Angin\t\t: {data_cuaca['Kecepatan Angin (km/jam)']} km/jam")
    print(f"Indeks UV\t\t: {data_cuaca['Indeks UV']} ({data_cuaca['Keterangan UV']})")
    print(f"Waktu\t\t\t: {data_cuaca['Waktu']}")

    print(f"Saran Aktivitas\t\t: {aktivitas_disarankan[data_cuaca['Cuaca']]}")

    if data_cuaca["Cuaca"] == "Hujan":
        print('Perkiraan\t\t: Hujan kemungkinan berlanjut 2-3 jam.')
    elif data_cuaca["Cuaca"] == "Badai":
        print('Perkiraan\t\t: Hati-hati, badai diperkirakan mereda sore hari.')
    else:
        print('Perkiraan\t\t: Cuaca cenderung stabil.')

    prediksi_hari_berikutnya = random.choice(cuaca_list)
    print(f"Prediksi Hari Berikutnya: {prediksi_hari_berikutnya}")

# main
print("Masukkan hari yang ingin Anda lihat cuacanya (contoh: Senin):")
pilihan_hari = input("Hari: ").strip().capitalize()

if pilihan_hari not in hari_list:
    print("\n⚠️ Hari tidak valid! Masukkan nama hari dengan benar (misal: Senin, Selasa, dst).")
else:
    data = simulasi_cuaca(pilihan_hari)
    tampil_cuaca(data)
