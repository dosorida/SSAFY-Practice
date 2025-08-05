import sys

sys.stdin = open('input.txt')

"""
문제 설명:
N개의 양의 정수가 첫번째부터 N번째까지 주어진다.
최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오.
단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
"""

T = int(input())  # testcase 받아오기

for test_case in range(1, T + 1):
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # N개의 양수

    max_idx = 0  # 최댓값의 위치
    min_idx = 0  # 최솟값의 위치

    for i in range(1, N):
        if arr[i] >= arr[max_idx]:  # 가장 큰 수가 여러 개이면 마지막으로 나오는 위치
            max_idx = i
        if arr[i] < arr[min_idx]:   # 가장 작은 수가 여러 개이면 먼저 나오는 위치
            min_idx = i

    print(f"#{test_case} {abs(max_idx - min_idx)}")  # 차이 절댓값으로 출력
