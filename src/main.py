from datetime import datetime
from pathlib import Path

def write_version():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version_file = Path(__file__).parent.parent / "version.md"
    version_file.write_text(current_time)
    print(f"Current date and time ({current_time}) written to version.md")

if __name__ == "__main__":
    write_version()
