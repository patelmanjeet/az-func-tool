import os
from dotenv import load_dotenv
from azure.storage.queue import QueueClient
import random

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")
queue_client = QueueClient.from_connection_string(connect_str, q_name)

message = "Hello World - " + str(random.randint(0,100))
print("Adding message: " + message)
queue_client.send_message(message)
