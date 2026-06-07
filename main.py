name = input("Masukkan nama mahasiswa: ")

a = float(input("Nilai 1: "))
b = float(input("Nilai 2: "))
c = float(input("Nilai 3: "))

r = (a + b + c) / 3

if r >= 75:
    print(name)
    print(r)
    print("Lulus")
else:
    print(name)
    print(r)
    print("Tidak Lulus")