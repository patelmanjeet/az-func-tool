import os
from dotenv import load_dotenv
from azure.storage.queue import QueueClient

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")
queue_client = QueueClient.from_connection_string(connect_str, q_name)

properties = queue_client.get_queue_properties()
count = properties.approximate_message_count
print("Message count: " + str(count))

# Peek at the 5 message
messages = queue_client.peek_messages(max_messages=5)
for peeked_message in messages:
    print("Peeked message: " + peeked_message.content)
