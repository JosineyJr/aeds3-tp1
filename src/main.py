# src/main.py

from algorithms.sequencial import sequential_search
from utils.data_loader import load_data_from_csv
from utils.analysis import analyze_search_performance, plot_results
from utils.random_data_generator import generate_random_data


def main():
    sizes = [100, 500, 1000, 5000, 10000]
    types = ["ordered", "unordered"]

    for data_type in types:
        time_results = {"Sequential": []}
        comparison_results = {"Sequential": []}

        for size in sizes:
            filename = f"data/data_{data_type}_{size}.csv"

            generate_random_data(
                num_records=size, data_type=data_type, output_file=filename)

            data = load_data_from_csv(filename)

            avg_time, avg_comparisons = analyze_search_performance(
                data, sequential_search)

            time_results["Sequential"].append(avg_time)
            comparison_results["Sequential"].append(avg_comparisons)

        plot_results(sizes, time_results, f"Average Time vs Data Size ({data_type})",
                     "Time (seconds)", f"reports/sequencial/time_analysis_({data_type}).png", decimal_places=5)

        plot_results(sizes, comparison_results, f"Average Comparisons vs Data Size ({data_type})",
                     "Number of Comparisons", f"reports/sequencial/comparison_analysis_({data_type}).png", decimal_places=2)


if __name__ == "__main__":
    main()
