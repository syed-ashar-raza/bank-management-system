from pathlib import Path

from src.file_manager import FileManager
from src.bank_account import BankAccount
from src.customer import Customer

def create_test_accounts():

    customer = Customer(
        "Ashar Raza",
        "03476371697"
    )

    account = BankAccount(
        customer,
        "ACC101",
        5000
    )

    return {
        account.account_number: account
    }

def test_save_and_load_accounts(tmp_path):

    test_file = tmp_path / "accounts.json"

    accounts = create_test_accounts()

    FileManager.save_accounts(
        accounts,
        test_file
    )

    loaded_accounts = FileManager.load_accounts(
        test_file
    )

    assert len(loaded_accounts) == 1

    loaded_account = loaded_accounts[0]

    assert loaded_account.account_number == "ACC101"
    assert loaded_account.get_balance() == 5000
    assert loaded_account.customer.name == "Ashar Raza"