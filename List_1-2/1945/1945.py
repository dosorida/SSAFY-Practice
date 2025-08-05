import sys

sys.stdin = open('input.txt')

"""
문제 설명:
숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.
"""

T = int(input())  # testcase 받아오기

for test_case in range(1, T + 1):
    N = int(input())  # 숫자 N 받아오기
    a = b = c = d = e = 0  # 지수들

    while N > 1:  # N이 1보다 큰 동안 소인수 분해
        if N % 2 == 0:
            a += 1
            N //= 2
        elif N % 3 == 0:
            b += 1
            N //= 3
        elif N % 5 == 0:
            c += 1
            N //= 5
        elif N % 7 == 0:
            d += 1
            N //= 7
        else:
            e += 1
            N //= 11

    print(f"#{test_case} {a} {b} {c} {d} {e}")
