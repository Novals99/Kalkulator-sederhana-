daftar_angka = []

jumlah_input = 5

print(f"Silakan masukkan {jumlah_input} angka: ")

for i in range(jumlah_input):
    angka = int(input(f"Angka ke-{i+1}: "))
    daftar_angka.append(angka)

angka_terbesar = max(daftar_angka)
angka_terkecil = min(daftar_angka)
total = sum(daftar_angka)
rata_rata = total / len(daftar_angka)

print(f"\nDari angka-angka yang dimasukkan: {daftar_angka}")
print(f"Angka terbesarnya adalah: {angka_terbesar}")
print(f"Angka terkecilnya adalah: {angka_terkecil}")
print(f"Total dari keseluruhan angka adaah: {total}")
print(f"Rata-rata dari keseluruhan angka adalah: {rata_rata}")