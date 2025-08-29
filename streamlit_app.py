import streamlit as st
import json
import pandas as pd
from datetime import datetime
from transaction import Transaction
from miner import Blockchain

class BlockchainSystemStreamlit:
    def __init__(self, roll_no="0000"):
        if 'blockchain' not in st.session_state:
            st.session_state.blockchain = Blockchain(roll_no)
        if 'accounts' not in st.session_state:
            st.session_state.accounts = {}
        if 'pending_transactions' not in st.session_state:
            st.session_state.pending_transactions = []
        if 'roll_no' not in st.session_state:
            st.session_state.roll_no = roll_no
        
        self.blockchain = st.session_state.blockchain
        self.accounts = st.session_state.accounts
        self.pending_transactions = st.session_state.pending_transactions
        self.roll_no = st.session_state.roll_no
    
    def create_account(self, account_name, initial_balance):
        """Create a new account with initial balance"""
        if account_name in self.accounts:
            return False, f"Account '{account_name}' already exists!"
        
        self.accounts[account_name] = initial_balance
        st.session_state.accounts = self.accounts
        return True, f"Account '{account_name}' created with balance: {initial_balance}"
    
    def get_balance(self, account_name):
        """Get account balance"""
        return self.accounts.get(account_name, 0)
    
    def calculate_zakat(self, amount):
        """Calculate zakat (2.5% of transaction amount)"""
        return round(amount * 0.025, 2)
    
    def create_transaction(self, sender, receiver, amount):
        """Create and add a transaction with automatic zakat deduction"""
        try:
            # Check if accounts exist
            if sender not in self.accounts:
                return False, f"Sender account '{sender}' does not exist!"
            if receiver not in self.accounts:
                return False, f"Receiver account '{receiver}' does not exist!"
            
            # Calculate zakat
            zakat_amount = self.calculate_zakat(amount)
            total_deduction = amount + zakat_amount
            
            # Check if sender has sufficient balance
            if self.accounts[sender] < total_deduction:
                return False, f"Insufficient balance! Required: {total_deduction} (Amount: {amount} + Zakat: {zakat_amount})"
            
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
                'total_deducted': total_deduction,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Update session state
            st.session_state.accounts = self.accounts
            st.session_state.pending_transactions = self.pending_transactions
            
            return True, f"Transaction successful! Amount: {amount}, Zakat: {zakat_amount}, Total deducted: {total_deduction}"
            
        except Exception as e:
            return False, f"Transaction failed: {str(e)}"
    
    def mine_block(self):
        """Mine a block with pending transactions"""
        if not self.pending_transactions:
            return False, "No pending transactions to mine!"
        
        # Convert transactions to string format for block
        transactions_str = json.dumps(self.pending_transactions, indent=2)
        
        # Add block to blockchain
        success = self.blockchain.add_block(transactions_str, self.roll_no)
        
        if success:
            block_num = len(self.blockchain.chain) - 1
            tx_count = len(self.pending_transactions)
            self.pending_transactions = []  # Clear pending transactions
            
            # Update session state
            st.session_state.blockchain = self.blockchain
            st.session_state.pending_transactions = self.pending_transactions
            
            return True, f"Block #{block_num} mined successfully with {tx_count} transactions!"
        else:
            return False, "Failed to mine block!"
    
    def validate_blockchain(self):
        """Validate the blockchain"""
        is_valid = self.blockchain.is_valid()
        return is_valid
    
    def get_blockchain_data(self):
        """Get blockchain data for display"""
        blocks_data = []
        for i, block in enumerate(self.blockchain.chain):
            block_info = {
                'Block #': i,
                'Timestamp': datetime.fromtimestamp(block.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                'Previous Hash': block.prev_hash[:16] + "..." if len(block.prev_hash) > 16 else block.prev_hash,
                'Current Hash': block.hash[:16] + "..." if len(block.hash) > 16 else block.hash,
                'Roll No': block.roll_no,
                'Transactions': "Genesis Block" if i == 0 else f"{len(json.loads(block.transactions))} transactions"
            }
            blocks_data.append(block_info)
        return blocks_data
    
    def get_transaction_details(self, block_index):
        """Get detailed transaction information for a specific block"""
        if block_index == 0:
            return []
        
        block = self.blockchain.chain[block_index]
        try:
            transactions = json.loads(block.transactions)
            return transactions
        except:
            return []


def main():
    # Page configuration
    st.set_page_config(
        page_title="Mini Blockchain System",
        page_icon="🔗",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        text-align: center;
        margin: 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .success-msg {
        padding: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        color: #155724;
    }
    .error-msg {
        padding: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 5px;
        color: #721c24;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔗 Mini Blockchain System</h1>
        <p style="text-align: center; color: white; margin: 0;">
            Complete Blockchain with Automatic Zakat Calculation
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize system
    if 'system' not in st.session_state:
        roll_no = st.sidebar.text_input("Enter Roll Number", value="3669", key="roll_input")
        st.session_state.system = BlockchainSystemStreamlit(roll_no)
    
    system = st.session_state.system
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Dashboard", "Account Management", "Transactions", "Mining", "Blockchain Explorer", "Settings"]
    )
    
    # Dashboard
    if page == "Dashboard":
        st.header("📊 Dashboard")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Accounts", len(system.accounts))
        
        with col2:
            st.metric("Pending Transactions", len(system.pending_transactions))
        
        with col3:
            st.metric("Blocks Mined", len(system.blockchain.chain) - 1)
        
        with col4:
            total_balance = sum(system.accounts.values()) if system.accounts else 0
            st.metric("Total Balance", f"{total_balance:.2f}")
        
        # Recent activity
        st.subheader("Recent Activity")
        if system.pending_transactions:
            for i, tx in enumerate(system.pending_transactions[-5:], 1):
                st.info(f"🔄 {tx['main_transaction']} | Zakat: {tx['zakat_transaction'].split(': ')[1]} | {tx['timestamp']}")
        else:
            st.info("No recent transactions")
        
        # Account balances chart
        if system.accounts:
            st.subheader("Account Balances")
            df = pd.DataFrame(list(system.accounts.items()), columns=['Account', 'Balance'])
            st.bar_chart(df.set_index('Account'))
    
    # Account Management
    elif page == "Account Management":
        st.header("👥 Account Management")
        
        tab1, tab2 = st.tabs(["Create Account", "View Accounts"])
        
        with tab1:
            st.subheader("Create New Account")
            with st.form("create_account_form"):
                account_name = st.text_input("Account Name")
                initial_balance = st.number_input("Initial Balance", min_value=0.0, step=0.01)
                submitted = st.form_submit_button("Create Account")
                
                if submitted:
                    if account_name:
                        success, message = system.create_account(account_name, initial_balance)
                        if success:
                            st.success(message)
                        else:
                            st.error(message)
                        st.rerun()
                    else:
                        st.error("Please enter an account name")
        
        with tab2:
            st.subheader("All Accounts")
            if system.accounts:
                df = pd.DataFrame(list(system.accounts.items()), columns=['Account', 'Balance'])
                st.dataframe(df, use_container_width=True)
                
                # Zakat fund highlight
                if "ZAKAT_FUND" in system.accounts:
                    st.info(f"💰 Zakat Fund Balance: {system.accounts['ZAKAT_FUND']:.2f}")
            else:
                st.info("No accounts created yet")
    
    # Transactions
    elif page == "Transactions":
        st.header("💸 Transactions")
        
        tab1, tab2 = st.tabs(["Create Transaction", "Pending Transactions"])
        
        with tab1:
            st.subheader("Create New Transaction")
            
            if len(system.accounts) < 2:
                st.warning("You need at least 2 accounts to create a transaction")
            else:
                with st.form("transaction_form"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        sender = st.selectbox("Sender", options=list(system.accounts.keys()))
                        if sender:
                            st.info(f"Current Balance: {system.accounts[sender]:.2f}")
                    
                    with col2:
                        receiver_options = [acc for acc in system.accounts.keys() if acc != sender]
                        receiver = st.selectbox("Receiver", options=receiver_options)
                    
                    amount = st.number_input("Amount", min_value=0.01, step=0.01)
                    
                    if amount > 0:
                        zakat = system.calculate_zakat(amount)
                        total_deduction = amount + zakat
                        st.info(f"Zakat (2.5%): {zakat:.2f} | Total Deduction: {total_deduction:.2f}")
                    
                    submitted = st.form_submit_button("Create Transaction")
                    
                    if submitted:
                        if sender and receiver and amount > 0:
                            success, message = system.create_transaction(sender, receiver, amount)
                            if success:
                                st.success(message)
                            else:
                                st.error(message)
                            st.rerun()
                        else:
                            st.error("Please fill all fields with valid values")
        
        with tab2:
            st.subheader("Pending Transactions")
            if system.pending_transactions:
                for i, tx in enumerate(system.pending_transactions, 1):
                    with st.expander(f"Transaction #{i} - {tx['timestamp']}"):
                        st.write(f"**Main Transaction:** {tx['main_transaction']}")
                        st.write(f"**Zakat Transaction:** {tx['zakat_transaction']}")
                        st.write(f"**Total Deducted:** {tx['total_deducted']}")
                
                st.success(f"Total pending transactions: {len(system.pending_transactions)}")
            else:
                st.info("No pending transactions")
    
    # Mining
    elif page == "Mining":
        st.header("⛏️ Mining")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Mine New Block")
            if system.pending_transactions:
                st.info(f"Ready to mine {len(system.pending_transactions)} pending transactions")
                
                if st.button("🔨 Mine Block", type="primary"):
                    with st.spinner("Mining block..."):
                        success, message = system.mine_block()
                        if success:
                            st.success(message)
                            st.balloons()
                        else:
                            st.error(message)
                        st.rerun()
            else:
                st.warning("No pending transactions to mine")
        
        with col2:
            st.subheader("Mining Stats")
            st.metric("Blocks Mined", len(system.blockchain.chain) - 1)
            st.metric("Genesis Block", "✅")
            
            # Blockchain validation
            if st.button("🔍 Validate Blockchain"):
                with st.spinner("Validating blockchain..."):
                    is_valid = system.validate_blockchain()
                    if is_valid:
                        st.success("✅ Blockchain is VALID")
                    else:
                        st.error("❌ Blockchain is INVALID")
    
    # Blockchain Explorer
    elif page == "Blockchain Explorer":
        st.header("🔍 Blockchain Explorer")
        
        # Blockchain overview
        blocks_data = system.get_blockchain_data()
        if blocks_data:
            st.subheader("Blockchain Overview")
            df = pd.DataFrame(blocks_data)
            st.dataframe(df, use_container_width=True)
            
            # Block details
            st.subheader("Block Details")
            selected_block = st.selectbox("Select Block", range(len(system.blockchain.chain)))
            
            if selected_block is not None:
                block = system.blockchain.chain[selected_block]
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Block Number:** {selected_block}")
                    st.write(f"**Timestamp:** {datetime.fromtimestamp(block.timestamp)}")
                    st.write(f"**Roll Number:** {block.roll_no}")
                
                with col2:
                    st.write(f"**Previous Hash:** `{block.prev_hash}`")
                    st.write(f"**Current Hash:** `{block.hash}`")
                
                # Transaction details
                if selected_block == 0:
                    st.info("Genesis Block - No transactions")
                else:
                    st.subheader("Transactions in this Block")
                    transactions = system.get_transaction_details(selected_block)
                    if transactions:
                        for i, tx in enumerate(transactions, 1):
                            with st.expander(f"Transaction #{i}"):
                                st.write(f"**Main:** {tx['main_transaction']}")
                                st.write(f"**Zakat:** {tx['zakat_transaction']}")
                                st.write(f"**Total Deducted:** {tx['total_deducted']}")
                                st.write(f"**Timestamp:** {tx.get('timestamp', 'N/A')}")
        else:
            st.info("No blocks in blockchain")
    
    # Settings
    elif page == "Settings":
        st.header("⚙️ Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("System Information")
            st.info(f"**Roll Number:** {system.roll_no}")
            st.info(f"**Zakat Rate:** 2.5%")
            st.info(f"**Total Accounts:** {len(system.accounts)}")
            st.info(f"**Blockchain Length:** {len(system.blockchain.chain)}")
        
        with col2:
            st.subheader("Actions")
            
            if st.button("🧹 Clear All Data", type="secondary"):
                if st.checkbox("I understand this will delete all data"):
                    st.session_state.clear()
                    st.success("All data cleared! Please refresh the page.")
            
            st.subheader("Export Data")
            if system.accounts:
                # Export accounts
                accounts_json = json.dumps(system.accounts, indent=2)
                st.download_button(
                    label="📄 Download Accounts (JSON)",
                    data=accounts_json,
                    file_name="accounts.json",
                    mime="application/json"
                )
            
            if len(system.blockchain.chain) > 1:
                # Export blockchain
                blockchain_data = []
                for i, block in enumerate(system.blockchain.chain):
                    blockchain_data.append({
                        'block_number': i,
                        'timestamp': block.timestamp,
                        'prev_hash': block.prev_hash,
                        'current_hash': block.hash,
                        'roll_no': block.roll_no,
                        'transactions': block.transactions
                    })
                
                blockchain_json = json.dumps(blockchain_data, indent=2)
                st.download_button(
                    label="🔗 Download Blockchain (JSON)",
                    data=blockchain_json,
                    file_name="blockchain.json",
                    mime="application/json"
                )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🔗 Mini Blockchain System | Built with Streamlit | Educational Purpose Only</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
