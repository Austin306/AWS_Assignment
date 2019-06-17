import boto3
def main():
        client=boto3.client('s3')
        response= client.list_object_versions(Bucket="<bucket name>", Prefix="<file name>")
        for i in response["Versions"]:
                print(i)
                print("\n\n")
        target=response["Versions"][1]["VersionId"]
        print("VersionId:",target)
        object= client.download_file("<bucket name>","<target fle in bucket>","<destination file on local system>",ExtraArgs={'VersionId':target})
if __name__=='__main__':
        main()
