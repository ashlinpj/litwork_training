n1 = int(input())
n2 = int(input())

a = [int(input()) for _ in range(n1)]
b = [int(input()) for _ in range(n2)]

arr = sorted(set(a + b))

n = len(arr)

if n % 2:
    print(arr[n // 2])
else:
    print((arr[n // 2 - 1] + arr[n // 2]) / 2)