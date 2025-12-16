import sys
from pathlib import Path
from core.config import get_app_name

sys.path.append(str(Path(__file__).resolve().parent))

def main():
    print(f"Starting {get_app_name()}")

if __name__ == "__main__":
    main()
