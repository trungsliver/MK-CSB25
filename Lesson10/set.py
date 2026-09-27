# ================= TẬP HỢP (SET) ================

# Định nghĩa:
    # Là 1 kiểu cấu trúc dữ liệu
    # Không có thứ tự
    # Không chứa phần tử trùng lặp

# Create - Khởi tạo
    # Tạo set rỗng
set1 = set()
    # Tạo set có sẵn phần tử
set2 = {1, 2, 3, 4, 5}

# Các thao tác cơ bản
    # Thêm phần tử: add()
set2.add(6)
    # Xóa phần tử
        # remove() - nếu không có phần tử sẽ báo lỗi
set2.remove(6)
        # discard() - nếu không có phần tử sẽ không báo lỗi
set2.discard(7)

print(set2)

# Các thao tác khác
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}  
    # union(): Hợp - trả về set mới chứa tất cả phần tử của 2 set
set_union = set3.union(set4)
set_union2 = set3 | set4
print("Union:", set_union)

    # intersection(): Giao - trả về tập hợp chưa phần tử chung
set_intersection = set3.intersection(set4)
set_intersection2 = set3 & set4
print("Intersection:", set_intersection)

    # difference(): Hiệu - trả về tập hợp chứa phần tử chỉ có trong tập hợp đầu tiên
set_difference = set3.difference(set4)
set_difference2 = set3 - set4
print("Difference:", set_difference)

# Duyệt phần tử
for item in set2:
    print(item)

# Kiểm tra phần tử có nằm trong tập hợp không
print("3 in set3:", 3 in set3)      # True
print("99 in set3:", 99 in set3)    # False