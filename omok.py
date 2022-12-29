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

def put():
    pass

count = 1
L = [['  ' for i in range(16)] for _ in range(16)]
display()