# import libraries
import os
import logging
from dotenv import load_dotenv, set_key, find_dotenv
from typing import Dict

logger = logging.getLogger(__name__)

def load_env():
    dotenv_path = find_dotenv()
    if not dotenv_path:
        logger.warning("Couldn't find .env file")
        return False
    load_dotenv(dotenv_path)
    logger.info(f"read .env file successfully")
    return True

def get_env_key():
    config_keys = [
        "NOTION_KEY",
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