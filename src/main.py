# scr/main.py
# import libraries
import logging
import time
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# print(f"PROJECT_ROOT: {PROJECT_ROOT}")

def setup_logging():
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"

    logging.basicConfig(
        level="INFO",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="a", encoding="utf-8"),
            RichHandler(rich_tracebacks=True)
        ]
    )

setup_logging()
logger = logging.getLogger(__name__)

# import modules
from .workflows import execute_test_connection

def main():
    setup_logging()
    console = Console()
    console.print(PROJECT_ROOT)
    execute_test_connection()

if __name__ == "__main__":
    main()