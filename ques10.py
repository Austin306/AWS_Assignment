import boto3
from boto3.dynamodb.conditions import Key, Attr
def main():
        dynamodb =boto3.resource('dynamodb', region_name="us-east-1")
        table= dynamodb.Table("AustGames")
        response= table.query(KeyConditionExpression=Key('gid').eq(2))
        for i in response ['Items']:
                print("gname=",i["gname"],"rating=",i["rating"])

if __name__=='__main__':
        main()
