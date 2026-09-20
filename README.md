# Bukhari Bank Management System

A Python-based command-line banking application demonstrating object-oriented design, modular architecture, JSON persistence, custom exception handling, and automated testing with pytest.

The project simulates core banking operations while emphasizing maintainable code organization, separation of responsibilities, data persistence, validation, and testable business logic.

## Features

- Create and manage customer accounts
- Create bank accounts
- Deposit funds
- Withdraw funds
- Transfer funds between accounts
- Search for accounts
- Display account information
- View transaction history
- Record transactions automatically
- Persist account data using JSON
- Restore saved accounts and transaction history
- Prevent duplicate account numbers
- Validate account and customer data
- Handle domain-specific errors with custom exceptions
- Automated testing with pytest

## Technical Stack

- Python 3
- Object-Oriented Programming
- JSON serialization and persistence
- pathlib
- Custom exception hierarchy
- pytest
- Modular multi-file architecture

## Architecture

The application separates responsibilities across focused modules.

### Core Components

- **Bank** — Coordinates bank-level account management and operations.
- **BankAccount** — Encapsulates account state and banking operations.
- **Customer** — Stores customer information associated with an account.
- **Transaction** — Represents individual account transactions.
- **FileManager** — Handles JSON serialization and persistence.
- **Exceptions** — Provides domain-specific application exceptions.

## Project Structure

```text
bank-management-system/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── bank.py
│   ├── bank_account.py
│   ├── customer.py
│   ├── transaction.py
│   ├── file_manager.py
│   └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_bank.py
│   ├── test_bank_account.py
│   └── test_file_manager.py
├── data/
│   └── accounts.json
├── .gitignore
├── LICENSE
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/syed-ashar-raza/bank-management-system.git
cd bank-management-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application from the project root:

```powershell
python -m src.main
```

The application provides menu-driven access to account creation, deposits, withdrawals, transfers, account searches, transaction history, and data persistence.

## Data Persistence

Account data and transaction history are stored in:

```text
data/accounts.json
```

The application loads existing account data when started and saves updated account information to JSON.

## Testing

Run the complete automated test suite:

```powershell
pytest -q
```

Current verification:

```text
12 passed
```

## Engineering Practices

- Object-oriented design
- Encapsulation
- Composition
- Separation of responsibilities
- Modular architecture
- Domain-specific exception handling
- JSON serialization and deserialization
- File-system handling with pathlib
- Input validation
- Automated testing
- Refactoring
- DRY principles
- Maintainable code organization
- Git-ready project structure

## Design Notes

The project uses JSON persistence to demonstrate application architecture and Python software engineering without unnecessary infrastructure.

Banking logic, persistence, and command-line interaction are separated into dedicated modules, making the application easier to test, maintain, and extend.

## Project Status

The current implementation is functional and verified with an automated test suite.

This project is maintained as part of a professional AI Developer portfolio to demonstrate foundational software engineering capability supporting larger Python, data, machine learning, and AI systems.

## Author

**Syed Ashar Raza**

Bachelor of Science in Artificial Intelligence (BSAI)

AI & Python Developer

## License

MIT License

See the `LICENSE` file for details.