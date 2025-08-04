# 버블 정렬
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):  # 매 반복마다 list 끝을 1씩 줄이기
        for j in range(0, i):  # 0에서 i - 1까지 버블 정렬
            if arr[j] > arr[j + 1]:  # 앞 숫자가 뒷 숫자보다 크면
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr  # 정렬된 array 반환


numbers = [64, 13, 9, 62, 3]  # input
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)  # output