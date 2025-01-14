# Miguel Jimenez
# CIS129
# Professor Farmer
# 10-15-24
# Lab 5
# Description of code: This file runs a program which collects the number of bottles collected in a week and returns the payout.
# This program asks for an input for the number of bottles per day for 7 days (it then gives total amount of bottles collected in the week and payout for the week).
# The program then finally asks if you want to enter another 7 day's worth of data. 


# Step 1: Declare variables
def main():
    totalBottles = 0
    totalPayout = 0.0
    todayBottles = 0
    counter = 0
    keepGoing = "y"

    # Step 2: Loop to run the program again
    while keepGoing == "y":
            totalBottles = 0
            counter = 0
        
        # Step 3: Collect bottles for 7 days. Input to set value of variables.
        while counter < 7:
            todayBottles = int(input(f"Enter number of bottles returned for day # {counter + 1}: "))
            totalBottles += todayBottles
            counter += 1

        # Step 5: Calculate total payout
        totalPayout = totalBottles * 0.10

        # Step 6: Print total bottles and total payout
        print(f"\nThe total number of bottles collected is {totalBottles}")
        print(f"The total paid out is ${totalPayout:.2f}\n")

        # Ask user if they want to enter another week of data
        keepGoing = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

# Call to run program
main()
