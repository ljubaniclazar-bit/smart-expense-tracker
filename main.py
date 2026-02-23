expenses = {}

while True:
    category = input("Unesi kategoriju (ili 'exit'): ")
    if category.lower() == "exit":
        break

    amount = float(input("Unesi iznos: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

total = sum(expenses.values())

print("\n--- IZVEŠTAJ ---")
for category, amount in expenses.items():
    print(f"{category}: {amount}")

print("Ukupno potrošeno:", total)

# Najveća kategorija
max_category = max(expenses, key=expenses.get)
print("Najviše potrošeno na:", max_category)