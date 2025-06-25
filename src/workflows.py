# import libraries
import time
import os
import sys
import json
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
console = Console()
api_key, parent_page_id = load_env()
notion_client = NotionApiClient(api_key)

def execute_test_connection():
    logger.info("Test connection with Notion")

    notion_bot_info = notion_client.test_connection()

    if not notion_bot_info:
        logger.critical("Connection failed")
        return False
    logger.info(f"Connection passed. Bot's name: {notion_bot_info.get("name")} ")

def execute_delete_blocks():
    logger.info(f"Detecting page block to delete...")
    response = notion_client.get_block_children(parent_page_id)
    logger.info(f"{type(response)}")
    
    if not response or response.status_code != 200:
        logger.error(f"Failed to get contents")
        sys.exit()
        
    blocks = response.json().get("results", [])
    logger.info(json.dumps(blocks, indent=4))

    if len(blocks) == 0:
        logger.info(f"No blocks detected")
        return

    logger.info(f"Get {len(blocks)} blocks.")
    logger.warning(f"Detected {len(blocks)} to delete")
    if console.input("Delete all blocks? (y/n)").lower() == "y":
        if console.input("Delete all blocks? (y/n)").lower() == "y":
            logger.info(f"Deleting {parent_page_id}")
            for block in tqdm(blocks, desc="Deleting...", unit="block"):
                notion_client.delete_block(block["id"])
            logger.info("Blocks deleted")         
        else:
            logger.info("Cancelled")        
    else:
        logger.info("Cancelled")