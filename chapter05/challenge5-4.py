My_favorite_color = {"1":"紫",
                     "2":"黄色",
                     "3":"水色",
                     "4":"赤色",
                     "5":"青色"}

n = input("私の好きな色ランキングです。数字を入力してください:")
if n in My_favorite_color:
    My_favorite_color = My_favorite_color[n]
    print(My_favorite_color)
else:
    print("ランキング外です")
