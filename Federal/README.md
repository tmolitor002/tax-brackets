# Federal Tax Brackets

Current collection of income tax brackets and description:

1. **IncomeTaxBrackets.csv:** Federal income tax brackets for various filing status for 2018 and 2019. Fields include
  * **`filing_status`:** Single, Head of Household, etc.,
    * Married Filing Jointly and Qualified Widow have the same brackets, and therefore listed together in the table as `Married Filing Jointly or Qualifying Widow`
  * **`tax_year`:** Currently 2018 and 2019 included, more coming soon!
  * **`bracket_min`:** The minimum amount or lower bound taxed at a given rate. e.g., for Married Filing Jointly in 2018, `bracket_min` would be `600000` for the 37% rate. The lowest tax bracket will have a value of `0`.
  * **`bracket_max`:** The maximum amount or upper bound taxed at a given rate. e.g, for Married Filing Jointly in 2018, `bracket_max` would be `600000` for the 35% rate. If the top tax bracket has no maximum, the value will be *empty*.
  * **`rate`:** tax rate for the given tax bracket. e.g, for Married Filing Jointly in 2018, the top rate would be `0.37`.
