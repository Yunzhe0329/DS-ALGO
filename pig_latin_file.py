def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
def pl_file(filepath):
    with open(filepath, 'r') as f:
        return ''.join([pl_word(word.lower().replace('.', ''))
                        for line in f
                            for word in line.split()])

print(pl_file(r'/Users/zacksiao/Desktop/DS-ALGO/pig_latin_practice.txt'))
