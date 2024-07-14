def main():
    n = int(input("n = "))
    m = int(input("m = "))

    arr = list(range(1, n + 1))

    current = 0
    path = []

    print("Path: ", end="")
    while True:
        print(arr[current], end="")
        path.append(arr[current])
        current = (current + m - 1) % n
        if current == 0:
            break
    print()

if __name__ == "__main__":
    main()