from collections import deque


def binary_search(list, item):
    # бинарный поиск
    # a = [1, 3, 5, 7, 9]
    # print(binary_search(a, 11))

    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def find_smallest(arr):
    # нахождение минимума
    smallest_index = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    # сортировка выбором
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def quick_sort(arr):
    # быстрая сортировка
    # b = [5, 3, 6, 2, 10, 1, 0, 900]
    # print(quick_sort(b))
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def search(name, graph, f):
    # поиск по графу в ширину
    # graph = dict()
    # graph['you'] = ['alice', 'bob', 'claire']
    # graph['alice'] = ['peggy']
    # graph['bob'] = ['anue', 'peggy']
    # graph['claire'] = ['tomm', 'jonny']
    # graph['anue'] = []
    # graph['peggy'] = []
    # graph['tomm'] = []
    # graph['jonny'] = []
    # def func(s):
    #     a = s
    #     return s[-1] == 'm'
    #
    # print(search('you', graph, func))
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if f(person):
                print('Here it is: ' + person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def depth_first_search():
    # поиск по графу в глубину
    # depth_first_search()
    # print('Parents: ' + str(parents))
    # print('Costs: ' + str(costs))


    graph = dict()
    graph['start'] = dict()
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = dict()
    graph['a']['fin'] = 1
    graph['b'] = dict()
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = dict()
    infinity = float('inf')
    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity
    parents = dict()
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        neighbors = graph[node]
        cost = costs[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

def run():
    pass

if __name__ == '__main__':
    run()






