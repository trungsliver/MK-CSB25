# Thao tác: CRUD (Create, Read, Update, Delete)

# Create: Khởi tạo
    # Tạo danh sách rỗng
arr = []
    # Tạo danh sách có sẵn phần tử
csb25 = ['Hải meme', 'Hữu Nguyên', 'Minh Tâm', 'Hoàng Long', 'Phan Anh']
arr1 = ['Hải meme', 16, 'male', 1.75, True]

# Read - Duyệt, hiện phần tử
    # len(): độ dài / số lượng phần tử danh sách
print('Số lượng phần tử của arr:', len(arr))
print('Số lượng phần tử của csb25:', len(csb25))
print('Số lượng phần tử của arr1:', len(arr1))
    # Hiển thị phần tử bằng index
print('Phần tử đầu tiên của csb25:', csb25[0])
print('Phần tử cuối cùng của csb25:', csb25[-1])
print('Phần tử cuối cùng của csb25:', csb25[len(csb25) - 1])
    # Duyệt và hiện phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(csb25)):
    print(f'Index: {i}, Value: {csb25[i]}')
        # Cách 2: Dùng value
for item in csb25:
    print(f'Value: {item}')
        # Cách 3: Dùng hàm có sẵn enumerate() 
for index, value in enumerate(csb25):
    print(f'Index: {index}, Value: {value}')
    # Hiện phần tử (để test)
print('Danh sách csb25:', csb25)

# Update - Cập nhật phần tử
    # Thêm phần tử vào cuối danh sách - append()
csb25.append('Đức Trung')
    # Thêm phần tử vào vị trí bất kỳ - insert()
csb25.insert(2, 'Donald Trump')
    # Cập nhật phần tử theo index
csb25[2] = 'Elon Musk'

# Delete - Xóa phần tử
    # Xóa bằng value - remove()
csb25.remove('Elon Musk')
    # Xóa bằng index - pop()
csb25.pop(-1)
    # Xóa tất cả phần tử - clear()
csb25.clear()

# Sắp xếp danh sách
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Sắp xếp tăng dần - sort()
num_list.sort()
print('num_list: ', num_list)
    # Sắp xếp giảm dần - sort(reverse=True)
num_list.sort(reverse=True)
print('num_list: ', num_list)

# Tìm giá trị lớn nhất, nhỏ nhất trong danh sách
    # max(): giá trị lớn nhất
print('Max value:', max(num_list))
    # min(): giá trị nhỏ nhất
print('Min value:', min(num_list))

# Tìm vị trí phần tử lớn nhất, nhỏ nhất trong danh sách
    # index phần tử lớn nhất
print('Index of max value:', num_list.index(max(num_list)))
    # index phần tử nhỏ nhất
print('Index of min value:', num_list.index(min(num_list)))