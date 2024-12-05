import boto3
import datetime
from constants import *

sns = boto3.client('sns')

def publish_message(topicArn, message, groupid):
    response = sns.publish(
        TopicArn= topicArn,
        Message= message,
        MessageGroupId= groupid,
        MessageDeduplicationId= str(datetime.datetime.now().timestamp())
        # to distinguish eacvh msg for deduplication
    )
    print("Published")