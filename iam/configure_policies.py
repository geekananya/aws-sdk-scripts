import boto3
import json

iam = boto3.client('iam')
policy_arn = 'arn:aws:iam::779846787648:policy/mys3policy'

def create_new_policy():

    with open('s3policy.json', 'r') as f:
        policy_document = json.load(f)

    response = iam.create_policy(
        PolicyName = 'mys3policy',
        PolicyDocument = json.dumps(policy_document),
        Description = 'Grants read only access to amazon s3.',
    )
    return response



def handle_user_policies(user):

    if(not iam.get_policy(PolicyArn=policy_arn)):
        policy = create_new_policy
        print("Created new policy: \n", policy)
    else:
        print("Policy already exists.")

    try:
        iam.attach_user_policy(
            UserName=user,
            PolicyArn= policy_arn
        )
        print(iam.list_attached_user_policies(UserName='test'))

    except iam.exceptions.NoSuchEntityException as e:
        print(e)


handle_user_policies(user='test')
