#!/usr/bin/env python3

import boto3, json

#Create the S3 client
s3client = boto3.client('s3')

#Creating a bucket name
bucket_name = "vsilva-week3-fall26"

bucket_response = s3client.create_bucket(Bucket=bucket_name)
del_access = s3client.delete_public_access_block(Bucket=bucket_name)

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}

bucket_policy_string = json.dumps(bucket_policy)

bucket_policy_response = s3client.put_bucket_policy(
    Bucket=bucket_name,
    Policy=bucket_policy_string
)

put_bucket_response = s3client.put_bucket_website(
    Bucket=bucket_name, 
    WebsiteConfiguration={ 
    'ErrorDocument': {'Key': 'error.html'}, 
    'IndexDocument': {'Suffix': 'index.html'}, 
    } 
)

#open index file to read it
indexFile = open('index.html', 'rb')
put_index_response = s3client.put_object(Body=indexFile, Bucket=bucket_name, Key='index.html',ContentType='text/html')
indexFile.close()
print(put_index_response)

#open error file to read it
errorFile = open('error.html', 'rb')
put_index_response = s3client.put_object(Body=errorFile, Bucket=bucket_name, Key='error.html',ContentType='text/html')
errorFile.close()
print(put_index_response)