def opening_message(): # This is just for fun
	name = input('Enter your name: ').upper()
	print("######################################################")
	print("#                                                    #")
	print("#                                                    #")
	print("  PLEASE WAIT {}, LIBRARY IS LOADING...                ".format(name))
	print("#                                                    #")
	print("#                                                    #")
	print("######################################################")

opening_message() # Opening message
	
import github_tax_brackets as gtb # github_tax_brackets.py is used to read in raw csv from github
import tax_year as taxy # tax_year.py is used to only accept valid tax years
import tax_status as file_status # tax_status.py is used to only accept valid filing status
import numpy as np # not currently used, but is might be in future?
import pandas as pd

# Current Location: C:\Users\tmolitor002\Documents\DA Training\Python\Tax Brackets\

# def main():
#	# Test of functionality of gtb.bracket_dt() and gtb.bracket_dtype()
	# print('')
	# print("hello world")
	# print('')
	# print("Test to show all brackets:")
	# print(gtb.bracket_dt())
	# print('')
	# print("test to show data types:")
	# print(gtb.bracket_dtype())
	# print('')
	# print("test of selected brackets:")
	# print(gtb.bracket_year_status(year = 2018, status = "Single"))
	# print('')
	# print("goodbye friend")
	# print('')

# if __name__ == '__main__': # test of file
	# # test of possible functions
	# main()

# grabs minimum and maximum year
full_table = gtb.bracket_dt()	
min_year = full_table['tax_year'].min()
max_year = full_table['tax_year'].max()
print('')	

tax_year = taxy.tax_year_int('Enter the applicable tax year: ', min = min_year, max = max_year) # Prompts for tax year that must be in possible range of years

tax_status = file_status.tax_status_str('Enter your filing status on December 31, {} (e.g. Head of Household, Married Filing Jointly, Married Filing Separately, Qualifying Widow, Single): '.format(str(tax_year))) # asks user for applicable tax status

#print('')
#tax_status = str(input('Enter your filing status on December 31, {} (e.g. Head of Household, Married Filing Jointly, Married Filing Separately, Qualifying Widow, Single): '.format(str(tax_year)))) # asks user for applicable tax status
print('')
	
bracket_table = gtb.bracket_year_status(year = tax_year, status = tax_status) # creates table with applicable tax brackets

print(bracket_table)

print('')
tax_income = float(input('Enter you taxable income for ' + str(tax_year) +': ')) # Ask for taxable income, utilizes tax_year above

top_bracket_1 = bracket_table[bracket_table.bracket_min < tax_income] # removes brackets with minimum greater than taxable income

top_bracket = top_bracket_1[-1:] # last bracket will be top applicable bracket

# Shows top applicable bracket
print('')
print('Top applicable tax bracket is:')
print('')
print(top_bracket)

print('')

to_tax = tax_income - top_bracket.iloc[0]['bracket_min'] # extracts remaing amount to be taxed in current bracket

# Various metrics calculated to return to user
top_rate = top_bracket.iloc[0]['rate']
top_rate_percent = (top_rate * 100)
top_tax = to_tax * top_rate
lower_tax = top_bracket.iloc[0]['add_tax']
tax_liability = top_tax + lower_tax
income_kept = tax_income - tax_liability
effective_tax_rate = ((tax_liability/tax_income) * 100)

if income_kept > 250000: # Consider updating for different filing status
	print("Wow! Your total tax liability in {} is ${:0.2f}. But hey! on the brightside, you still got to keep ${:0.2f}. That's not bad right? Pretty good year if you ask me. Wish I made that much money :/".format(tax_year, tax_liability, income_kept))
else:
	print("Wow! Your total tax liability in {} is ${:0.2f}. But hey! On the brightside, you still got to keep ${:0.2f}. That's not bad, right?".format(tax_year, tax_liability, income_kept)) 


print('')
print("Did you know that your effective tax rate is {:0.2f}%? That sounds like it's below the top rate of {:0.2f}%, so looks like you're getting a great deal!".format(effective_tax_rate, top_rate_percent))
print('')

def credits(): # this is also just for fun
	print('')
	print("######################################################")
	print("#                                                    #")
	print("#                  END OF PROGRAM                    #")
	print("#                                                    #")
	print("# CREATED BY TOM MOLITOR (HIS FIRST PYTHON PROJECT)  #")
	print("#                                                    #")
	print("######################################################")
	print('')
	
credits() # closing message
