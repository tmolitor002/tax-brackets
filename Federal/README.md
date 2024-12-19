# Federal Tax Brackets

Current collection of income tax brackets and description:

1. **IncomeTaxBrackets.csv:** Federal income tax brackets for various filing status for 2008 through 2024. Fields include:
  * **`filing_status`:**
    * `Head of Household`
    * `Married Filing Jointly`
    * `Married Filing Separately`
    * `Qualifying Widow`
    * `Single`
  * **`tax_year`:** Currently 2008 through ~~2024~~ 2025 included.
  * **`bracket_min`:** The minimum amount or lower bound taxed at a given rate. e.g., for Married Filing Jointly in 2018, `bracket_min` would be `600000` for the 37% rate. The lowest tax bracket will have a value of `0`.
  * **`bracket_max`:** The maximum amount or upper bound taxed at a given rate. e.g, for Married Filing Jointly in 2018, `bracket_max` would be `600000` for the 35% rate. If the top tax bracket has no maximum, the value will be *empty*.
  * **`rate`:** Tax rate for the given tax bracket. e.g, for Married Filing Jointly in 2018, the top rate of 37% would be `0.37`.
  * **`add_tax`:** The amount of tax to be added from lower tax brackets.
  * **`updated_y_m_d`:** The last time the record was reviewed for accuracy.
  
2. **python:** Program to calculate a very rough estimated tax liability based on year, filing status, and taxable income.
 * **`tax_brackets.py`:** Main program. Contains interactions and calls to other python files within this folder.
 * **`github_tax_brackets.py`:** Method used to import `IncomeTaxBrackets.csv` into the other software.
 * **`tax_status.py`:** Method used to validate and standardized filing status.
 * **`tax_year.py`:** Method used to validate tax year. When combined with `tax_status.py`, will minimize the tax brackets returned.

~~2. **Tax Brackets.yxmc:** An Alteryx Macro that will pull `IncomeTaxBrackets.csv` from Github and perform minor data transformation to prepare the output for use.~~

~~3. **FederalIncome Tax Brackets Example.yxzp:** A packaged Alteryx file with three examples on how the macro can be utilized. Further insturction is also included.~~

## To reiterate the license, THERE IS NO GUARANTEE OF ACCURACY. THIS SOFTWARE SHALL NOT BE CONSIDERED TAX ADVICE. CONSULT WITH A CERTIFIED PUBLIC ACCOUNTANT OR TAX PROFESSIONAL.
