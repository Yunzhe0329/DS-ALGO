#Python內建hex()，可以將10進位轉成16進位
print(hex(42))
#換算的方式，42(2a) = 16^1*2 + 16^0 * 10，可觀察到power的值和字串的index相反，所以我們將字串Reverse即可
for t in reversed("Python"):
    print(t)
#我們需要同時取得 index 和 值 => enumerate()可以同時做到這兩件事
for index, char in enumerate(reversed("Python")):
    print(index, char)
#怎麼處理十六進位 A~F的值？ => 轉ASCII => 減去ord("A")再加上10,轉換成10-15的值
print(ord("A"))
print(ord("F"))

#十六進制轉十進制的函式
def hex_to_dec():
    hexnum = input("請輸入十六進位數字：")
    decnum = 0
    
    for power, digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            digit_num = int(digit)
        else:
            digit_num = ord(digit.upper()) - ord("A") + 10
        decnum+= digit_num * 16**power
    print("十進位的結果:", decnum)
hex_to_dec()

#Note : int()也能做到同樣的效果，第二個參數代表字串內的數字是幾進位
hexnum = input("請輸入十六進位的數字:")
decnum = int(hexnum, 16)
print("十進位的結果:", decnum)