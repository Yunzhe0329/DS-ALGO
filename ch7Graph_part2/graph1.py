graph = {
    'start':{'a': 2, 'b': 5},
    'a':{'b': 8, 'd': 7},
    'b':{'c': 4, 'd': 2},
    'c':{'d': 6, 'fin': 3},
    'd':{'fin': 1},
    'fin':{}
}
infinity = float("inf")
costs = {
    'a': 2,
    'b': 5,
    'c': infinity,
    'd': infinity,
    'fin': infinity
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
# zacksiao@ZackdeMacBook-Air DS-ALGO % /usr/local/bin/python3 /Users/zacksiao/Desktop/DS-ALGO/ch7/graph1.py
# {'a': 2, 'b': 5, 'c': 9, 'd': 7, 'fin': 8}