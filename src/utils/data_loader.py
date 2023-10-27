import csv


def load_data_from_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            chave, dado1, dado2 = int(row[0]), int(row[1]), row[2]
            data.append((chave, dado1, dado2))
    return data
