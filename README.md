# data_verification

## Intro
Sometimes emissions data can be misreported. This script does some simple checks to ensure that the numbers reported are not too ridiculous.

## Usage
1. Ensure that your file headers are of a similar format
```
"population", "baseline_emissions", "baseline_year", "total_co2_emissions", "total_co2_emissions_year"
```

2. Run the script on your .csv file

3. It for each line in your file whether it passes the following:
  - per capita co2 emissions
  - per capita baseline emissions
  - compound annual growth rate of emissions
  - co2 vs baseline emissions
  
