#### This project is designed to act as a collection of building blocks required to automate the build process of AWS cloud architectures and to demonstrate them using Boto3.  

## Details about the notebooks present in this directory


### Create_resources.ipynb

This notebook demonstrates the following programatically:

- Installation of boto3
- Creating s3 buckets
- Creating lambda function
- Creating RDS DB
- Creating Resource group
- Setting up "Amazon Simple Queue Service" trigger to the lambda function (along with Kinesis and DynamoDB)
- Setting up "s3 bucket" trigger to the lambda function

### Master-Slave architecture documentation.ipynb

This notebook demonstrates the creation of building serverless architecture by automating resource creation and their alignment programatically:

- Demonstrates "master-slave" like fuctioning architecture using lambda functions
- Resource creation functions from "Create_resources.ipynb" are used to create/integrate/align the resources

### Requirements:

- boto3==1.9.160
- botocore==1.12.160
- certifi==2019.3.9
- chardet==3.0.4
- docutils==0.14
- idna==2.8
- jmespath==0.9.4
- numpy==1.16.4
- pandas==0.24.2
- python-dateutil==2.8.0
- pytz==2019.1
- requests==2.22.0
- s3transfer==0.2.0
- six==1.12.0
- SQLAlchemy==1.3.4
- urllib3==1.25.3


