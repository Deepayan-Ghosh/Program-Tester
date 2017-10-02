t = int(input())
print(t)
for _ in range(t):
    hold = input()
    print(hold)
    m,n = map(int,hold.split())
    matrix = []
    for _ in range(m):
        row = []
        matrix.append(list(map(int,input().split())))
    print(matrix)