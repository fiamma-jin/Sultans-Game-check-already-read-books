# 【苏丹的游戏】已读书籍情况查看及全部书籍清单
文件介绍：

    1. read.py  是查询读了多少书的程序
    2. 书籍清单.csv是当前游戏内全部可读物
    3. round_xxx.json  是玩家的进度数据（这里需要替换成自己的
    
    4. cards.json 是游戏自带的数据
    5. 为了方便python直接读取已经生成了cards_fixed.json（删除了所有报错的备注行和一些符号错误，没有改数据内容）。但还是存在很多废弃书籍所以最后还是使用csv文件去比对了。

文件地址：

cards.json在以下路径查找
    
      ...\steam\steamapps\common\Sultan's Game\Sultan's Game_Data\StreamingAssets\config\cards.json
玩家自己的进度数据,这里找距离你保存时间最近的就好了
    
       ...\Users\...\AppData\LocalLow\DoubleCross\SultansGame\SAVEDATA\76561198900100722\round_xxx.json

使用教程：

用自己的round_xxx.json 文件名替换代码里我的游戏数据文件名就可以了

<img width="361" height="160" alt="image" src="https://github.com/user-attachments/assets/53835dd1-71ce-4134-8253-0bbfb0535275" />


可以返回读到了哪些书，如下图

<img width="311" height="224" alt="image" src="https://github.com/user-attachments/assets/079daf31-d489-4082-9640-7653e13f28dd" />


游戏不加新书的话直接看excel文件就行了

PS：本人代码水平很差，大家查着玩玩算了
555来自一个不甘心一局内无法读完所有书的女人 :(
