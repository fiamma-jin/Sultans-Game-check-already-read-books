import json
import pandas as pd

# 读取卡片数据文件
with open("cards_fixed.json", "r", encoding="utf-8") as f:
    cards_data = json.load(f)

# -----------------------------
# 1. 提取所有 title 为 "书籍" 的卡片
# -----------------------------
books_data = []

for key, card in cards_data.items():
    # 只筛选 title 为 "书籍" 的卡片
    if card.get("title") == "书籍":
        # 提取需要的字段
        book_info = {
            "书籍ID": card.get("id"),
            "书籍名称": card.get("name"),
            "书籍描述": card.get("text", ""),  # 如果没有text字段，就留空
            "稀有度": card.get("rare", 0)      # 顺便把稀有度也加上，方便筛选
        }
        books_data.append(book_info)

# -----------------------------
# 2. 转换为 DataFrame (表格)
# -----------------------------
df = pd.DataFrame(books_data)

# 如果提取到了数据，就导出 Excel
if not df.empty:
    # 按照稀有度降序排个序（可选）
    df = df.sort_values(by="稀有度", ascending=False)
    
    # 导出为 Excel 文件
    output_file = "书籍清单.xlsx"
    df.to_excel(output_file, index=False, engine="openpyxl")
    
    print(f"✅ 成功导出！共提取了 {len(df)} 本书籍。")
    print(f"📁 文件已保存为: {output_file}")
    
    # 在控制台预览前 5 行
    print("\n📖 预览前 5 本书：")
    print(df.head(5))
    
else:
    print("⚠️ 没有找到任何 title 为 '书籍' 的卡片，请检查 JSON 文件！")