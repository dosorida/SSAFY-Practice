import sys

sys.stdin = open('input.txt')


T = int(input())  # testcase 개수 받기

for test_case in range(1, T + 1):  # testcase 동안 반복
    N = int(input())  # 양수의 개수 N 받기
    arr = list(map(int, input().split()))  # N개의 양수 arr에 받기

    max_num = arr[0]  # 최댓값 저장할 변수
    min_num = arr[0]  # 최솟값 저장할 변수

    for i in range(N):  # array 한 바퀴 돌면서
        if max_num < arr[i]:  # max_num보다 arr[i]가 크면
            max_num = arr[i]  # arr[i]로 max_num update
        if min_num > arr[i]:  # min_num보다 arr[i]가 작으면
            min_num = arr[i]  # arr[i]로 min_num update

    print(f"#{test_case} {max_num - min_num}")  # 각 testcase마다 결과 출력
