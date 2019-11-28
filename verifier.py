# simple check for discrepancies in climate reporting

import csv
import sys

# csv_file = "test.csv"

header = {"population": "none", "baseline_emissions": "none", "baseline_year": "none",
          "total_co2_emissions": "none", "total_co2_emissions_year": "none"}


# checks that the baseline emissions per capita isn't excessive or too low
def capita_emissions_check_baseline(baseline_emissions, population):
    try:
        metric = float(baseline_emissions) / float(population)
        if metric < 0.2 or metric > 40:
            print("Fail Baseline emissions Data check")
        else:
            print("Pass Baseline emissions Data check")
    except ValueError:
        print("Missing Baseline emissions Data")

# checks that the co2 emissions per capita isn't excessive or too low
def capita_emissions_check_co2(total_co2_emissions, population):
    try:
        metric = float(total_co2_emissions) / float(population)
        if metric < 0.2 or metric > 40:
            print("Fail Total CO2 Emissions Data check")
        else:
            print("Pass Total CO2 Emissions Data check")
    except ValueError:
        print("Missing Total CO2 Emissions Data")

# checks that the compound annual growth rate of emissions isn't too high or low
def CAGR_check(total_co2_emissions, total_co2_emissions_year, baseline_emissions, baseline_year):
    try:
        metric = ((float(total_co2_emissions) / float(baseline_emissions)) **
                  (1 / (float(total_co2_emissions_year) - float(baseline_year))) - 1)
        if abs(metric) > 40:
            print("Fail CAGR check")
        else:
            print("Pass CAGR check")
    except ValueError:
        print("Missing Total CO2 Emissions Data or Baseline Emissions data")

# checks that the co2 emissions do not differ too much from the baseline emissions
def co2_v_baseline_check(total_co2_emissions, baseline_emissions):
    try:
        total_co2_emissions = float(total_co2_emissions)
        baseline_emissions = float(baseline_emissions)
        if total_co2_emissions * 10 < baseline_emissions or baseline_emissions * 10 < total_co2_emissions:
            print("Fail CO2 vs Baseline emissions check")
        else:
            print("Pass CO2 vs Baseline emissions check")
    except ValueError:
        print("Missing Total CO2 Emissions Data or Baseline Emissions data")

# searches for the headers you need and runs the checks
def check_file(file):
    x = 0
    with open(file, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_count = 0

        for row in csv_reader:
            row_count += 1
            if line_count == 0:
                for enum, i in enumerate(row):
                    if i == "baseline_emissions":
                        x = enum
                        header[i] = enum
                    elif i == "population":
                        x = enum
                        header[i] = enum
                    elif i == "total_co2_emissions":
                        x = enum
                        header[i] = enum
                    elif i == "total_co2_emissions_year":
                        x = enum
                        header[i] = enum
                    elif i == "baseline_year":
                        x = enum
                        header[i] = enum

                line_count += 1
            else:
                print("City " + row[0] + " From row " + str(row_count))
                baseline_check = capita_emissions_check_baseline(
                    row[header["baseline_emissions"]], row[header["population"]])
                totalco2_check = capita_emissions_check_co2(
                    row[header["total_co2_emissions"]], row[header["population"]])
                CAGR_check(row[header["total_co2_emissions"]], row[header["total_co2_emissions_year"]],
                           row[header["baseline_emissions"]], row[header["baseline_year"]])
                co2_v_baseline_check(
                    row[header["total_co2_emissions"]], row[header["baseline_emissions"]])


if __name__ == '__main__':
    csv_file = sys.argv[1]
    check_file(csv_file)
