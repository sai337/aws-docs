import boto3

# Your Lambda function code here import boto3 def lambda_handler(event, context):
    # Initialize the SSM and EC2 clients
def lambda_handler(event, context):    
    ssm_client = boto3.client('ssm')
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')
    lambda_client = boto3.client('lambda')
    elbv2_client = boto3.client('elbv2')
    sns_client = boto3.client('sns')
    sqs_client = boto3.client('sqs')
    efs_client = boto3.client('efs')
    es_client = boto3.client('es')
    elasticache_client = boto3.client('elasticache')
    apigateway_client = boto3.client('apigateway')
    events_client = boto3.client('events')
    stepfunctions_client = boto3.client('stepfunctions')
    rds_client = boto3.client('rds')
    dynamodb_client = boto3.client('dynamodb')
    docdb_client = boto3.client('docdb')
    cloudwatch_client = boto3.client('cloudwatch')
    memorydb_client = boto3.client('memorydb')
    aurora_client = boto3.client('rds-data')
    athena_client = boto3.client('athena')
    glue_client = boto3.client('glue')
    kinesis_client = boto3.client ('kinesis') 
    backup_client = boto3.client('backup')
    acm_client = boto3.client('acm')
    acm_pca_client = boto3.client('acm-pca')
    cloudtrail_client = boto3.client('cloudtrail')
    config_client = boto3.client('config')
    dlm_client = boto3.client('dlm')
    ecr_client = boto3.client('ecr')
    elasticbeanstalk_client = boto3.client('elasticbeanstalk')
    kms_client = boto3.client('kms')
    kinesisfirehose_client = boto3.client('firehose')
    mq_client = boto3.client('mq')
    route53_client = boto3.client('route53')
    workspaces_client = boto3.client('workspaces')
    ses_client = boto3.client('ses')
    swf_client = boto3.client('swf')
    xray_client = boto3.client('xray')
    secretsmanager_client = boto3.client('secretsmanager')
    ram_client = boto3.client('ram')
    redshift_client = boto3.client('redshift')
    emr_client = boto3.client('emr')
    globalaccelerator_client = boto3.client ('globalaccelerator')
    fsx_client = boto3.client('fsx')
    datapipeline_client = boto3.client('datapipeline')
    appsync_client = boto3.client('appsync')
    appconfig_client = boto3.client('appconfig')
    codeBuild_client = boto3.client('codebuild')
    codepipeline_client = boto3.client('codepipeline')
    codecommit_client = boto3.client('codecommit')
    cloudfront_client = boto3.client('cloudfront')
    ecs_client = boto3.client('ecs')
    kafka_client = boto3.client('kafka')
    servicecatalog_client = boto3.client('servicecatalog')
    cognito_client = boto3.client('cognito-idp')
    storagegateway_client = boto3.client('storagegateway')
    guardduty_client = boto3.client('guardduty')
    
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
    
    if event['detail']['eventName'] == 'RunInstances': 
      instance_id == event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
      print("instance_id", instance_id)
      print("beforecreatetags")
       
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
    elif event['detail']['eventName'] == 'CreateSnapshot':
        snapshotId = event['detail']['responseElements']['snapshotId']
        ec2_client.create_tags(
        Resources=[snapshotId],
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
        launchtemplateId = event['detail']['responseElements']['launchtemplateId']
        ec2_client.create_tags(
        Resources=[launchtemplateId],
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
    elif event['detail']['eventName'] == 'Createkeypair':
        keypairId = event['detail']['responseElements']['keypairId']
        ec2_client.create_tags(
        Resources=[keypairId],
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
    elif event['detail']['eventName'] == 'Createfleet':
        fleetId = event['detail']['responseElements']['fleetId']
        ec2_client.create_tags(
        Resources=[fleetId],
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
        subnetId = event['detail']['responseElements']['subnetId']
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
    elif event['detail']['eventName'] == 'CreateImage':
        ImageId = event['detail']['responseElements']['ImageId']
        ec2_client.create_tags(
        Resources=[ImageId],
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
        vpcId = event['detail']['responseElements']['vpcId']
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
        prefixListId = event['detail']['responseElements']['prefixListId']
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
        vpcEndpointId = event['detail']['responseElements']['vpcEndpointId']
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
        routeTableId = event['detail']['responseElements']['routeTableId']
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
    elif event['detail']['eventName'] == 'CreateFunction20150331':
        functionName = event['detail']['responseElements']['functionName']
        lambda_client.tag_resource(
        Resources=[functionName],
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
    elif event['detail']['eventName'] == 'CreateBucket':
        bucketName = event['detail']['requestParameters']['bucketName']
        s3_client.put_bucket_tagging(
        Resources=[bucketName],
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
          ###EFS
    elif event['detail']['eventName'] == 'CreateMountTarget':
        efsId = event['detail']['responseElements']['fileSystemId']
        efs_client.tag_resource(
        Resources=[efsId],
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
          ###kms###
    elif event['detail']['eventName'] == 'CreateKey':
        keyId = event['detail']['responseElements']['keyMetadata']['keyId']
        kms_client.tag_resource(
        Resources=[keyId],
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
          ###DynamoDB
    elif event['detail']['eventName'] == 'CreateTable':
        table_name = event['detail']['responseElements']['tableDescription']['tableName']
        dynamodb_client.tag_resource(
        Resources=[table_name],
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
          ###sns
    elif event['detail']['eventName'] == 'Createtopic':
        topicName = event['detail']['requestParameters']['name']
        sns_client.tag_resource(
        Resources=[topicName],
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
# def aws_s3(event,context): #     s3_client = boto3.client('s3') #     if event['detail']['eventName'] == 'CreateBucket': #       bucketName = event['detail']['requestParameters']['bucketName'] #       s3_client.create_tags( #       Resources=[bucketName], #           Tags=[ #             {  #             'Key': parameter_name1, #             'Value': parameter_value1 #             }, #             { #             'Key': parameter_name2, #             'Value': parameter_value2 #             }, #             { #             'Key': parameter_name3, #           #   'Key': AppName, #             'Value': parameter_value3 #             }, #             { #             'Key': parameter_name4, #             'Value': parameter_value4 #             }, #             { #             'Key': parameter_name5, #             'Value': parameter_value5 #             }, #             { #             'Key': parameter_name6, #             'Value': parameter_value6 #             } #           ]    #           )  
          
#     response = client.create_tags( #     Resources=[ #         'ami-78a54011', #     ], #     Tags=[ #         { #             'Key': 'Stack', #             'Value': 'production', #         }, #     ], # )
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
