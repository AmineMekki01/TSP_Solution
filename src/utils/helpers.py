import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist


def set_diag_to_inf(matrix):
    np.fill_diagonal(matrix.values, np.inf)


def prepare_data(file_path):

    df = pd.read_csv(f"instances/{file_path}", sep=' ', names=['X', 'Y'], skiprows=1, skipfooter=1, engine='python')
    df.index += 1  
    
    dist_matrix = pd.DataFrame(
        squareform(pdist(df)), 
        columns=df.index,
        index=df.index
    )
    
    set_diag_to_inf(dist_matrix)
    return dist_matrix, len(df)




def read_path_from_file(file_path):
    with open(file_path, 'r') as f:
        nodes = list(map(int, f.read().strip().split()))
    return nodes



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
    