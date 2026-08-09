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