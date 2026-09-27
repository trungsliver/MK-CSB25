# ================== DICTIONARY ==================

# Đặc điểm:
    # Là 1 cấu trúc dữ liệu
    # Đặc trưng: key-value

# Create - khởi tạo
    # Tạo dict trống
dict1 = {}
    # Tạo dict có sẵn dữ liệu
dict2 = {
    # key - value
    'name': 'Duc Trung',
    'age': 2,
    'city': 'Ha Noi',
    'work': 'MindX Technology School'
}

# Read
    # Truy cập bằng key
print('Name:', dict2['name'])
# print(dict2['cash']) # KeyError
    # Truy cập bằng get()
print('Age:', dict2.get('age'))
        # Không tồn tại sẽ trả về None
print('Cash:', dict2.get('cash'))
        #  Hoặc giá trị mặc định
print('Hobbies:', dict2.get('hobbies', '404 not found'))
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f'{key}: {value}')

# Update - Chỉnh sửa
    # Thêm mới
dict2['hobbies'] = ['football', 'game']
    # Cập nhật
dict2['age'] = 9

# Delete
    # Del - Xoá theo key
del dict2['hobbies']
    # Pop - Xoá theo key và trả về giá trị
work = dict2.pop('work')
print('Work:', work)

    # Kiểm tra key có tồn tại không
print('name' in dict2)  # True
print('hobbies' in dict2)  # False    

    # Lấy tất cả key
print('Keys:', dict2.keys())
    # Lấy tất cả value
print('Values:', dict2.values())
    # Lấy tất cả items (bao gồm cả key và value)
print('Items:', dict2.items())

# ======================= MAP =======================
    # Hàm map(function, itertable)
        # function: hàm biến đổi phần tử
        # itertable: đối tượng dữ liệu (list, set, dictionary,...)

# Ví dụ: Cho 1 danh sách điểm hệ số 10
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên thành hệ số 4
gpa_10 = [5, 7, 8, 10, 9]

    # Cách 1: Dùng hàm thông thường
def convert_gpa(score:float):
    return score / 10 * 4
gpa_4 = map(convert_gpa, gpa_10)
print('GPA hệ số 4 (cách 1):', list(gpa_4))

    # Cách 2: Dùng lambda function (hàm vô danh)
gpa4 = map(lambda score: score / 10 * 4, gpa_10)
print('GPA hệ số 4 (cách 2):', list(gpa4))

# Ví dụ: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
     # tRunG -> TRUNG
students = ['mInH aNH', 'tHu hUoNg', 'lAM KhANh', 'dUy anH', 'tUAN lINh']

    # Cách 1:
def convert_name(name:str):
    return name.upper()
upper_students = map(convert_name, students)
print('Students (cách 1):', list(upper_students))

    # Cách 2:
upper_students2 = map(lambda name: name.upper(), students)
print('Students (cách 2):', list(upper_students2))