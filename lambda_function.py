import boto3

region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)

def lambda_handler(event, context):
    action = event["action"]

    instances = ec2.instances.filter(Filters = [{'Name': 'tag:AutoStartStop', 'Values': ['true']}])

    for instance in instances:
        if action == 'Start':     
            print(f"Iniciando a instância {instance.id}...")
            instance.start()
            
        elif action == 'Stop':
            print(f"Desligando a instância {instance.id}...")
            instance.stop()
    
        else:
            print("Parâmetro inválido!")