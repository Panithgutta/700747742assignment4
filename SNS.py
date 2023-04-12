import boto3
import yaml

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

sns_topic_name = config['sns_topic_name']
email_address_1 = config['email_address_1']
email_address_2 = config['email_address_2']
sns_client = boto3.client('sns')

response = sns_client.create_topic(Name=sns_topic_name)

sns_topic_arn = response['TopicArn']
sns_client.subscribe(
    TopicArn=sns_topic_arn,
    Protocol='email',
    Endpoint=email_address_1
)

sns_client.subscribe(
    TopicArn=sns_topic_arn,
    Protocol='email',
    Endpoint=email_address_2
)