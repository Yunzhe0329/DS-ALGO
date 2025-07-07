# 我們要做 4 件事：行數、字元數、單字數、不重複單字數  
def wordcount(filepath):
    result = {
        'Characters' : 0,
        'Words' : 0,
        'Unique_words' : 0,
        'Lines' : 0
    }
    unique_words = set()
    with open(filepath) as f:
        for line in f:
            words = line.split()
            result['Lines']+=1
            result['Characters']+= len(line)
            result['Words']+= len(words)
            unique_words.update(words)
        result['Unique_words'] = len(unique_words)
    for key, value in result.items():
        print(f'{key} : {value}')
wordcount(r'/Users/zacksiao/Desktop/DS-ALGO/self_describing_text.txt')
            
