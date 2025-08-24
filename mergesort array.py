def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    if i < len(left):  out.extend(left[i:])
    if j < len(right): out.extend(right[j:])
    return out

def main():
    infile = "numbers.txt"

    with open(infile, "r", encoding="utf-8") as f:
        nums = list(map(int, f.read().split()))

    sorted_nums = merge_sort(nums)
    print(sorted_nums)

if __name__ == "__main__":
    main()