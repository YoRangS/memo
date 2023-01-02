def display():
    print()
    print("  ", end=" ")
    for i in range(1, 16):
        print("{0:>2}".format(i), end=" ")
    print()
    for i in range(1, 16):
        print("{0:>2}".format(i), end=" ")
        for j in range(15):
            print("{}".format(L[i][j]), end=" ")
        print()
def is_end():
    pass

def put(count):
    color = "흑" if count % 2 == 1 else "백"
    print("{}이 둘 곳 : ".format(color), end = "")
    x, y = map(int, input().split())
    L[y][x] = color

count = 1
L = [['  ' for i in range(16)] for _ in range(16)]
while True:
    put(count)
    count += 1

    display()