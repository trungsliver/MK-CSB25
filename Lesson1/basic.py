# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi giá trị khi lập trình
name = 'Duc Trung'
a, b, c = 1, 2, 3

# Quy tắc đặt tên biến:
    # chỉ gồm chữ cái tiếng anh, số, dấu gạch dưới
    # không được bắt đầu bằng số
    # không được trùng với từ khóa của Python (if, else, for, ...)

# 2 kiểu đặt tên biến phổ biến:
    # camelCase: viết hoa chữ cái đầu mỗi từ, trừ từ đầu tiên
myFullName = 'Bui Duc Trung'
    # snake_case: mỗi từ cách nhau bằng dấu gạch dưới
my_full_name = 'Bui Duc Trung'

# Data types - Kiểu dữ liệu
    # String: chuỗi / xâu ký tự
name = 'Duc Trung'
    # int (integer): số nguyên
age = 2
    # float: số thực (real number, số thập phân)
score = 8.5
    # boolean: giá trị đúng hoặc sai (True/False)
is_male = True

# Các cách hiển thị dữ liệu
    # Cách 1: Dùng dấu + (chỉ dùng được với cùng kiểu dữ liệu)
print('Họ tên: ' + name)
print('Tuổi: ' + str(age))  # Cần chuyển đổi int sang string

    # Cách 2: Dùng dấu , 
print('Điểm: ', score)
print('Giới tính nam: ', is_male)

    # Cách 3: Dùng f-string (truyền dữ liệu vào string)
print(f'Họ tên: {name}, Tuổi: {age}, Điểm: {score}, Giới tính nam: {is_male}')

    # Cách 4: Hiển thị trên nhiều dòng
print(f'''
========== THÔNG TIN ==========      
Họ tên: {name}
Tuổi: {age}
Điểm: {score}
Giới tính nam: {is_male}
===============================''')
