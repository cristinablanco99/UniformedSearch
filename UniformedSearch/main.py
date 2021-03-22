graph = {
    'H' : ['P','D','M'],
    'P' : ['N'],
    'D' : ['L','E'],
    'M' : ['J','C'],
    'N' : ['I','K','O'],
    'L' : ['Q','R','G'],
    'E' : [],
    'J' : [],
    'C' : [],
    'I' : [],
    'K' : ['F','B'],
    'O' : [],
    'Q' : ['A'],
    'R' : [],
    'G' : [],
    'F' : [],
    'B' : [],
    'A' : []
} # Declaring our graph as a ser of Arrays

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node,searchedNode):
    """
    Deep First Search Method
    :param visited: a list of already visited nodes
    :param graph: whole graph with all nodes
    :param node: current node were we are located
    :param searchedNode: node we are looking for
    :return:
    """
    if node == searchedNode:
        print (node)
        print("The node you are looking for has been found:" + node)
        quit()


    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour,searchedNode)

    if(len(visited)==len(graph)):
        print("Node NOT FOUND")
        quit()

def extractFirst(lst):
    """
    Method to obtain the first element of a Graph
    :param lst: a list that contains the graph
    :return: First element in the list
    """
    return [item[0] for item in lst][0]

# Call to DFS Funcion, establishing H as our first Node and A as the Node we are looking for
print("---Deep First Search---")
print('Which node are you searching for?')
node=input()
dfs(visited, graph, extractFirst(graph), node.upper())
