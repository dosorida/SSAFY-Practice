'''
문제 설명:
상자들이 쌓여있는 방이 있다.
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 낙차가 가장 큰 상자를 구하여 그 낙차를 return
주의 사항:
- 설명은 2차원이지만 문제 풀이는 1차원으로 충분
- 1차원 배열의 원소 A[i]의 오른쪽 원소 중 A[i]보다 더 작은 원소의 개수를 세고, 이 중 최댓값을 찾는 문제
'''

import sys

sys.stdin = open('input.txt')

T = int(input())  # testcase 입력 받기

for test_case in range(1, T + 1):  # testcase 돌면서
    N = int(input())  # 상자 list 원소 개수 입력 받기
    boxes = list(map(int, input().split()))  # 각 상자 높이 저장할 list

    max_drop = 0  # 가장 큰 낙차 저장할 변수

    # 가장 위에 위치한 상자가 낙차가 제일 클 것이므로 1차원으로 풀이
    for i in range(N):
        # 현재 상자의 낙차 구하기(각 상자 탑의 맨 꼭대기 상자 기준으로 계산)
        current_drop = 0
        for j in range(i + 1, N):  # 현재 상자 이후 상자 리스트를 돌면서
            if boxes[i] > boxes[j]:  # 현재 상자보다 낮은 박스 세기
                current_drop += 1

        # 최대 낙차 구하기
        max_drop = max(max_drop, current_drop)

    print(f"#{test_case} {max_drop}")  # output 출력
