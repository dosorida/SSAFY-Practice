import sys

sys.stdin = open('input.txt')

"""
문제 설명:
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
"""

T = int(input())  # testcase 받아오기

for test_case in range(1, T + 1):
    N = int(input())  # 버스 노선 개수
    bus_lines = [list(map(int, input().split())) for _ in range(N)]  # 각 버스 노선 저장
    P = int(input())  # 버스 정류장 수
    bus_stops = [int(input()) for _ in range(P)]  # 각 버스 정류장 저장

    counts = [0] * P  # 버스 정류장 별로 노선 count

    for a, b in bus_lines:  # 각 버스 노선에 대해
        for i in range(P):
            if bus_stops[i] >= a and bus_stops[i] <= b:  # 버스 정류장이 노선에 포함되면
                counts[i] += 1  # count 올리기

    print(f"#{test_case} ", end='')
    print(*counts)
