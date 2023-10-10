# TSP_Solution
Solution of the traveling salesman problem using many algorithms.

run using the following 

python new_solution.py <file_name> <time_limit> <seed>
seed is optional you can use it to reproduce the same results. use 42 for example.
python new_solution.py pb1.txt  60 42

helpers:
| Function Name                   | Purpose                                           | Input                                                       | Output                                      |
|--------------------------------|---------------------------------------------------|-------------------------------------------------------------|---------------------------------------------|
| `set_diag_to_inf(matrix)`       | Set the diagonal of a matrix to infinity.        | A distance matrix.                                          | None (The matrix `matrix` is modified in-place). |
| `prepare_data(file_path)`       | Prepare city coordinates and compute distance matrix. | File path containing city coordinates.                      | Distance matrix, Number of cities.          |
| `read_path_from_file(file_path)`| Read the city path from the provided file.       | File path containing city path data.                        | List of city paths.                         |
| `plot_graph(df, nodes)`         | Plot cities and their path on a 2D plane.        | DataFrame containing city coordinates, List of city paths. | None (Displays the plotted graph).          |
