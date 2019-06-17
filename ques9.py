import boto3
def main():
    client= boto3.resource('dynamodb', region_name='us-east-1')

    table = client.create_table(
        TableName='AustGames',
        KeySchema=[
            {
                'AttributeName': 'gid',
                'KeyType': 'HASH'  #Partition key
            },
        ],
        AttributeDefinitions=[

            {
                'AttributeName': 'gid',
                'AttributeType':'N'
            },


        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    
    )

    # inserting data into dynamodb

    table=client.Table("AustGames")

    response=table.put_item( Item={ 'gid':1, 'gname': "Mario", 'publisher':'nintando','rating': 20 , 'release_date' : '2001', 'genres': { 'info':""}
    })

    response1=table.put_item( Item={ 'gid':2, 'gname': "PubG", 'publisher':'Tencent','rating': 200 , 'release_date' : '2019', 'genres': { 'info':""}
    })
    response2=table.put_item( Item={ 'gid':3, 'gname': "Fifa19", 'publisher':'EA-Sports','rating': 20 , 'release_date' : '2019', 'genres': { 'info':" "}
    })

if __name__=='__main__':
    main()
