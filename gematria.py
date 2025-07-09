# part 1 build a hashmap
import string
print(string.ascii_lowercase) #abcdefghijklmnopqrstuvwxyz
# 透過 list 中 enumerate() 去回傳對應的 key-value
print(list(enumerate(string.ascii_lowercase, 1)))
def gematria_dict():
    return {char:index for index, char in enumerate(string.ascii_lowercase, 1)}
GEMATRIA = gematria_dict()
def gematria_value(word):
    return sum(GEMATRIA[char] for char in word.lower() if char in GEMATRIA)

def gematria_equal_words(input_word, filepath):
    input_value = gematria_value(input_word)
    with open(filepath, 'r') as f:
        return [word
                for line in f
                for word in line.lower().split()
                if input_value == gematria_value(word)]
print(gematria_equal_words('programming', r'/Users/zacksiao/Desktop/DS-ALGO/pg11.txt'))
print(gematria_value('explanation'))
print(gematria_value('puzzling'))
print(gematria_value('programming'))
#output :
#abcdefghijklmnopqrstuvwxyz
#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (12, 'l'), (13, 'm'), (14, 'n'), (15, 'o'), (16, 'p'), (17, 'q'), (18, 'r'), (19, 's'), (20, 't'), (21, 'u'), (22, 'v'), (23, 'w'), (24, 'x'), (25, 'y'), (26, 'z')]
[#'puzzling', 'puzzling', 'puzzling', 'puzzling', 'explanation.', 'explanation;', 'ridiculous', 'upsetting', 'distributed:', 'distributed', 'explanation', 'explanation.', 'distributed', 'unsolicited', 'professor', 'distributed']
#131
#131
#131
