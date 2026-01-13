# Website Traffic Analytics

# As a Data Analyst your job is to analyze the website traffic datat for an ecommerce site.
# The marketing team needs ti understand which paes users visit more frequently to optimize
# ad spend and/or marketing strategy.


# The Problem
# You have a log of page visit from 50 users. You need to:
# 1. Count how manmy times each page was visisted.
# 2. Find the most and least popular pages.
# 3. Calculate the percentage of traffic each page recieves.
# 4. Identify pages with low traffic, that need prpmotion.

import random
from pprint import pprint

pages = ["products", "product profile","about", "home", "checkout", "cart", "contacts"]
users = 50

log_of_pages_visited = []

for i in range(users):
    rounds = random.randint(3, 20)
    for take in range(rounds):
        index = random.randint(0, 6)
        log_of_pages_visited.append(pages[index])

print(log_of_pages_visited)

# STep 1 Count page visists
# Conecpt: Use dictionaries to count frequency - a fundamental data science task

page_counts = {}

for page in log_of_pages_visited:
     if page in page_counts:
        page_counts[page] = page_counts[page] + 1
     else:
        page_counts[page] = 1

print(log_of_pages_visited)
print("***************************************************")
print("\n")
pprint(page_counts)
print("***************************************************")
print("\n")


# print(len(log_of_pages_visited))
# print(log_of_pages_visited[:20])


# STep 2 FInd the most and least visisted pages
# Concept: Extract insightss from the freqyuency data

all_counts = page_counts.values()
max_visits = max(all_counts)
min_visits = min(all_counts)

print("\nMost popuar pages:")
for (key, value) in page_counts.items():
    # In this conetxt, the key is the page name, while the value is the visist frequency - i.e hoe many times the page was visisted.
    if value == max_visits:
        print(f"       -{key}: {value} visits")

print("\nLeast popular pages:")

for (key, value) in page_counts.items():
    # In this conetxt, the key is the page name, while the value is the visist frequency - i.e hoe many times the page was visisted.
    if value == min_visits:
        print(f"       -{key}: {value} visits")


print("***************************************************")
print("\n")
# STep 3 Calculate traffic percentatge
# Concept: COnvert page vsist count to percentages for better insight.

total_visits = page_counts.values()
total_visits = sum(page_counts.values())

print(f"\nTotal visits: {total_visits}")
print("\nTraffic Distribution:")


page_percentages = {}

for item in page_counts.items():
    percentage = (value/total_visits ) * 100
    page_percentages[key] + f"{percentage:.1f}"
    print(f"   {key}: {value} visits ({page_percentages[key]}%)")




print("***************************************************")
print("\n")
# STep 3: Identify Pages Needing Promotion
# Concept: CUse conditional logic with dictionary data to gather insight

low_traffic_threshold = 13 #percentage
low_traffic_pages = []

print("\nPAGES NEEDEING PROMOTION :")

for (key, value) in page_percentages.items():
    percentage_val = float(value)


    if percentage_val <= low_traffic_threshold:
        low_traffic_pages[page] = percentage_val

if len(low_traffic_pages) == 0:
    print(" All pages have adequate traffic")
else:
    pprint(low_traffic_pages)

print("*****************************************")
print("*****************************************")
print("*****************************************")