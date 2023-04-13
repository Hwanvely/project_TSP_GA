import random


class Selection:

    # 유전 과정이 끝난 후 나온 세대에 대해 적합도(거리)에 따라 정렬하는 메소드
    def sort_distance_genetic(sol_list_cost):
        return sorted(sol_list_cost, key=lambda sol_list_cost: sol_list_cost[1])

    # sol_list와 cost의 list인 sol_list_cost(N개의 요소가 있어야 됨)를 인자로 받아서
    # 적합도에 따라 정해둔 확률을 통해 초기집단에 사용할 sol_list_cost를 반환하는 메소드
    def ranking(sol_list_cost, n):
        prob_list = [0.15, 0.14, 0.13, 0.12, 0.11, 0.09, 0.08, 0.07, 0.06, 0.05]
        p = random.random()
        check = 0
        for i in range(n):
            check += prob_list[i]
            if check >= p:
                idx = i
                break
        return sol_list_cost[idx]
