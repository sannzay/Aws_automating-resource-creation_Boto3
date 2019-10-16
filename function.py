import json
import pandas 
import pyodbc
import sqlalchemy

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda with all my imports working/')
    }
