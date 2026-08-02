# OOP: Object-Oriented Programming
# Lập trình hướng đối tượng

# Tổng quát: OOP là cách mà chúng ta mô tả thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Ví dụ: mô tả con người (Human)
    # Thuộc tính (attributes): đặc điểm của đối tượng (tên, tuổi, giới tính,...)
    # Phương thức (methods): hành vi/hành động của đối tượng (ăn, ngủ, đi, nói,...)

# 4 tính chất của lập trình hướng đối tượng:
    # Đóng gói (Encapsulation): che dữ liệu (password, info,...)
    # Kế thừa (Inheritance): dùng lại dữ liệu cũ
    # Đa hình (Polymorphism): cùng 1 tên hàm, hành động khác nhau
    # Trừu tượng (Abstraction): khai báo phương thức trước, ghi hành động sau

# Khai báo lớp đối tượng (class)
class Human:
    # Khởi tạo đối tượng (constructor)
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (method)
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'===== INFO =====')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'================')

    def sing(self, song):
        print(f'{self.name} is singing {song}')

# Khởi tạo đối tượng cụ thể (object)
human1 = Human('Hải meme', 15, 'male')
human2 = Human('Minh Tâm', 15, 'male')
    # Sử dụng phương thức __str__
print(human1)
    # Sử dụng phương thức display_info
print(human2.display_info())
    # Sử dụng phương thức sing
human1.sing('baby shark')

# Tính chất kế thừa (Inheritance)
class Student(Human):
    def __init__(self, name, age, gender, school):
        # Gọi phương thức khởi tạo của lớp cha (Human)
        super().__init__(name, age, gender)
        self.school = school

    # Ghi đè phương thức hiển thị thông tin (tính đa hình)
    def display_info(self):
        print(f'===== INFO =====')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'School: {self.school}')
        print(f'================')

# Khởi tạo đối tượng Student
student1 = Student('Hoàng Long', 15, 'male', 'FPT')
student2 = Student('Hữu Nguyên', 15, 'male', 'MindX')
    # Phương thức
student1.sing('Một con vịt')    # Kế thừa
student2.display_info()         # Đa hình