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


def highest_active_cases(countries):
    highest_active = 0
    highest_country = ""

    for country in countries:
        active = countries[country]["active_cases"]
        if active > highest_active:
            highest_active = active
            highest_country = country

    print(f"1) Highest active cases: {highest_country} with {highest_active:,} cases")


def active_cases_ratio(countries):
    ratios = {}

    for country in countries:
        active = countries[country]["active_cases"]
        population = countries[country]["population"]
        ratios[country] = (active / population) * 100

    print("2) Active cases to population ratio (%):")
    pprint(ratios)


def highest_recovery_rate(countries):
    highest_rate = 0
    best_country = ""

    for country in countries:
        recoveries = countries[country]["recoveries"]
        total_cases = countries[country]["total_cases"]
        rate = recoveries / total_cases

        if rate > highest_rate:
            highest_rate = rate
            best_country = country

    print(f"3) Highest recovery rate: {best_country} with rate {highest_rate:.4f}")


def active_cases_percentage(countries):
    percentages = {}

    for country in countries:
        active = countries[country]["active_cases"]
        population = countries[country]["population"]
        percentages[country] = (active / population) * 100

    print("4) Active cases percentage of population (%):")
    pprint(percentages)


def countries_over_20000_active(countries):
    result = {}

    for country in countries:
        if countries[country]["active_cases"] > 20000:
            result[country] = countries[country]["active_cases"]

    print("5) Countries with more than 20,000 active cases:")
    pprint(result)


def total_active_cases(countries):
    total = 0

    for country in countries:
        total = total + countries[country]["active_cases"]

    print(f"6) Total active cases across all countries: {total:,}")
    return total 


def add_cases_per_million(countries):
    for country in countries:
        total_cases = countries[country]["total_cases"]
        population = countries[country]["population"]
        countries[country]["cases_per_million"] = (total_cases / population) * 1000000

    print("7) Added cases_per_million:")
    for country in countries:
        print(country, "=", countries[country]["cases_per_million"])


def update_active_cases(countries):
    country_name = input("Enter country you want to update active cases for: ")
    new_active = int(input("Enter new active cases number: "))

    if country_name in countries:
        countries[country_name]["active_cases"] = new_active
        print(f"8) Updated {country_name} active cases to {new_active:,}")
    else:
        print("8) Country not found!")


def update_global_active(covid_data):
    countries = covid_data["countries"]
    total = 0

    for country in countries:
        total = total + countries[country]["active_cases"]

    covid_data["global"]["active_cases"] = total
    print(f"8b) New global active cases: {total:,}")


def percent_of_global_active(covid_data):
    countries = covid_data["countries"]
    global_active = covid_data["global"]["active_cases"]
    result = {}

    for country in countries:
        active = countries[country]["active_cases"]
        result[country] = (active / global_active) * 100

    print("9) Percentage of global active cases (%):")
    pprint(result)


def full_report():
    countries = covid19_data["countries"]

    highest_active_cases(countries)
    print()

    active_cases_ratio(countries)
    print()

    highest_recovery_rate(countries)
    print()

    active_cases_percentage(countries)
    print()

    countries_over_20000_active(countries)
    print()

    total_active_cases(countries)
    print()

    add_cases_per_million(countries)
    print()

    update_active_cases(countries)
    print()

    update_global_active(covid19_data)
    print()

    percent_of_global_active(covid19_data)


full_report()
