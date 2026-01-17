from pprint import pprint

covid19_data ={
    "countries": {
        "Nigeria": {
            "population": 5000000,
            "total_cases": 250000,
            "active_cases": 16500,
            "deaths": 3500,
            "recoveries": 230000,
            "testing": 1200000,
            "vaccination": {
                "first_dose": 3500000,
                "fully_vaccinated": 3200000,
                "boosters": 1800000
            },
            "monthly_cases": {
                "Jan": 45000,
                "Feb": 32000,
                "Mar": 25000,
                "Apr": 18000,
                "May": 15000,
                "Jun": 10000
            }
        },
        "Ghana": {
            "population": 8000000,
            "total_cases": 420000,
            "active_cases": 23800,
            "deaths": 6200,
            "recoveries": 390000,
            "testing": 1900000,
            "vaccination": {
                "first_dose": 5100000,
                "fully_vaccinated": 4800000,
                "boosters": 2500000
            },
            "monthly_cases": {
                "Jan": 80000,
                "Feb": 65000,
                "Mar": 40000,
                "Apr": 25000,
                "May": 12000,
                "Jun": 8000
            }
        },
        "England": {
            "population": 3000000,
            "total_cases": 180000,
            "active_cases": 5900,
            "deaths": 2100,
            "recoveries": 172000,
            "testing": 950000,
            "vaccination": {
                "first_dose": 2100000,
                "fully_vaccinated": 1950000,
                "boosters": 900000
            },
            "monthly_cases": {
                "Jan": 35000,
                "Feb": 30000,
                "Mar": 20000,
                "Apr": 12000,
                "May": 8000,
                "Jun": 5000
            }
        },
        "Kenya": {
            "population": 6500000,
            "total_cases": 350000,
            "active_cases": 15200,
            "deaths": 4800,
            "recoveries": 330000,
            "testing": 1600000,
            "vaccination": {
                "first_dose": 3900000,
                "fully_vaccinated": 3500000,
                "boosters": 1600000
            },
            "monthly_cases": {
                "Jan": 70000,
                "Feb": 50000,
                "Mar": 35000,
                "Apr": 20000,
                "May": 10000,
                "Jun": 5000
            }
        }
    },
    "global": {
        "total_cases": 1200000,
        "active_cases": 61400,
        "total_deaths": 16600,
        "total_recoveries": 1122000,
        "total_vaccines_distributed": 25000000
    },
    "variants": {
        "Alpha": {"first_detected": "Sep 2020", "transmissibility": "Medium"},
        "Beta": {"first_detected": "Oct 2020", "transmissibility": "Medium"},
        "Delta": {"first_detected": "Dec 2020", "transmissibility": "High"},
        "Omicron": {"first_detected": "Nov 2021", "transmissibility": "Very High"}
    }
}

countries = covid19_data["countries"]

# 1. Country with the highest number of active states
highest_active_cases = 0
highest_country = ""

for country in countries:
    active = countries[country]["active_cases"]
    if active > highest_active_cases:
        highest_active_cases = active
        highest_country = country

print("1) Highest country with active cases is:",highest_country, "with", highest_active_cases, "cases")
print("\n")
# 2. Ratio of active cases to population for each country
active_to_population_ratio = {}

for country in countries:
    active = countries[country]["active_cases"]
    population = countries[country]["population"]
    active_to_population_ratio[country] = active/population

print("2) Ratio of active cases to population for each country is: ", "\n", active_to_population_ratio)
print("\n")

# 3. Find the country with the highest recovery rate (recoveries/total_cases)
highest_recovery_rate = 0
country_best_recovery = ""

for country in countries:
    recoveries = countries[country]["recoveries"]
    total_cases = countries[country]["total_cases"]
    recovery_rate = recoveries / total_cases

    if recovery_rate > highest_recovery_rate:
        highest_recovery_rate = recovery_rate
        country_best_recovery = country

print("3) Country with highest recovery rate is:", country_best_recovery, "with a rate of:", highest_recovery_rate)

print("\n")

# 4. Calculate active cases as a percentage of population for each country

active_case_percentage = {}

for country in countries:
    active = countries[country]["active_cases"]
    population = countries[country]["population"]
    active_case_percentage[country] = (active/population) * 100

print("4) Active percentage for each country are :","\n", active_case_percentage )

print("\n")

# 5. Generate a new dictionary showing which countries have more than 20,000 active cases
active_cases_over_20000 = {}

for country in countries:
    if countries[country]["active_cases"] > 20000:
        active_cases_over_20000[country] = countries[country]["active_cases"]

print("5) Countries with more than 20,000 active cases are:","\n", active_cases_over_20000)

print("\n")

# 6. Calculate the total number of active cases across all countries
total_number_active_cases = 0

for country in countries:
    total_number_active_cases = total_number_active_cases + countries[country]["active_cases"]

print("6) Total number of active cases across all countries is:", total_number_active_cases)

print("\n")

# 7. Add a new key called "cases_per_million" to each country based on total_cases
for country in countries:
    total_cases = countries[country]["total_cases"]
    population = countries[country]["population"]
    countries[country]["cases_per_million"] = (total_cases / population) * 1000000

print("7) Cases per million for each country:") 
for country in countries:
    print(country,":","\n""cases_per_million:",countries[country]["cases_per_million"])

print("\n")

# 8. Using user input, update the active cases for a specific country and recalculate the global total
country_name = input("Enter country you want to update active cases for: ")
new_active = int(input("Enter new active cases number: "))

if country_name in countries:
    countries[country_name]["active_cases"] = new_active
    print("8) New active cases for", country_name, "is", new_active)
else:
    print("Country not found!")