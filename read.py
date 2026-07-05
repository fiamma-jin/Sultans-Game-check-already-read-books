import json

# 读取文件
with open("cards_fixed.json", "r", encoding="utf-8") as f:
    cards_data = json.load(f)

with open("round_146.json", "r", encoding="utf-8") as f:
    round_data = json.load(f)

# -----------------------------
# 找出所有 title == "书籍"
# -----------------------------
books = {}

for key, card in cards_data.items():
    if card.get("title") == "书籍":
        books[card["id"]] = card["name"]

# -----------------------------
# 当前存档拥有的卡
# -----------------------------
owned_ids = set()

for card in round_data["cards"]:
    owned_ids.add(card["id"])

# -----------------------------
# 分类
# -----------------------------
read_books = []
unread_books = []

for book_id, name in books.items():
    if book_id in owned_ids:
        read_books.append((book_id, name))
    else:
        unread_books.append((book_id, name))

read_books.sort()
unread_books.sort()

# -----------------------------
# 输出
# -----------------------------
print("=" * 50)
print(f"书籍总数：{len(books)}")
print(f"已读：{len(read_books)}")
print(f"未读：{len(unread_books)}")
print("=" * 50)

print("\n【已读书籍】")
for bid, name in read_books:
    print(f"{bid}  {name}")

print("\n【未读书籍】")
for bid, name in unread_books:
    print(f"{bid}  {name}")