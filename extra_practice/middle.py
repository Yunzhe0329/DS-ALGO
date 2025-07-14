def count_vowel(s: str) -> int:
    vowel = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for word in s.lower():
        if word in vowel:
            count+=1
    return  count
print(count_vowel("Hello World"))


def count_words_starting_with_vowel(s : str) -> int:
    vowel = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for word in s.lower().split():
        if word and word[0] in vowel:
            count+=1
    return count

print(count_words_starting_with_vowel("Apple is a fruit and orange too"))

from collections import Counter
def most_common_vowel(s : str) -> tuple[str,  int]:
    vowels = {'a':0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    counter = Counter(c for c in s.lower() if c in vowels)

    if not counter:
        return (None, 0)
    return counter.most_common(1)[0]
print(count_words_starting_with_vowel("hello world and universe"))
