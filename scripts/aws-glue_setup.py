import boto3

# Initialize clients
glue = boto3.client('glue')
iam = boto3.client('iam')  # for iam access

def create_glue_role(role_name):

    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument='''{
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "glue.amazonaws.com"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }'''
        )
        
        # Attach necessary policies
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
        )
        
        print(f"Successfully created role {role_name}")
        return response['Role']['Arn']
    except Exception as e:
        print(f"Error creating role: {e}")
        return None

def create_glue_crawler(crawler_name, role_arn, s3_path, db_name):
    """Create Glue crawler to catalog data"""
    try:
        response = glue.create_crawler(
            Name=crawler_name,
            Role=role_arn,
            DatabaseName=db_name,
            Targets={
                'S3Targets': [
                    {
                        'Path': s3_path,
                        'Exclusions': []
                    }
                ]
            },
            SchemaChangePolicy={
                'UpdateBehavior': 'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
            }
        )
        print(f"Successfully created our cloudy a3 crawler {crawler_name}")
        return response
    except Exception as e:
        print(f"Error creating crawler: {e}")
        return None

# Example usage
if __name__ == "__main__":
    ROLE_NAME = "GlueSmogRole"
    CRAWLER_NAME = "smog-crawler"
    S3_PATH = "s3://smog-analysis-india/raw/"
    DB_NAME = "smogdb"
    
    role_arn = create_glue_role(ROLE_NAME)
    if role_arn:
        create_glue_crawler(CRAWLER_NAME, role_arn, S3_PATH, DB_NAME)