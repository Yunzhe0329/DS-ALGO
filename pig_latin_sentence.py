def pig_latin_sentence(sentence):
    output = []
    for word in sentence.lower().split():#把每個單字分開單獨處理
        if word[0] == "aeiou":
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)
print(pig_latin_sentence('This is a test'))           