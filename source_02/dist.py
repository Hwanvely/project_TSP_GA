import numpy as np
import paths
from util import Util

distances = []
def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist

cities = Util.read_csv_file(paths.CSV / 'TSP.csv')
# distances 전역 변수 넣어줌
for i in range(len(cities)):
    distances.append([])
    for j in range(len(cities)):
        pos_city_i = [float(cities[i][0]), float(cities[i][1])]
        pos_city_j = [float(cities[j][0]), float(cities[j][1])]
        dist = distance(pos_city_i, pos_city_j)
        distances[i].append(dist)

def total_cost(sol_list):
    idx = sol_list.index(0)

    front = sol_list[idx:]
    back = sol_list[0:idx]

    sol_list = front + back

    sol_list.append(int(0))

    t_cost = 0

    # t_cost 코드 좀 줄임
    for idx in range(len(sol_list) - 1):
        t_cost += distances[sol_list[idx]][sol_list[idx+1]]
    return t_cost
