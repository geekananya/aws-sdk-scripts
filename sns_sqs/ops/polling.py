import boto3

sns = boto3.client('sns')
sqs = boto3.client('sqs')

def poll_queue(queueUrl):
    messages = []
    while True:
        resp = sqs.receive_message(
            QueueUrl= queueUrl,
            AttributeNames=['All',] ,
            MaxNumberOfMessages= 3,
            WaitTimeSeconds= 10     # long polling
        )

        if resp.get('Messages'):
            messages = resp.get('Messages')

            for msg in messages:
                sqs.delete_message(
                    QueueUrl= queueUrl,
                    ReceiptHandle= msg['ReceiptHandle']
                )
            print("Message(s) found")
            break
        else:
            print("No messages found")
        
    return messages