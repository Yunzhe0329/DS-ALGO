
import pprint
def passwd_to_dict(filepath):
    users = {}
    with open(filepath) as f:
        for line in f:
            user_info = line.split(':')
            users.update({user_info[0]:user_info[2]})
        return users
print(passwd_to_dict(r'/Users/zacksiao/Desktop/DS-ALGO/passwd.cfg'))
pprint.pprint(passwd_to_dict(r'/Users/zacksiao/Desktop/DS-ALGO/passwd.cfg'))
