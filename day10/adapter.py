import networkx as nx

def find_diffs(adapters: list) -> tuple:
    diffs = {}
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    return diffs


def find_arrangements(adapters: list) -> int:
    graph = to_graph(adapters)
    diGraph = nx.DiGraph()
    diGraph.add_edges_from(graph)
    return len(list(nx.all_simple_paths(diGraph, graph[0][0], graph[-1][0])))


def to_graph(adapters: list) -> list:
    sorted_adapters = adapters.copy()
    sorted_adapters.append(0)
    sorted_adapters.sort()
    sorted_adapters.append(sorted_adapters[-1] + 3)
    print(sorted_adapters)

    graph = []
    for i in range(len(sorted_adapters) -1):
        j=i+1
        while j < len(sorted_adapters) and sorted_adapters[j] - sorted_adapters[i] <=3:
            graph.append((sorted_adapters[i], sorted_adapters[j]))
            j+=1
    print(graph)
    return graph

if __name__ == '__main__':
    with open('input.txt') as data:
        adapters = [int(adapter) for adapter in data.readlines()]
        print(find_arrangements(adapters))
