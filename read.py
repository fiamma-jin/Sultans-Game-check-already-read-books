import json
import csv
import os

# =============================
# 1. 读取你自己整理的 CSV 文件（按列位置读取，不依赖表头名称）
# =============================
csv_file = "书籍清单.csv"
books = {}  # 结构: { "书籍ID": "书名" }

if not os.path.exists(csv_file):
    print(f"❌ 致命错误：找不到文件 {csv_file}，请确保它和代码在一个文件夹下！")
    exit()

with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    # 跳过第一行表头（不管表头写的什么，都跳过）
    next(reader, None) 
    
    for row in reader:
        # 确保这行至少有 2 列数据
        if len(row) >= 2:
            # 第一列是 ID，第二列是名字，直接按位置取，完全不怕列名写错！
            book_id = str(row[0]).strip()
            book_name = row[1].strip()
            
            if book_id and book_name: # 防止空行
                books[book_id] = book_name

print(f"✅ 成功从 CSV 读取了 {len(books)} 本读物。")

# =============================
# 2. 读取你的 round 存档文件
# =============================
round_file = "round_134.json"
if not os.path.exists(round_file):
    print(f"❌ 致命错误：找不到文件 {round_file}！")
    exit()

with open(round_file, "r", encoding="utf-8") as f:
    round_data = json.load(f)

# =============================
# 3. 统计已读次数 (使用 notes 字段)
# =============================
book_total_counts = {}

for note_group in round_data.get("notes", []):
    for item in note_group:
        if item.get("type") == 10002 and item.get("count", 0) > 0:
            
            entity_id = str(item["id"]).strip() 
            count = item.get("count", 0)
            
            if entity_id in books:
                book_name = books[entity_id]
                
                if book_name in book_total_counts:
                    existing_id, current_total = book_total_counts[book_name]
                    book_total_counts[book_name] = [existing_id, current_total + count]
                else:
                    book_total_counts[book_name] = [entity_id, count]

# =============================
# 4. 分类已读和未读
# =============================
read_books = []
unread_books = []

for book_id, name in books.items():
    if name in book_total_counts:
        original_id, total_count = book_total_counts[name]
        read_books.append((original_id, name, total_count))
    else:
        unread_books.append((book_id, name, 0))

read_books.sort(key=lambda x: int(x[0]))
unread_books.sort(key=lambda x: int(x[0]))

# =============================
# 5. 打印最终结果
# =============================
print("=" * 50)
print(f" 已读书籍：{len(read_books)} 本")
print(f" 未读书籍：{len(unread_books)} 本")
print("=" * 50)

print("\n【已读清单 (去重并统计总次数)】")
for bid, name, total_count in read_books:
    if total_count > 1:
        print(f"{bid}  {name}  (x{total_count})")
    else:
        print(f"{bid}  {name}")

print("\n【未读清单】")
for bid, name, total_count in unread_books:
    print(f"{bid}  {name}")