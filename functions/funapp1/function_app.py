import logging
import azure.functions as func
import json

app = func.FunctionApp()

@app.function_name(name="QueueFunc")
@app.queue_trigger(arg_name="msg", queue_name="testq",
                   connection="AzureWebJobsStorage")  # Queue trigger
def test_function(msg: func.QueueMessage) -> None:
    message_json = msg.get_json()

    if message_json['id'] == 50:
        logging.error('Python queue trigger function processed a queue item: %s with error', message_json)
        raise Exception('This key message not allowd')
    else:
        logging.info('Python queue trigger function processed a queue item: %s', message_json)
