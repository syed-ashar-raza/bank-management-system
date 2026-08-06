"""
File Manager module.

This module handles saving and loading bank account data
using JSON file storage.
"""


import json
from pathlib import Path

from src.customer import Customer
from src.bank_account import BankAccount
from src.transaction import Transaction


BASE_DIR = Path(__file__).resolve().parent.parent

FILE_NAME = (
    BASE_DIR
    / "data"
    / "accounts.json"
)


class FileManager:
    """
    Handles saving and loading bank account data.

    This class provides methods to serialize BankAccount
    objects into JSON format and reconstruct them back
    into Python objects.
    """


    @staticmethod
    def save_accounts(
    accounts: dict[str, BankAccount],
    file_name: Path = FILE_NAME,
) -> None:
        """
        Save bank accounts to JSON file.

        Parameters:
            accounts (dict[str, BankAccount]):
                Dictionary containing account numbers
                and BankAccount objects.

        Returns:
            None
        """

        data = [
            account.to_dict()
            for account in accounts.values()
        ]

        try:
            with open(
                file_name,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )

        except OSError as error:

            print(
                f"Error saving accounts to "
                f"{file_name}: {error}"
            )


    @staticmethod
    def load_accounts(
        file_name: Path = FILE_NAME,
    ) -> list[BankAccount]:
        """
        Load bank accounts from JSON file.

        Returns:
            list[BankAccount]:
                List of reconstructed BankAccount objects.

                Returns an empty list if the file does
                not exist or JSON is invalid.
        """

        try:

            with open(
                file_name,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            return FileManager.create_accounts(
                data
            )

        except json.JSONDecodeError:

            print(
                "Warning: accounts.json is corrupted. "
                "Starting with empty accounts."
            )

            return []

        except FileNotFoundError:

            print(
                f"Warning: {file_name} not found. "
                "Starting with empty accounts."
            )

            return []


    @staticmethod
    def create_accounts(
        data: list[dict]
    ) -> list[BankAccount]:
        """
        Convert JSON data into BankAccount objects.

        Parameters:
            data (list[dict]):
                List of dictionaries loaded from JSON.

        Returns:
            list[BankAccount]:
                Reconstructed bank accounts.
        """

        accounts: list[BankAccount] = []

        for account_data in data:

            customer_data = account_data["customer"]

            customer = Customer(
                customer_data["name"],
                customer_data["phone"]
            )

            account = BankAccount(
                customer,
                account_data["account_number"],
                account_data["balance"]
            )

            for transaction_data in account_data.get(
                "transactions",
                []
            ):

                transaction = Transaction(
                    transaction_data["transaction_type"],
                    transaction_data["amount"]
                )

                account.transactions.append(
                    transaction
                )

            accounts.append(
                account
            )

        return accounts