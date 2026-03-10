# # 1. Understand 
# # 2. Input 
# # 3. Output 
# # 4. Pattern 
# # 5. Skeleton 
# # 6. Implement


# # Problem: Calculate the average order value by product categories

# # 1. Understading the problem set
# # average order value = total sales amount / total number of orders

# def average_order_by_category(orders):
#     # Step 1: Group by category, track the sum and count values for each category

#     # NOTE: You can use one dictionary (rather than two as done below) to keep track of the
#     # total order value and count (number of occurrences) for each category

#     category_totals = {}
#     category_counts = {}

#     for order in orders:
#         # Get the category name and purchase amount
#         category_name = order["Product_Category"]
#         purchase_amt = order["Purchase_Amount"]

#         #region Recursively increment to total amount, and increment the count (by 1)

#         # - For the `category_totals` variable
#         if category_name not in category_totals:
#             category_totals[category_name] = purchase_amt
#         else:
#             category_totals[category_name] += purchase_amt

#         #- For the `category_counts` variable
#         if category_name not in category_counts:
#             category_counts[category_name] = 1
#         else:
#             category_counts[category_name] += 1
#         #end category
    
#     # Step 2: Calculate averages
#     # Introduce a new variable to keep track of average values
#     category_averages = {}

#     # Loop through the category_totals, get the category name, the total order value
#     #   Use the category name to retrieve the count/occurrences
#     for (category, total) in category_totals.items():
#         count = category_counts[category]

#         # Calculate average using the total order value and the count
#         category_averages[category] = total / count
    
#     # Neatly display the result (categories and their respective average order values)
#     print("")
#     print(f"{'Product Category':<24} {'Avg Order Value (USD)':<8}")
#     print("-"*50)
#     for (cat, avg) in category_averages.items():
#         print(f"{cat:<24} ${avg:>8,.2f}")
#     print("")

# def main():
#     import csv

#     with open("../Files/customer_transaction.csv") as file:
#         reader = csv.DictReader(file)

#         transactions = []

#         for item in reader:
#             item["Purchase_Amount"] = float(item["Purchase_Amount"])
#             transactions.append(item)

#         average_order_by_category(transactions)

# main()




# from collections import defaultdict
# import csv


# def average_order_by_category(orders):
#     """
#     Calculate and display average order value per product category.
#     average = total_sales / number_of_orders
#     """

#     # Step 1: Group by category, track totals + counts
#     category_totals = defaultdict(float)  # missing keys start at 0.0
#     category_counts = defaultdict(int)    # missing keys start at 0

#     for order in orders:
#         category_name = order["Product_Category"]
#         purchase_amt = order["Purchase_Amount"]  # already converted to float in main()

#         category_totals[category_name] += purchase_amt
#         category_counts[category_name] += 1

#     # Step 2: Compute averages
#     category_averages = {}
#     # for x, y in category_totals.items(): - this is anither way of writing the below
#     for category, total in category_totals.items():
#         count = category_counts[category]
#         category_averages[category] = total / count if count else 0.0

#     # Step 3: Display neatly (sorted by category name)
#     print("")
#     print(f"{'Product Category':<24} {'Avg Order Value (USD)':>20}")
#     print("-" * 50)

#     for cat in sorted(category_averages.keys()):
#         avg = category_averages[cat]
#         print(f"{cat:<24} ${avg:>19,.2f}")

#     print("")


# def main():
#     with open("../Files/customer_transaction.csv", newline="") as file:
#         reader = csv.DictReader(file)

#         orders = []
#         for item in reader:
#             # Ensure numeric type for calculations
#             item["Purchase_Amount"] = float(item["Purchase_Amount"])
#             orders.append(item)

#     average_order_by_category(orders)


# if __name__ == "__main__":
#     main()


#Another method
from collections import defaultdict
import csv


def average_order_by_category(orders):
    """
    Calculate and display average order value per product category.
    average = total_sales / number_of_orders
    """

    # ONE dictionary tracking both total and count
    category_stats = defaultdict(lambda: {"total": 0.0, "count": 0})

    # Step 1: Aggregate
    for order in orders:
        category_name = order["Product_Category"]
        purchase_amt = order["Purchase_Amount"]

        category_stats[category_name]["total"] += purchase_amt
        category_stats[category_name]["count"] += 1

    # Step 2: Compute averages
    category_averages = {}

    for category, stats in category_stats.items():
        total = stats["total"]
        count = stats["count"]
        category_averages[category] = total / count if count else 0.0

    # Step 3: Display neatly
    print("")
    print(f"{'Product Category':<24} {'Avg Order Value (USD)':>20}")
    print("-" * 50)

    for cat in sorted(category_averages.keys()):
        avg = category_averages[cat]
        print(f"{cat:<24} ${avg:>19,.2f}")

    print("")


def main():
    with open("../Files/customer_transaction.csv", newline="") as file:
        reader = csv.DictReader(file)

        orders = []
        for item in reader:
            # Ensure numeric type for calculations
            item["Purchase_Amount"] = float(item["Purchase_Amount"])
            orders.append(item)

    average_order_by_category(orders)


if __name__ == "__main__":
    main()
