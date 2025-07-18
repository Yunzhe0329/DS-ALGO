def wordGenerator(filepath, max_words):
    index = 0
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                if index >= max_words:
                    break #也可以使用 return  -> return 後面沒寫東西，會自動回傳 None
                yield word.replace('.', '')
                index += 1
ten_words = wordGenerator(r'/Users/zacksiao/Desktop/DS-ALGO/longest_word.txt' ,10)

for word in ten_words:
    print(word)