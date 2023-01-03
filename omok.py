def display():
    print()
    print("  ", end=" ")
    for i in range(1, 16):
        print("{0:>2}".format(i), end=" ")
    print()
    for i in range(1, 16):
        print("{0:>2}".format(i), end=" ")
        for j in range(1, 16):
            print("{}".format(L[i][j]), end=" ")
        print()

def is_end():
    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, 1]
    for y in range(1, 16):
        for x in range(1, 16):
            if L[y][x] == "  ":
                continue
            for i in range(4):
                if depth(dx[i], dy[i]):
                    return true
            
def depth(x, y):
    pass


def put(count):
    color = "흑" if count % 2 == 1 else "백"
    stone = "@@" if count % 2 == 1 else "<>"
    while True:
        try:
            print("{}이 둘 곳 (x y): ".format(color), end = "")
            x, y = map(int, input().split())
            if L[y][x] == "  ":
                L[y][x] = stone
                break
            print("거긴 이미 둔 곳이에요.")
        except IndexError:
            print("거긴 두는 곳이 아니에요.")

count = 1
L = [['  ' for i in range(16)] for _ in range(16)]
while True:
    put(count)
    count += 1

    display()