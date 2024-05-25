# used to bring IncomeTaxBrackets.csv into system

import numpy as np # not currently used, but is might be in future?
import pandas as pd

def bracket_dt(url = "https://raw.githubusercontent.com/tmolitor002/tax-brackets/master/Federal/IncomeTaxBrackets.csv"):
	# Imports tax bracket from raw github
	
	df = pd.read_csv(url, on_bad_lines='skip') # creates tax bracket data table
	return df

# URL: https://raw.githubusercontent.com/tmolitor002/tax-brackets/master/Federal/IncomeTaxBrackets.csv
	
def bracket_dtype(url = "https://raw.githubusercontent.com/tmolitor002/tax-brackets/master/Federal/IncomeTaxBrackets.csv"):
	# Imports tax brackets from raw github and returns data table types
	
	df = pd.read_csv(url, on_bad_lines='skip') # creates tax bracket data table
	df_dtypes = df.dtypes # creates data types from table
	return df_dtypes
	
def bracket_year_status(year, status, url = "https://raw.githubusercontent.com/tmolitor002/tax-brackets/master/Federal/IncomeTaxBrackets.csv"):
	# Imports applicable tax brackets based on tax year and filing status
	
	# import pandas as pd
	# import numpy as np	
	
	df = pd.read_csv(url, on_bad_lines='skip') # creates tax bracket data table
	df_sub1 = df[df.tax_year == year] # creates bracket with only certain tax year
	df_sub2 = df_sub1[df_sub1['filing_status'].isin([status])] # creates sub-set with only certain filing status
	return df_sub2
	
	
def main():
	# Used for testing of bracket_dt() and bracket_dtype()
	
	print('')
	print('hello world')
	print('')
	print("Testing import of tax bracket table:")
	print(bracket_dt())
	print('')
	print("Testing data types of tax bracket table:")
	print(bracket_dtype())
	print('')
	print("Testing bracket_year_status:")
	print(bracket_year_status(year = 2018, status = "Single"))
	print('')
if __name__ == '__main__':
	main()
	print('goodbye friend')
