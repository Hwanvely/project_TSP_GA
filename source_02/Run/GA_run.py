import dist
import csv
from randomGA import Random
from selection import Selection
from crossover import order
from mutation import Mutation

N = 100
ITERATOR = 10



# randomsearch를 초기집단으로 해서 유전알고리즘을 한 번 돌리는 과정
fitness = Random.sort_distance_random(N)
result_list = fitness[0][0]
result_cost = fitness[0][1]
selection_list_cost = []
sol_list_cost = []
for i in range(N):
    selection_list_cost.append([])
    selection_list_cost[i] = Selection.ranking(fitness, N)
for i in range(N):
    sol_list_cost.append([])
    if (i % 2 == 0):
        sol_list_cost[i].append(order(selection_list_cost[i][0], selection_list_cost[i + 1][0]))
    else:
        sol_list_cost[i].append(order(selection_list_cost[i][0], selection_list_cost[i - 1][0]))
for i in range(N):
    sol_list_cost[i][0] = Mutation.reverse(sol_list_cost[i][0])
    sol_list_cost[i].append(dist.total_cost(sol_list_cost[i][0]))
    if result_cost > sol_list_cost[i][1]:
        result_list = sol_list_cost[i][0]
        result_cost = sol_list_cost[i][1]


# 처음 유전알고리즘을 진행해서 나온 자식을 통해 유전알고리즘을 1000번 더 수행하는 과정
for i in range(ITERATOR):
    fitness = Selection.sort_distance_genetic(sol_list_cost)
    for i in range(N):
        selection_list_cost[i] = Selection.ranking(fitness, N)
    for i in range(N):
        if i % 2 == 0:
            sol_list_cost[i][0] = order(selection_list_cost[i][0], selection_list_cost[i + 1][0])
        else:
            sol_list_cost[i][0] = order(selection_list_cost[i][0], selection_list_cost[i - 1][0])
    for i in range(N):
        sol_list_cost[i][0] = Mutation.reverse(sol_list_cost[i][0])
        sol_list_cost[i][1] = dist.total_cost(sol_list_cost[i][0])
        if result_cost > sol_list_cost[i][1]:
            result_list = sol_list_cost[i][0]
            result_cost = sol_list_cost[i][1]

##### 파일 쓰고 정렬 후 다시 쓰기 ######
with open('./csv/sol_random_GA.csv', mode='w', newline='') as f:
    wr = csv.writer(f)
    for i in result_list:
        wr.writerow([i])

sol = []
with open('./csv/sol_random_GA.csv', mode='r', newline='') as solution:
    reader = csv.reader(solution)
    for row in reader:
        sol.append(int(row[0]))

    idx = sol.index(0)
    front = sol[idx:]
    back = sol[0:idx]
    sol = front + back
    sol.append(int(0))

with open('./csv/sol_random_GA.csv',mode='w',newline='') as solutionList:
    wr = csv.writer(solutionList)
    for i in sol:
        wr.writerow([i])

print(result_list)
print(result_cost)
