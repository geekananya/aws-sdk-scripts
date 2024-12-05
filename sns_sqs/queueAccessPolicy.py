from constants import *

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "SQS:SendMessage",
            "Resource": f"arn:aws:sqs:{aws_env}:{main_q_name}",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": f"arn:aws:sns:{aws_env}:{sns_topic_name}"
                }
            }
        }
    ]
}