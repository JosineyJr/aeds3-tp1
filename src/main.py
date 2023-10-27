import sys

from algorithms.search_function import search_functions
from utils.data_loader import load
from analysis.analysis import analyze_search_performance, plot_results
from utils.random_data_generator import generate_random_data
from analysis.generate_pdf import generate_pdf


def main():
    algorithms = ['sequential', 'binary tree', 'avl tree']
    search_types = ['Presente', 'Não Presente']
    file_types = ["Ordenado", "Não Ordenado"]
    sizes = [100, 500, 1000, 5000, 10000, 15000]

    sys.setrecursionlimit(max(sizes) + 500)

    reports_qty = (len(search_types) * len(file_types) * len(sizes))

    pdf_report_data = [None] * reports_qty

    for algorithm in algorithms:
        print(f"Algorithm: {algorithm}")

        for search_index, search_type in enumerate(search_types):

            for file_type_index, file_type in enumerate(file_types):
                time_results = {algorithm: []}
                comparison_results = {algorithm: []}

                for size_index, size in enumerate(sizes):
                    filename = f"data/data_{file_type}_{size}.csv"

                    generate_random_data(
                        num_records=size, data_type=file_type, output_file=filename)

                    data = load(algo=algorithm, filename=filename)

                    avg_time, avg_comparisons = analyze_search_performance(
                        data, search_functions[algorithm], key_type=search_type)

                    time_results[algorithm].append(avg_time)
                    comparison_results[algorithm].append(avg_comparisons)

                    report_index = (
                        size_index * (len(search_types) + len(file_types))) + ((file_type_index*2)+search_index)

                    if not pdf_report_data[report_index]:
                        pdf_report_data[report_index] = [
                            size, file_type, search_type]

                    pdf_report_data[report_index] += [
                        f'{avg_comparisons:.2f}', f'{avg_time:.7f}']

                plot_results(sizes, time_results, f"Average Time vs Data Size - {file_type} - Key {search_type}",
                             "Time (seconds)", f"reports/{algorithm}/time_analysis_{file_type}_{search_type}.png", decimal_places=7)

                plot_results(sizes, comparison_results, f"Average Comparisons vs Data Size - {file_type} - Key {search_type}",
                             "Number of Comparisons", f"reports/{algorithm}/comparison_analysis_{file_type}_{search_type}.png", decimal_places=2)

    generate_pdf(analysis_data=pdf_report_data, sizes_qty=len(sizes))


if __name__ == "__main__":
    main()
