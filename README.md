# Mini Blockchain System

A comprehensive blockchain implementation with automatic zakat calculation for educational purposes. Available in both **console** and **web interface** versions.

## 🚀 Features

### Core Blockchain Features
- **Account Management**: Create and manage accounts with balances
- **Transaction Processing**: Transfer funds between accounts with validation
- **Automatic Zakat**: 2.5% zakat automatically calculated and deducted
- **Blockchain**: Secure block creation with SHA-256 hashing
- **Mining**: Mine blocks containing pending transactions
- **Validation**: Complete blockchain integrity validation

### Interface Options
- **� Console Interface**: Traditional command-line interface (`main.py`)
- **🌐 Web Interface**: Modern Streamlit-based web application (`streamlit_app.py`)
- **🤖 Demo Mode**: Automated demonstration (`demo.py`)

## �📁 Project Structure

```
├── Core Blockchain Files
│   ├── block.py              # Block class implementation
│   ├── transaction.py        # Transaction class implementation  
│   └── miner.py             # Blockchain class implementation
├── Interface Files
│   ├── main.py              # Interactive console interface
│   ├── streamlit_app.py     # Web-based Streamlit interface
│   └── demo.py              # Automated demonstration
├── Configuration
│   ├── requirements.txt     # Python dependencies
│   ├── run_streamlit.bat    # Windows batch file to start web app
│   └── .gitignore          # Git ignore rules
└── Documentation
    ├── README.md           # This file
    ├── LICENSE             # MIT License
    └── CONTRIBUTING.md     # Contribution guidelines
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/FAIZAN-Bor/Mini-Blockchain-System.git
cd Mini-Blockchain-System
```

2. **Install dependencies:**
```bash
# For console version only (no additional dependencies required)
python main.py

# For web interface version
pip install -r requirements.txt
```

### Quick Start Options

#### Option 1: Console Interface (No Dependencies)
```bash
python main.py
```

#### Option 2: Web Interface
```bash
# Install dependencies first
pip install streamlit pandas

# Run the web application
streamlit run streamlit_app.py
```

#### Option 3: Demo Mode
```bash
python demo.py
```

## 🎮 Usage Guide

### 📺 Console Interface (`main.py`)

Interactive command-line interface with menu-driven navigation:

**Menu Options:**
1. **Create Account** - Add new accounts with initial balances
2. **View Account Balances** - Display all account balances
3. **Create Transaction** - Transfer funds between accounts (with automatic zakat)
4. **View Pending Transactions** - Show transactions waiting to be mined
5. **Mine Block** - Create a new block with pending transactions
6. **View Blockchain** - Display the complete blockchain
7. **Validate Blockchain** - Verify blockchain integrity
8. **Exit** - Close the application

**Example Usage:**
```bash
$ python main.py
Enter your roll number (default: 0000): 2024

MINI BLOCKCHAIN SYSTEM
==============================
Welcome to the Mini Blockchain System!
This system automatically applies 2.5% zakat on all transactions.

MENU:
1. Create Account
2. View Account Balances
...
```

### � Web Interface (`streamlit_app.py`)

Modern web-based interface with multiple sections:

#### **Dashboard** 📊
- Real-time metrics (accounts, transactions, blocks, total balance)
- Recent activity feed with timestamps
- Interactive balance distribution charts

#### **Account Management** 👥
- **Create Account Tab**: Easy form-based account creation
- **View Accounts Tab**: Comprehensive table view of all accounts
- Special highlighting of ZAKAT_FUND balance

#### **Transactions** 💸
- **Create Transaction Tab**: 
  - Smart dropdown selection for sender/receiver
  - Real-time balance display
  - Automatic zakat calculation preview
  - Input validation and error handling
- **Pending Transactions Tab**: Expandable transaction details

#### **Mining** ⛏️
- One-click block mining with visual feedback
- Mining statistics and blockchain validation
- Celebration animations on successful mining

#### **Blockchain Explorer** 🔍
- Complete blockchain overview table
- Detailed block inspection with transaction history
- Hash visualization and metadata display

#### **Settings** ⚙️
- System information and configuration
- Data export functionality (JSON format)
- Data reset options with confirmations

**Starting the Web Interface:**
```bash
streamlit run streamlit_app.py
# Then open: http://localhost:8501
```

### 🤖 Demo Mode (`demo.py`)

Automated demonstration showing all features:
```bash
$ python demo.py
MINI BLOCKCHAIN SYSTEM DEMO
============================================================

1. Creating accounts...
Account 'Alice' created with balance: 1000
Account 'Bob' created with balance: 500
Account 'Charlie' created with balance: 750
...
```

