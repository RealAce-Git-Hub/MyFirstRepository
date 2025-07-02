daily_items = {"Phone":55, "Food":30, "Toothbrush":10, "Toothpaste":3, "Pencil":3, "Notebook":6, "Plate":5, "Laptop":70, "Tablet": 50, "Pen": 4}
weekly_expense = {"Week1":0, "Week2":0, "Week3":0, "Week4":0}

for k1, v1 in weekly_expense.items():
    expense = 0
    for k2, v2 in daily_items.items():
        expense = expense + v2 * 1
    weekly_expense[k1] = expense

print(weekly_expense)