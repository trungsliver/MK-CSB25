# Đề bài: Quản lý môn học của học sinh
# Yêu cầu:
    # Mỗi sinh viên có tên, nhiều môn học
    # Mỗi môn học có tên môn và điểm số
    # Tạo menu:
        # Add a new student
        # Add subject for a student
        # Calculate average score of a student
        # Calculate average score of all students
        # Save data to file
        # Exit

import oop

# Khởi tạo StudentManager
student_manager = oop.StudentManager()

while True:
    print("\n========== QUẢN LÝ SINH VIÊN ==========")
    print("1. Thêm học sinh mới")
    print("2. Thêm môn học cho học sinh")
    print("3. Tính điểm trung bình của học sinh")
    print("4. Tính điểm trung bình của tất cả học sinh")
    print("5. Lưu dữ liệu vào file")
    print("6. Thoát")
    print("=======================================")

    choice = input("Nhập lựa chọn (1-6): ")

    match choice:
        case "1":
            name = input("Nhập tên học sinh: ")
            student_manager.add_student(name)
            print(f"Đã thêm học sinh: {name}")

        case "2":
            student_name = input("Nhập tên học sinh: ")
            subject_name = input("Nhập tên môn học: ")
            grade = float(input("Nhập điểm số: "))
            
            sucess = student_manager.add_subject_to_student(student_name, subject_name, grade)
            if sucess:
                print(f"Đã thêm môn học thành công cho học sinh {student_name}")
            else:
                print(f"Không tìm thấy học sinh {student_name}")

        case "3":
            student_name = input("Nhập tên học sinh: ")
            found = False
            for student in student_manager.students:
                if student.name == student_name:
                    average = student.calculate_average()
                    print(f"Điểm trung bình của học sinh {student_name} là: {average:.2f}")
                    found = True
                    break
            if not found:
                print(f"Không tìm thấy học sinh {student_name}")

        case "4":
            average_all = student_manager.calculate_average_for_all()
            # .2f : làm tròn đến 2 chữ số thập phân
            print(f"Điểm trung bình của tất cả học sinh là: {average_all:.2f}")

        case "5":
            student_manager.save_to_file("student_data.txt")
            print("Đã lưu dữ liệu vào file student_data.txt!")

        case "6":
            print("Thoát chương trình.")
            break

        case _: # khi người dùng nhập lựa chọn không hợp lệ
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")