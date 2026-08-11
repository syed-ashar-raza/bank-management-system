from src.bank import Bank
from src.bank_account import BankAccount
from src.customer import Customer
from src.exceptions import AccountNotFoundError


def create_test_account():
    customer = Customer(
        "Ashar Raza",
        "03476371697"
    )

    return BankAccount(
        customer,
        "ACC101",
        5000
    )


def test_find_account():
    bank = Bank("Test Bank")

    account = create_test_account()

    bank.add_account(
        account,
        show_message=False
    )

    found_account = bank.find_account(
        "ACC101"
    )

    assert found_account is account


def test_find_account_not_found():
    bank = Bank("Test Bank")

    try:
        bank.find_account("ACC999")

    except AccountNotFoundError:
        assert True

    else:
        assert False