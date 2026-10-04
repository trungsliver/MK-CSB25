# =============== STACK - NGĂN XẾP ===============

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: LIFO (last in first out) - Vào sau ra trước

# Ví dụ: 
    # Xếp đĩa chồng lên nhau
    # Lịch sử trình duyệt (khi ấn back lần đầu tiên, trở về trang truy cập cuối cùng)

# Các thao tác cơ bản:
    # Create - Khởi tạo stack
stack = []

    # push/append: thêm phần tử vào đỉnh stack (cuối stack)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

    # pop: loại bỏ phần tử ở đỉnh stack và trả về phần tử đó
top_element = stack.pop()
print("Popped element:", top_element)
print(stack)

    # peek: Xem phần tử ở đỉnh stack (không xóa)
top_element = stack[-1]  
print('Top element (peek):', top_element)

    # is_empty: Kiểm tra xem stack có rỗng không
def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
print("Is stack empty:", is_empty(stack))