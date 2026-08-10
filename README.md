# 🏦 Bukhari Bank Management System

**Version:** v1.0.0

A professional command-line Bank Management System built with Python using Object-Oriented Programming (OOP), JSON data persistence, custom exception handling, and automated testing with pytest.

This project simulates a real-world banking system where users can create accounts, manage customers, perform banking transactions, and permanently store data using JSON file handling.

---

# 📌 Project Description

The **Bukhari Bank Management System** is a console-based banking application developed in Python as a professional software engineering project.

The main objective of this project is to practice clean code, object-oriented programming, modular software architecture, testing, and professional Python development practices.

This project demonstrates:

- Object-Oriented Programming (OOP)
- Clean Code Organization
- Professional Multi-file Architecture
- Exception Handling
- JSON File Handling
- Data Persistence
- Unit Testing with pytest
- Code Refactoring
- DRY (Don't Repeat Yourself) Principle

---

# 🚀 Features

- Create customer accounts
- Create bank accounts
- Deposit money
- Withdraw money
- Transfer money between accounts
- Display account details
- View transaction history
- Record every transaction automatically
- Save account data permanently
- Automatically load saved accounts
- Duplicate account prevention
- Custom exception handling
- Account data validation
- Professional project structure
- Automated unit testing

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Encapsulation
- Composition
- Exception Handling
- JSON File Handling
- pathlib
- pytest
- Multi-file Project Architecture

---

# 📦 Requirements

- Python 3.11 or later
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📂 Project Structure

```text
Bank Management/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── bank.py
│   ├── bank_account.py
│   ├── customer.py
│   ├── transaction.py
│   ├── file_manager.py
│   └── exceptions.py
│
├── tests/
│   ├── __init__.py
│   ├── test_bank_account.py
│   └── test_file_manager.py
│
├── data/
│   └── accounts.json
│
├── .gitignore
├── requirements.txt
├── LICENSE
├── pytest.ini
└── README.md
```

---

# 🏗 Project Architecture

```text
                Customer
                    │
                    │
            BankAccount
                    │
        ┌───────────┴───────────┐
        │                       │
 Transaction History        Account Balance
        │
        │
   Transaction


                 Bank
                   │
        ┌──────────┴──────────┐
        │                     │
 Create Account       Manage Accounts


            FileManager
                  │
                  │
          data/accounts.json
```

---

# ⚙️ How the System Works

## 👤 Customer

Stores customer information:

- Customer Name
- Phone Number

---

## 🏦 Bank Account

Manages:

- Account Number
- Balance
- Deposits
- Withdrawals
- Transfers
- Transaction History

---

## 💳 Transaction

Records:

- Transaction Type
- Amount
- Date and Time

Examples:

- Deposit
- Withdraw
- Transfer In
- Transfer Out

---

## 💾 File Manager

Responsible for:

- Saving accounts into JSON
- Loading saved accounts
- Restoring transaction history
- Permanent data storage

---

# ▶️ How to Run

### Step 1

Clone or download the project.

### Step 2

Open the project folder.

### Step 3

Open a terminal.

### Step 4

Run:

```bash
python src/main.py
```

---

# 💾 Data Storage

The project uses JSON for permanent data storage.

Data is stored in:

```text
data/accounts.json
```

Stored information includes:

- Customer Information
- Account Number
- Current Balance
- Transaction History

---

# ✅ Running Tests

Run all automated tests:

```bash
pytest
```

Current Status:

- ✅ 7/7 Tests Passing

---

# 🧠 Concepts Practiced

- Python Programming
- Object-Oriented Programming
- Classes and Objects
- Constructors
- Encapsulation
- Composition
- Exception Handling
- Custom Exceptions
- File Handling
- JSON Serialization
- Multi-file Python Projects
- Project Packaging
- Unit Testing
- Code Refactoring
- DRY Principle
- Clean Code
- Professional Documentation

---

# 🔮 Future Improvements

Possible future upgrades include:

- Graphical User Interface (GUI)
- Database Integration (SQLite/PostgreSQL/MySQL)
- User Authentication
- Password Encryption
- Admin Dashboard
- ATM Simulation
- Online Banking
- Interest Calculation
- Loan Management
- REST API
- Web Version (Flask/Django)
- Email Notifications

---

# 👨‍💻 Author

**Syed Ashar Raza**

Bachelor of Science in Artificial Intelligence (BSAI)

Python & AI Developer

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for details.

## Development Status

Version 1.0.0 released.

Branch Practice — Feature branch created successfully.