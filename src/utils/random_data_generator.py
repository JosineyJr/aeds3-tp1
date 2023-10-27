import random
import string
import csv


def generate_random_data(num_records=1000, output_file="data.csv", data_type="Ordenado"):
    data = []
    generated_keys = set()

    for _ in range(num_records):
        chave = random.randint(1, 10**9)
        while chave in generated_keys:
            chave = random.randint(1, 10**9)
        generated_keys.add(chave)

        dado1 = random.randint(1, 10**9)

        dado2 = ''.join(random.choices(
            string.ascii_letters + string.digits, k=1000))

        data.append([chave, dado1, dado2])

    if data_type == 'Ordenado':
        data.sort(key=lambda x: x[0])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(["chave", "dado1", "dado2"])

        writer.writerows(data)