## � Zakat System

### Automatic Zakat Integration
The system seamlessly integrates Islamic financial principles:

- **Rate**: 2.5% zakat automatically calculated on all transactions
- **Deduction**: Zakat deducted from sender's account along with transaction amount
- **Fund Management**: Automatic creation and management of `ZAKAT_FUND` account
- **Transparency**: Clear feedback on zakat amounts in all interfaces
- **Validation**: Ensures sufficient balance including zakat before processing

### Example Zakat Calculation
```
Transaction: Alice sends 100 to Bob
├── Main Amount: 100.00
├── Zakat (2.5%): 2.50
├── Total Deducted: 102.50
└── Result:
    ├── Alice: -102.50
    ├── Bob: +100.00
    └── ZAKAT_FUND: +2.50
```

## 🔗 Blockchain Architecture

### Block Structure
```json
{
  "transactions": "JSON string of transaction data",
  "timestamp": "Unix timestamp",
  "prev_hash": "SHA-256 hash of previous block",
  "hash": "SHA-256 hash of current block",
  "roll_no": "Student/system identifier"
}
```

### Key Features
- **Genesis Block**: Automatically created on initialization
- **Hash Linking**: Each block cryptographically linked to previous
- **Validation**: Complete chain integrity verification
- **Transaction Storage**: Detailed JSON-formatted transaction records
- **Mining Process**: Proof-of-work simulation with hash verification

### Validation Rules
- ✅ Account existence verification
- ✅ Sufficient balance checking (including zakat)
- ✅ Hash consistency verification
- ✅ Block sequence validation
- ✅ Transaction integrity checks

## 🧪 Testing & Examples

### Quick Test - Demo Mode
```bash
python demo.py
```
**Output:**
```
MINI BLOCKCHAIN SYSTEM DEMO
============================================================

1. Creating accounts...
Account 'Alice' created with balance: 1000
Account 'Bob' created with balance: 500
Account 'Charlie' created with balance: 750

2. Creating transactions...
Transaction successful! Amount: 100, Zakat: 2.5, Total deducted: 102.5
Transaction successful! Amount: 50, Zakat: 1.25, Total deducted: 51.25

3. Mining block...
Block #1 mined successfully with 2 transactions!

4. Validating blockchain...
Blockchain validation: VALID
```

### Manual Testing Steps

#### Console Interface Testing
1. **Account Creation**:
   ```
   Menu Choice: 1
   Account Name: Alice
   Initial Balance: 1000
   ```

2. **Transaction Testing**:
   ```
   Menu Choice: 3
   Sender: Alice
   Receiver: Bob
   Amount: 100
   Result: Alice loses 102.5 (100 + 2.5 zakat), Bob gains 100
   ```

3. **Mining & Validation**:
   ```
   Menu Choice: 5 (Mine Block)
   Menu Choice: 7 (Validate Blockchain)
   ```

#### Web Interface Testing
1. Start: `streamlit run streamlit_app.py`
2. Navigate to `http://localhost:8501`
3. Test all sections: Dashboard → Accounts → Transactions → Mining → Explorer

### Expected Results
✅ **Successful Transaction Flow**:
```
Initial: Alice: 1000, Bob: 500
Transaction: Alice → Bob (100)
Final: Alice: 897.5, Bob: 600, ZAKAT_FUND: 2.5
```

✅ **Blockchain Validation**: All blocks properly linked with valid hashes
✅ **Zakat Calculation**: Always 2.5% of transaction amount
✅ **Balance Validation**: Prevents transactions exceeding available balance

## 🔧 Technical Specifications

### Dependencies

#### Console Version
- **Python**: 3.7+
- **Standard Library Only**: hashlib, time, json

#### Web Version  
- **Python**: 3.7+
- **Streamlit**: >=1.28.0
- **Pandas**: >=1.3.0

### Performance
- **Block Creation**: Instant (no proof-of-work complexity)
- **Transaction Processing**: O(1) time complexity
- **Blockchain Validation**: O(n) where n = number of blocks
- **Memory Usage**: Minimal (in-memory storage only)

### File Descriptions

| File | Purpose | Dependencies |
|------|---------|--------------|
| `block.py` | Core block implementation | hashlib, time |
| `transaction.py` | Transaction logic | None |
| `miner.py` | Blockchain management | block.py |
| `main.py` | Console interface | All core files, json |
| `streamlit_app.py` | Web interface | All files, streamlit, pandas |
| `demo.py` | Automated testing | All core files, json |

