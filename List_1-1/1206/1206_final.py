import sys

sys.stdin = open('input.txt')

"""
문제:
- 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램 작성하기
- 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보됨!
제약 사항:
- 가로 길이는 항상 1000이하로 주어진다.
- 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)
- 각 빌딩의 높이는 최대 255이다.
"""

T = 10  # testcase 10개 주어짐

for test_case in range(1, T + 1):  # 각 testcase에 대해
    N = int(input())  # 빌딩 수
    buildings = list(map(int, input().split()))  # N개의 빌딩 높이 정보

    total = 0  # 조망권 확보된 세대 수

    for i in range(2, N - 2):  # 각 건물에 대해(맨 왼쪽, 오른쪽 두 칸은 0이므로 pass)
        # 현재 건물 높이
        curr = buildings[i]

        # 왼쪽 건물
        left1 = buildings[i - 1]
        left2 = buildings[i - 2]

        # 오른쪽 건물
        right1 = buildings[i + 1]
        right2 = buildings[i + 2]

        # 조망권 계산하기
        view = min(curr - left1, curr - left2, curr - right1, curr - right2)

        if view > 0:
            total += view

    print(f"#{test_case} {total}")
