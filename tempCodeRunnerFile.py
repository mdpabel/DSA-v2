import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


# 🔥🔥🔥
n, m = inlt()

rem = 240 - m

i = 1

while n > 0:
    rem -= (i * 5)
    i += 1

i -= 1
print(i)
