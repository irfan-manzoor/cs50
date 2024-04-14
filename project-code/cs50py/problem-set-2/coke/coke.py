total_amount_due = 50  # Total amount due for a bottle of Coke
amount_inserted = 0  # Initialize the amount inserted by the user

print("Welcome to the Coke machine!")
print("Please insert coins one at a time.")

# Loop until the user has inserted enough money
while amount_inserted < total_amount_due:
    print("Amount Due:", total_amount_due - amount_inserted) #, "cents")
    coin = int(input("Insert coin (25, 10, or 5): "))

    # Check if the coin is a valid denomination
    if coin in [25, 10, 5]:
        amount_inserted += coin
    else:
        print("Invalid coin denomination. Please try again.")

# Calculate the change
change = amount_inserted - total_amount_due

# Output the change
print("Change Owed:", change) #, "cents")
