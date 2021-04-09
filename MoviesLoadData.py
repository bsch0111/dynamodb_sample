from decimal import Decimal
import json
import boto3

def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000" \
        , region_name = 'eu-west-1',aws_access_key_id='DUMMYIDEXAMPLE', aws_secret_access_key='DUMMYEXAMPLEKEY')

        table = dynamodb.Table('Movies')
        for movie in movies:
            year = int(movie['year'])
            title = movie['title']
            print("Adding movie:",year,title)
            table.put_item(Item=movie)

if __name__ == '__main__':
    with open("moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)
