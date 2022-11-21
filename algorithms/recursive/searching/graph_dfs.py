'''
DFS implementation on a Graph
'''


class Node:
    '''
    Assume the Node class provides all the used/necessary methods
    '''
    pass

``
def dfs(node: Node, visited: set, goal: int) -> bool:
    if not node:
        return False

    if node.val == goal:
        return True

    for neighbour in node.get_neighbours():
        if neighbour in visited:
            continue
        visited.add(neighbour)
        if dfs(neighbour, visited, goal):
            return True
    return False  # if value does not exist in graph
