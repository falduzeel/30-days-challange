print("=== Daily Expense Tracker ===")

budget = float(input("Enter your total budget: ₹"))

food = float(input("Food / Snacks expense: ₹"))
transport = float(input("Transport expense: ₹"))
study = float(input("Books / Study expense: ₹"))
other = float(input("Other expense: ₹"))

total_expense = food + transport + study + other
remaining_balance = budget - total_expense

print("\n--- Summary ---")
print(f"Total Budget: ₹{budget}")
print(f"Total Spent : ₹{total_expense}")
print(f"Remaining   : ₹{remaining_balance}")

if remaining_balance < 0:
    print("Warning: Your expenses exceed your budget!")
else:
    print("Great! Your expenses are within budget.")