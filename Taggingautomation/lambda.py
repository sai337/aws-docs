import boto3

# Your Lambda function code here import boto3 def lambda_handler(event, context):
    # Initialize the SSM and EC2 clients
def lambda_handler(event, context):    
    ssm_client = boto3.client('ssm')
    ec2_client = boto3.client('ec2')
    cloudformation_client = boto3.client('cloudformation')
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
    
    if event['detail']['eventName'] == 'CreateDocument':
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
      # no method tags for cloudformation 
    # elif event['detail']['eventName'] == 'CreateStack':
    #   Stackid = event['detail']['responseElements']['Stackid']
    #   cloudformation_client.create_tags(
    #   Resources=[Stackid],
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
    # elif event['detail']['eventName'] == 'CreateStackSet':
    #   StackSetid = event['detail']['responseElements']['StackSetid']
    #   cloudformation_client.create_tags(
    #   Resources=[StackSetid],
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
    # elif event['detail']['eventName'] == 'CreateResources':
    #   Resourceid = event['detail']['responseElements']['Resourceid']
    #   cloudformation_client.create_tags(
    #   Resources=[Resourceid],
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
        'alue': parameter_value6
        }
      ]   
      )
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
    elif event['detail']['eventName'] == 'CreateBackup':
      ResourceARN = event['detail']['responseElements']['BackupID']
      fsx_client.tag_resource(
      ResourceARN = ResourceARN,
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
    elif event['detail']['eventName'] == 'CreateDataRepositoryTask':
      TaskArn = event['detail']['responseElements']['TaskID']
      fsx_client.tag_resource(
      ResourceARN = TaskArn,
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
    elif event['detail']['eventName'] == 'CreateFileSystem':
      SystemArn = event['detail']['responseElements']['SystemID']
      fsx_client.tag_resource(
      ResourceARN = SystemArn,
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
    elif event['detail']['eventName'] == 'CreateFileSystemFromBackup':
      BackupArn = event['detail']['responseElements']['BackupID']
      fsx_client.tag_resource(
      ResourceARN = BackupArn,
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
      SnapshotArn = event['detail']['responseElements']['SnapshotID']
      fsx_client.tag_resource(
      ResourceARN = SnapshotArn,
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
      VolumeArn = event['detail']['responseElements']['VolumeID']
      fsx_client.tag_resource(
      ResourceARN = VolumeArn,
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
    elif event['detail']['eventName'] == 'CreateLifecyclePolicy':
      PolicyArn = event['detail']['responseElements']['PolicyID']
      dlm_client.tag_resource(
      ResourceArn = PolicyArn,
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
    elif event['detail']['eventName'] == 'RequestCertificate':
      CertificateArn = event['detail']['responseElements']['Certificateid']
      acm_client.add_tags_to_certificate(
      CertificateArn = CerticateArn,
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
    elif event['detail']['eventName'] == 'CreateTrail':
      TrailArn = event['detail']['responseElements']['Trailid']
      cloudtrail_client.add_tags(
      ResourceArn = TrailArn,
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
    elif event['detail']['eventName'] == 'CreateProject':
      ProjectArn = event['detail']['responseElements']['Projectid']
      codecommit_client.tag_resource(
      ResourceArn = ProjectArn,
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
    elif event['detail']['eventName'] == 'CreatePipeline':
      PipelineArn = event['detail']['responseElements']['Pipelineid']
      codepipeline_client.tag_resource(
      ResourceArn = PipelineArn,
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
    elif event['detail']['eventName'] == 'PutConfigRule':
      ConfigRuleArn = event['detail']['responseElements']['Ruleid']
      config_client.tag_resource(
      ResourceARN = PipelineArn,
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
    elif event['detail']['eventName'] == 'CreateApplication':
      ApplicationArn = event['detail']['responseElements']['Applicationid']
      elasticbeanstalk_client.update_tags_for_resource(
      ResourceARN = ApplicationArn,
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
    elif event['detail']['eventName'] == 'CreateApplicationVersion':
      ApplicationVersionArn = event['detail']['responseElements']['ApplicationVersionid']
      elasticbeanstalk_client.update_tags_for_resource(
      ResourceARN = ApplicationVersionArn,
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
    elif event['detail']['eventName'] == 'CreateConfigurationTemplate':
      TemplateArn = event['detail']['responseElements']['Templateid']
      elasticbeanstalk_client.update_tags_for_resource(
      ResourceARN = TemplateArn,
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
    elif event['detail']['eventName'] == 'CreateEnvironment':
      EnvironmentArn = event['detail']['responseElements']['Environmentid']
      elasticbeanstalk_client.update_tags_for_resource(
      ResourceARN = EnvironmentArn,
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
    elif event['detail']['eventName'] == 'CreateActivity':
      ActivityArn = event['detail']['responseElements']['Activityid']
      stepfunctions_client.tag_resource(
      ResourceARN = ActivityArn,
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
    elif event['detail']['eventName'] == 'CreateStateMachine':
      MachineArn = event['detail']['responseElements']['Machineid']
      stepfunctions_client.tag_resource(
      ResourceARN = MachineArn,
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
      
