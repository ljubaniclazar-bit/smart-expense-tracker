expenses = {}

while True:
    category = input("Enter a category (or 'exit'): ")
    if category.lower() == "exit":
        break

    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

total = sum(expenses.values())

print("\n--- REPORT ---")
for category, amount in expenses.items():
    print(f"{category}: {amount}")

print("Total spent:", total)

# Highest spending category
max_category = max(expenses, key=expenses.get)
print("Highest spending category:", max_category)