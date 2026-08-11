"""
Main entry point for the Bank Management System.

This module provides the command-line interface (CLI) that allows users
to interact with the Bank Management System. It handles user input,
menu navigation, account operations, and data persistence.
"""


from src.exceptions import (
    DuplicateAccountError,
    InvalidAccountDataError,
    InvalidAmountError,
    AccountNotFoundError,
    InvalidCustomerDataError,
)

from src.file_manager import FileManager
from src.customer import Customer
from src.bank_account import BankAccount
from src.bank import Bank


def get_amount(message: str) -> float:
    """
    Get a valid positive monetary amount from user.

    Parameters:
        message (str):
            Message displayed to user.

    Returns:
        float:
            Valid positive amount.
    """

    while True:

        try:

            amount = float(
                input(message)
            )

            if amount <= 0:

                raise InvalidAmountError(
                    "Amount must be greater than zero."
                )

            return amount

        except ValueError:

            print(
                "❌ Please enter a valid number!"
            )

        except InvalidAmountError as error:

            print(
                f"❌ Error: {error}"
            )


def handle_error(
    error: Exception
) -> None:
    """
    Display formatted error message.

    Parameters:
        error (Exception):
            Error to display.

    Returns:
        None
    """

    print(
        f"❌ Error: {error}"
    )


def display_menu() -> None:
    """
    Display the main application menu.

    Returns:
        None
    """

    print(
        "\n========== BUKHARI BANK =========="
    )
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Display Accounts")
    print("6. Search Account")
    print("7. Save Data")
    print("8. Display Transactions")
    print("9. Search Transactions")
    print("10. Exit")


def create_account(
    bank: Bank
) -> None:
    """
    Create a new bank account.

    Parameters:
        bank (Bank):
            Bank instance managing accounts.

    Returns:
        None
    """

    name = input(
        "Enter Customer Name: "
    )

    phone = input(
        "Enter Phone Number: "
    )

    account_number = input(
        "Enter Account Number: "
    )

    balance = get_amount(
        "Enter Initial Balance: "
    )

    try:

        customer = Customer(
            name,
            phone
        )

        account = BankAccount(
            customer,
            account_number,
            balance
        )

        bank.add_account(
            account
        )

        print(
            "✅ Account Created Successfully!"
        )

    except (
        DuplicateAccountError,
        InvalidCustomerDataError,
        InvalidAccountDataError,
    ) as error:

        handle_error(error)


def deposit_money(
    bank: Bank
) -> None:
    """
    Deposit money into an account.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    account_number = input(
        "Enter Account Number: "
    )

    amount = get_amount(
        "Enter Deposit Amount: "
    )

    try:

        account = bank.find_account(
            account_number
        )

        account.deposit(
            amount
        )

        print(
            "✅ Deposit Successful!"
        )

        account.display_balance()

    except (
        InvalidAmountError,
        AccountNotFoundError,
    ) as error:

        handle_error(error)


def withdraw_money(
    bank: Bank
) -> None:
    """
    Withdraw money from an account.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    account_number = input(
        "Enter Account Number: "
    )

    amount = get_amount(
        "Enter Withdrawal Amount: "
    )

    try:

        account = bank.find_account(
            account_number
        )

        account.withdraw(
            amount
        )

    except (
        InvalidAmountError,
        AccountNotFoundError,
    ) as error:

        handle_error(error)


def transfer_money(
    bank: Bank
) -> None:
    """
    Transfer money between accounts.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    sender_account = input(
        "Enter Sender Account Number: "
    )

    receiver_account = input(
        "Enter Receiver Account Number: "
    )

    amount = get_amount(
        "Enter Transfer Amount: "
    )

    try:

        bank.transfer(
            sender_account,
            receiver_account,
            amount
        )

    except (
        InvalidAmountError,
        AccountNotFoundError,
    ) as error:

        handle_error(error)


def display_accounts(
    bank: Bank
) -> None:
    """
    Display all accounts.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    bank.display_accounts()

def search_account(
    bank: Bank
) -> None:
    """
    Search for an account by account number.

    Parameters:
        bank (Bank):
            Bank instance managing accounts.

    Returns:
        None
    """

    account_number = input(
        "Enter Account Number: "
    )

    try:

        account = bank.find_account(
            account_number
        )

        print("\n✅ Account Found!")
        print("-" * 28)

        account.display_balance()

        print("-" * 28)

    except AccountNotFoundError as error:

        handle_error(error)


def save_accounts(
    bank: Bank
) -> None:
    """
    Save account data permanently.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    FileManager.save_accounts(
        bank.accounts
    )

    print(
        "✅ Data saved successfully!"
    )


def display_transactions(
    bank: Bank
) -> None:
    """
    Display transaction history.

    Parameters:
        bank (Bank):
            Bank instance.

    Returns:
        None
    """

    try:

        account_number = input(
            "Enter Account Number: "
        )

        account = bank.find_account(
            account_number
        )

        account.display_transactions()

    except AccountNotFoundError as error:

        handle_error(error)

def search_transactions(bank: Bank) -> None:
    """
    Search transactions by transaction type.

    Parameters:
        bank (Bank):
            Bank instance managing accounts.

    Returns:
        None
    """

    try:

        account_number = input(
            "Enter Account Number: "
        )

        account = bank.find_account(
            account_number
        )

        transaction_type = input(
            "Enter Transaction Type: "
        )

        results = account.search_transactions(
            transaction_type
        )

        if not results:

            print(
                "No matching transactions found."
            )

            return

        print(
            f"\nTransactions matching "
            f"'{transaction_type}':\n"
        )

        for transaction in results:

            transaction.display_transaction()

    except AccountNotFoundError as error:

        handle_error(error)


def main() -> None:
    """
    Run the Bank Management System application.

    Loads saved accounts, displays menu,
    and processes user operations.

    Returns:
        None
    """

    bank = Bank(
        "Bukhari Bank"
    )

    loaded_accounts = FileManager.load_accounts()

    for account in loaded_accounts:

        bank.add_account(
            account,
            False
        )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            create_account(bank)

        elif choice == "2":

            deposit_money(bank)

        elif choice == "3":

            withdraw_money(bank)

        elif choice == "4":

            transfer_money(bank)

        elif choice == "5":

            display_accounts(bank)

        elif choice == "6":

            search_account(bank)

        elif choice == "7":

            save_accounts(bank)

        elif choice == "8":

            display_transactions(bank)

        elif choice == "9":

            search_transactions(bank)

        elif choice == "10":

            FileManager.save_accounts(
            bank.accounts
            )

            print(
                "✅ Data saved successfully!"
            )

            print(
                "Thank you for using Bukhari Bank!"
            )

            break

        else:

            print(
                "❌ Invalid choice! "
                "Please select a number from 1 to 10."
            )


if __name__ == "__main__":
    main()