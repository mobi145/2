
n = int(input("n: "))
for i in range(1, n+1):
    j = i
    right = ""
    while j != 1:
        j-= 1
        right += " " + str(j)
    left = right[::-1]
    padding = " " * (2 * (n - i))
    print(f" {padding} {left}{i}{right} {padding}")