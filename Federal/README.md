# Federal Tax Brackets

Current collection of income tax brackets and description:

1. **IncomeTaxBrackets.csv:** Federal income tax brackets for various filing status for 2008 through 2020. Fields include:
  * **`filing_status`:**
    * `Head of Household`
    * `Married Filing Jointly`
    * `Married Filing Separately`
    * `Qualifying Widow`
    * `Single`
  * **`tax_year`:** Currently 2008 through 2020 included. More coming soon!
  * **`bracket_min`:** The minimum amount or lower bound taxed at a given rate. e.g., for Married Filing Jointly in 2018, `bracket_min` would be `600000` for the 37% rate. The lowest tax bracket will have a value of `0`.
  * **`bracket_max`:** The maximum amount or upper bound taxed at a given rate. e.g, for Married Filing Jointly in 2018, `bracket_max` would be `600000` for the 35% rate. If the top tax bracket has no maximum, the value will be *empty*.
  * **`rate`:** tax rate for the given tax bracket. e.g, for Married Filing Jointly in 2018, the top rate of 37% would be `0.37`.
  * **`updated_y_m_D`:** The last time the record was reviewed for accuracy.
  * **`null`:** An empty field to denote that last field in the file. All fields before `null` may have usefull information, and additinal fields may be added in the future.

2. **Tax Brackets.yxmc:** An Alteryx Macro that will pull `IncomeTaxBrackets.csv` from Github and perform minor data transformation to prepare the output for use.

3. **FederalIncome Tax Brackets Example.yxzp:** A packaged Alteryx file with three examples on how the macro can be utilized. Further insturction is also included.
