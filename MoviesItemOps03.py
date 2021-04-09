from decimal import Decimal
#Decimal : 소수
from pprint import pprint
import boto3

def update_movie(title, year, rating, plot, actors, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', \
        region_name ='eu-west-1', aws_access_key_id='DUMMYIDEXAMPLE', aws_secret_access_key='DUMMYEXAMPLEKEY')

        
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
        
    )
    return response

if __name__ == '__main__':
    update_response = update_movie(
        "The Big New Movie", 2015, 5.5, "Everything happens all at ones.",
        ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)
