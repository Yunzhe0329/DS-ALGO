#use hash map to build graph page 6-14
graph = {}
graph['You'] = ['Alice', 'Bob', 'Claire']
graph['Bob'] = ['Peggy', 'Anuj']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Thom', 'Jonny']
graph['Peggy'] = []
graph['Anuj'] = []
graph['Thom'] = []
graph['Jonny'] = []
# print(graph)
from collections import deque

def person_is_seller(name):
        return name[-1]=='m'
# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person+"是芒果經銷商")
#     else:
#         search_queue+=graph[person]

#加入避免重複判斷

def search(name):
        search_queue = deque()
        search_queue+= graph[name]
        searched = []
        while search_queue:
                person = search_queue.popleft()
                if person_is_seller(person):
                        print(person+"是芒果經銷商")
                else:
                        search_queue+=graph[person]
                        searched.append(person)
                        
search("You")