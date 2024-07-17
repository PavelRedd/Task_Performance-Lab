import sys

def main():
    if len(sys.argv) < 3:
        n = int(input("n = "))
        m = int(input("m = "))
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])

    arr = list(range(1, n + 1))
    print("Массив: ", "".join(map(str, arr)))
    current = 0
    path = []
    intervals = []
    print("Путь: ", end="")
    while True:
        print(arr[current], end="")
        path.append(arr[current])
        interval = [arr[(current + i) % n] for i in range(m)]
        intervals.append(interval)

        current = (current + m - 1) % n
        if current == 0:
            break
    print()
    print("Интервалы: ", end="")
    for interval in intervals:
        print("".join(map(str, interval)), end=" ")
    print()

if __name__ == "__main__":
    main()
