def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr, threshold=10):
    n = len(arr)
    if n <= 1:
        return arr[:]
    mid = n // 2

    if n <= threshold:
        tmp = arr[:]
        return insertion_sort(tmp)

    left_sorted = mergesort(arr[:mid], threshold)
    right_sorted = mergesort(arr[mid:], threshold)
    return merge(left_sorted, right_sorted)

def main():
    infile = "numbers.txt"

    with open(infile, "r", encoding="utf-8") as f:
        nums = list(map(int, f.read().split()))

    sorted_nums = mergesort(nums)

    print(sorted_nums)

if __name__ == "__main__":
    main()