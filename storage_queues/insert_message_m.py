import os
from dotenv import load_dotenv
from azure.storage.queue import QueueClient
import json

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING" )
q_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")
queue_client = QueueClient.from_connection_string(connect_str, q_name)

count = 1
while True:
    message = { "id": count, "key": "value - " + str(count) }  # JSON message
    message = json.dumps(message)
    print("Adding message: " + message)
    queue_client.send_message(message)
    count = count + 1
