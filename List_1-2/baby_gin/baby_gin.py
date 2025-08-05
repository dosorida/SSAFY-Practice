import sys

sys.stdin = open("input.txt")

"""
문제 설명:
o ~ 9 사이의 숫자 카드에서 임의의 카트 6장을 뽑았을 때
- 3장의 카드가 연속적인 번호를 갖는 경우를 run
- 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
6자리 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램 작성하기
"""

T = int(input())  # testcase 받기

for test_case in range(1, T + 1):
    nums = input()
    counts = [0] * 12  # index 오류 안 나게 padding 추가
    
    for num in nums:
        num = int(num)  # 정수로 변환
        counts[num] += 1

    triplet = 0  # triplet에 해당되는지 검사할 변수
    run = 0  # run에 해당되는지 검사할 변수
    i = 0  # counts의 index

    # counts 돌면서 triplet, run 순으로 조건 검사
    while i < 12:
        # triplet에 해당되는지 검사
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1
            continue

        # run에 해당되는지 검사
        if counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1
            run += 1
            continue

        i += 1
    
    baby_gin = 0  # baby_gin에 해당되는지 저장할 변수
    if run + triplet == 2:
        baby_gin = 1
    print(f"#{test_case} {baby_gin}")
