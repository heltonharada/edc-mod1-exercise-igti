import boto3
import pandas as pd
import os

#criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

#subir dados enem 2019

s3_client.upload_file('enem2019/MICRODADOS_ENEM_2019.csv', 'datalake-helton-739010676765', 'raw-data/enem/ENEM_2019.csv')


# s3_client.download_file('datalake-helton-739010676765', 'raw-data/ITENS_PROVA_2020.csv', 'ITENS_PROVA_2020.csv')

# df = pd.read_csv('ITENS_PROVA_2020.csv')
# print(df)