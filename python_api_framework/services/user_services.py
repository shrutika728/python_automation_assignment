import requests
from typing import Optional, Tuple, Any, Dict
from config.config import Config

class UserService:
    """Thin wrapper around the API endpoints used in tests."""

    def __init__(self, base_url: Optional[str] = None, timeout: Optional[int] = None, session: Optional[requests.Session] = None):
        self.base_url = base_url or Config.BASE_URL
        self.timeout = timeout or Config.TIMEOUT
        self.session = session or requests.Session()

    def _safe_json(self, resp: requests.Response) -> Any:
        try:
            return resp.json()
        except (ValueError, requests.exceptions.JSONDecodeError):
            return {}

    def get_users(self, page: int = 1) -> Tuple[Dict, int]:
        url = f"{self.base_url}/users"
        resp = self.session.get(url, params={"page": page}, timeout=self.timeout)
        if resp.status_code == 404:
            return {}, 404
        return self._safe_json(resp), resp.status_code

    def get_user(self, user_id: int) -> Tuple[Dict, int]:
        url = f"{self.base_url}/users/{user_id}"
        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code == 404:
            return {}, 404
        return self._safe_json(resp), resp.status_code

    def create_user(self, payload: dict) -> Tuple[Dict, int]:
        url = f"{self.base_url}/users"
        resp = self.session.post(url, json=payload, timeout=self.timeout)
        return self._safe_json(resp), resp.status_code

