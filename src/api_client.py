# src/api_client.py
import requests


class APIClient:
    def __init__(self, base_url, auth_token=None):
        self.base_url = base_url
        self.auth_token = auth_token

    def get_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response

    def post(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.get_headers(), json=json)
        response.raise_for_status()
        return response

    def put(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=self.get_headers(), json=json)
        response.raise_for_status()
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=self.get_headers())
        response.raise_for_status()
        return response
