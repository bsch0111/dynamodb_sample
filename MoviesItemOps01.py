from pprint import pprint
import boto3

def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000',\
            region_name = 'eu-west-1',aws_access_key_id='DUMMYIDEXAMPLE', aws_secret_access_key='DUMMYEXAMPLEKEY')

    table = dynamodb.Table('Movies')
    response = table.put_item(
        Item={
            'year' : year,
            'title' : title,
            'info' : {
                'plot' : plot,
                'rating' : rating
            }
        }
    )
    return response

if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", 2015, \
        "Nothing Happens At All.", 0)
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)