import boto3

region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)

def lambda_handler(event, context):
    action = event["action"]

    instances = ec2.instances.filter(Filters = [{'Name': 'tag:AutoStartStop', 'Values': ['true']}])

    if action == 'Start':
        for instance in instances:
            print(f"Ligando a instância {instance.id}...")
            instance.start()
            
    elif action == 'Stop':
        for instance in instances:
            print(f"Desligando a instância {instance.id}...")
            instance.stop()
            