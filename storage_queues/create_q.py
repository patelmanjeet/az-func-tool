import os
from dotenv import load_dotenv
from azure.storage.queue import QueueClient
from azure.core.exceptions import ResourceExistsError

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")

print("Creating queue: " + q_name)
queue_client = QueueClient.from_connection_string(connect_str, q_name)

try:
    queue_client.create_queue()
except ResourceExistsError:
    pass
