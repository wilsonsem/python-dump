#variable to store filename
filename = "sample_file.txt"

#Writing to the file--w stands for write mode. In write mode it wipes the file and write to it

file = open(filename, 'w')

for i in range(1, 11):
    file.write("This is line %i.\n" %i)
file.close()

# reading fom file
file = open(filename, 'r')

for line in file:
    print(line, end = " ")
file.close()

