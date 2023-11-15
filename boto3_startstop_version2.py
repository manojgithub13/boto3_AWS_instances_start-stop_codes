import boto3
import sys

aws_management_console = boto3.Session(profile_name='default', region_name='eu-north-1')
ec2_console = aws_management_console.client('ec2')
instance_ids =['i-0b304055da94cb48d']

if len(sys.argv) > 1:
    state = sys.argv[1].lower()
    if state == 'start':
        response = ec2_console.start_instances(InstanceIds=instance_ids)
        print(response)
    elif state == 'stop':
        response = ec2_console.stop_instances(InstanceIds=instance_ids)
        print(response)
    else:
        print('Invalid state. Please enter either "start" or "stop".')
else:
    state = input('Enter the instance state (start/stop): ').lower()
    if state == 'start':
        response = ec2_console.start_instances(InstanceIds=instance_ids)
        print(response)
    elif state == 'stop':
        response = ec2_console.stop_instances(InstanceIds=instance_ids)
        print(response)
    else:
        print('Invalid state. Please enter either "start" or "stop".')
