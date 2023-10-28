from time import time
from utils.generate_search_keys import generate_search_keys
import matplotlib.pyplot as plt
import os


def analyze_search_performance(data, search_function, key_type='present'):
    keys_present, keys_absent = generate_search_keys(
        data_or_tree=data, num_keys=15)

    if key_type == 'present':
        keys = keys_present
    else:
        keys = keys_absent

    total_comparisons = 0
    total_time = 0

    for key in keys:
        start_time = time()
        _, comparisons = search_function(data, key)
        end_time = time()

        total_time += (end_time - start_time)
        total_comparisons += comparisons

    avg_time = total_time / len(keys)
    avg_comparisons = total_comparisons / len(keys)

    return avg_time, avg_comparisons


def plot_results(sizes, results, title, ylabel, save_as, decimal_places, color='red'):
    plt.figure(figsize=(16, 8), dpi=100)

    for algo, values in results.items():
        plt.plot(sizes, values, label=algo, marker='o', color=color)

        for i, value in enumerate(values):
            plt.annotate(f'{value:.{decimal_places}f}', (
                sizes[i], value), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title(title)
    plt.xlabel('Quantidade de chaves')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)

    os.makedirs(os.path.dirname(save_as), exist_ok=True)

    plt.xticks(sizes)

    plt.savefig(save_as, format='png', dpi=100)
    plt.close()
