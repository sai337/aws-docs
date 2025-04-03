import boto3

# parameter_name = 'AppName'
# elbv2_client = boto3.client('elbv2')
# def tagkey(**tagkeyvalue):
#   print(tagkeyvalue)
  
#   if_name_=="_main_":
#     tagkey(parameter_name1='AppName', parameter_name2='AppOwner')x

# def tagkey_value(event, context):
#     ssm_client = boto3.client('ssm')
#     parameter_name1 = 'AppName'
#     parameter_name2 = 'AppOwner'
#     parameter_name3 = 'Environment'
#     parameter_name4 = 'BusinessUnit'
#     parameter_name5 = 'ImpactArea'
#     parameter_name6 = 'SupportOwner'

#     print(parameter_name1)
#     print(parameter_name2)
#     print(parameter_name3)
#     print(parameter_name4)
#     print(parameter_name5)
#     print(parameter_name6)
#     response = ssm_client.get_parameter(Name=parameter_name1)
#     parameter_value1 = response['Parameter']['Value']
#     print(parameter_value1)
#     response = ssm_client.get_parameter(Name=parameter_name2)
#     parameter_value2 = response['Parameter']['Value']
#     print(parameter_value2)
#     response = ssm_client.get_parameter(Name=parameter_name3)
#     parameter_value3 = response['Parameter']['Value']
#     print(parameter_value3)
#     response = ssm_client.get_parameter(Name=parameter_name4)
#     parameter_value4 = response['Parameter']['Value']
#     print(parameter_value4)
#     response = ssm_client.get_parameter(Name=parameter_name5)
#     parameter_value5 = response['Parameter']['Value']
#     print(parameter_value5)
#     response = ssm_client.get_parameter(Name=parameter_name6)
#     parameter_value6 = response['Parameter']['Value']
#     print(parameter_value6)
    
