# rows = ["100", "N/A", "200"]

# for r in rows:
#     try:
#         value = int(r)
#     except:
#         continue
#     print(value)

# print("Done")


# rows = ["100", "N/A", "200", "bad", "300"]

# total = 0
# converted = 0
# skipped = 0

# for r in rows:
#     total += 1
#     try:
#         value = int(r)
#         converted += 1
#     except ValueError:
#         skipped += 1
#         continue

# print("Total:", total)
# print("Converted:", converted)
# print("Skipped:", skipped)

# def parse(row):
#     parts = row.split(",")
#     return parts[0], parts[1], parts[2]

# rows = ["2026,Canada,120000", "2026,Nigeria,N/A"]

# for row in rows:
#     year, country, rev = parse(row)
#     try:
#         revenue = int(rev)
#     except ValueError:
#         print("skip", country)
#         continue
#     print("ok", country, revenue)


# for row in rows:
#     try:
#         revenue = int(rev)
#     except ValueError:
#         print("bad")
#     if revenue > 100000:
#         print("high")

rows = ["100", "N/A", "200"]

for r in rows:
    try:
        revenue = int(r)
    except ValueError:
        print("Bad row")
    print("Revenue is", revenue)