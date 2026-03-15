# 計算幾次方



# 簡單斷句

class FileEditor:
    # 建構函式 > 在物件建立的時候 要給 file_path
    def __init__(self,file_path):
        self.file_path = file_path

    # 定義 Method
    def get_text(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            texts = f.read()
        return texts
    
    def insert_text(self,text):
        with open(self.file_path,"a",encoding="utf-8") as f:
            f.write(text)


# 折扣後金額
def after_discount(x,y=2000,z=200):
    if x <= 0:
        return 0
    if x >= y:
        x = x-z*(x//y)
    # return x

    print(f"折扣後:{x}元")
    return x



# print(f"myModule 的 __name__: {__name__}")
if __name__ == "__main__":
    # 測試
    after_discount(3208)





# 測試模組


