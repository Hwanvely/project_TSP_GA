import os
import random
import math
import dist
import paths
from util import Util

os.chdir("..")

THRESHOLD = 1
CHECK_DEGREE = True
cities = Util.read_csv_file(paths.CSV / 'TSP.csv')

def getDegreeScore(pre, now, front):
    rad1 = math.atan2(float(cities[pre][1]) - float(cities[now][1]), float(cities[pre][0]) - float(cities[now][0]))
    deg1 = (rad1 * 180 / math.pi + 360) % 360
    rad2 = math.atan2(float(cities[front][1]) - float(cities[now][1]), float(cities[front][0]) - float(cities[now][0]))
    deg2 = (rad2 * 180 / math.pi + 360) % 360
    check = abs(deg1 - deg2) % 180
    return -(check / 600) + 2.0


def citiesDist(startIndex, preCity, checkDegree):  #
    distance = []
    nowDist=0.0
    now = 0
    score = []
    for i in cities:
        if startIndex != now and i[2]:
            nowCity = [float(cities[startIndex][0]), float(cities[startIndex][1])]

            destCity = [float(i[0]), float(i[1])]
            nowDist = dist.distance(nowCity, destCity)
            if checkDegree:
                if preCity != -1:
                    score.append([nowDist * getDegreeScore(preCity, startIndex, now), now])
                else:
                    score.append([nowDist, now])
            else:
                score.append([nowDist, now])
        now += 1

    score.sort(key=lambda x: x[0])
    distance = score[0:THRESHOLD]

    return distance


def getTreeSolution():
    traveling = []

    nextCity = 0
    nowCity = 0
    preCity = -1
    traveling.append(0)
    for i in cities:
        i.append(True)
    for i in range(999):
        dist = citiesDist(nowCity, preCity, CHECK_DEGREE)
        cities[nowCity][2] = False
        nextCity = dist[random.randrange(0, len(dist))][1]
        traveling.append(nextCity)
        preCity = nowCity
        nowCity = nextCity
    for i in cities:
        i.pop()

    return traveling


# treesearch한 초기집단의 적합도(거리)에 따라 정렬하는 메소드
def sort_distance_tree(n):
    sol_list_cost = []

    for i in range(n):
        sol_list = getTreeSolution()
        sol_list_cost.append([])
        sol_list_cost[i].append(sol_list)
        sol_list_cost[i].append(dist.total_cost(sol_list))

    sol_list_cost = sorted(sol_list_cost, key=lambda sol_list_cost: sol_list_cost[1])
    return sol_list_cost
