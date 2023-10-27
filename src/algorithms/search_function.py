from algorithms.sequential import sequential_search

search_functions = {'avl tree': lambda tree, x: tree.search(x), 'binary tree': lambda tree, x: tree.search(
    x), 'sequential': lambda list, x: sequential_search(list, x)}
