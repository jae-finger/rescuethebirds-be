from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

code_enviroment = os.getenv("CODE_ENVIRONMENT")

print(code_enviroment)