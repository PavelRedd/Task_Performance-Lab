import sys
from math import sqrt

def main():
    if len(sys.argv) < 3:
        print("Usage: python task2.py <D:/.../path_to_file>")
        return
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    with open(path1) as f:
        xc, yc = f.readline().split()
        xc, yc = float(xc), float(yc)
        r = float(f.readline().strip())
    with open(path2) as f:
        points = f.readlines()
    for point in points:
        x, y = map(float, point.split())
        s = sqrt((xc - x) ** 2 + (yc - y) ** 2)
        if s == r:
            print(0)
        elif s < r:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()
