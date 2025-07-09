def passwd_to_dict(filepath):
    with open(filepath, 'r') as f:
        d = {words[0]:words[2] for words in [line.split(':') for line in f]}
    return d
print(passwd_to_dict(r'/Users/zacksiao/Desktop/DS-ALGO/passwd.cfg'))
