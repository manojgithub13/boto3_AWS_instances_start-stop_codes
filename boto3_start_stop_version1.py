import boto3

# Specify your AWS credentials
aws_access_key_id = 'AKIA425UW2UF2M3NVIGK'
aws_secret_access_key = 'C7wcfkm4fpaRlE8A/X0vW5Vr9pDiMjB/Mn8fxi8Q'
aws_region = 'eu-north-1'  # Replace with your desired AWS region

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Replace 'i-1234567890abcdef0' with the instance ID you want to stop
instance_id = 'i-0b304055da94cb48d'

# Stop the EC2 instance
response = ec2.stop_instances(InstanceIds=[instance_id])

# Print the response
print("Response:", response)
