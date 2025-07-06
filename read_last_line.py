# file 物件即資源管理器(Context manager), with 是專門搭配的語法，會自動呼叫相關的method 來取得和釋放資源，並可以攔截潛在錯誤
with open(r'/Users/zacksiao/Desktop/DS-ALGO/example_log.txt', 'r') as file:
    for line in file:
        last_line = line
print(last_line)

def read_last_line(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            pass
    return line
print(read_last_line(r'/Users/zacksiao/Desktop/DS-ALGO/example_log.txt'))

#without using with
f = open(r'/Users/zacksiao/Desktop/DS-ALGO/example_log.txt')
try:
    for line in f:
        print(line)
finally:
    f.close()
