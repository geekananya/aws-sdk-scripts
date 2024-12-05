import boto3
import json
from constants import *
from queueAccessPolicy import policy as qpolicy

sns = boto3.client('sns')
sqs = boto3.client('sqs')

def create_dlq():
    dlq = sqs.create_queue(
        QueueName= dlq_name,
        Attributes={
            'FifoQueue': 'true',
            'ContentBasedDeduplication': 'true'
        }
    )
    return dlq['QueueUrl']


def create_main_q():
    queue = sqs.create_queue(
        QueueName = main_q_name,
        Attributes = {
            'FifoQueue': 'true',
            'ContentBasedDeduplication': 'true',
            'Policy': json.dumps(qpolicy),
            'RedrivePolicy': json.dumps({
                'deadLetterTargetArn': f"arn:aws:sqs:{aws_env}:{dlq_name}",
                'maxReceiveCount': 3  # Number of times a message can be delivered before being moved to DLQ
            })
        }
    )
    return queue['QueueUrl']
