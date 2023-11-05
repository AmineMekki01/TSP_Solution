import numpy as np


def set_diag_to_inf(matrix):
    np.fill_diagonal(matrix.values, np.inf)


def prepare_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]
    nodes = {}
    for idx, line in enumerate(lines):
        x, y = line.strip().split(' ')
        nodes[idx] = (float(x), float(y))
    coords = np.array(tuple(nodes.values()))

    dist_matrix = np.sqrt(((coords[:, np.newaxis, :] - coords)**2).sum(axis=2))
    np.fill_diagonal(dist_matrix, np.inf)
    return dist_matrix, len(coords)
