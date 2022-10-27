
n = int(input("Enter the number of rows : "))
num = 1

for row in range(1, n+1):
    for col in range ( 1, row+1):
        print(num, end = " ")
        num += 1
    print()

#number pattern 
for i in range(1, n+1):
    for j in range (1, i+1):
        print(j, end = " ")
    print() 

# another number pattern 
for i in range(1, n+1):
    for j in range (1, i+1):
        print(i, end = " ")
    print() 