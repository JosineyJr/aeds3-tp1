def sequential_search(data, key):
    comparisons = 0
    for item in data:
        comparisons += 1
        if item[0] == key:
            return item, comparisons
    return None, comparisons
