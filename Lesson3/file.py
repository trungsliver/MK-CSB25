import json

students = [
    {"name": "Hai meme", "age": 15, "gender": "male"},
    {"name": "Minh Tâm", "age": 15, "gender": "male"},
    {"name": "Hoàng Long", "age": 15, "gender": "male"},
    {"name": "Hữu Nguyên", "age": 15, "gender": "male"}
]

# Ghi nội dung vào file Json
# Ghi nội dung vào file JSON
with open("data.json", "w", encoding="utf-8") as f:
    # indent=4: định dạng giúp file dễ đọc
    # ensure_ascii=False: để giữ nguyên ký tự Unicode (giữ nguyên tiếng việt)
    json.dump(students, f, indent=4, ensure_ascii=False)

# Đọc nội dung từ file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)