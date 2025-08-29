# Mini Blockchain System

A console-based mini blockchain implementation with automatic zakat calculation for educational purposes.

## 🚀 Features

- **Account Management**: Create and manage accounts with balances
- **Transaction Processing**: Transfer funds between accounts
- **Automatic Zakat**: 2.5% zakat automatically calculated and deducted
- **Blockchain**: Secure block creation and validation
- **Mining**: Mine blocks containing pending transactions
- **Validation**: Complete blockchain integrity validation

## 📁 Project Structure

```
├── block.py           # Block class implementation
├── transaction.py     # Transaction class implementation  
├── miner.py          # Blockchain class implementation
├── main.py           # Interactive console interface
├── demo.py           # Automated demonstration
└── README.md         # This file
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mini-blockchain-system
```

2. Ensure Python 3.x is installed on your system

3. No additional dependencies required (uses only standard library)

## 🎮 Usage

### Interactive Mode
Run the main console interface:
```bash
python main.py
```

### Demo Mode
Run the automated demonstration:
```bash
python demo.py
```

## 📋 Menu Options

1. **Create Account** - Add new accounts with initial balances
2. **View Account Balances** - Display all account balances
3. **Create Transaction** - Transfer funds between accounts (with automatic zakat)
4. **View Pending Transactions** - Show transactions waiting to be mined
5. **Mine Block** - Create a new block with pending transactions
6. **View Blockchain** - Display the complete blockchain
7. **Validate Blockchain** - Verify blockchain integrity
8. **Exit** - Close the application

## 💰 Zakat System

The system automatically:
- Calculates 2.5% zakat on all transactions
- Deducts zakat from the sender's account
- Transfers zakat to a special `ZAKAT_FUND` account
- Provides clear feedback on zakat amounts

## 🔗 Blockchain Features

- **Genesis Block**: Automatically created on initialization
- **Hash Linking**: Each block references the previous block's hash
- **Validation**: Ensures hash integrity across the entire chain
- **Transaction Storage**: Stores detailed transaction records in blocks

## 📊 Example Transaction Flow

```
Initial State:
- Alice: 1000
- Bob: 500

Transaction: Alice sends 100 to Bob
- Amount transferred: 100
- Zakat deducted: 2.5 (2.5% of 100)
- Total deducted from Alice: 102.5

Final State:
- Alice: 897.5 (1000 - 102.5)
- Bob: 600 (500 + 100)
- ZAKAT_FUND: 2.5
```

## 🧪 Testing

Run the demo to see the system in action:
```bash
python demo.py
```

This will demonstrate:
- Account creation
- Multiple transactions with zakat
- Block mining
- Blockchain validation

## 🔧 Technical Details

### Block Structure
- Transactions (JSON format)
- Timestamp
- Previous block hash
- Current block hash
- Roll number

### Transaction Structure
- Main transaction details
- Zakat transaction details
- Total amount deducted

### Validation Rules
- Account existence validation
- Sufficient balance checking (including zakat)
- Hash consistency verification
- Block linking validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🎯 Future Enhancements

- Web interface using Streamlit
- Persistent data storage
- Advanced mining algorithms
- Network consensus mechanisms
- Smart contracts integration

## 📞 Support

For questions or issues, please open an issue in the repository.

---

**Note**: This is an educational implementation of blockchain concepts and should not be used for production financial systems.
