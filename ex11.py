#asking questions
#python3 is not able to include input() in the print method
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight?", end = ' ')
weight = input()

#python3 is not able to include multiple % in the print string.
#print("So, you're %r old, %r tall and %r heavy.", %age, %height, %weight)
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

