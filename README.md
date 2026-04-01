The Grade Analyzer

This program takes a list of grades and processes them to calculate useful statistics. 
It starts by setting total to 0 so it can add all the grades together, and pass_count to 0 so it can count how many grades are 50 or higher. 
Then it loops through each grade in the list: every grade gets added to total, and if the grade is 50 or above, the program increases pass_count by 1. 
After the loop finishes, it uses max(grades) to find the highest grade and min(grades) to find the lowest. It calculates the average by dividing the total of 
all grades by the number of grades using len(grades). Finally, it prints the average grade, the highest grade, the lowest grade, and how many students passed.
