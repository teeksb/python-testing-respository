rows = [
    "2026,Canada,120000",
    "2026,USA,95000",
    "2026,Nigeria,40000"
]

for row in rows:
    parts = row.split(",")
    print(parts)
    country = parts[1]
    revenue = int(parts[2])

    if revenue > 100000:
        print(country, "is high value")

print(parts)

# What your code does (correct mental model)
# First row (Canada)
# Splits the row → parts = ['2026','Canada','120000']
# Prints the first row
# Checks the value → 120000 > 100000 ✅
# Prints: Canada is high value
# Goes back up to the loop
# Second row (USA)
# Splits the row → parts = ['2026','USA','95000']
# Prints the second row
# Validation fails ❌
# Nothing else prints
# Goes back up to the loop
# Third row (Nigeria)
# Splits the row → parts = ['2026','Nigeria','40000']
# Prints the third row
# Validation fails ❌
# Loop ends
# After the loop
# parts still exists
# It contains the last stored value
# Prints Nigeria again