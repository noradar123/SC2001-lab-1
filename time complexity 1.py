import matplotlib.pyplot as plt
import random
import time

start = time.time()

def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            count += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, count

def merge(left, right):
    count = 0
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        count += 1
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

def mergesort(arr, threshold=10):
    n = len(arr)
    if n <= 1:
        return arr[:], 0
    if n <= threshold:
        tmp = arr[:] 
        return insertion_sort(tmp)

    mid = n // 2
    left_sorted, c1 = mergesort(arr[:mid], threshold)
    right_sorted, c2 = mergesort(arr[mid:], threshold)
    merged, c3 = merge(left_sorted, right_sorted)
    return merged, c1 + c2 + c3

def main():
    random.seed(0)
    sizes = []
    comps = []

    for i in range(100):
        n = 1000 * i
        r = [random.randint(1, 2147483647) for _ in range(n)]
        _, comparisons = mergesort(r, threshold=32)
        sizes.append(n)
        comps.append(comparisons)
    end = time.time()
    print(end - start, "s")
    plt.plot(sizes, comps, marker='o')
    plt.title("Comparisons vs. Array Size (Hybrid Merge + Insertion)")
    plt.xlabel("Array size")
    plt.ylabel("Number of comparisons")
    plt.grid(True)
    plt.show()


    with open("output1.txt", "w") as f:
        f.write(str(comps))



if __name__ == "__main__":
    main()