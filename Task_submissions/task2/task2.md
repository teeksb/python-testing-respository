{
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

# Using the provided COVID-19 sample data, attempt the following tasks

1. Find the country with the highest number of active cases
2. Calculate the ratio of active cases to population for each country
3. Find the country with the highest recovery rate (recoveries/total_cases)
4. Calculate active cases as a percentage of population for each country
5. Generate a new dictionary showing which countries have more than 20,000 active cases
6. Calculate the total number of active cases across all countries
7. Add a new key called "cases_per_million" to each country based on total_cases
8. Using user input, update the active cases for a specific country and recalculate the global total
9. Calculate what percentage of global active cases each country represents. Represent the result as a dictionary.
