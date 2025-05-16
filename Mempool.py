class Mempool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, tx):
        if self.validate_transaction(tx):
            self.transactions.append(tx)
            print(f"Transaction {tx['id']} added.")
        else:
            print(f"Transaction {tx['id']} is invalid and was not added.")

    def remove_transaction(self, tx_id):
        before = len(self.transactions)
        self.transactions = [tx for tx in self.transactions if tx['id'] != tx_id]
        after = len(self.transactions)
        if before != after:
            print(f"Transaction {tx_id} removed.")
        else:
            print(f"Transaction {tx_id} not found.")

    def validate_transaction(self, tx):
        # Simple placeholder: always valid
        # Add real validation logic here!
        return True

    def get_transactions(self):
        return self.transactions

# Example usage
if __name__ == "__main__":
    mempool = Mempool()
    tx1 = {'id': 'tx123', 'sender': 'A', 'receiver': 'B', 'amount': 10}
    tx2 = {'id': 'tx124', 'sender': 'C', 'receiver': 'D', 'amount': 5}
    
    mempool.add_transaction(tx1)
    mempool.add_transaction(tx2)
    
    print("All transactions in mempool:")
    for tx in mempool.get_transactions():
        print(tx)
    
    mempool.remove_transaction('tx123')
    print("After removal:")
    for tx in mempool.get_transactions():
        print(tx)