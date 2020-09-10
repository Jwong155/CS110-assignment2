'''
ASSIGNMENT DESCRIPTION:
Write a program to compute the total purchase price given the price of a
single item, the count of that item purchased, and the tax rates applied.

The state sales tax is 5% and the county sales tax  is 2.5% (You'll need to
represent these values as floats).
Your program should display the number of items, and the price for one item.
You can represent all price variables as floats. It should then display the
state tax, the county tax and the total sales tax for the purchase.
Finally, it should display the total purchase price including tax.

Remember to use the template you were given to structure your program
(header, analysis, named constants, design comments, interleaved code, etc.)
Do not use literal values in your program (aka, magic numbers), follow
the style conventions, and perform adequate test runs.


Name: Jonathan Wong
email: jwong155@binghamton.edu
Section #B55
Assignment #2
'''

## Do not write anything past column 78
## Go to next line instead (no wrapping!)
## USE MEANINGFUL NAMES!
## variables will use lower_snake_case
## constants will use UPPER_SNAKE_CASE

'''
ANALYSIS

RESTATEMENT:
  Ask to compute the total purchase price given the price of a single
  item, the count of that item purchased, and the two tax rates applied.

OUTPUT to monitor:
  STATE_SALES_TAX_TOTAL (float) - cost with a 5% tax
  COUNTRY_SALES_TAX_TOTAL (float) - cost with a 2.5% tax
  SALES_TAX_TOTAL (float) - total sales tax
  TOTAL_COST (float) - total cost of purchase with sales tax

INPUT from keyboard:
  item_price_str (str) - price of the item
  num_items_str (str) - number of the item(s)

GIVEN: 
  STATE_SALES_TAX (float) - 0.05
  COUNTRY_SALES_TAX (float) - 0.025

FORMULAS:
  STATE_SALES_TAX_TOTAL = (item_price * num_items) * STATE_SALES_TAX

  COUNTRY_SALES_TAX_TOTAL = (item_price * num_items) * COUNTRY_SALES_TAX

  SALES_TAX_TOTAL = STATE_SALES_TAX_TOTAL + COUNTRY_SALES_TAX_TOTAL

  TOTAL_COST = (item_price * num_items) + SALES_TAX_TOTAL
  
PROCESSING:
  First the program will get a value for item_price, then num_items. Next,
  the program will compute sales tax for the state and country using the
  formula above. The output will show the formulas results to the user.

'''
#IMPORTS

# CONSTANTS (NO LITERALS ALLOWED!  Except 1, -1, and 0)
STATE_SALES_TAX = 0.05
COUNTRY_SALES_TAX = 0.025
SALES_TAX_TOTAL = 0
STATE_SALES_TAX_TOTAL = 0
COUNTRY_SALES_TAX_TOTAL = 0
TOTAL_COST = 0
  
#  This program computes the total purchase price of an item along with its
#  quantity with a state sales tax of 5% and a country sales tax of 2.5%

def main():

  # Explain purpose of program to user
  print("Hello user, this is assignment 2! This program will output the " +
        "total purchase price of an item along with its quantity with a " +
        "state sales tax of 5% and a country sales tax of 2.5% applied.\n")
  
  # Usually you are going to ask the user for some input
  item_price_str = input("Please input the price of the item: $ ")
  num_items_str = input("Please input the quantity of this item: ")

  # You may need to convert the input
  item_price = float(item_price_str)
  num_items = int(num_items_str)
  
  # Printing out class and variables, only variables are required
  print("Item costs $ %.2f" % item_price)
  #print(type(item_price))
  print("Items quantity: ", num_items)
  #print(type(num_items))
        
  # Usually you will have to process the input in some way to get the outputs
  STATE_SALES_TAX_TOTAL = (item_price * num_items) * STATE_SALES_TAX

  COUNTRY_SALES_TAX_TOTAL = (item_price * num_items) * COUNTRY_SALES_TAX

  SALES_TAX_TOTAL = STATE_SALES_TAX_TOTAL + COUNTRY_SALES_TAX_TOTAL

  TOTAL_COST = (item_price * num_items) + SALES_TAX_TOTAL

  # Finally, you will have to display your labeled and formatted output
  # I was trying to include two things in a print statement but don't know how
  print("For", num_items, "item(s) costing $ %.2f each" % item_price)
  print("State sales tax from purchase is $ %.2f" % STATE_SALES_TAX_TOTAL)
  print("Country sales tax from purchase is $ %.2f" % COUNTRY_SALES_TAX_TOTAL)
  print("Total sales tax is $ %.2f" % SALES_TAX_TOTAL)
  print("Total cost of sales tax and purchase is $ %.2f" % TOTAL_COST)

if __name__ == '__main__':
  main()
