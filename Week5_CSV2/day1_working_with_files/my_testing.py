rows = [
    "2026,Canada,120000",
    "2026,USA,95000",
    "2026,Nigeria,40000"
]

with open("high_value.csv", "w") as out:
    out.write("year,country,revenue\n")

    for row in rows:
        parts = row.split(",")
        revenue = int(parts[2])

        if revenue > 100000:
            out.write(row + "\n")



