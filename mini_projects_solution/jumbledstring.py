import random

string = "My name is sem and i love solving dsa questions"
string = list(string)
jumbled = " "

for letter in range(0 , len(string)):
    jumbled += string.pop(random.randint(0, len(string) - 1))
    
    print(string)
    print(jumbled)