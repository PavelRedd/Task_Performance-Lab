import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python task4.py <D:/.../path_to_file>")
        return
    path_nums = sys.argv[1]
    with open(path_nums) as f:
        nums = f.readlines()
        numbers = [int(num.strip()) for num in nums]  
    numbers.sort()
    median = len(numbers) // 2
    result = sum(abs(n - numbers[median]) for n in numbers)
    print(result)

if __name__ == '__main__':
    main()
