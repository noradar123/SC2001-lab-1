import random

def generate_numbers(n=10, low=1, high=100):
    return [random.randint(low, high) for _ in range(n)]

def main():
    n = int(input("length of random numbers"))
    low = int(input("enter lower bound"))
    high = int(input("enter higher bound"))
    out_file = "numbers.txt"

    nums = generate_numbers(n, low, high)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, nums)))

    print(f"generated {len(nums)} random numbers to {out_file}：")
    print(nums)

if __name__ == "__main__":
    main()