from algorithms.search_function import search_functions
from utils.data_loader import load
from utils.analysis import analyze_search_performance, plot_results
from utils.random_data_generator import generate_random_data
import sys

def main():
    algorithms = ['avl tree', 'sequential', 'binary tree']
    keys = ['present', 'absent']
    types = ["ordered", "unordered"]
    sizes = [100, 500, 1000, 5000, 10000]

    sys.setrecursionlimit(max(sizes) + 500)

    for algorithm in algorithms:
        print(f"Algorithm: {algorithm}")

        for key in keys:

            for data_type in types:
                time_results = {algorithm: []}
                comparison_results = {algorithm: []}

                for size in sizes:
                    filename = f"data/data_{data_type}_{size}.csv"

                    generate_random_data(
                        num_records=size, data_type=data_type, output_file=filename)

                    data = load(algo=algorithm, filename=filename)

                    avg_time, avg_comparisons = analyze_search_performance(
                        data, search_functions[algorithm], key_type=key)

                    time_results[algorithm].append(avg_time)
                    comparison_results[algorithm].append(avg_comparisons)

                plot_results(sizes, time_results, f"Average Time vs Data Size - {data_type} - Key {key}",
                             "Time (seconds)", f"reports/{algorithm}/time_analysis_{data_type}_{key}.png", decimal_places=7)

                plot_results(sizes, comparison_results, f"Average Comparisons vs Data Size - {data_type} - Key {key}",
                             "Number of Comparisons", f"reports/{algorithm}/comparison_analysis_{data_type}_{key}.png", decimal_places=2)


if __name__ == "__main__":
    main()
