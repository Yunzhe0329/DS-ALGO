#字首是母音 -> 在單字的結尾加上"way"
#不是母音 -> 把字首挪到結尾並加上"ay"

def pig_latin(word):
    if word[0] in "aeiou":
        return word+"way"
    else:
        return word[1:]+word[0]+"ay"
print(pig_latin("python"))
print(pig_latin("air"))
#Note : Python切片： 字串[起始索引, 終點索引（不包含）]
test = "computer"
print(test[3:6])
#Python 的字串是immutable 不可更改的
test2 = "Python"
# test2[0] = "x" #TypeError: 'str' object does not support item assignment

#執行assingnment時不會更改原本字串內容，而是組合成新的字串
print(id(test2))#4368144480
test2 = test2+"Workout"
print(id(test2))#4368607088

#f-string字串格式化的用法
def pig_latinf(word):
    if word[0] in "aeiou":
        return (f'{word}way')
    else:
        return (f'{word[1:]}{word[0]}ay')
print(pig_latinf("apple"))