import requests
from config import Config

class HSBCAPI:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {Config.HSBC_API_KEY}",
            "Content-Type": "application/json"
        }

    def get_account_balance(self, account_id):
        url = f"{Config.HSBC_BASE_URL}/accounts/{account_id}/balance"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error retrieving balance: {response.status_code} - {response.text}")

    def get_transaction_history(self, account_id):
        url = f"{Config.HSBC_BASE_URL}/accounts/{account_id}/transactions"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error retrieving transactions: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    hsbc_api = HSBCAPI()
    try:
        account_id = " 123456789"  # Replace with a valid account ID
        balance = hsbc_api.get_account_balance(account_id)
        print("Account Balance:", balance)

        transactions = hsbc_api.get_transaction_history(account_id)
        print("Transaction History:", transactions)

    except Exception as e:
        print("An error occurred:", e)
``` ### 4. `wells_fargo_api.py`
This file contains the API client for Wells Fargo.
```python
import requests
from config import Config

class WellsFargoAPI:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {Config.WELLS_FARGO_API_KEY}",
            "Content-Type": "application/json"
        }

    def get_account_balance(self, account_id):
        url = f"{Config.WELLS_FARGO_BASE_URL}/accounts/{account_id}/balance"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error retrieving balance: {response.status_code} - {response.text}")

    def get_transaction_history(self, account_id):
        url = f"{Config.WELLS_FARGO_BASE_URL}/accounts/{account_id}/transactions"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error retrieving transactions: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    wells_fargo_api = WellsFargoAPI()
    try:
        account_id = "1122334455"  # Replace with a valid account ID
        balance = wells_fargo_api.get_account_balance(account_id)
        print("Account Balance:", balance)

        transactions = wells_fargo_api.get_transaction_history(account_id)
        print("Transaction History:", transactions)

    except Exception as e:
        print("An error occurred:", e)