# Dijkstra cannot handle negative weights => bellman-ford can!
graph = {
    'start':{'a': 2, 'b':2},
    'a' : {'b': 2},
    'b' : {'c' : 2, 'fin': 2},
    'c' : {'a': -1, 'fin': 2},
    'fin':{}
}

infinity = float('inf')
costs = {
    'a' : 2,
    'b' : 2,
    'c' : infinity, 
    'fin' : infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []

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
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_the_lowest_cost_node(costs)

print(costs)
# zacksiao@ZackdeMacBook-Air DS-ALGO % /usr/local/bin/python3 /Users/zacksiao/Desktop/DS-ALGO/ch7/graph3.py
# {'a': 2, 'b': 2, 'c': 4, 'fin': 4}