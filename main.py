#Assignment 3.1
'''
write a while loop that will determine how long it takes for an investment to double
'''
import decimal  #decided to import decimal over float to try again from last week

interest_rate = decimal.Decimal(
    input("Enter interest rate as decimal, ex. .05 as 5% :")) # Allows to be read properly
print() 
initial_investment = decimal.Decimal(input("Enter amount investing:"))
print()
investment = initial_investment #create investment variable now to calculate in loop
year_count = 0 #create year_count at 0 for starting point calculated in loop
while investment < initial_investment * 2:  #loop will cont. if not at least double
  investment = (interest_rate * investment) + investment #adds accrued amount on
  year_count += 1 #adds year
  print("Year", year_count, "investment is:", investment)
print("Your investment doubled in", year_count, "years!") #states how many years it took
