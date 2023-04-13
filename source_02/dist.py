import numpy as np

import paths
from util import Util


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


def total_cost(sol_list):
    idx = sol_list.index(0)

    front = sol_list[idx:]
    back = sol_list[0:idx]

    sol_list = front + back

    sol_list.append(int(0))

    t_cost = 0
    cities = Util.read_csv_file(paths.CSV / 'TSP.csv')

    for idx in range(len(sol_list) - 1):
        pos_city_1 = [float(cities[sol_list[idx]][0]), float(cities[sol_list[idx]][1])]
        pos_city_2 = [float(cities[sol_list[idx + 1]][0]), float(cities[sol_list[idx + 1]][1])]
        dist = distance(pos_city_1, pos_city_2)
        t_cost += dist

    return t_cost
