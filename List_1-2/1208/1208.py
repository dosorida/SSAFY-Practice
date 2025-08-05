import sys

sys.stdin = open('input.txt')

"""
문제 설명:
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램 작성하기
제약 사항:
주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다
"""

T = 10  # testcase 10개로 주어짐

for test_case in range(1, T + 1):
    dump = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 각 상자의 높이 값

    # 주어진 덤프 횟수 동안
    for i in range(dump):
        max_box_idx = boxes.index(max(boxes))  # 최고점의 index
        min_box_idx = boxes.index(min(boxes))  # 최저점의 index

        # 박스 하나 넘기기
        boxes[max_box_idx] -= 1
        boxes[min_box_idx] += 1

    difference = max(boxes) - min(boxes)

    print(f"#{test_case} {difference}")
