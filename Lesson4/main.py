import oop

# Khởi tạo PlayerDatabase
db = oop.PlayerDatabase("data.json")

# Hiển thị số lượng phần tử ở 2 danh sách trong UserDatabase
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Chuyển từ dictionary sang object
db.dict_to_object()

print('Sau chuyển đổi:')
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Hiển thị toàn bộ phần tử trong danh sách object
db.show_all()

# Tìm kiếm 1 player theo tên
find1 = db.find_player_by_name('Messi')
find2 = db.find_player_by_name('Hai meme')
    # Tìm thấy
if find1 is not None:
    print('Tìm thấy player:', find1.name)
else:
    print('Không tìm thấy player')
    # Không tìm thấy
if find2 is not None:
    print('Tìm thấy player:', find2.name)
else:
    print('Không tìm thấy player')

# Thêm 1 player mới
new_player = {
    "id": 67,
    "name": "Hải Meme",
    "dob": "01/04/2011",
    "region": "Viet Nam",
    "club": "SCP",
    "rating": 100,
    "worth": 0
}
db.add_player(new_player)
db.show_all()

# Sửa thông tin player
edit_name = 'Hải Meme'
new_player = {
    "id": 67,
        "name": "Hải Meme",
        "dob": "01/04/2011",
        "region": "Viet Nam",
        "club": "SCP",
        "rating": 100,
        "worth": 100
}
db.edit_player(edit_name, new_player)
db.show_all()

# Xóa thông tin
db.delete_player("Hải meme")