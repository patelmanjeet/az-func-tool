import os
from dotenv import load_dotenv
from azure.storage.queue import QueueClient
import random

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")
queue_client = QueueClient.from_connection_string(connect_str, q_name)

messages = queue_client.receive_messages()
for message in messages:
    print("Dequeueing message: " + message.content)
    queue_client.delete_message(message.id, message.pop_receipt)
