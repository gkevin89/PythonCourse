# Assignment 4:
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.

    Example:
    ---------------
    word1 = "Vehicle"
    word2 = "Robot"
    result - ehicleRbot

"""

word1 = "Computer"
word2 = "Truck"

# Expected Result Printed: omputerTuck

# Your code below:

cat1 = word1[1:]
cat2 = word2[0:1] + word2[-3:]
cat3 = word2.replace("r","")

result =cat1+cat2
result2=cat1+cat3

print(result)
print(result2)































# Solution Below:
# result = word1[1:] + word2[0:1] + word2[2:]
# print(result)


