PASSING_GRADE = 75


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def get_status(self):
        if self.calculate_average() >= PASSING_GRADE:
            return "Lulus"
        return "Tidak Lulus"

    def display_result(self):
        print("=" * 30)
        print(f"Nama     : {self.name}")
        print(f"Nilai    : {self.scores}")
        print(f"Rata-rata: {self.calculate_average():.2f}")
        print(f"Status   : {self.get_status()}")
        print("=" * 30)


def input_scores():
    scores = []

    for i in range(3):
        score = float(input(f"Masukkan nilai ke-{i+1}: "))
        scores.append(score)

    return scores


def main():
    student_name = input("Masukkan nama mahasiswa: ")

    scores = input_scores()

    student = Student(student_name, scores)

    student.display_result()


if __name__ == "__main__":
    main()