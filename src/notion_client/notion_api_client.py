import requests
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)

class NotionApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def _send_request(self, method: str, endpoint: str, payload: Optional[Dict[str, Any]] = None) -> Optional[requests.Response]:
            url = f"{self.base_url}/{endpoint}"
            try:
                response = requests.request(method, url, headers=self.headers, json=payload)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                logger.error(f"API 請求失敗: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    logger.error(f"回應內容: {e.response.text}")
                return None
            
    def test_connection(self):
        response = self._send_request("GET", "users/me")
        return response.json() if response else None