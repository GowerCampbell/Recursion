# banking_recursive.py - Gower Campbell  
# A simple banking app using recursion for transaction analysis and file I/O for data persistence.

class TransactionAnalyzer:
    number_of_transactions = 0  # Class-level counter for all added transactions

    def __init__(self):
        self.transactions = []  # Stores transactions as (date, description, amount)

    def add_transaction(self, date, description, amount):
        self.transactions.append((date, description, amount))
        TransactionAnalyzer.number_of_transactions += 1

    def sum_deposits(self, transactions=None):
        """
        Recursively sums all positive amounts (deposits).
        If no list is passed, it defaults to self.transactions.
        """
        if transactions is None:
            transactions = self.transactions
        if not transactions:  # Base case: no more transactions
            return 0
        amount = transactions[0][2]
        return (amount if amount > 0 else 0) + self.sum_deposits(transactions[1:])

    def count_below(self, threshold, transactions=None):
        """
        Recursively counts how many transactions are below a certain threshold.
        Great for tracking small expenses.
        """
        if transactions is None:
            transactions = self.transactions
        if not transactions:
            return 0
        return (1 if transactions[0][2] < threshold else 0) + self.count_below(threshold, transactions[1:])

def load_transactions(filename):
    """
    Loads transactions from a file and returns a TransactionAnalyzer.
    Each line must be formatted as: date,description,amount
    """
    analyzer = TransactionAnalyzer()
    try:
        with open(filename, 'r') as file:
            for line in file:
                date, desc, amount = line.strip().split(',')
                analyzer.add_transaction(date, desc, float(amount))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with a blank slate.")
    return analyzer

def save_transactions(filename, analyzer):
    """
    Saves all transactions to the file in CSV format.
    """
    with open(filename, 'w') as file:
        for date, desc, amount in analyzer.transactions:
            file.write(f"{date},{desc},{amount}\n")

def main():
    filename = "transactions.txt"
    analyzer = load_transactions(filename)

    print("Welcome to Recursive Banking")

    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. Sum Deposits (Recursive)")
        print("3. Count Expenses Below Threshold (Recursive)")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Date (e.g., 2025-01-01): ")
            desc = input("Description: ")
            try:
                amount = float(input("Amount (use negative for expenses): "))
                analyzer.add_transaction(date, desc, amount)
                print("Transaction added.")
            except ValueError:
                print("Please enter a valid number for amount.")
        elif choice == "2":
            total = analyzer.sum_deposits()
            print(f"Total Deposits: ${total:.2f}")
        elif choice == "3":
            try:
                threshold = float(input("Enter threshold amount (e.g., -10): "))
                count = analyzer.count_below(threshold)
                print(f"Transactions below {threshold}: {count}")
            except ValueError:
                print("Please enter a valid number for threshold.")
        elif choice == "4":
            save_transactions(filename, analyzer)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    # Adding recursion here made basic banking logic feel way more powerful.
    # Summing deposits and counting expenses are classic recursive use cases.
