#Given a string as input, you need to output how many times each letter appears in the string.
#You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
#Create a program to take a string as input and output a dictionary, which represents the letter count.

#Sample Input
#hello

#Sample Output
#{'h': 1, 'e': 1, 'l': 2, 'o': 1}
#You need to output the dictionary object.
#Note, that the letters are in the order of appearance in the string.


text = input()
dict = {}
for i in text:
    if i not in dict:
        dict[i] = 1

    else:
        dict[i] += 1
print(dict)

