import boto3

sns = boto3.client('sns')
sqs = boto3.client('sqs')


def init():
    topic = sns.create_topic(
        Name='messageTopic.fifo',
        Attributes={
            'FifoTopic': 'true'
        },
    )
    queue = sqs.create_queue(
        QueueName='someQueue'
    )

    # subscribe to sns topic
    subscription = sns.subscribe(
        TopicArn= topic.get('TopicArn'),
        Protocol='sqs',
        Endpoint= queue.get('QueueArn'),
        ReturnSubscriptionArn= True
    )

    return {
        'topicArn': topic.get('TopicArn'),
        'queueArn': queue.get('QueueArn'),
        'subscriptionArn': subscription.get('SubscriptionArn')
    }


def publish_message(topicArn):
    pass

def poll_queue(queueArn):
    pass

def main():
    topicArn, queueArn = init().values()
    publish_message(topicArn=topicArn)
    poll_queue(queueArn=queueArn)