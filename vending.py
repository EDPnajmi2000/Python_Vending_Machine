# Function to Display the drinks available
def displayDrinks(drinkMenu):
    print("==========================================")
    print("Welcome to the Vending Machine")
    print("==========================================")
    print("Drinks: ")
    for name, price in drinkMenu.items():
        print(f"{name}: RM {price}.00")
    print("==========================================")


# function to calculate the min number of notes for the balance
def calculateBalanceNotes(balance):
    balanceNotes = []

    # check for RM 50 notes:
    if balance/50 >= 1:
        numNotes = int(balance/50)
        balanceNotes.extend([50]*numNotes)
        balance = balance - (50*numNotes)

    # check for RM 20 notes:
    if balance/20 >= 1:
        numNotes = int(balance/20)
        balanceNotes.extend([20]*numNotes)
        balance = balance - (20*numNotes)

    # check for RM 10 notes:
    if balance/10 >= 1:
        numNotes = int(balance/10)
        balanceNotes.extend([10]*numNotes)
        balance = balance - (10*numNotes)

    # check for RM 5 notes:
    if balance/5 >= 1:
        numNotes = int(balance/5)
        balanceNotes.extend([5]*numNotes)
        balance = balance - (5*numNotes)

    # check for RM 1 notes:
    if balance/1 >= 1:
        numNotes = int(balance/1)
        balanceNotes.extend([1]*numNotes)
        balance = balance - (1*numNotes)

    return balanceNotes

#Define the drinks
drinkMenu = {
    "COCA-COLA":2,
    "PEPSI":3,
    "FANTA":1,
    "MILO":4,
    "WONDA COFFEE":5,
    "SPRITZER":1,
}


# Main Code

displayDrinks(drinkMenu)

# Get the drink selection
while True:
    drinkSelection = input("Enter Drink Name: ").upper()
    if drinkSelection in drinkMenu:
        break
    else:
        print("Invalid drink name")

# Get the number of drinks
while True:
    numDrinks = input("Enter the number of drinks to purchase: ")
    if numDrinks.isdigit():
        break
    else:
        print("Please enter whole number only")

total = int(drinkMenu[drinkSelection])*int(numDrinks)
print(f"Total Price: {total}")

totalNotesInserted = 0

while totalNotesInserted<total:
    noteInserted = input("Please enter notes: ")
    if noteInserted.isdigit():
        totalNotesInserted += int(noteInserted)
        print(f"Total Inserted RM {totalNotesInserted}")

balance = totalNotesInserted - total

if balance>0:
    print(f"Total Balance RM {balance}")

    balanceNotes = calculateBalanceNotes(balance)

    print("Returning Balance: ")

    for note in balanceNotes:
        print(f"RM {note}")

    print("Balance Returned")
    
    


else:
    print("Exact ammount inserted. No balance will be returned")

print("Thank you for purchasing with us :D")
print("Email najmiarif2000@gmail.com for any business inquiries (•‿•)")
