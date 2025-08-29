from transaction import Transaction
from miner import Blockchain
import json

class BlockchainSystem:
    def __init__(self, roll_no="0000"):
        self.blockchain = Blockchain(roll_no)
        self.accounts = {}
        self.pending_transactions = []
        self.roll_no = roll_no
        
    def create_account(self, account_name, initial_balance):
        """Create a new account with initial balance"""
        if account_name in self.accounts:
            print(f"Account '{account_name}' already exists!")
            return False
        
        self.accounts[account_name] = initial_balance
        print(f"Account '{account_name}' created with balance: {initial_balance}")
        return True
    
    def get_balance(self, account_name):
        """Get account balance"""
        return self.accounts.get(account_name, 0)
    
    def calculate_zakat(self, amount):
        """Calculate zakat (2.5% of transaction amount)"""
        return amount * 0.025
    
    def create_transaction(self, sender, receiver, amount):
        """Create and add a transaction with automatic zakat deduction"""
        try:
            # Check if accounts exist
            if sender not in self.accounts:
                print(f"Sender account '{sender}' does not exist!")
                return False
            if receiver not in self.accounts:
                print(f"Receiver account '{receiver}' does not exist!")
                return False
            
            # Calculate zakat
            zakat_amount = self.calculate_zakat(amount)
            total_deduction = amount + zakat_amount
            
            # Check if sender has sufficient balance
            if self.accounts[sender] < total_deduction:
                print(f"Insufficient balance! Required: {total_deduction} (Amount: {amount} + Zakat: {zakat_amount})")
                return False
            
            # Create main transaction
            transaction = Transaction(sender, receiver, amount)
            
            # Apply transaction
            self.accounts = transaction.apply(self.accounts)
            
            # Deduct zakat from sender
            self.accounts[sender] -= zakat_amount
            
            # Add zakat to a special zakat account (create if doesn't exist)
            if "ZAKAT_FUND" not in self.accounts:
                self.accounts["ZAKAT_FUND"] = 0
            self.accounts["ZAKAT_FUND"] += zakat_amount
            
            # Add to pending transactions
            self.pending_transactions.append({
                'main_transaction': f"{sender} -> {receiver}: {amount}",
                'zakat_transaction': f"{sender} -> ZAKAT_FUND: {zakat_amount}",
                'total_deducted': total_deduction
            })
            
            print(f"Transaction successful!")
            print(f"Amount transferred: {amount}")
            print(f"Zakat deducted: {zakat_amount}")
            print(f"Total deducted from {sender}: {total_deduction}")
            
            return True
            
        except Exception as e:
            print(f"Transaction failed: {str(e)}")
            return False
    
    def mine_block(self):
        """Mine a block with pending transactions"""
        if not self.pending_transactions:
            print("No pending transactions to mine!")
            return False
        
        # Convert transactions to string format for block
        transactions_str = json.dumps(self.pending_transactions, indent=2)
        
        # Add block to blockchain
        success = self.blockchain.add_block(transactions_str, self.roll_no)
        
        if success:
            print(f"Block mined successfully! Block #{len(self.blockchain.chain) - 1}")
            print(f"Transactions included: {len(self.pending_transactions)}")
            self.pending_transactions = []  # Clear pending transactions
            return True
        else:
            print("Failed to mine block!")
            return False
    
    def display_accounts(self):
        """Display all accounts and their balances"""
        print("\n" + "="*50)
        print("ACCOUNT BALANCES")
        print("="*50)
        if not self.accounts:
            print("No accounts found!")
        else:
            for account, balance in self.accounts.items():
                print(f"{account}: {balance}")
        print("="*50)
    
    def display_blockchain(self):
        """Display the entire blockchain"""
        print("\n" + "="*70)
        print("BLOCKCHAIN")
        print("="*70)
        
        for i, block in enumerate(self.blockchain.chain):
            print(f"\nBlock #{i}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.prev_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Roll No: {block.roll_no}")
            
            if i == 0:  # Genesis block
                print(f"Transactions: {block.transactions}")
            else:
                print("Transactions:")
                try:
                    transactions = json.loads(block.transactions)
                    for j, tx in enumerate(transactions, 1):
                        print(f"  {j}. Main: {tx['main_transaction']}")
                        print(f"     Zakat: {tx['zakat_transaction']}")
                        print(f"     Total Deducted: {tx['total_deducted']}")
                except:
                    print(f"  {block.transactions}")
            
            print("-" * 70)
    
    def validate_blockchain(self):
        """Validate the blockchain"""
        is_valid = self.blockchain.is_valid()
        print(f"\nBlockchain validation: {'VALID' if is_valid else 'INVALID'}")
        return is_valid
    
    def display_pending_transactions(self):
        """Display pending transactions"""
        print("\n" + "="*50)
        print("PENDING TRANSACTIONS")
        print("="*50)
        if not self.pending_transactions:
            print("No pending transactions!")
        else:
            for i, tx in enumerate(self.pending_transactions, 1):
                print(f"{i}. Main: {tx['main_transaction']}")
                print(f"   Zakat: {tx['zakat_transaction']}")
                print(f"   Total Deducted: {tx['total_deducted']}")
        print("="*50)


def main():
    # Initialize blockchain system
    roll_no = input("Enter your roll number (default: 0000): ").strip() or "0000"
    system = BlockchainSystem(roll_no)
    
    print("\n" + "="*60)
    print("MINI BLOCKCHAIN SYSTEM")
    print("="*60)
    print("Welcome to the Mini Blockchain System!")
    print("This system automatically applies 2.5% zakat on all transactions.")
    
    while True:
        print("\n" + "-"*40)
        print("MENU:")
        print("1. Create Account")
        print("2. View Account Balances")
        print("3. Create Transaction")
        # print("4. View Pending Transactions")
        # print("5. Mine Block")
        print("6. View Blockchain")
        print("7. Validate Blockchain")
        print("8. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            account_name = input("Enter account name: ").strip()
            try:
                balance = float(input("Enter initial balance: "))
                system.create_account(account_name, balance)
            except ValueError:
                print("Invalid balance! Please enter a numeric value.")
        
        elif choice == "2":
            system.display_accounts()
        
        elif choice == "3":
            sender = input("Enter sender account: ").strip()
            receiver = input("Enter receiver account: ").strip()
            try:
                amount = float(input("Enter transaction amount: "))
                system.create_transaction(sender, receiver, amount)
            except ValueError:
                print("Invalid amount! Please enter a numeric value.")
        
        elif choice == "4":
            system.display_pending_transactions()
        
        elif choice == "5":
            system.mine_block()
        
        elif choice == "6":
            system.display_blockchain()
        
        elif choice == "7":
            system.validate_blockchain()
        
        elif choice == "8":
            print("Thank you for using Mini Blockchain System!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-8.")


if __name__ == "__main__":
    main()
