n=int(input())
binary=bin(n)
binaryf=str(binary[2:])
result=""

for i in binaryf:
    if i=="0":
        result+="1"
    else:
        result+="0"

print(int(result,2))




