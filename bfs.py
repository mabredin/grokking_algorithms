from collections import deque


def person_is_seller(name: str) -> bool:
    return name in mango_seller


def find_mango_seller(name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

mango_seller = ['jonny', 'claire']

print(find_mango_seller('you'))
