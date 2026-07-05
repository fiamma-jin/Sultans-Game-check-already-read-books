
文件介绍：

    1. cards.json 是游戏自带的数据
    2. 为了方便python直接读取已经生成了cards_fixed.json（删除了所有报错的备注行和一些符号错误，没有改数据内容）
    3. read.py  是查询读了多少书的程序
    4. round_xxx.json  是玩家的进度数据（这里需要替换成自己的

    5. booklist.py 是导出所有书的程序
    6. 书籍清单.xlsx是当前cards.json中提取出的全部书籍

文件地址：

如需替换最新的cards.json, 可以去以下路径查找
    
      ...\steam\steamapps\common\Sultan's Game\Sultan's Game_Data\StreamingAssets\config\cards.json
玩家自己的进度数据,这里找距离你保存时间最近的就好了
    
       ...\Users\...\AppData\LocalLow\DoubleCross\SultansGame\SAVEDATA\76561198900100722\round_xxx.json

使用教程：

用自己的round_xxx.json 文件名替换代码里我的游戏数据文件名就可以了

<img width="388" height="125" alt="image" src="https://github.com/user-attachments/assets/b391db87-e19f-4520-ac61-6c868282c176" />

可以返回读到了哪些书，如下图

<img width="312" height="173" alt="8cb341076d036bbfef63caff3610b46b" src="https://github.com/user-attachments/assets/29072cd1-547d-466c-bda8-0ff7464ad66d" />

书籍清单的话是booklist.py直接根据数据跑出来的，游戏不加新书的话直接看excel文件就行了

PS：本人代码水平很差，大家查着玩玩算了
555来自一个不甘心一局内无法读完所有书的女人 :(
