class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")


class Student(Person):  
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   
        self.student_id = student_id

    def study(self):
        print(f"Sinh viên {self.name} đang học bài...")

    def display_info(self):
        super().display_info()  
        print(f"Mã sinh viên: {self.student_id}")
        print("-" * 30)


if __name__ == "__main__":
    student1 = Student("Nguyễn Văn A", 20, "SV001")

    student1.display_info()
    student1.study()