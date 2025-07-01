#以前網路論壇常用的加密手段，將每個英文字母換成該字母往後數13個字母
# ord(str)可以轉換成ASCII碼，幫助我們做計算
print(ord('a'))

def pot13(word):
    output = []
    for i in word.lower():
        new_ord = ord(i) + 13
        if new_ord > ord('z'):
            new_ord-=26
        output.append(chr(new_ord))
    return ''.join(output)

print(pot13("apple"))