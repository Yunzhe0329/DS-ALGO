import os
import json
print(os.listdir(r'/Users/zacksiao/desktop/ds-algo/classes'))
# 可以搭配 endswith()去過濾檔案 
for filename in os.listdir(r'/Users/zacksiao/desktop/ds-algo/classes'):
    if filename.endswith('.json'):
        print(filename)
#結合練習
from collections import defaultdict

def print_scores(filepath):
    with open(filepath) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
        print('班級', record['class'])

        for record in record['scores']:
            for subject, score in record.items():
                result[subject].append(score)
    for subject, scores in result.items():
        print('科目', subject)
        print('\t最高分', max(scores))
        print('\t最低分', min(scores))
        print('\t平均分', sum(scores)/len(scores))
def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案 : ', filename)
            print_scores(os.path.join(dirname, filename))
print_dir_scores(r'/Users/zacksiao/desktop/ds-algo/classes')
    
# pathlib 模組來走訪資料夾
import pathlib

p = pathlib.Path(r'/Users/zacksiao/desktop/ds-algo/classes') #建立 pathlib 的 PosixPath 物件
for filename in p.iterdir(): #走訪這個物件會得到包含路徑的檔名
    print(filename)
#print_dir_scores 函式改寫
def print_dir_scores_with_pathlib(folderpath):
    p = pathlib.Path(folderpath)
    for file in p.iterdir():
        print('讀取檔案 : ', file)
        print_scores(file)
print_dir_scores_with_pathlib(r'/Users/zacksiao/desktop/ds-algo/classes')
# 更簡單的寫法 glob 模組
import glob
for file in glob.glob(r'/Users/zacksiao/desktop/ds-algo/classes/*.json'):#要記得加上你要過濾的檔案
    print(file) 
def print_dir_scores_with_glob(folderpath):
    for filename in glob.glob(folderpath):
        print('檔案名稱 : ', filename)
        print_scores(filename)
print_dir_scores_with_glob(r'/Users/zacksiao/desktop/ds-algo/classes/*.json')
