n1=int(input())

arr=[]

for i in range(n1):

    n2=int(input())

    arr.append(n2)

n3=int(input())

result=""

for i in arr:

    binary=bin(i)

    binaryf=str(binary[2:])

    if len(binaryf) <= n3:
        result += "0 "
    else:
        result += str(int(binaryf[:-n3],2)) + " "

print(result)