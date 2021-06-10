import json
import boto3
import requests
import shutil
from time import sleep

def lambda_handler(event, context):
    pokedex_number = str(event['PokedexEntry'])
    s3_client = boto3.client('s3')
    sleep(10)
    r = requests.get(f'https://pokeres.bastionbot.org/images/pokemon/{pokedex_number}.png').content
    with open(f'/tmp/{pokedex_number}.png', 'wb') as f:
        f.write(r) 
    s3_client.upload_file(f'/tmp/{pokedex_number}.png', 'bucket-do-roni-pokemon-pics', f'images/{pokedex_number}/{pokedex_number}.png')
