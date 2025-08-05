def counting_sort(input_arr, k):
    counts = [0] * (k + 1)  # input_arr의 각 요소 개수 저장할 array

    # 1. input_arr의 각 요소 counts에 개수 세기
    for num in input_arr:
        counts[num] += 1

    # 2. counts 누적합 계산:
    for i in range(1, k + 1):
        counts[i] += counts[i - 1]

    # 3. counts 바탕으로 sorting 결과 list 만들기
    tmp = [0] * len(input_arr)
    for num in input_arr[-1:0:-1]:
        counts[num] -= 1
        tmp[counts[num]] = num

    return tmp


arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]
