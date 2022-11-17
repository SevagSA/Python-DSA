'''
Breadth First Search implementation on a graph
'''
from collections import deque


def bfs(graph, source):
    visited = set()  # visited nodes
    bfs_traversal = []  # the BFS traversal result
    queue = deque()

    # push the root node to the queue and mark it as visited
    queue.append(source)
    visited.add(source)

    # while queue is not empty
    while queue:
        # pop first node of the queue and add it to bfs_traversal
        curr_node = queue.popleft()
        bfs_traversal.append(curr_node)

        # evaluate all neighors of curr_node
        for neighbor_node in graph[curr_node]:
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                queue.append(neighbor_node)
    return bfs_traversal


def main():
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'A', 'E'],
        'E': ['B', 'D']
    }
    print(f'BFS: {bfs(graph, input("Enter source node: "))}')


if __name__ == '__main__':
    main()
