
# Import the built-in logging module
import logging

logging.basicConfig(filename='2_vending_machine/vending_machine.log',format='%(lineno)d %(levelname)s:%(message)s',
                    level=logging.DEBUG)
# For every log
logging.debug("start application")



# Welcome the user
print("Welcome to Make-it coffee machine!")

# Tell the user what we offer
print("Here is what we offer:")
print(" 1) Coffee")
print(" 2) Tea")

# Ask the user for their choice
choice = int(input("Please enter the number of your choice: "))
logging.debug("choice="+str(choice))

# Ask how much sugar they want (between 0 and 5)
sugar = int(input("How much sugar would you like from 0-5? "))
logging.debug("sugar="+str(sugar))

# Ask if they want milk
#strip and lower to avoid errors
milk = input("Would you like to add milk? (yes/no): ").strip().lower()
logging.debug("milk="+str(milk))

file_variable = open("2_vending_machine/number_cups.txt", "r")
text = file_variable.read()
file_variable.close()

#number of cups available
number_remaining_cups = int(text) 

# Check cups before serving
if number_remaining_cups > 0:
    number_remaining_cups -= 1  # Reduce cup count
else:
    print("Sorry, we are out of cups.")
# Stop execution if no cups left
    exit() 

# Create message variable to store output
message = ""

# Serve the beverage
if choice == 1:
    message += "Here is your coffee"
elif choice == 2:
    message += "Here is your tea"
else:
    message += "Sorry, I do not know this choice."
    print(message)
    exit()  # Exit if an invalid choice is made

# Add sugar information
if sugar > 0:
    message += " with " + str(sugar) + " sugar(s)"
else:
    message += " with no sugar"

# Add milk information
if milk == "yes":
    message += " and with milk."
else:
    message += " and without milk."
    
#check the ammount of sugar + additional message 
if sugar <= 1:
    message += " What a healthy choice!"
else:
    message += " Maybe next time try decreasing the sugar."

# If choice is coffee without sugar nor milk
#     Add to message "Here is your black coffee."
# Else if choice is equal to 1
selection = "coffee" if choice == 1 else "tea"
if choice == 1 and sugar == 0 and milk == "no": 
    message += " Enjoy your black " + selection
else:
    message += " Enjoy your " + selection 

# Print final message
print(message)

#print cups
print ("The number of remaining cups is " + str(number_remaining_cups))


file_variable = open("2_vending_machine/number_cups.txt", "w")
file_variable.write(str(number_remaining_cups))
file_variable.close()