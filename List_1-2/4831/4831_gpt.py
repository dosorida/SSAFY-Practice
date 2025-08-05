import sys

sys.stdin = open("input.txt")

"""
문제 설명:
전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
"""

T = int(input())  # 노선 수

def bus(K, N, M, charge):
    charge_set = set(charge)
    curr = 0  # 현재 정류장 위치
    charge_count = 0

    while curr + K < N:
        for step in range(K, 0, -1):  # K칸 내에서 가장 멀리 있는 충전소 찾기
            if (curr + step) in charge_set:
                curr += step
                charge_count += 1
                break
        else:
            return 0  # 충전소를 찾지 못한 경우

    return charge_count


for test_case in range(1, T + 1):
    # K: 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    # N: 종점
    # M: 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))  # 충전기가 설치된 정류장 번호 list

    charge_count = bus(K, N, M, charge)

    print(f"#{test_case} {charge_count}")
