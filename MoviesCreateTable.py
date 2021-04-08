import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",\
            region_name ='eu-west-1', aws_access_key_id='DUMMYIDEXAMPLE', aws_secret_access_key='DUMMYEXAMPLEKEY')
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },
            {
                'AttributeName' : 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }
    )
    return table

if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status : ", movie_table.table_status)
