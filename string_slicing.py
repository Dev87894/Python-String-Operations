# extraction of first 5 characters 
text1 = "Programming"
print("first 5 characters:",text1[:5])

# Extract the last four characters
text2 = "Programming"
print("last four characters:",text2[-4:])

# print every second character 
text3 = "PythonProgramming"
print("every second character:",text3[0 : len(text3) : 2])

# reverse a string using slicing
text4 = "Python"
print("reverse of given string:",text4[len(text4) :  : -1])

# Extract characters from index 2 to index 7
text5 = "Artificial"
print("characters from index 2 to index 7:",text5[2 : 7])

# Extract every third character
text6 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("every third character:",text6[0 :  : 3])

# Print all characters except the first and last
text7 = "Computer"
print("Print of all characters except the first and last:",text7[1 : len(text7) - 1])

# Reverse every alternate character
text8 = "PythonProgramming"
print("Reverse of every alternate character is:",text8[len(text8) :  : -2])

# Extract username and domain from an email
text9 = "student@example.com"
user_name = text9[0 : 7]
domain = text9[8 : len(text9)]
print("user name is:",user_name)
print("domain name is:",domain)


# Home Work
# text = "PythonProgramming"

# Print the following using only slicing:

# Python
# Programming
# Pto rgamn
# gnimmargorPnohtyP
# Every character except the last three.
# Every second character in reverse order.