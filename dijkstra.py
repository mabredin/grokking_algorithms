from typing import Optional


graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['finish'] = 3
graph['c']['d'] = 6
graph['d'] = {}
graph['d']['finish'] = 1
graph['finish'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['finish'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['finish'] = None

processed = []


def find_lowest_cost() -> None:
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()


def find_lowest_cost_node() -> Optional[str]:
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def create_path() -> str:
    string = 'finish'
    node = 'finish'
    while node != 'start':
        string = f'{parents[node]} --> ' + string
        node = parents[node]
    return string


find_lowest_cost()
print(f'Наименьшая стоимость = {costs["finish"]}')
print(f'Кратчайший путь: {create_path(parents)}')
