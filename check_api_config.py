
import os
from pathlib import Path
from dotenv import load_dotenv

project_folder = Path(__file__).resolve().parent
env_file = project_folder / ".env"

print("Project folder:", project_folder)
print(".env file exists:", env_file.is_file())

load_dotenv(dotenv_path=env_file, override=True)

api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.strip():
    print("API key detected: YES")
else:
    print("API key detected: NO")
