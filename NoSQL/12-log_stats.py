#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
from pymongo import MongoClient

client = MongoClient()

db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})
print(f"{total_logs} logs")

print("Methods:")
print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"method GET /status: {status_count}")
