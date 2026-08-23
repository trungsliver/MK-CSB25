#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

import random
# Tạo số ngẫu nhiên trong khoảng [1,100]
number = random.randint(1, 100)

print('Số cần tìm:', number)  # In ra số đặc biệt để kiểm tra

count = 1
guess = int(input('Nhập số bạn đoán (1-100): '))
while guess != number:
    if guess < number:
        print('Số bạn đoán nhỏ hơn số đặc biệt')
    else:
        print('Số bạn đoán lớn hơn số đặc biệt')
    count += 1
    guess = int(input('\nNhập số bạn đoán (1-100): '))
print('Bạn đã đoán đúng số đặc biệt sau', count, 'lần đoán')