# # for loops = execute a block of code a fixed number of times
#     # you can iterate over a rage, string, sequnce, ect.

# for x in range(1, 11, 2): # ,2 alows to count by 2          # reverse coomad allows to count in revrsed starting by 10 to 1 
#     print(x)
# print("HAPPY NEW YEAR!")

# # credit_card = "1234-5678-9012-3456"

# # for x in credit_card:
# #     print(credit_card)

# for x in range(1, 21):
#     if x == 13:
#         continue                # continue command allows the loop to go on, if a break command is implied the it'll break out of the loop 
#     else:
#         print(x)






# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)


# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))
for subject in subjects:
    print(subject)

for subject in subjects:
    if subject == "History":
        break           
    else:
        print(subject)

for subject in subjects:
    if subject == "Science":
        break           
    else:
        print(subject)

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])



# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.



total = 0
for number in numbers:
    total += number
print("total: " ,total)

#-------------------------------------------------------------


new_numbers = list(range(1, 6001))
new_total= 0

for number in new_numbers:
    new_total += number
print("total: " ,new_total)