### Data Flow
```
User Input → Validation → Transaction Creation → Pending Pool → Mining → Blockchain → Validation
```

## 🎯 Educational Objectives

### Learning Outcomes
This project demonstrates key concepts in:

#### **Blockchain Technology**
- Block creation and linking mechanisms
- Hash-based security and integrity
- Consensus and validation processes
- Transaction processing and state management

#### **Islamic Finance Integration**
- Zakat calculation and automatic deduction
- Transparent fund management
- Ethical financial transaction processing

#### **Software Engineering**
- Object-oriented programming principles
- Modular code architecture
- User interface design (console and web)
- Data persistence and state management

#### **Web Development** (Streamlit Version)
- Modern web application development
- Real-time data visualization
- Interactive user interfaces
- Session state management

### Practical Applications
- Understanding cryptocurrency mechanics
- Learning blockchain validation processes
- Exploring Islamic fintech solutions
- Practicing full-stack development skills

## 🚀 Advanced Features & Extensions

### Current Implementation
✅ **Basic Blockchain**: Block creation, linking, validation  
✅ **Account System**: Multi-account management  
✅ **Zakat Integration**: Automatic 2.5% calculation  
✅ **Dual Interface**: Console and web versions  
✅ **Data Export**: JSON format blockchain export  
✅ **Real-time Validation**: Instant blockchain integrity checks  

### Potential Enhancements

#### **Backend Improvements**
- 🔄 **Persistent Storage**: SQLite/PostgreSQL database integration
- 🔐 **Enhanced Security**: Digital signatures and encryption
- ⚡ **Performance Optimization**: Merkle trees for efficient validation
- 🌐 **Network Simulation**: Multi-node consensus mechanisms

#### **Frontend Enhancements** 
- 👤 **User Authentication**: Multi-user support with login system
- 📊 **Advanced Analytics**: Transaction trends and zakat analytics
- 📱 **Mobile Responsive**: Mobile-optimized interface
- 🎨 **Custom Themes**: Multiple UI themes and customization

#### **Feature Extensions**
- 📋 **Smart Contracts**: Basic contract execution engine
- 💱 **Multi-Currency**: Support for different currency types
- 📈 **Transaction Fees**: Dynamic fee calculation beyond zakat
- 🔄 **Transaction Reversal**: Dispute resolution mechanisms
- 📤 **API Development**: RESTful API for external integrations

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Ways to Contribute
- 🐛 **Bug Reports**: Report issues and bugs
- ✨ **Feature Requests**: Suggest new functionality
- 📝 **Documentation**: Improve documentation and examples
- 🔧 **Code Contributions**: Submit pull requests with improvements

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with clear description

### Coding Standards
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include unit tests for new features
- Maintain backward compatibility

## 📝 License & Usage

### License
This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

### Educational Use
- ✅ **Freely usable** for educational and learning purposes
- ✅ **Modification allowed** for academic projects
- ✅ **Distribution permitted** with proper attribution

### Important Disclaimers
⚠️ **This is an educational implementation only**
- Not suitable for production financial systems
- Simplified security model
- No real-world transaction processing
- Lacks enterprise-grade features

## 🌟 Acknowledgments

### Technologies Used
- **Python**: Core programming language
- **Streamlit**: Web interface framework
- **Pandas**: Data manipulation and analysis
- **Hashlib**: Cryptographic hashing

### Educational Context
- Developed for blockchain education
- Demonstrates Islamic finance principles
- Suitable for computer science coursework
- Ideal for fintech learning projects

## 📞 Support & Community

### Getting Help
- 📧 **Issues**: Open GitHub issues for bugs and questions
- 💬 **Discussions**: Use GitHub discussions for general questions
- 📖 **Documentation**: Refer to this README and inline comments

### Contact Information
- **Repository**: [Mini-Blockchain-System](https://github.com/FAIZAN-Bor/Mini-Blockchain-System)
- **Maintainer**: FAIZAN-Bor
- **Purpose**: Educational blockchain demonstration

---

## 🎉 Quick Start Summary

### For Beginners (Console Only)
```bash
git clone https://github.com/FAIZAN-Bor/Mini-Blockchain-System.git
cd Mini-Blockchain-System
python main.py
```

### For Web Interface
```bash
git clone https://github.com/FAIZAN-Bor/Mini-Blockchain-System.git
cd Mini-Blockchain-System
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### For Quick Demo
```bash
python demo.py
```

**🚀 Start exploring blockchain technology with automatic zakat integration today!**

---

*"This project bridges traditional Islamic finance principles with modern blockchain technology for educational excellence."*
