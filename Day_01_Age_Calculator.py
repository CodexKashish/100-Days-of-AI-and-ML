# Project: Age to Days Converter
# Focus: TypeCasting, Input Handling, and Error Prevention

# 1. Get input from the user
user_input= input("ENTER YOUR AGE IN YEARS:")
#2. Convert the input to a number (integer)
#This is called 'Type Casting'
age= int(user_input) 
#After TypeCasting we changed the datatype from string to an integer
#3. Perform the Calculation(365 days per year)
total_days= age*365
#4. Display the result clearly
print(f"Since you are {age} years old, you have lived for over {total_days} days!")

print("----------------------------")
print("Day1 Complete: Input, Output and Math.")
