import sys

sys.stdin = open('input.txt')

"""
문제 설명:
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
"""

T = int(input())  # testcase 받아오기

for test_case in range(1, T + 1):
    N = int(input())  # 수열의 길이
    arr = list(map(int, input()))  # 수열

    max_num = 0  # 연속한 1의 개수 중 최댓값
    curr_num = 0 # 연속한 1의 개수(for문 도는 동안 계속 업데이트)

    for i in range(N):   # 수열 돌면서
        if arr[i] == 1:  # 값이 1이면 curr_num +1
            curr_num += 1
        else:            # 값이 0이면 curr_num 0으로 초기화
            curr_num = 0
        if max_num < curr_num:  # 최댓값 갱신
            max_num = curr_num

    print(f"#{test_case} {max_num}")
