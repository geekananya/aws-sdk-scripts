from init.sns import *
from init.sqs import *
from ops.publish import publish_message
from ops.polling import poll_queue

import boto3
sns = boto3.client('sns')
sqs = boto3.client('sqs')

message1 = "This is message 1"
message2 = "This is message 2"
message3 = "This is message 3"
message4 = "This is message 4"
message5 = "This is message 5"


def main():
    create_dlq()
    queueUrl = create_main_q()
    topicArn = create_topic()
    create_subscription()


    publish_message(topicArn=topicArn, message=message1, groupid='group1')
    publish_message(topicArn=topicArn, message=message2, groupid='group1')
    publish_message(topicArn=topicArn, message=message3, groupid='group1')
    publish_message(topicArn=topicArn, message=message4, groupid='group1')

    messages = poll_queue(queueUrl=queueUrl)
    for msg in messages:
        print(msg.get('Body'))

    publish_message(topicArn=topicArn, message=message5, groupid='group1')

    messages = poll_queue(queueUrl=queueUrl)
    for msg in messages:
        print(msg.get('Body'))

    messages = poll_queue(queueUrl=queueUrl)
    for msg in messages:
        print(msg.get('Body'))


main()