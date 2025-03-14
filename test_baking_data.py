# Testing account creation and initial state
# Testing basic deposit functionality
# Testing deposit validation (positive amounts)
# Testing withdrawal functionality
# Testing withdrawal validation
# Testing transaction recording
# Testing statement printing

from baking_data import Account

def test_new_account_0_balance():
    account = Account()
    assert account.balance == 0

