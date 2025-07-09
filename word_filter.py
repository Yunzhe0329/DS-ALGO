# 能讀取文字檔，並將其中含有三個以上母音字母的單字（不含句點）篩選出來用 list 回傳
def word_filter(filepath):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filepath, 'r') as f:
        words = [word.replace('.', '')
                  for line in f
                    for word in line.split()
                        if len(set(word) & vowels) >= 3]
    return words
print(word_filter(r'/Users/zacksiao/Desktop/DS-ALGO/pig_latin_practice.txt'))
