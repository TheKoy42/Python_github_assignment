#welcome to the program

print("Welcome to my Python program!")
#Gets users hours and turns it into a float and multiplies it by 7
hours = input("How many hours did you study today? ")
hours = float(hours)
weekly_hours = hours * 7
#Prints Calculated results 
print(f"You are on track to study {weekly_hours} hours this week.")
#Erorr Prevention 
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()