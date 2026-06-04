def f(x):
    try:
        return float(x)
    except ValueError:
        print("数値に変換できません。")

x=("3.14")
print(x)

