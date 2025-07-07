import json
# json 物件
json_str = '{"math" : 90, "literature" : 80, "science" : 98 }'
# load()是用來讀取json檔案
# loads()是用來讀取json格式資料的字串
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))

with open(r'/Users/zacksiao/Desktop/DS-ALGO/9a.json', 'r') as f:
    print(json.load(f))

from collections import defaultdict

def print_scores(filepath):
    with open(filepath) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
        #print(result)
        print('班級', record['class'])
        for record in record['scores']:
            for subject, score in record.items():
                result[subject].append(score) #Defaultdict 的特性，自動建立 subject : []
                #print(result)
        for subject, scores in result.items():
            print('科目', subject)
            print('\t最高分', max(scores))
            print('\t最低分', min(scores))
            print('\t平均分', sum(scores)/len(scores))
print_scores(r'/Users/zacksiao/Desktop/DS-ALGO/9a.json')
