import numpy as np

n: float = 0.0002
p: float = 0.5
G: float = 0.75

def music_synthesis(grid_size: int = 4, iterations: int = 3, start_point: list[int] = [2, 2]):
    u: np.array = np.zeros(shape=(grid_size, grid_size))
    u1: np.array = np.zeros(shape=(grid_size, grid_size))
    u1[start_point[0]][start_point[1]] = 1
    u2: np.array = np.zeros(shape=(grid_size, grid_size))
    simulation_result: list = list()
    for i in range(iterations):
        u = calculate_inner_elements(u, u1, u2, grid_size)
        u = calculate_edge_elements(u, grid_size)
        u = calculate_corner_elements(u, grid_size)
        u2 = u1.copy()
        u1 = u.copy()
        iteration_result: np.array = np.around(u, decimals=4)
        simulation_result.append(iteration_result)
    return simulation_result

def calculate_inner_elements(u: np.array, u1: np.array, u2: np.array, grid_size):
    result: np.array = u.copy()
    for i in range(1, grid_size-1):
        for j in range(1, grid_size-1):
            result[i][j] = (p * (u1[i-1][j] + u1[i+1][j] + u1[i][j-1] + u1[i][j+1] - (4 * u1[i][j])) + (2 * u1[i][j]) - ((1 - n) * u2[i][j])) / (1 + n)
    return result

def calculate_edge_elements(u, grid_size):
    result: np.array = u.copy()
    for i in range(i, grid_size-1):
        result[0][i] = G * result[1][i]
        result[grid_size-1][i] = G * result[grid_size-2][i]
        result[i][0] = G * result[i][1]
        result[i][grid_size-1] = G * result[i][grid_size-2]
    return result

def calculate_corner_elements(u, grid_size):
    result: np.array = u.copy()
    result[0][0] = G * result[1][0]
    result[grid_size-1][0] = G * result[grid_size-2][0]
    result[0][grid_size-1] = G * result[0][grid_size-2]
    result[grid_size-1][grid_size-1] = G * result[grid_size-1][grid_size-2]
    return result       