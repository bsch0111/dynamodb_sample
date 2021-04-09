from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', \
        region_name ='eu-west-1', aws_access_key_id='DUMMYIDEXAMPLE', aws_secret_access_key='DUMMYEXAMPLEKEY')

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year':year, \
        'title':title})
    except ClientError as e :
        print(e.response['Error']['Message'])
    else:
        return response['Item']

if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("get movie succed:")
        pprint(movie, sort_dicts=False)