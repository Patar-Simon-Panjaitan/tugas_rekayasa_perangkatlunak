PASSING_GRADE = 75

student_name = input("Masukkan nama mahasiswa: ")

score1 = float(input("Nilai 1: "))
score2 = float(input("Nilai 2: "))
score3 = float(input("Nilai 3: "))

average_score = (score1 + score2 + score3) / 3

if average_score >= PASSING_GRADE:
    print(student_name)
    print(average_score)
    print("Lulus")
else:
    print(student_name)
    print(average_score)
    print("Tidak Lulus")