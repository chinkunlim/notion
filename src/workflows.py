# import libraries
import time
import os
import logging
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path
from rich.console import Console
from tqdm import tqdm

# import modules
from .config_manager import load_env, get_env_key, set_env_key
from .notion_client.notion_api_client import NotionApiClient

logger = logging.getLogger(__name__)

def execute_test_connection():
    logger.info("Test connection with Notion")
    
    if not load_env():
        logger.error(f"Failed to load")
        return False

    config = get_env_key()
    api_key = config.get("NOTION_KEY")
    parent_page_id = config.get("PARENT_PAGE_ID")

    if not api_key:
        logger.critical("NOTION_KEY not found!")
        return False
    
    if not parent_page_id:
        logger.critical("PARENT_PAGE_ID not found!")
        return False
    
    notion_client = NotionApiClient(api_key)
    notion_bot_info = notion_client.test_connection()
    if not notion_bot_info:
        logger.critical("Connection failed")
        return False
    logger.info(f"Connection passed. Bot's name: {notion_bot_info.get("name")} ")