def lambda_handler(event, context):
    # Initialize the SSM and EC2 clients
    ssm_client = boto3.client('ssm')
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')
    lambda_client = boto3.client('lambda')
    elbv2_client = boto3.client('elbv2')
    kms_client = boto3.client('kms')
    efs_client =boto3.client('efs')
    sqs_client = boto3.client('sqs')
    sns_client = boto3.client('sns')
    dynamodb_client = boto3.client('dynamodb')
    lambda_client = boto3.client('lambda')
    apigateway_client = boto3.client('apigateway')
    cloudfront_client = boto3.client('cloudfront')
    ecs_client = boto3.client('ecs')
    globalaccelerator_client = boto3.client ('globalaccelerator')
    kafka_client = boto3.client('kafka')
    stepfunction_client = boto3.client('stepfunctions')
    elasticbeanstalk_client = boto3.client('elasticbeanstalk')
    acm_client = boto3.client('acm')
    cloudtrail_client = boto3.client('cloudtrail')
    ecs_client = boto3.client('ecs')
    codecommit_client = boto3.client('codecommit')
    codepipeline_client = boto3.client('codepipeline')
    cloudformation_client = boto3.client('cloudformation')
    ecr_client = boto3.client('ecr')     
    ram_client = boto3.client('ram')
    fsx_client = boto3.client('fsx')
    mq_client = boto3.client('mq')
    es_client = boto3.client('es')
    rds_client = boto3.client('rds')
    events_client = boto3.client('events')
    logs_client = boto3.client('logs')
    autoscaling_client = boto3.client('autoscaling')
    eks_client = boto3.client('eks')
    athena_client = boto3.client('athena')
    secretsmanager_client = boto3.client('secretsmanager')
    backup_client = boto3.client('backup')
    kafka_client = boto3.client('kafka')
    opensearch_client = boto3.client('opensearch')
    elasticache_client = boto3.client('elasticache')
    redshift_client = boto3.client('redshift')
    glue_client = boto3.client('glue')
    appconfig_client = boto3.client('appconfig')
    kinesis_client = boto3.client('kinesis')
    fireshose_client = boto3.client('firehose')
    amplify_client = boto3.client('amplify')
    print(event)
    parameter_name1 = 'AppName'
    parameter_name2 = 'AppOwner'
    parameter_name3 = 'Environment'
    parameter_name4 = 'BusinessUnit'
    parameter_name5 = 'ImpactArea'
    parameter_name6 = 'SupportOwner'
    
   

    # print(parameter_name1)
    # print(parameter_name2)
    # print(parameter_name3)
    # print(parameter_name4)
    # print(parameter_name5)
    # print(parameter_name6)
    response = ssm_client.get_parameter(Name=parameter_name1)
    parameter_value1 = response['Parameter']['Value']
    print(parameter_value1)
    response = ssm_client.get_parameter(Name=parameter_name2)
    parameter_value2 = response['Parameter']['Value']
    print(parameter_value2)
    response = ssm_client.get_parameter(Name=parameter_name3)
    parameter_value3 = response['Parameter']['Value']
    print(parameter_value3)
    response = ssm_client.get_parameter(Name=parameter_name4)
    parameter_value4 = response['Parameter']['Value']
    print(parameter_value4)
    response = ssm_client.get_parameter(Name=parameter_name5)
    parameter_value5 = response['Parameter']['Value']
    print(parameter_value5)
    response = ssm_client.get_parameter(Name=parameter_name6)
    parameter_value6 = response['Parameter']['Value']
    print(parameter_value6)
    
    tags=[
        { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]
        
    #  tag1={ 
    #         parameter_name1 :   parameter_value1 ,
    #         parameter_name2 :   parameter_value2 ,
    #         parameter_name3 :   parameter_value3 ,
    #         parameter_name4 :   parameter_value4 ,
    #         parameter_name5 :   parameter_value5 ,
    #         parameter_name6 :   parameter_value6 ,
    #       }      
    # Specify the SSM parameter name containing tags (JSON format)
    # parameter_name1 = 'AppName'
    # parameter_name2 = 'AppOwner'
    # parameter_name3 = 'Environment'
    # parameter_name4 = 'BusinessUnit'
    # parameter_name5 = 'ImpactArea'
    # parameter_name6 = 'SupportOwner'

    # print(parameter_name1)
    # print(parameter_name2)
    # print(parameter_name3)
    # print(parameter_name4)
    # print(parameter_name5)
    # print(parameter_name6)
    # # try:
    # print("afterenteringtryblock")
    # # Get the SSM parameter value
    # response = ssm_client.get_parameter(Name=parameter_name1)
    # parameter_value1 = response['Parameter']['Value']
    # print(parameter_value1)
    # response = ssm_client.get_parameter(Name=parameter_name2)
    # parameter_value2 = response['Parameter']['Value']
    # print(parameter_value2)
    # response = ssm_client.get_parameter(Name=parameter_name3)
    # parameter_value3 = response['Parameter']['Value']
    # print(parameter_value3)
    # response = ssm_client.get_parameter(Name=parameter_name4)
    # parameter_value4 = response['Parameter']['Value']
    # print(parameter_value4)
    # response = ssm_client.get_parameter(Name=parameter_name5)
    # parameter_value5 = response['Parameter']['Value']
    # print(parameter_value5)
    # response = ssm_client.get_parameter(Name=parameter_name6)
    # parameter_value6 = response['Parameter']['Value']
    # print(parameter_value6)
    
    # Convert the parameter value to a dictionary
    # tags = eval(parameter_value)
    # tags1 = parameter_value1
    # tags2 = parameter_value2
    # tags3 = parameter_value3
    # tags4 = parameter_value4
    # tags5 = parameter_value5
    # tags6 = parameter_value6
    
    # print("tags",tags1)
    # Extract the EC2 instance ID from the EventBridge event
    # instance_id = event['detail']['responseElements']['instancesSet']['items']['instanceId']
    # if instance_id == event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']:
    if event['detail']['eventName'] == 'RunInstances':
      print(event)
      instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
      print(instance_id)
      ec2_client.create_tags(
      Resources=[instance_id],
      Tags=[
        { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ] 
      )
    elif event['detail']['eventName'] == 'CreateVolume':
        volumeId = event['detail']['responseElements']['volumeId']
        ec2_client.create_tags(
        Resources=[volumeId],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateSnapshot':
        snapshot_id = event['detail']['responseElements']['snapshotId']
        ec2_client.create_tags(
        Resources=[snapshot_id],
        Tags=[
          { 
           'Key': parameter_name1,
            'Value': parameter_value1
          },
          {
           'Key': parameter_name2,
           'Value': parameter_value2
          },
          {
           'Key': parameter_name3,
            'Value': parameter_value3
          },
          {
           'Key': parameter_name4,
           'Value': parameter_value4
          },
          {
           'Key': parameter_name5,
           'Value': parameter_value5
          },
          {
           'Key': parameter_name6,
           'Value': parameter_value6
          }
        ]   
    )
    elif event['detail']['eventName'] == 'CreateSecurityGroup':
        groupId = event['detail']['responseElements']['groupId']
        ec2_client.create_tags(
        Resources=[groupId],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateSubnet':
        subnetId = event['detail']['responseElements']['subnet']['subnetId']
        ec2_client.create_tags(
        Resources=[subnetId],
        Tags=[
          {
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateKeyPair':
        keyPairId = event['detail']['responseElements']['keyPairId']
        ec2_client.create_tags(
        Resources=[keyPairId],
        Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
    elif event['detail']['eventName'] == 'CreateVpc':
        vpcId = event['detail']['responseElements']['vpc']['vpcId']
        ec2_client.create_tags(
        Resources=[vpcId],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateManagedPrefixList':
        prefixListId = event['detail']['responseElements']['CreateManagedPrefixListResponse']['prefixList']['prefixListId']
        ec2_client.create_tags(
        Resources=[prefixListId],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateVpcEndpoint':
        vpcEndpointId = event['detail']['responseElements']['CreateVpcEndpointResponse']['vpcEndpoint']['vpcEndpointId']
        ec2_client.create_tags(
        Resources=[vpcEndpointId],
        Tags=[
          { 
       
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateRouteTable':
        routeTableId = event['detail']['responseElements']['routeTable']['routeTableId']
        ec2_client.create_tags(
        Resources=[routeTableId],
        Tags=[
          { 
      
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateLaunchTemplate':
        launch_template_id = event['detail']['responseElements']['CreateLaunchTemplateResponse']['launchTemplate']['launchTemplateId']
        ec2_client.create_tags(
        Resources=[launch_template_id],
        Tags=[
          { 
      
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )   
    elif event['detail']['eventName'] == 'CreateImage':
        image_id = event['detail']['responseElements']['imageId']
        ec2_client.create_tags(
        Resources=[image_id],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )       
    # elif event['detail']['eventName'] == 'CreateFleet':
    #     fleet_id = event['detail']['responseElements']['fleetId']
    #     ec2_client.create_tags(
    #     Resources=[fleet_id],
    #     Tags=[
    #       { 
      
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )
    #############################ssm############################
    elif event['detail']['eventName'] == 'CreateDocument':
      name = event['detail']['requestParameters']['name']
      ssm_client.add_tags_to_resource(
      ResourceType = 'Document',
      ResourceId = name,
      Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
    elif event['detail']['eventName'] == 'PutParameter':
      name = event['detail']['requestParameters']['name']
      ssm_client.add_tags_to_resource(
      ResourceType = 'Parameter',
      ResourceId = name,
      Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
    #Got Error
    elif event['detail']['eventName'] == 'CreateMaintenanceWindow':
      windowId = event['detail']['responseElements']['windowId']
      ssm_client.add_tags_to_resource(
      ResourceType = 'MaintenanceWindow',
      ResourceId = windowId,
      Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
    elif event['detail']['eventName'] == 'CreateOpsItem':
      OpsItemId = event['detail']['responseElements']['OpsItemId']
      ssm_client.add_tags_to_resource(
      ResourceType = 'OpsItem',
      ResourceId = OpsItemId,
      Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
          'Value': parameter_value6
        }
      ]   
      )
      ##blocked in scp
    elif event['detail']['eventName'] == 'CreatePatchBaseline':
      BaselineId = event['detail']['responseElements']['name']
      ssm_client.add_tags_to_resource(
      ResourceType = 'Baseline',
      ResourceId = BaselineId,
      Tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
    #############################amplify############################
    if event['detail']['eventName'] == 'CreateApp': 
      appArn = event['detail']['responseElements']['app']['appArn']
      amplify_client.tag_resource(
      resourceArn=appArn,
      Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 , 
          }
      )
    # if event['detail']['eventName'] == 'CreateBranch': 
    #   appArn = event['detail']['responseElements']['app']['appArn']
    #   amplify_client.tag_resource(
    #   resourceArn=appArn,
    #   Tags={ 
    #         parameter_name1 :   parameter_value1 ,
    #         parameter_name2 :   parameter_value2 ,
    #         parameter_name3 :   parameter_value3 ,
    #         parameter_name4 :   parameter_value4 ,
    #         parameter_name5 :   parameter_value5 ,
    #         parameter_name6 :   parameter_value6 , 
    #       }
    #   )  
    #############################kinesis#############################
    if event['detail']['eventName'] == 'CreateStream': 
      StreamName = event['detail']['requestParameters']['streamName']
      kinesis_client.add_tags_to_stream(
      StreamName=StreamName,
      Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 , 
          }
      )
    if event['detail']['eventName'] == 'CreateDeliveryStream': 
      DeliveryStreamName = event['detail']['requestParameters']['deliveryStreamName']
      fireshose_client.tag_delivery_stream(
      DeliveryStreamName=DeliveryStreamName,
      Tags=[
           { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]  
      )  
    #############################msk kafka#############################    
    
    if event['detail']['eventName'] == 'CreateClusterV2': 
      clusterArn = event['detail']['responseElements']['clusterArn']
      kafka_client.tag_resource(
      ResourceArn=clusterArn,
      Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 , 
          }
      )
    if event['detail']['eventName'] == 'CreateReplicator': 
      instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
      kafka_client.tag_resource(
      ResourceArn=[instance_id],
      Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 , 
          }
      )
    if event['detail']['eventName'] == 'CreateVpnConnection': 
      instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
      kafka_client.tag_resource(
      ResourceArn=[instance_id],
      Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 , 
          }
      )    
    #############################AppConfig#############################    
    elif event['detail']['eventName'] == 'CreateApplication':
        applicationid = event['detail']['responseElements']['id']
        appconfig_client.tag_resource(
        ResourceArn = f'arn:aws:appconfig:{event["awsRegion"]}:{event["accountId"]}:application/{applicationid}',
        Tags={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateEnvironment':
        environmentid = event['detail']['responseElements']['id']
        appconfig_client.tag_resource(
        ResourceArn = f'arn:aws:appconfig:{event["awsRegion"]}:{event["accountId"]}:environment/{environmentid}',
        Tags={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateConfigurationProfile':
        configurationid = event['detail']['responseElements']['id']
        appconfig_client.tag_resource(
        ResourceArn = f'arn:aws:appconfig:{event["awsRegion"]}:{event["accountId"]}:configurationprofile/{configurationid}',
        Tags={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )        
    elif event['detail']['eventName'] == 'CreateDeploymentStrategy':
        name = event['detail']['responseElements']['name']
        appconfig_client.tag_resource(
        ResourceArn = f'arn:aws:appconfig:{event["awsRegion"]}:{event["accountId"]}:deploymentstrategy/{name}',
        Tags={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    # elif event['detail']['eventName'] == 'CreateExtensionAssociation':
    #     name = event['detail']['responseElements']['name']
    #     appconfig_client.tag_resource(
    #     ResourceArn = f'arn:aws:appconfig:{event["awsRegion"]}:{event["accountId"]}:deploymentstrategy/{name},
    #     Tags={
    #         parameter_name1 :   parameter_value1 ,
    #         parameter_name2 :   parameter_value2 ,
    #         parameter_name3 :   parameter_value3 ,
    #         parameter_name4 :   parameter_value4 ,
    #         parameter_name5 :   parameter_value5 ,
    #         parameter_name6 :   parameter_value6 ,
    #       }
    #     )            
    #############################GLUE#############################    
    elif event['detail']['eventName'] == 'CreateConnection':
        connectionname = event['detail']['requestParameters']['connectionInput']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:connection/{connectionname}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateCrawler':
        Crawlername = event['detail']['requestParameters']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:crawler/{Crawlername}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateDatabase':
        Databasename = event['detail']['requestParameters']['databaseInput']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:database/{Databasename}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateJob':
        jobname = event['detail']['requestParameters']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:job/{jobname}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateMLTransform':
        jobname = event['detail']['requestParameters']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:mlTransform/{jobname}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateSession':
        sessionname = event['detail']['requestParameters']['session']['command']['name']
        glue_client.add_tags_to_resource(
        ResourceArn = f'arn:aws:glue:{event["awsRegion"]}:{event["accountId"]}:session/{sessionname}',
        TagsToAdd={
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )                        
    ############################# redshift ##########################
    
    elif event['detail']['eventName'] == 'CreateCluster':
        clusterIdentifier = event['detail']['responseElements']['clusterIdentifier']
        account_id = event['detail']['userIdentity']['accountId']
        redshift_client.create_tags(
        ResourceName = f'arn:aws:redshift:us-west-2:{account_id}:/redshift/{clusterIdentifier}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
          ]
        )
    elif event['detail']['eventName'] == 'CreateClusterSubnetGroup':
        subnetgroupname = event['detail']['responseElements']['clusterSubnetGroupName']
        account_id = event['detail']['userIdentity']['accountId']
        redshift_client.create_tags(
        ResourceName = f'arn:aws:redshift:us-west-2:{account_id}:/subnetgroup/{subnetgroupname}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
          ]
        )
    # elif event['detail']['eventName'] == 'CreateClusterSecurityGroup':
    #     domainArn = event['detail']['responseElements']['domainStatus']['aRN']
    #     redshift_client.add_tags(
    #     ResourceName = f'arn:aws:apigateway:us-west-2::/redshift/{subnetgroupname}',
    #     TagList=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       { 
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       { 
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       { 
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       { 
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       { 
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #       ]
    #     )        
    elif event['detail']['eventName'] == 'CreateClusterParameterGroup':
        parametergroupname = event['detail']['responseElements']['parameterGroupName']
        account_id = event['detail']['userIdentity']['accountId']
        redshift_client.add_tags(
        ResourceName = f'arn:aws:redshift:us-west-2:{account_id}:/parametergroupname/{parametergroupname}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
          ]
        )
    elif event['detail']['eventName'] == 'CreateClusterSnapshot':
        clustersnapshotname = event['detail']['responseElements']['snapshotIdentifier']
        account_id = event['detail']['userIdentity']['accountId']
        redshift_client.add_tags(
        ResourceName = f'arn:aws:redshift:us-west-2:{accountId}:/clustersnapshotname/{clustersnapshotname}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
          ]
        )            
    ############################# elastic cache ##########################
    
    elif event['detail']['eventName'] == 'CreateCacheCluster':
        clustername = event['detail']['responseElements']['domainStatus']['aRN']
        elasticache_client.add_tags_to_resource(
        ResourceName = clustername,
        Tags=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )
    elif event['detail']['eventName'] == 'CreateCacheParameterGroup':
        cacheparamtergroupname = event['detail']['responseElements']['cacheParameterGroupName']
        elasticache_client.add_tags_to_resource(
        ResourceName = cacheparamtergroupname,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )    
    elif event['detail']['eventName'] == 'CreateCacheSubnetGroup':
        cachesubnetgroupname = event['detail']['responseElements']['cacheSubnetGroupName']
        elasticache_client.add_tags_to_resource(
        ResourceName = cachesubnetgroupname,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )        
    elif event['detail']['eventName'] == 'CreateCacheSecurityGroup':
        cachesecuritygroupname = event['detail']['responseElements']['domainStatus']['aRN']
        elasticache_client.add_tags_to_resource(
        ResourceName = cachesecuritygroupname,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )
    elif event['detail']['eventName'] == 'CreateReplicationGroup':
        CreateReplicationGroupname = event['detail']['responseElements']['replicationGroupId']
        elasticache_client.add_tags_to_resource(
        ResourceName = CreateReplicationGroupname,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )        
    elif event['detail']['eventName'] == 'CreateServerlessCache':
        CreateServerlessCachename = event['detail']['responseElements']['serverlessCache']['serverlessCacheName']
        elasticache_client.add_tags_to_resource(
        ResourceName = CreateServerlessCachename,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )
    elif event['detail']['eventName'] == 'CreateSnapshot':
        CreateSnapshotname = event['detail']['responseElements']['snapshotName']
        elasticache_client.add_tags_to_resource(
        ResourceName = CreateSnapshotname,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )
    elif event['detail']['eventName'] == 'CreateUser':
        CreateUserName = event['detail']['responseElements']['userName']
        elasticache_client.add_tags_to_resource(
        ResourceName = CreateUserName,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )
    elif event['detail']['eventName'] == 'CreateGroup':
        GroupName = event['detail']['responseElements']['userGroupId']
        elasticache_client.add_tags_to_resource(
        ResourceName = GroupName,
        TagList=[
          {
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
          ]
        )                                
    
    ############################# elastic search domain ##########################
    
    elif event['detail']['eventName'] == 'CreateDomain':
        domainArn = event['detail']['responseElements']['domainStatus']['aRN']
        opensearch_client.add_tags(
        ARN = domainArn,
        TagList=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          { 
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          { 
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          { 
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          { 
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          { 
          'Key': parameter_name6,
          'Value': parameter_value6
          }
          ]
        )

    #############################Backup##########################
    
    elif event['detail']['eventName'] == 'CreateBackupPlan':
        backupPlanArn = event['detail']['responseElements']['backupPlanArn']
        backup_client.tag_resource(
        ResourceArn = backupPlanArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateBackupVault':
        backupvaultArn = event['detail']['responseElements']['backupVaultArn']
        backup_client.tag_resource(
        ResourceArn = backupvaultArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )    
    elif event['detail']['eventName'] == 'CreateFramework':
        frameworkArn = event['detail']['responseElements']['frameworkArn']
        backup_client.tag_resource(
        ResourceArn = frameworkArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )
    elif event['detail']['eventName'] == 'CreateReportPlan':
        reportPlanArn = event['detail']['responseElements']['reportPlanArn']
        backup_client.tag_resource(
        ResourceArn = reportPlanArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }   
        )
    elif event['detail']['eventName'] == 'CreateRestoreTestingPlan':
        restoreTestingPlanArn = event['detail']['responseElements']['restoreTestingPlanArn']
        backup_client.tag_resource(
        ResourceArn = restoreTestingPlanArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }
        )                
    #############################SecretManager##########################
    
    elif event['detail']['eventName'] == 'CreateSecret':
        SecretId = event['detail']['responseElements']['arn']
        secretsmanager_client.tag_resource(
        SecretId = SecretId,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    #############################AutoScaling##########################
    
    elif event['detail']['eventName'] == 'CreateAutoScalingGroup':
        autoscalinggroupname = event['detail']['requestParameters']['autoScalingGroupName']
        autoscaling_client.create_or_update_tags(
        Tags=[{ 
            'ResourceId' : autoscalinggroupname,
            'Key': parameter_name1,
            'Value': parameter_value1,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
          },
          { 
            'ResourceId' : autoscalinggroupname,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
            'Key': parameter_name2,
            'Value': parameter_value2,
          },
          { 
            'ResourceId' : autoscalinggroupname,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
            'Key': parameter_name3,
            'Value': parameter_value3,
          },
          { 
            'ResourceId' : autoscalinggroupname,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
            'Key': parameter_name4,
            'Value': parameter_value4,
          },
          { 
            'ResourceId' : autoscalinggroupname,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
            'Key': parameter_name5,
            'Value': parameter_value5,
          },
          { 
            'ResourceId' : autoscalinggroupname,
            'ResourceType': 'auto-scaling-group',
            'PropagateAtLaunch': True,
            'Key': parameter_name6,
            'Value': parameter_value6,
          }
          ]
        )
    #############################ELB2##########################
    elif event['detail']['eventName'] == 'CreateListener':
        listenerArn = event['detail']['responseElements']['listeners'][0]['listenerArn']
        elbv2_client.add_tags(
        ResourceArns = [
            listenerArn,
          ],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateLoadBalancer':
        loadBalancerArn = event['detail']['responseElements']['loadBalancers'][0]['loadBalancerArn']
        elbv2_client.add_tags(
        ResourceArns = [
            loadBalancerArn,
          ],
        Tags=tags
        )    
    elif event['detail']['eventName'] == 'CreateTargetGroup':
        print(event)
        targetGroupArn = event['detail']['responseElements']['targetGroups'][0]['targetGroupArn']
        print(targetGroupArn)
        elbv2_client.add_tags(
        ResourceArns = [
            targetGroupArn,
          ],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )        
    elif event['detail']['eventName'] == 'CreateRule':
        targetGroupArn = event['detail']['responseElements']['targetGroups'][0]['loadBalancerArn']
        elbv2_client.add_tags(
        ResourceArns = [
            targetGroupArn,
          ],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )            
    
    #############################Athena##########################
    elif event['detail']['eventName'] == 'CreateWorkGroup':
        workgroupname = event['detail']['requestParameters']['name']
        athena_client.tag_resource(
        ResourceARN = f'arn:aws:athena:us-west-2:712415140816:workgroup/{workgroupname}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateCapacityReservation':
        name = event['detail']['requestParameters']['name']
        athena_client.tag_resource(
        ResourceARN = f'arn:aws:athena:us-west-2:712415140816:capacity-reservation/{name}',
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )            
    #############################EKS#############################
    
    elif event['detail']['eventName'] == 'CreateFargateProfile':
        fargateProfileArn = event['detail']['responseElements']['fargateProfile']['fargateProfileArn']
        eks_client.tag_resource(
        resourceArn = fargateProfileArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )    
    elif event['detail']['eventName'] == 'CreateCluster':
        clusterArn = event['detail']['responseElements']['cluster']['arn']
        eks_client.tag_resource(
        resourceArn = clusterArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )        
    elif event['detail']['eventName'] == 'CreateNodegroup':
        nodegroupArn = event['detail']['responseElements']['nodegroup']['nodegroupArn']
        eks_client.tag_resource(
        resourceArn = nodegroupArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )            
    elif event['detail']['eventName'] == 'CreateAddon':
        addonArn = event['detail']['responseElements']['addon']['addonArn']
        eks_client.tag_resource(
        resourceArn = addonArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )                
    elif event['detail']['eventName'] == 'CreateAccessEntry':
        accessEntryArn = event['detail']['responseElements']['accessEntry']['accessEntryArn']
        eks_client.tag_resource(
        resourceArn = accessEntryArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )                    
    elif event['detail']['eventName'] == 'CreatePodIdentityAssociation':
        associationArn = event['detail']['responseElements']['association']['associationArn']
        eks_client.tag_resource(
        resourceArn = associationArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )                        
    #############################cloudwatch##########################
    
    elif event['detail']['eventName'] == 'CreateLogGroup':
        logGroupName = event['detail']['requestParameters']['logGroupName']
        logs_client.tag_log_group(
        logGroupName=logGroupName,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )
    elif event['detail']['eventName'] == 'CreateLogAnomalyDetector':
        resourceArn = event['detail']['responseElements']['anomalyDetectorArn']
        logs_client.tag_resource(
        resourceArn=resourceArn,
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          }  
        )    
    #############################EventBridge##########################
    elif event['detail']['eventName'] == 'CreateEventBus':
        eventBusArn = event['detail']['responseElements']['eventBusArn']
        rds_client.tags_resource(
        ResourceARN=[eventBusArn],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    #############################IAM##########################
    # elif event['detail']['eventName'] == 'CreateRole':
    #     rolename = event['detail']['responseElements']['eventBusArn']
    #     iam_client.tag_role(
    #     RoleName=[rolename],
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )
    # elif event['detail']['eventName'] == 'CreatePolicy':
    #     policyarn = event['detail']['responseElements']['eventBusArn']
    #     iam_client.tags_policy(
    #     PolicyArn=[policyarn],
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )          
    # elif event['detail']['eventName'] == 'CreateInstanceProfile':
    #     instanceprofilename = event['detail']['responseElements']['eventBusArn']
    #     iam_client.tag_instance_profile(
    #     InstanceProfileName=[instanceprofilename],
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )
    # elif event['detail']['eventName'] == 'CreateOpenIDConnectProvider':
    #     openidConnectproviderarn = event['detail']['responseElements']['eventBusArn']
    #     iam_client.tag_open_id_connect_provider(
    #     OpenIDConnectProviderArn=[openidConnectproviderarn],
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )
    # elif event['detail']['eventName'] == 'CreateUser':
    #     username = event['detail']['responseElements']['eventBusArn']
    #     iam_client.tag_user(
    #     UserName=[username],
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )    
    #############################Create RDS database##########################
    elif event['detail']['eventName'] == 'CreateDatabase':
        database_name = event['detail']['responseElements']['imageId']
        rds_client.add_tags_to_resource(
        ResourceName=[database_name],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )  
    elif event['detail']['eventName'] == 'CreateDBCluster':
        dBClusterArn = event['detail']['responseElements']['dBClusterArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBClusterArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )      
    elif event['detail']['eventName'] == 'CreateDBClusterSnapshot':
        dBClusterSnapshotArn = event['detail']['responseElements']['dBClusterSnapshotArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBClusterSnapshotArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateDBSubnetGroup':
        dBSubnetGroupArn = event['detail']['responseElements']['dBSubnetGroupArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBSubnetGroupArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )              
    elif event['detail']['eventName'] == 'CreateDBSecurityGroup':
        database_name = event['detail']['responseElements']['imageId']
        rds_client.add_tags_to_resource(
        ResourceName=[database_name],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )    
    elif event['detail']['eventName'] == 'CreateDBClusterParameterGroup':
        dBClusterParameterGroupArn = event['detail']['responseElements']['dBClusterParameterGroupArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBClusterParameterGroupArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        ) 
    # elif event['detail']['eventName'] == 'CreateDBInstance':
    #     dBInstanceArn = event['detail']['responseElements']['dBInstanceArn']
    #     rds_client.add_tags_to_resource(
    #     ResourceName=dBInstanceArn,
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )     
    elif event['detail']['eventName'] == 'CreateDBInstanceReadReplica':
        database_name = event['detail']['responseElements']['imageId']
        rds_client.add_tags_to_resource(
        ResourceName=[database_name],
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateDBParameterGroup':
        dBParameterGroupArn = event['detail']['responseElements']['dBParameterGroupArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBParameterGroupArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )             
    elif event['detail']['eventName'] == 'CreateDBSnapshot':
        dBSnapshotArn = event['detail']['responseElements']['dBSnapshotArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBSnapshotArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    elif event['detail']['eventName'] == 'CreateDBProxy':
        dBProxyArn = event['detail']['responseElements']['dBProxyArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBProxyArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )                     
    elif event['detail']['eventName'] == 'CreateDBProxyEndpoint':
        dBProxyEndpointArn = event['detail']['responseElements']['dBProxyEndpoint']['dBProxyEndpointArn']
        rds_client.add_tags_to_resource(
        ResourceName=dBProxyEndpointArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )                         
    ########################## SQS ##########################
    elif event['detail']['eventName'] == 'CreateQueue':
        queueName = event['detail']['requestParameters']['queueName']
        sqs_client.tag_resource(
        Resources=[queueName],
        Tags=[
            { 
            'Key': parameter_name1,
            'Value': parameter_value1
            },
            {
            'Key': parameter_name2,
            'Value': parameter_value2
            },
            {
            'Key': parameter_name3,
            'Value': parameter_value3
            },
            {
            'Key': parameter_name4,
            'Value': parameter_value4
            },
            {
            'Key': parameter_name5,
            'Value': parameter_value5
            },
            {
            'Key': parameter_name6,
            'Value': parameter_value6
            }
          ]   
          )    
          ##Create KMS key
    elif event['detail']['eventName'] == 'CreateKey':
         KmsKey = event['detail']['responseElements']['keyMetadata']['keyId']
         print(type(KmsKey))
         kms_client.tag_resource(
           KeyId=KmsKey,
           Tags=[
           { 
           'TagKey': parameter_name1,
           'TagValue': parameter_value1
           },
           {
           'TagKey': parameter_name2,
           'TagValue': parameter_value2
           },
           {
           'TagKey': parameter_name3,
           'TagValue': parameter_value3
           },
           {
           'TagKey': parameter_name4,
           'TagValue': parameter_value4
           },
           {
           'TagKey': parameter_name5,
           'TagValue': parameter_value5
           },
           {
           'TagKey': parameter_name6,
           'TagValue': parameter_value6
           }
        ]   
        )         
        ##EFS - CreateFileSystem
    elif event['detail']['eventName'] == 'CreateFileSystem':
         efsId = event['detail']['responseElements']['fileSystemId']
         efs_client.tag_resource(
         ResourceId=efsId,
         Tags=[
            { 
            'Key': parameter_name1,
            'Value': parameter_value1
            },
            {
            'Key': parameter_name2,
            'Value': parameter_value2
            },
            {
            'Key': parameter_name3,
            'Value': parameter_value3
            },
            {
            'Key': parameter_name4,
            'Value': parameter_value4
            },
            {
            'Key': parameter_name5,
            'Value': parameter_value5
            },
            {
            'Key': parameter_name6,
            'Value': parameter_value6
            }
          ]   
          )    
          ##EFS - CreateAccessPoint
    elif event['detail']['eventName'] == 'CreateAccessPoint':
         ResourceId = event['detail']['responseElements']['accessPointId']
         efs_client.tag_resource(
         ResourceId=ResourceId,
         Tags=[
            { 
            'Key': parameter_name1,
            'Value': parameter_value1
            },
            {
            'Key': parameter_name2,
            'Value': parameter_value2
            },
            {
            'Key': parameter_name3,
            'Value': parameter_value3
            },
            {
            'Key': parameter_name4,
            'Value': parameter_value4
            },
            {
            'Key': parameter_name5,
            'Value': parameter_value5
            },
            {
            'Key': parameter_name6,
            'Value': parameter_value6
            }
          ]   
          )          
    elif event['detail']['eventName'] == 'CreateTopic':
         topicArn = event['detail']['responseElements']['topicArn']
         sns_client.tag_resource(
         ResourceArn=topicArn,
         Tags=[
            { 
            'Key': parameter_name1,
            'Value': parameter_value1
            },
            {
            'Key': parameter_name2,
            'Value': parameter_value2
            },
            {
            'Key': parameter_name3,
            'Value': parameter_value3
            },
            {
            'Key': parameter_name4,
            'Value': parameter_value4
            },
            {
            'Key': parameter_name5,
            'Value': parameter_value5
            },
            {
            'Key': parameter_name6,
            'Value': parameter_value6
            }
          ]   
          )      
    ##################DynamoDB#####################      
    elif event['detail']['eventName'] == 'CreateTable':
         tableArn = event['detail']['responseElements']['tableDescription']['tableName']
         dynamodb_client.tag_resource(
         ResourceArn=tableArn,
         Tags=[
            { 
            'Key': parameter_name1,
            'Value': parameter_value1
            },
            {
            'Key': parameter_name2,
            'Value': parameter_value2
            },
            {
            'Key': parameter_name3,
            'Value': parameter_value3
            },
            {
            'Key': parameter_name4,
            'Value': parameter_value4
            },
            {
            'Key': parameter_name5,
            'Value': parameter_value5
            },
            {
            'Key': parameter_name6,
            'Value': parameter_value6
            }
          ]   
          )            
    #############################apigateway-v1-createrestapi#############################
    elif event['detail']['eventName'] == 'CreateRestApi':
        restApiId = event['detail']['responseElements']['restapiUpdate']['restApiId']
        apigateway_client.tag_resource(
        resourceArn=f'arn:aws:apigateway:us-west-2::/restapis/{restApiId}',
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
        )    
        ##apigateway-v1-createdomain         
    elif event['detail']['eventName'] == 'CreateDomainName':
        customdomainname = event['detail']['requestParameters']['domainName']
        apigateway_client.tag_resource(
        resourceArn=f'arn:aws:apigateway:{event["region"]}::/domainnames/{customdomainname}',
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
        )        
    ##apigateway-v1-createstage
    elif event['detail']['eventName'] == 'CreateStage':
        api_id = event['detail']['responseElements']['restApiId']
        stage_name = event['detail']['responseElements']['stageName']
        apigateway_client.tag_resource(
        resourceArn=f'arn:aws:apigateway:{event["region"]}::/restapis/{api_id}/stages/{stage_name}',
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
        )
    ##apigateway-v1-createvpclink
    elif event['detail']['eventName'] == 'CreateVpcLink':
        vpc_link_id = event['detail']['responseElements']['vpclinkUpdate']['vpcLinkId']
        apigateway_client.tag_resource(
        resourceArn=f'arn:aws:apigateway:{event["region"]}::/vpclinks/{vpc_link_id}',
        tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
        )         
        ##CreateLamdbafuntion
    elif event['detail']['eventName'] == 'CreateFunction20150331':
        functionArn = event['detail']['responseElements']['functionArn']
        print(functionArn)
        lambda_client.tag_resource(
        Resource=functionArn,
        Tags={ 
            parameter_name1 :   parameter_value1 ,
            parameter_name2 :   parameter_value2 ,
            parameter_name3 :   parameter_value3 ,
            parameter_name4 :   parameter_value4 ,
            parameter_name5 :   parameter_value5 ,
            parameter_name6 :   parameter_value6 ,
          },
        )  
        ##Ecs cluster 
    elif event['detail']['eventName'] == 'CreateCluster':
        ecsclusterArn = event['detail']['responseElements']['cluster']['clusterArn']
        ecs_client.tag_resource(
        resourceArn=ecsclusterArn,
        tags=[
          { 
          'key': parameter_name1,
          'value': parameter_value1
          },
          {
          'key': parameter_name2,
          'value': parameter_value2
          },
          {
          'key': parameter_name3,
          'value': parameter_value3
          },
          {
          'key': parameter_name4,
          'value': parameter_value4
          },
          {
          'key': parameter_name5,
          'value': parameter_value5
          },
          {
          'key': parameter_name6,
          'value': parameter_value6
          }
        ]   
        )
        ##Ecs service 
    elif event['detail']['eventName'] == 'CreatService':
        ecsserviceArn = event['detail']['responseElements']['service']['serviceArn']
        ecs_client.tag_resource(
        resourceArn=ecsserviceArn,
        tags=[
          { 
          'key': parameter_name1,
          'value': parameter_value1
          },
          {
          'key': parameter_name2,
          'value': parameter_value2
          },
          {
          'key': parameter_name3,
          'value': parameter_value3
          },
          {
          'key': parameter_name4,
          'value': parameter_value4
          },
          {
          'key': parameter_name5,
          'value': parameter_value5
          },
          {
          'key': parameter_name6,
          'value': parameter_value6
          }
        ]   
        )   
    ##Ecs taskset
    elif event['detail']['eventName'] == 'CreateTaskSet':
        ecsserviceArn = event['detail']['responseElements']['routeTableId']
        ecs_client.create_tags(
        resourceArn=ecsserviceArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
        ########################CreateCodecommitrepo########################
    elif event['detail']['eventName'] == 'CreateRepository':
      repositoryArn = event['detail']['responseElements']['repositoryArn']
      codecommit_client.tag_resource(
      resourceArn = repositoryArn,
      tags= {
          parameter_name1 :   parameter_value1 ,
          parameter_name2 :   parameter_value2 ,
          parameter_name3 :   parameter_value3 ,
          parameter_name4 :   parameter_value4 ,
          parameter_name5 :   parameter_value5 ,
          parameter_name6 :   parameter_value6 ,
      }   
      )    
    ###########################kafka###########################
    elif event['detail']['eventName'] == 'CreateClusterV2':
        ResourceArn = event['detail']['responseElements']['clusterArn']
        ecs_client.tag_resource(
        ResourceArn=ResourceArn,
        Tags={
          parameter_name1 :   parameter_value1 ,
          parameter_name2 :   parameter_value2 ,
          parameter_name3 :   parameter_value3 ,
          parameter_name4 :   parameter_value4 ,
          parameter_name5 :   parameter_value5 ,
          parameter_name6 :   parameter_value6 ,
          }   
        )
    elif event['detail']['eventName'] == 'CreateConfiguration':
        ResourceArn = event['detail']['responseElements']['arn']
        ecs_client.tag_resource(
        ResourceArn=ResourceArn,
        Tags={
          parameter_name1 :   parameter_value1 ,
          parameter_name2 :   parameter_value2 ,
          parameter_name3 :   parameter_value3 ,
          parameter_name4 :   parameter_value4 ,
          parameter_name5 :   parameter_value5 ,
          parameter_name6 :   parameter_value6 ,
          }   
        )    
    #######################CreateStepfuntions############################
    elif event['detail']['eventName'] == 'CreateStateMachine':
        functionArn = event['detail']['responseElements']['functionArn']
        stepfunction_client.create_tags(
        resourceArn=functionArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
    ##CreateStepfuntionActivity
    elif event['detail']['eventName'] == 'CreateActivity':
        activityArn = event['detail']['responseElements']['activityArn']
        stepfunction_client.create_tags(
        resourceArn=activityArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )
      ##MQ-CreateBroker
    elif event['detail']['eventName'] == 'CreateBroker':
        brokerArn = event['detail']['responseElements']['brokerArn']
        mq_client.create_tags(
        ResourceArn=brokerArn,
        Tags=[
          { 
             parameter_name1 :   parameter_value1 ,
             parameter_name2 :   parameter_value2 ,
             parameter_name3 :   parameter_value3 ,
             parameter_name4 :   parameter_value4 ,
             parameter_name5 :   parameter_value5 ,
             parameter_name6 :   parameter_value6 ,
          }
        ]   
        )  
    ##CreateElasticSearchDomain
    elif event['detail']['eventName'] == 'CreateDomain':
        Arn = event['detail']['responseElements']['domainStatus']['aRN']
        es_client.add_tags(
        ARN=Arn,
        TagList=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]   
        )    
    # ##Createelasticbeanstalk-CreateApplication
    # elif event['detail']['eventName'] == 'CreateApplication':
    #     activityArn = event['detail']['responseElements']['activityArn']
    #     stepfunction_client.update_tags_for_resource(
    #     ResourceArn='string',
    #     TagsToAdd=[
    #       {
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]
    #     )                   
    # ##Createelasticbeanstalk-CreateApplicationVersion
    # elif event['detail']['eventName'] == 'CreateApplicationVersion':
    #     activityArn = event['detail']['responseElements']['activityArn']
    #     stepfunction_client.create_tags(
    #     resourceArn=activityArn,
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )                       
    # ##Createelasticbeanstalk-CreateConfigurationTemplate
    # elif event['detail']['eventName'] == 'CreateConfigurationTemplate':
    #     activityArn = event['detail']['responseElements']['activityArn']
    #     stepfunction_client.create_tags(
    #     resourceArn=activityArn,
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )
    # ##Createelasticbeanstalk-CreateEnvironment
    # elif event['detail']['eventName'] == 'CreateEnvironment':
    #     activityArn = event['detail']['responseElements']['activityArn']
    #     stepfunction_client.create_tags(
    #     resourceArn=activityArn,
    #     Tags=[
    #       { 
    #       'Key': parameter_name1,
    #       'Value': parameter_value1
    #       },
    #       {
    #       'Key': parameter_name2,
    #       'Value': parameter_value2
    #       },
    #       {
    #       'Key': parameter_name3,
    #       'Value': parameter_value3
    #       },
    #       {
    #       'Key': parameter_name4,
    #       'Value': parameter_value4
    #       },
    #       {
    #       'Key': parameter_name5,
    #       'Value': parameter_value5
    #       },
    #       {
    #       'Key': parameter_name6,
    #       'Value': parameter_value6
    #       }
    #     ]   
    #     )   
        ##acm-requestcertificate
    elif event['detail']['eventName'] == 'RequestCertificate':
        CertificateArn = event['detail']['responseElements']['certificateArn']
        acm_client.add_tags_to_certificate(
        CertificateArn = CertificateArn,
        Tags=[
          { 
          'Key': parameter_name1,
          'Value': parameter_value1
          },
          {
          'Key': parameter_name2,
          'Value': parameter_value2
          },
          {
          'Key': parameter_name3,
          'Value': parameter_value3
          },
          {
          'Key': parameter_name4,
          'Value': parameter_value4
          },
          {
          'Key': parameter_name5,
          'Value': parameter_value5
          },
          {
          'Key': parameter_name6,
          'Value': parameter_value6
          }
        ]  
        )
      ## cloudtrail- createtrail
    elif event['detail']['eventName'] == 'CreateTrail':
      TrailArn = event['detail']['responseElements']['trailARN']
      cloudtrail_client.add_tags(
      ResourceId=TrailArn,
      # ResourceArn = TrailArn,
      TagsList=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )
      ################################ECR################################
    elif event['detail']['eventName'] == 'CreateRepository':
      resourceArn = event['detail']['responseElements']['repository']['repositoryArn']
      ecr_client.tag_resource(
      resourceArn = resourceArn,
      tags=[
        { 
        'Key': parameter_name1,
        'Value': parameter_value1
        },
        {
        'Key': parameter_name2,
        'Value': parameter_value2
        },
        {
        'Key': parameter_name3,
        'Value': parameter_value3
        },
        {
        'Key': parameter_name4,
        'Value': parameter_value4
        },
        {
        'Key': parameter_name5,
        'Value': parameter_value5
        },
        {
        'Key': parameter_name6,
        'Value': parameter_value6
        }
      ]   
      )  
      
      ###################RAM###################
    elif event['detail']['eventName'] == 'CreateResourceShare':
      resourceShareArn = event['detail']['responseElements']['resourceShare']['resourceShareArn']
      ram_client.tag_resource(
      resourceShareArn = resourceShareArn,
      tags=[
        { 
        'key': parameter_name1,
        'value': parameter_value1
        },
        {
        'key': parameter_name2,
        'value': parameter_value2
        },
        {
        'key': parameter_name3,
        'value': parameter_value3
        },
        {
        'key': parameter_name4,
        'value': parameter_value4
        },
        {
        'key': parameter_name5,
        'value': parameter_value5
        },
        {
        'key': parameter_name6,
        'value': parameter_value6
        }
      ]   
      )
      ##ram-CreatePermission
    elif event['detail']['eventName'] == 'CreatePermission':
      resourceArn = event['detail']['responseElements']['permission']['arn']
      ram_client.tag_resource(
      resourceArn = resourceArn,
      tags=[
        { 
        'key': parameter_name1,
        'value': parameter_value1
        },
        {
        'key': parameter_name2,
        'value': parameter_value2
        },
        {
        'key': parameter_name3,
        'value': parameter_value3
        },
        {
        'key': parameter_name4,
        'value': parameter_value4
        },
        {
        'key': parameter_name5,
        'value': parameter_value5
        },
        {
        'key': parameter_name6,
        'value': parameter_value6
        }
      ]   
      )  
    # ## codepipeline- CreatePipeline
    # elif event['detail']['eventName'] == 'CreatePipeline':
    #   codepipelineArn = event['detail']['requestParameters']['pipeline']['name']
    #   codepipeline_client.tag_resource(
    #   # resourceArn=arn:aws:codepipeline:us-west-2:account-id:MyPipeline,
    #   resourceArn=f'arn:aws:codepipeline:{event["awsRegion"]}:{event["accountId"]}:{codepipelineArn}',
    #   # ResourceArn = TrailArn,
    #   tags=[
    #     { 
    #     'Key': parameter_name1,
    #     'Value': parameter_value1
    #     },
    #     {
    #     'Key': parameter_name2,
    #     'Value': parameter_value2
    #     },
    #     {
    #     'Key': parameter_name3,
    #     'Value': parameter_value3
    #     },
    #     {
    #     'Key': parameter_name4,
    #     'Value': parameter_value4
    #     },
    #     {
    #     'Key': parameter_name5,
    #     'Value': parameter_value5
    #     },
    #     {
    #     'Key': parameter_name6,
    #     'Value': parameter_value6
    #     }
    #   ]   
    #   )  
      ##cloudformation-CreateStack
    # elif event['detail']['eventName'] == 'CreateStack':
    #   StackArn = event['detail']['responseElements']['stackId']
    #   cloudformation_client.tags_resource(
    #   ResourcesArn=StackArn,
    #   Tags=[
    #     { 
    #     'Key': parameter_name1,
    #     'Value': parameter_value1
    #     },
    #     {
    #     'Key': parameter_name2,
    #     'Value': parameter_value2
    #     },
    #     {
    #     'Key': parameter_name3,
    #     'Value': parameter_value3
    #     },
    #     {
    #     'Key': parameter_name4,
    #     'Value': parameter_value4
    #     },
    #     {
    #     'Key': parameter_name5,
    #     'Value': parameter_value5
    #     },
    #     {
    #     'Key': parameter_name6,
    #     'Value': parameter_value6
    #     }
    #   ]   
    #   )  
    ##########################s3##########################
    elif event['detail']['eventName'] == 'CreateBucket':
         bucketName = event['detail']['requestParameters']['bucketName']
         s3_client.put_bucket_tagging(
         Bucket = bucketName ,   
         Tagging={
             'TagSet' : [
                 { 
                      'Key': parameter_name1,
                      'Value': parameter_value1
                 },
                 {
                      'Key': parameter_name2,
                      'Value': parameter_value2
                 },
                 {
                      'Key': parameter_name3,
                      'Value': parameter_value3
                 },
                 {
                      'Key': parameter_name4,
                      'Value': parameter_value4
                 },
                 {
                      'Key': parameter_name5,
                      'Value': parameter_value5
                 },
                 {
                      'Key': parameter_name6,
                      'Value': parameter_value6
                 },
              ],
           },    
        )
# def aws_s3(event,context):
#     s3_client = boto3.client('s3')
#     if event['detail']['eventName'] == 'CreateBucket':
#       bucketName = event['detail']['requestParameters']['bucketName']
#       s3_client.create_tags(
#       Resources=[bucketName],
#           Tags=[
#             { 
#             'Key': parameter_name1,
#             'Value': parameter_value1
#             },
#             {
#             'Key': parameter_name2,
#             'Value': parameter_value2
#             },
#             {
#             'Key': parameter_name3,
#           #   'Key': AppName,
#             'Value': parameter_value3
#             },
#             {
#             'Key': parameter_name4,
#             'Value': parameter_value4
#             },
#             {
#             'Key': parameter_name5,
#             'Value': parameter_value5
#             },
#             {
#             'Key': parameter_name6,
#             'Value': parameter_value6
#             }
#           ]   
#           )  
          
#     response = client.create_tags(
#     Resources=[
#         'ami-78a54011',
#     ],
#     Tags=[
#         {
#             'Key': 'Stack',
#             'Value': 'production',
#         },
#     ],
# )

# print(response)        
    #     return {
    #         'statusCode': 200,
    #         'body': 'Tags added successfully.'
    #     }
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'body': f"Error: {str(e)}"
    #     }0
