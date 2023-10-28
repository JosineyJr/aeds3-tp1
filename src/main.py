import sys
import os

from algorithms.search_function import search_functions
from utils.data_loader import load
from analysis.analysis import analyze_search_performance, plot_results
from utils.random_data_generator import generate_random_data
from analysis.generate_pdf import generate_pdf
from algorithms.binary_tree import BinaryTree


def main():
    algorithms = ['sequential', 'binary tree', 'avl tree']

    colors = ['red', 'green', 'blue']

    search_types = [{'code': 'present', 'name': 'Presente'},
                    {'code': 'absent', 'name': 'Não Presente'}]

    file_types = [{'code': 'ordered', 'name': 'Ordenado'},
                  {'code': 'unordered', 'name': 'Não Ordenado'}]

    sizes = [100, 500, 1000, 5000, 10000, 15000]

    sys.setrecursionlimit(max(sizes) + 500)

    reports_qty = (len(search_types) * len(file_types) * len(sizes))

    pdf_report_data = [None] * reports_qty

    imgs_path = []

    for algo_index, algorithm in enumerate(algorithms):
        print(f"Algorithm: {algorithm}")

        for search_index, search_type in enumerate(search_types):

            for file_type_index, file_type in enumerate(file_types):
                time_results = {algorithm: []}
                comparison_results = {algorithm: []}

                for size_index, size in enumerate(sizes):
                    filename = f"data/data_{file_type['code']}_{size}.csv"

                    if not os.path.exists(filename):
                        generate_random_data(
                            num_records=size, data_type=file_type['code'], output_file=filename)

                    data = load(algo=algorithm, filename=filename)

                    # if size == 15 and isinstance(data, BinaryTree):
                    #     tree_img_path = f"reports/{algorithm}_{file_type['code']}.png"
                    #     data.draw(tree_img_path)

                    avg_time, avg_comparisons = analyze_search_performance(
                        data, search_functions[algorithm], key_type=search_type['code'])

                    time_results[algorithm].append(avg_time)
                    comparison_results[algorithm].append(avg_comparisons)

                    report_index = (
                        size_index * (len(search_types) + len(file_types))) + ((file_type_index*2)+search_index)

                    if not pdf_report_data[report_index]:
                        pdf_report_data[report_index] = [
                            size, file_type['name'], search_type['name']]

                    pdf_report_data[report_index] += [
                        f'{avg_comparisons:.2f}', f'{avg_time:.8f}']

                time_analysis_img_path = f"reports/{algorithm}/time_analysis_{file_type['code']}_{search_type['code']}.png"
                comparison_analysis_img_path = f"reports/{algorithm}/comparison_analysis_{file_type['code']}_{search_type['code']}.png"

                imgs_path.append(time_analysis_img_path)
                imgs_path.append(comparison_analysis_img_path)

                plot_results(sizes=sizes, results=time_results, title=f"Tempo médio para encontrar a chave - {file_type['name']} - {search_type['name']}",
                             ylabel="Tempo (segundos)", save_as=time_analysis_img_path, decimal_places=8, color=colors[algo_index])

                plot_results(sizes=sizes, results=comparison_results, title=f"Nº médio de comparações para encontrar a chave - {file_type['name']} - {search_type['name']}",
                             ylabel="Número de comparações", save_as=comparison_analysis_img_path, decimal_places=2, color=colors[algo_index])

    generate_pdf(analysis_data=pdf_report_data,
                 sizes_qty=len(sizes), imgs_path=imgs_path)


if __name__ == "__main__":
    main()
