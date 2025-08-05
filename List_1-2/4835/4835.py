import sys

sys.stdin = open('input.txt')

"""
문제 설명:
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
"""

T = int(input())  # testcase 받기

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: 정수의 개수, M: 구간의 개수
    arr = list(map(int, input().split()))  # 정수들 저장할 arr

    min_sum = 1e7  # 이웃한 M개의 합이 가장 작은 경우
    max_sum = 0    # 이웃한 M개의 합이 가장 큰 경우

    for i in range(N - M + 1):
        curr_sum = 0  # 현재 M개의 합 구할 변수

        for j in range(M):
            curr_sum += arr[i + j]

        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > max_sum:
            max_sum = curr_sum

    difference = max_sum - min_sum
    print(f"#{test_case} {difference}")
