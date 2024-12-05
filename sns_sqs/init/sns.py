import boto3
from constants import *

sns = boto3.client('sns')
sqs = boto3.client('sqs')

def create_topic():
    topic = sns.create_topic(
        Name= sns_topic_name,
        Attributes={
            'FifoTopic': 'true'
        },
    )
    return topic['TopicArn']

def create_subscription():
    # subscribe to sns topic
    subscription = sns.subscribe(
        TopicArn= f"arn:aws:sns:{aws_env}:{sns_topic_name}",
        Protocol='sqs',
        Endpoint= f"arn:aws:sqs:{aws_env}:{main_q_name}",
        ReturnSubscriptionArn= True
    )
    return subscription.get('SubscriptionArn')