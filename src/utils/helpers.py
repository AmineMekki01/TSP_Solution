import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist


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



def plot_graph(df, nodes):
    plt.scatter(df['X'], df['Y'], c='blue')

    for idx, row in df.iterrows():
        plt.text(row['X'], row['Y'], str(idx))

    for i in range(len(nodes) - 1):
        point1 = df.loc[nodes[i]]
        point2 = df.loc[nodes[i + 1]]
        plt.plot([point1['X'], point2['X']], [point1['Y'], point2['Y']], 'k-')

    point1 = df.loc[nodes[-1]]
    point2 = df.loc[nodes[0]]
    plt.plot([point1['X'], point2['X']], [point1['Y'], point2['Y']], 'k-')

    plt.show()
    