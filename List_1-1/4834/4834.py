import sys

sys.stdin = open('input.txt')

T = int(input())  # testcase 수 받아오기

for test_case in range(1, T + 1):  # 매 testcase 동안
    N = int(input())  # 카드 장수 N 받아오기
    arr = list(map(int, input()))  # N개의 숫자 받아와서 arr에 저장

    numbers = [0] * 10  # 각 숫자 카드(0~9)마다 몇 장인지 저장할 array (index는 카드에 적힌 숫자)

    for i in range(N):  # 숫자 array 돌면서 각 숫자 카드 개수 세기
        numbers[arr[i]] += 1

    max_idx = 0  # 가장 많은 카드의 인덱스 저장할 변수
    for i in range(len(numbers)):  # 숫자 카드 개수 array 돌면서
        if numbers[max_idx] <= numbers[i]:  # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽 출력
            max_idx = i  # 가장 많은 수의 카드 저장

    print(f"#{test_case} {max_idx} {numbers[max_idx]}")  # output 출력
