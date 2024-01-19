import requests

class EtherPy:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_balance(self, address):
        response = requests.get(f"{self.endpoint}/balance?address={address}")
        return response.json()["balance"]
