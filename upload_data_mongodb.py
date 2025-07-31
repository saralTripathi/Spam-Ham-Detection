import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# 1. Load CSV into DataFrame
csv_file_path = "spamham.csv"  # Replace with your actual path
df = pd.read_csv(csv_file_path)

# 2. Connect to MongoDB
mongo_uri = os.getenv("MONGODB_URL")  # Load MongoDB URI from .env file
client = MongoClient(mongo_uri)

# 3. Access DB and Collection
db = client["pws_projects"]       # Replace with your database name
collection = db["spam_ham"] # Replace with your collection name

# 4. Upload data
data = df.to_dict(orient="records")  # Convert DataFrame to list of dicts
collection.insert_many(data)

print(f"Inserted {len(data)} documents into MongoDB collection!")
