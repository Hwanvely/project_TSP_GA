import random

# 순서교차가 이루어지는 메소드
def order(sol_list1, sol_list2):

    #경로 하나에서 교차를 진행 할 구간을 랜덤으로 설정
    start_idx = random.randint(0, len(sol_list1) - 1)
    end_idx = random.randint(start_idx + 1, len(sol_list1))
    
    # 시작 할 인덱스와 끝 인덱스 사이의 도시들을 새로운 리스트로 생성
    new_list = sol_list1[start_idx:end_idx]
    result_list = []
    tmp_set = set()

    # 새로운 경로의 도시들을 리스트로 생성하여 결과값으로 반환
    for i in range(len(new_list)):
        tmp_set.add(new_list[i])
    for i in range(len(sol_list2) - end_idx):
        if sol_list2[end_idx + i] not in tmp_set:
            result_list.append(sol_list2[end_idx + i])
    for i in range(end_idx):
        if sol_list2[i] not in tmp_set:
            result_list.append(sol_list2[i])
    front = result_list[0:start_idx]
    back = result_list[start_idx:]
    result_list = front + new_list + back
    return result_list
