import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://psbhardwaj181_db_user:MMnsjhQRFXAa3cFu@cluster0.sjrvasq.mongodb.net/?appName=Cluster0")
DB_NAME = os.getenv("MONGODB_DB", "emrs_dornala")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]
