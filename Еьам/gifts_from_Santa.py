N = int(input())
M = int(input())
S = int(input())


for address in range(M, N - 1, -1):
    if address % 6 == 0:
        if address == S:
            break
        print(address, end=" ")