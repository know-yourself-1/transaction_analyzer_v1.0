import csv

transactions = [
    {'amount': 1000.00, 'category': 'Salary', 'type': 'income', 'date': '2025-01-01', 'description': 'Monthly salary'},
    {'amount': 150.50, 'category': 'Groceries', 'type': 'expense', 'date': '2025-01-02', 'description': 'Weekly shopping'},
    {'amount': 300.00, 'category': 'Utilities', 'type': 'expense', 'date': '2025-01-05', 'description': 'Electricity bill'},
    {'amount': 200.00, 'category': 'Freelance', 'type': 'income', 'date': '2025-01-10', 'description': 'Web development'},
    {'amount': 45.99, 'category': 'Entertainment', 'type': 'expense', 'date': '2025-01-15', 'description': 'Cinema tickets'}
]

with open('transactions.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['amount', 'category', 'type', 'date', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for transaction in transactions:
        writer.writerow(transaction)

print("Файл transactions.csv успешно создан")