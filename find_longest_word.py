def find_lonest_word(filepath):
    longest = ''
    with open(filepath) as f:
        for line in f:
            for word in line.replace('.', '').split():
                if len(word) > len(longest):
                    longest = word
    return longest
print(find_lonest_word(r'/Users/zacksiao/Desktop/DS-ALGO/longest_word.txt'))

# 用 set 來整理並找出最長單字
def find_lonest_word_with_set(filepath):
    words = set()
    with open(filepath) as f:
        for line in f:
            words.update(line.replace('.', '').split())
        return sorted(words, key = len)[-1]
print(find_lonest_word_with_set(r'/Users/zacksiao/Desktop/DS-ALGO/longest_word.txt'))
