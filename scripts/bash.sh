#!/bin/bash
# Uploads dataset to S3 bucket

BUCKET="smog-analysis-india"
DATASET="city_hour.csv"

echo "Uploading dataset to S3..."
aws s3 cp $DATASET s3://$BUCKET/raw/

echo "Verifying upload..."
aws s3 ls s3://$BUCKET/raw/