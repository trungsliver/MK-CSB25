# COMPLEXITY - Độ phức tạp của thuật toán

# Biểu diễn độ phức tạp bằng Big-O Notation
    # Độ phức tạp: (O) = n * số phép toán
    #  n là kích thước dữ liệu đầu vào

# Ví dụ về độ phức tạp:

# O(1) - Độ phức tạp hằng số (constant): gán, nhập, xuất, tính toán cơ bản
name = 25
# age = input()
print(name)
print(1 + 1)

# O(n) - tuyến tính
arr = [1, 2, 3, 4, 5]       # n = 5
for item in arr:            # thực hiện n lần (5 lần) => O(n)
    print(item)

# O(n^2) - bình phương (quadratic): lặp 2 vòng lặp
    # In ra bảng cửu chương từ 1 đến 10
for i in range(1, 11):      # thực hiện n lần (10 lần) => O(n)
    print('\nBảng cửu chương của', i)
    for j in range(1, 11):  # thực hiện n lần (10 lần) => O(n)
        print(i, 'x', j, '=', i * j)

# O(log n) - logarit
    # Vid dụ logarit: 2^3 = 8 => log2(8) = 3
    # Game đoán số: đoán số trong khoảng [1,100], number = 67
    # 50, 75, 62, 68, 65, 66, 67 => đoán đúng sau 7 lần đoán
    # Trường hợp xấu nhất log2(100) = 6.64 => làm tròn lên 7 lần đoán

# So sánh thời gian thực hiện: O(n^2) > O(n) > O(log n) > O(1)