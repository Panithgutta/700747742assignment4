# mymodule.py

import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get topic name and email addresses
topic_name = config.get('Settings', 'topic')
email_address1 = config.get('Settings', 'email_address1')
email_address2 = config.get('Settings', 'email_address2')

# Define a function that uses the configuration values
def my_function():
    print('Topic name:', topic_name)
    print('Email address 1:', email_address1)
    print('Email address 2:', email_address2)


# Create SNS client
sns = boto3.client('sns')

# Create SNS topic
response = sns.create_topic(Name=topic_name)
topic_arn = response['TopicArn']

# Configure email addresses as subscribers
sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address1
)

sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address2
)

print('SNS topic created with name:', topic_name)
print('Email addresses configured as subscribers:', email_address1, email_address2)
