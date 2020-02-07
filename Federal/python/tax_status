import github_tax_brackets as gtb
import numpy as np
import pandas as pd
import re as regex # Regex is used to modify and standardize different entries for filing status

# Regex and open ended prompts for filing status should eventually be replaced by a dropdown option.

def tax_status_str(prompt):
	hoh = "Head of Household"
	mfj = "Married Filing Jointly"
	mfs = "Married Filing Separately"
	qw = "Qualifying Widow"
	sin = "Single"
	while True:
		try:
			# Note: 2.x users should use raw_input, the equivalent of 3.x's input
			value_1 = regex.sub('[^A-Za-z]+', '', input(prompt)).upper()
		except ValueError:
			print("Sorry, I didn't undertand that. Would you please try again?")
			# Better try again ... return to the start of the loop
			continue
			# Value is a string
			
		# Looking for different possible entries to determine filing status.
		# There is probably a wayyyyy better way to do this.
		if value_1 == "H" or value_1 == "HOH" or value_1 == "HEADOFHOUSEHOLD":
			value = hoh
			break
		elif value_1 == "MFJ" or value_1 == "M" or value_1 == "MARRIEDFILINGJOINTLY":
			value = mfj
			break
		elif value_1 == "MFS" or value_1 == "MARRIEDFILINGSEPARATELY":
			value = mfs
			break
		elif value_1 == "QW" or value_1 == "W" or value_1 == "WIDOW" or value_1 == "QUALIFYINGWIDOW":
			value = qw
			break
		elif value_1 == "S" or value_1 == "SINGLE" or value_1 == "ALONE":
			value = sin
			break
		else:
			print("Sorry, that's not an available option. Please try again")
			continue
	return value
	
	
	
def main():
	print('Test of main function:')
	print('')
	tax_status = tax_status_str("What is your tax status? :")
	print(tax_status)
	print('End of test')

if __name__ == '__main__':
	main()
