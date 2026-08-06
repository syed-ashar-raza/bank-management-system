"""
Bank module.

This module contains the Bank class which manages multiple
bank accounts and provides account-related operations.
"""


from src.bank_account import BankAccount
from src.exceptions import (
    AccountNotFoundError,
    DuplicateAccountError
)


class Bank:
    """
    Represents a bank that manages multiple accounts.

    Attributes:
        bank_name (str):
            Name of the bank.

        accounts (dict[str, BankAccount]):
            Dictionary containing accounts using account numbers
            as keys.
    """

    def __init__(
        self,
        bank_name: str
    ) -> None:
        """
        Initialize a Bank object.

        Parameters:
            bank_name (str):
                Name of the bank.
        """

        self.bank_name = bank_name
        self.accounts: dict[str, BankAccount] = {}


    def add_account(
        self,
        account: BankAccount,
        show_message: bool = True
    ) -> BankAccount:
        """
        Add a new account to the bank.

        Parameters:
            account (BankAccount):
                Account to add.

            show_message (bool):
                Whether to display success message.

        Returns:
            BankAccount:
                The added account.

        Raises:
            DuplicateAccountError:
                If account number already exists.
        """

        account_number = account.account_number

        if account_number in self.accounts:

            raise DuplicateAccountError(
                f"Account {account_number} already exists!"
            )

        self.accounts[account_number] = account

        if show_message:

            print(
                f"{account.customer.name}'s account "
                f"added to {self.bank_name}."
            )

        return account


    def find_account(
        self,
        account_number: str
    ) -> BankAccount:
        """
        Find an account by account number.

        Parameters:
            account_number (str):
                Account number to search.

        Returns:
            BankAccount:
                Matching bank account.

        Raises:
            AccountNotFoundError:
                If account does not exist.
        """

        try:

            return self.accounts[account_number]

        except KeyError:

            raise AccountNotFoundError(
                f"Account {account_number} not found!"
            )


    def transfer(
        self,
        sender_account_number: str,
        receiver_account_number: str,
        amount: float
    ) -> None:
        """
        Transfer money between two accounts.

        Parameters:
            sender_account_number (str):
                Account sending money.

            receiver_account_number (str):
                Account receiving money.

            amount (float):
                Transfer amount.

        Returns:
            None
        """

        sender = self.find_account(
            sender_account_number
        )

        receiver = self.find_account(
            receiver_account_number
        )

        sender.transfer(
            receiver,
            amount
        )


    def display_accounts(self) -> None:
        """
        Display all bank accounts.

        Returns:
            None
        """

        if not self.accounts:

            print("No accounts found.")
            return

        print(
            f"\nAccounts in {self.bank_name}:\n"
        )

        for account in self.accounts.values():

            account.display_balance()

            print("-" * 28)


    def __str__(self) -> str:
        """
        Return bank information.

        Returns:
            str:
                Bank name and account count.
        """

        return (
            f"{self.bank_name} - "
            f"Total Accounts: {len(self.accounts)}"
        )