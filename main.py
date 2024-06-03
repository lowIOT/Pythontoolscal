# 電卓の機能を持つPythonプログラム

# 足し算
def add(x, y):
    return x + y

# 引き算
def subtract(x, y):
    return x - y

# 掛け算
def multiply(x, y):
    return x * y

# 割り算
def divide(x, y):
    if y == 0:
        return "エラー: 0で割ることはできません"
    else:
        return x / y

print("選択してください:")
print("1. 足し算")
print("2. 引き算")
print("3. 掛け算")
print("4. 割り算")

while True:
    choice = input("選択(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("最初の数を入力してください: "))
        num2 = float(input("2番目の数を入力してください: "))

        if choice == '1':
            print("結果:", add(num1, num2))
        elif choice == '2':
            print("結果:", subtract(num1, num2))
        elif choice == '3':
            print("結果:", multiply(num1, num2))
        elif choice == '4':
            print("結果:", divide(num1, num2))
        
        break
    else:
        print("無効な入力です。正しい選択をしてください。")
