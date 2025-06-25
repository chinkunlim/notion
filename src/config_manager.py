# import libraries
import os
import sys
import logging
from dotenv import load_dotenv, set_key, find_dotenv
from dataclasses import dataclass
from typing import Dict
from rich.console import Console

logger = logging.getLogger(__name__)
console = Console()

@dataclass
class NotionConfig:
    api_key: str
    parent_page_id: str

def load_env():
    dotenv_path = find_dotenv()
    if not dotenv_path:
        logger.warning("Couldn't find .env file")
        sys.exit()

    load_dotenv(dotenv_path)
    logger.info(f"read .env file successfully")

    config = get_env_key()
    api_key=config.get("NOTION_API_KEY")
    parent_page_id=config.get("PARENT_PAGE_ID")

    if not api_key or not parent_page_id:
        logger.critical("NOTION_KEY or PARENT_PAGE_ID not found!")
        sys.exit()
    
    return api_key, parent_page_id

def get_env_key():
    config_keys = [
        "NOTION_API_KEY",
        "PARENT_PAGE_ID",
        "DASHBOARD_TITLE",
        "SUBJECT_DATABASE_ID",
        "COURSE_DATABASE_ID",
        "TASK_DATABASE_ID",
        "NOTE_DATABASE_ID",
        "PROJECTS_DATABASE_ID",
        "RESOURCES_DATABASE_ID",
        "LOGIN_URL",
        "USERNAME",
        "PASSWORD",
    ]
    return {key: os.getenv(key) for key in config_keys if os.getenv(key) is not None}

def set_env_key(key, value):
    dotenv_path = find_dotenv()
    if not dotenv_path:
        project_root = os.path.dirname(os.path.abspath(__file__))
        print(project_root)
        dotenv_path = os.path.join(project_root, ".env")
        logger.warning(f".env file not found. .env file created {dotenv_path}")
    
    setting_env_key = set_key(dotenv_path, key, value)
    if setting_env_key:
        logger.info(f"{key} setting successfully")
    else:
        logger.error(f"{key} setting failed")