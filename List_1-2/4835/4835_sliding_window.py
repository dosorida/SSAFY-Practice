import sys

sys.stdin = open('input.txt')

"""
문제 설명:
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

[슬라이딩 윈도우 사용하기]
첫 구간의 합을 구한 뒤, 다음 구간으로 이동할 때 빠지는 값과 새로 들어오는 값만 계산하여
불필요한 중복 덧셈을 제거하는 효율적인 방식. -> for문 하나 줄일 수 있음
"""

T = int(input())  # testcase 받기

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: 정수의 개수, M: 구간의 개수
    arr = list(map(int, input().split()))  # 정수들 저장할 arr

    # 슬라이딩 윈도우 시작점
    curr_sum = sum(arr[:M])  # arr의 처음 M개 만큼 더한 값
    min_sum = curr_sum  # 이웃한 M개의 합이 가장 작은 경우
    max_sum = curr_sum  # 이웃한 M개의 합이 가장 큰 경우

    for i in range(1, N - M + 1):
        previous_first = arr[i - 1]  # 이전 구간합의 맨 앞 요소
        current_last = arr[i + M - 1]  # 현재 구간합의 맨 뒤 요소
        # 현재 구간합 = 이전 구간합 - 이전 구간합의 맨 앞 요소 + 현재 구간합의 맨 뒤 요소
        curr_sum = curr_sum - previous_first + current_last

        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > max_sum:
            max_sum = curr_sum

    difference = max_sum - min_sum
    print(f"#{test_case} {difference}")
