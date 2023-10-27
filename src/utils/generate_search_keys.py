import random


def generate_search_keys(data, num_keys=15):
    """Generate random search keys (both present and absent in the data)."""
    present_keys = [item[0] for item in data]
    absent_keys = list(set(range(1, 10**6)) - set(present_keys))
    search_keys = random.sample(present_keys, num_keys // 2) + \
        random.sample(absent_keys, num_keys - (num_keys // 2))
    return search_keys
