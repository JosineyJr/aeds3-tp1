import random


def generate_search_keys_for_list(data, num_keys=15):
    keys_present = random.sample([item[0] for item in data], num_keys)
    
    keys_absent = []
    while len(keys_absent) < num_keys:
        random_key = random.randint(1, 10**9)
        if random_key not in keys_present:
            keys_absent.append(random_key)
  

    return keys_present, keys_absent

def generate_search_keys_for_tree(tree, num_keys=15):
    keys_present = random.sample(tree.get_all_keys(), num_keys)

    keys_absent = []
    while len(keys_absent) < num_keys:
        random_key = random.randint(1, 10**9)
        item, _ = tree.search(random_key)
        if not item:
            keys_absent.append(random_key)

    return keys_present, keys_absent


def generate_search_keys(data_or_tree, num_keys=15):
    if isinstance(data_or_tree, list):
        return generate_search_keys_for_list(data_or_tree, num_keys)
    else:
        return generate_search_keys_for_tree(data_or_tree, num_keys)
