# ============= QUEUE - Hàng đợi ================

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: FIFO (First In First Out) - Vào trước ra trước
# Ví dụ:
    # Xếp hàng đợi thanh toán trong siêu thị
    # Hàng đợi in tài liệu

# Các thao tác cơ bản 
    # Khởi tạo
        # Cách 1:
queue1 = []
        # Cách 2:
from collections import deque
queue2 = deque()

    # enqueue: thêm phần tử vào cuối hàng đợi
queue1.append('A')  
queue1.append('B')  
print("Queue1 sau khi enqueue:", queue1)

queue2.append('A')  
queue2.append('B')  
queue2.append('C')  
queue2.append('D')  
print("Queue2 sau khi enqueue:", queue2)

    # dequeue: loại bỏ phần tử ở đầu hàng đợi
        # Cách 1: tốn thời gian vì phải dịch chuyển các phần tử còn lại
item1 = queue1.pop(0)
print('Phần tử được dequeue từ queue1:', item1)

        # Cách 2: sử dụng deque, hiệu quả hơn
item2 = queue2.popleft()
print('Phần tử được dequeue từ queue2:', item2)

    # peek: xem phần tử ở đầu queue mà không xóa
print('Phần tử ở đầu queue1:', queue1[0])
print('Phần tử ở đầu queue2:', queue2[0])

    # is_empty: kiểm tra queue có rỗng hay không
def is_empty(queue):
    return len(queue) == 0

# Ví dụ: Xếp hàng đợi thanh toán trong siêu thị
    # Khởi tạo hàng đợi
line = deque()
    # Thêm khách hàng vào hàng đợi
line.append('Hải meme')
line.append('Hữu Nguyên')
line.append('Minh Tâm')
line.append('Hoàng Long')
    # Hiển thị danh sách người đang xếp hàng
print('Hàng đợi sau khi thêm khách hàng:', line)
    # Phục vụ khách hàng theo thứu tự xếp hàng
while not is_empty(line):
    current_customer = line.popleft()
    print('\nPhục vụ khách hàng:', current_customer)
    # Hiển thị danh sách người xép hàng còn lại
    print('Khách hàng còn lại:', line)

print('\nTất cả khách hàng đã được phục vụ.')
