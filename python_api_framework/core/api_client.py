import requests
from config.config  import Config
from core.exceptions import APIException
from core.logger import logger

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"GET Request URL: {url}")
        response = requests.get(url, timeout=Config.TIMEOUT)
        return self._handle_response(response)

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"POST Request URL: {url} with data: {payload}")
        response = requests.post(url, json=payload, timeout=Config.TIMEOUT)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code >= 400:
            logger.error(f"API Error: {response.status_code} - {response.text}")
            raise APIException(f"API Error: {response.status_code} - {response.text}")
        logger.info(f"Response Status: {response.status_code}")
        return response.json(), response.status_code
        