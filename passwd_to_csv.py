import csv
# 讀寫 csv 檔
# 利用 csv.reader() 將檔案轉成 csv 的格式
with open('passwd.cfg', 'r') as f:
    csv_reader = csv.reader(f, delimiter = ':')
    for line in csv_reader:
        print(line)
# 寫入 csv -> csv.writer()
users = [
    ['lerner', 'x', '1000', '1000', 'Reuven Lerner', '/home/lerner', '/bin/bash'],
    ['alice', 'x', '1001', '1001', 'Alice Wonderland', '/home/alice', '/bin/zsh'],
    ['bob', 'x', '1002', '1001', 'Bob Builder', '/home/bob', '/bin/bash'],
    ['charlie', 'x', '1003', '1002', 'Charlie Brown', '/home/charlie', '/bin/sh'],
    ['diana', 'x', '1004', '1002', 'Diana Prince', '/home/diana', '/bin/bash'],
    ['eve', 'x', '1005', '1003', 'Eve Hacker', '/home/eve', '/usr/sbin/nologin']
]
with open('passwd.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter = '\t') # 分行符號設為 TAB
    for line in users:
        csv_writer.writerow(line) #替換成.writerows(data) 就可一次寫多行，不需用 for-loop
def passwd_to_csv(passwd_filepath, csv_filepath):
    with open(passwd_filepath, 'r') as f_read,open(csv_filepath, 'w') as f_write:
            csv_reader = csv.reader(f_read, delimiter = ':')
            csv_writer = csv.writer(f_write, delimiter = '\t', lineterminator = '\n')

            for line in csv_reader:
                csv_writer.writerow([line[0], line[2]])
passwd_to_csv(r'/Users/zacksiao/Desktop/DS-ALGO/passwd.cfg', r'/Users/zacksiao/Desktop/DS-ALGO/passwd_final_csv.csv')

