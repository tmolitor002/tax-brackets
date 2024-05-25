import github_tax_brackets as gtb # reference to tax-brackets/Federal/python/github_tax_brackets.py
import numpy as np
import pandas as pd

# grabs minimum and maximum year
full_table = gtb.bracket_dt()	
min_year = full_table['tax_year'].min()
max_year = full_table['tax_year'].max()

def tax_year_int(prompt, min = min_year, max=max_year):
	while True:
		try:
			# Note: 2.x users should use raw_input, the equivalent of 3.x's input
			value = int(input(prompt))
		except ValueError:
			print("Sorry, I didn't undertand that. Would you please try again?")
			# better try again ... Return to the start of the loop
			continue
			# Tax year is a number
		
		if value < min:
			print("Sorry, the first available year is {} Would you like to try a later year?".format(min))
			continue
		elif value > max:
			print("Sorry, the latest available year is {}. Would you like to try an earlier year?".format(max))
			continue
		else:
			break
	return value		

def main():
	print('Test of main function:\n')
	print(min_year)
	print(max_year)
	print(tax_year_int(2018, min_year, max_year))
	print('')
	print('#######################################################')
	print('')

if __name__ == '__main__':
	main()
