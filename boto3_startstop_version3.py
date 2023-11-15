import boto3
import sys

instance_id = 'i-0417fdd70c26ed9cc'  #instance id should be changed 

ec2_console = boto3.client('ec2')

def get_instance_status(instance_id):
    response = ec2_console.describe_instances(InstanceIds=[instance_id])

    if 'Reservations' in response and len(response['Reservations']) > 0:
        instances = response['Reservations'][0]['Instances']
        if instances:
            instance = instances[0]
            instance_status = instance['State']['Name']
            return instance_status
        else:
            return f"No instances found with ID: {instance_id}"
    else:
        return f"No reservations found with ID: {instance_id}"

if len(sys.argv) > 1:
    state = sys.argv[1].lower()
    current_status = get_instance_status(instance_id)
    
    if state == 'start':
        if current_status == 'running':
            print('Instance is already running')
        elif current_status == 'stopped':
            response = ec2_console.start_instances(InstanceIds=[instance_id])
            print(response)
        else:
            print(f'Instance is in an invalid state for starting: {current_status}')
    elif state == 'stop':
        if current_status == 'stopped':
            print('Instance is already stopped')
        elif current_status == 'running':
            response = ec2_console.stop_instances(InstanceIds=[instance_id])
            print(response)
        else:
            print(f'Instance is in an invalid state for stopping: {current_status}')
    elif state == 'status':
        print(f"Instance Status: {current_status}")
    else:
        print('Invalid state. Please enter either "start", "stop", or "status".')
else:
    state = input('Enter the instance state (start/stop/status): ').lower()
    current_status = get_instance_status(instance_id)
    
    if state == 'start':
        if current_status == 'running':
            print('Instance is already running')
        elif current_status == 'stopped':
            response = ec2_console.start_instances(InstanceIds=[instance_id])
            print(response)
        else:
            print(f'Instance is in an invalid state for starting: {current_status}')
    elif state == 'stop':
        if current_status == 'stopped':
            print('Instance is already stopped')
        elif current_status == 'running':
            response = ec2_console.stop_instances(InstanceIds=[instance_id])
            print(response)
        else:
            print(f'Instance is in an invalid state for stopping: {current_status}')
    elif state == 'status':
        print(f"Instance Status: {current_status}")
    else:
        print('Invalid state. Please enter either "start", "stop", or "status".')
