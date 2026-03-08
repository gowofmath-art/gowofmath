# input() 函數 讓使用者在終端機輸入資料

# 取得使用者輸入的資料

user_input = input("輸入數字:")
print(type(user_input))


# 將使用者輸入強制轉型成 int
user_input = int(user_input)
print(type(user_input))
total = user_input + 100
print(total)
#ctrl + ` 打開終端機
