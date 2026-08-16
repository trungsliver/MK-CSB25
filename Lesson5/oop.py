class Subject:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = [] # Danh sách môn học

    def add_subject(self, subject):
        self.subjects.append(subject)

    def calculate_average(self):
        if not self.subjects:
            return 0
        total = 0
        for subject in self.subjects:
            total += subject.grade
        return total / len(self.subjects)
    
class StudentManager:
    def __init__(self):
        self.students = [] # Danh sách sinh viên

    def add_student(self, student_name):
        # Tạo học sinh mới
        new_student = Student(student_name)
        # Thêm học sinh vào danh sách (thuộc tính students)
        self.students.append(new_student)

    def add_subject_to_student(self, student_name, subject_name, grade):
        # Tìm học sinh theo tên
        for student in self.students:
            if student.name == student_name:
                # Tạo môn học mới
                new_subject = Subject(subject_name, grade)
                # Thêm môn học vào học sinh
                student.add_subject(new_subject)
                return True
        # Không tìm thấy học sinh
        print(f"Student {student_name} not found.")
        return False
    
    # Tính điểm trung bình của tất cả học sinh
    def calculate_average_for_all(self):
        if not self.students:
            return 0
        total = 0
        for student in self.students:
            total += student.calculate_average()
        return total / len(self.students)
    
    # Lưu dữ liệu vào file
    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            # Ghi thông tin từng học sinh và môn học của họ vào file
            for student in self.students:
                # Tên học sinh
                file.write(f"Student: {student.name}\n")
                # Từng môn học của học sinh đó
                for subject in student.subjects:
                    file.write(f"  Subject: {subject.name}, Grade: {subject.grade}\n")
                # Điểm trung bình của học sinh đó
                file.write(f"  Average Score: {student.calculate_average()}\n\n")