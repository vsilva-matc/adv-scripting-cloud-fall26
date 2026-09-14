#!/usr/bin/env python3
import boto3, json

#Create the S3 client
s3client = boto3.client('s3')

#List buckets
bucket_list = s3client.list_buckets()

for bucket in bucket_list['Buckets']:
    bucket_name = bucket['Name']
    print(f"Bucket Name is: {bucket_name}")

#List the objects inside the bucket
bucket_objects = s3client.list_objects_v2(Bucket=bucket_name)

#Checking if bucket is empty or has objects
if 'Contents' in bucket_objects:
    for obj in bucket_objects['Contents']:
        print(f"Object: {obj['Key']}")
else:
    print(" (No objects were found)")