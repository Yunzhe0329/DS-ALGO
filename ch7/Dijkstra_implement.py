
graph = {
    'start':{'a': 6, 'b': 2},
    'a':{'fin': 1},
    'b':{'a': 3, 'fin': 5},
    'fin': {}
}



#build cost hash map
infinity = float("inf")
costs = {
    'a' : 6,
    'b' : 2,
    'fin' : infinity
}

#build parent node hash map
parents = {
    'a' : 'start', 
    'b' : 'start',
    'fin' : None
}


#create a list obj to store the node that has been processed
processed = []


#dijkastra algo
def find_the_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_the_lowest_cost_node(costs)
while node is not None:
    cost= costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]#處理相鄰的節點
        if new_cost < costs[n]:
            costs[n] = new_cost #更新目前節點的抵達成本
            parents[n] = node # 此節點會新增成為相鄰節點的父節點
    processed.append(node)
    node = find_the_lowest_cost_node(costs)
print(costs)
# zacksiao@ZackdeMacBook-Air DS-ALGO % /usr/local/bin/python3 /Users/zacksiao/Desktop/DS-ALGO/ch7/Dijkstra_implement.py
# {'a': 5, 'b': 2, 'fin': 6}        