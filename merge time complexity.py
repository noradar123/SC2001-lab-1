import matplotlib.pyplot as plt
import random
import time

start = time.time()

def merge(left, right):
    i = j = 0
    out = []
    count = 0
    while i < len(left) and j < len(right):
        count += 1
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    if i < len(left): out.extend(left[i:])
    if j < len(right): out.extend(right[j:])
    return out, count

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr[:], 0

    mid = n // 2
    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])
    merged, c3 = merge(left, right)
    return merged, c1 + c2 + c3

def main():
    random.seed(0)
    sizes, comps = [], []

    for i in range(100):
        n = 1000 * i
        r = [random.randint(1, 2_147_483_647) for _ in range(n)]
        _, comparisons = merge_sort(r)
        sizes.append(n)
        comps.append(comparisons)
    end = time.time()
    print(end - start, "s")
    plt.plot(sizes, comps, marker='o')
    plt.title("Comparisons vs. Array Size (Pure Merge Sort)")
    plt.xlabel("Array size")
    plt.ylabel("Number of key comparisons")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    with open("comparison of mergesort.txt", "w") as f:
        f.write(str(comps))


if __name__ == "__main__":
    main()