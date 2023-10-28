import csv
from algorithms.binary_tree import BinaryTree
from algorithms.avl_tree import AVLTree


def load_data_from_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            chave, dado1, dado2 = int(row[0]), int(row[1]), row[2]
            data.append((chave, dado1, dado2))
    return data


def load_data_into_tree(filename, tree_type="avl tree"):
    if tree_type == "binary tree":
        tree = BinaryTree()
    elif tree_type == "avl tree":
        tree = AVLTree()
    else:
        raise ValueError("Invalid tree type specified")

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            chave = int(row[0])
            tree.insert(chave)

    return tree


def load(filename, algo="avl tree"):
    if algo == 'sequential':
        return load_data_from_csv(filename=filename)

    return load_data_into_tree(filename=filename, tree_type=algo)
