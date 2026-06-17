number = [8, 15, 24, 1, 23,]

while True:
    xyz = input("数字を入力してください！qで終了")
    if xyz == "q":
        break
    try:
        xyz = int(xyz)
    except valueError:
        print("数字かqを入力してください")
    if xyz in number:
        print("正解！")
    else:
        print("不正解！")
