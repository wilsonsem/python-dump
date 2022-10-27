filename = "sample_file.txt"

#appending to a file
file = open(filename, 'a')

for i in range (0,5):
    name = input("Enter your name: ")
    file.write(name +"\n")
file.close()