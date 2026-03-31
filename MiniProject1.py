grades = [70, 90, 45, 67, 88, 36, 99]

total = 0
pass_count = 0

# Add all grades together and count passes
for grade in grades:
    total = total + grade

    if grade >= 50:
        pass_count = pass_count + 1

# Use max() and min() to find highest and lowest
highest = max(grades)
lowest = min(grades)

# Divide total by number of grades
average = total / len(grades)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Pass count:", pass_count)