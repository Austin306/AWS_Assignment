import boto3,json
def main():
	iam=boto3.client('iam')
	ec2=boto3.client('ec2',region_name="us-east-1")
	ec2_instance=''
	path='/'
	ProfileName=""
	RoleName=""
	description="testing boto3"
	trust_policy={
  	"Version": "2012-10-17",
  	"Statement": [
    	{
      	"Sid": "createRole",
      	"Effect": "Allow",
      	"Principal": {
        	"Service": "ec2.amazonaws.com"
      	},
      	"Action": "sts:AssumeRole"
    	}
 	 ]
	}
	tags=[
    	{
        	'Key': '',
        	'Value': ''
    	}
	]
	try:
    		
    		#creating a role
    		response = iam.create_role(
        		Path=path,
        		RoleName=RoleName,
        		AssumeRolePolicyDocument=json.dumps(trust_policy),
        		Description=description,
        		MaxSessionDuration=3600,
        		Tags=tags
    		)

    		print(response)
		#creating a policy

        	policyDoc={"Version": "2012-10-17",
    		"Statement": [
       			{
       	    		"Effect": "Allow",
       	    		"Action": "s3:*",
       	    		"Resource": "*"
        		}
    			]
   	
        		}
        	policy= iam.create_policy( PolicyName="s3_Full_access2",PolicyDocument=json.dumps(policyDoc) )
       		attaching_policy=iam.attach_role_policy(RoleName=RoleName,PolicyArn=policy['Policy']['Arn'])
		#creating profile instance
		instance_profile= iam.create_instance_profile( InstanceProfileName=ProfileName, Path=path)
		#attach role to instance
		response= iam.add_role_to_instance_profile(InstanceProfileName=ProfileName,RoleName=RoleName)
		associate=ec2.describe_iam_instance_profile_associations(Filters=[{'Name': 'instance-id','Values': [ec2_instance,]}])
		#Associating instance profile with ec2
		AssociationId=associate['IamInstanceProfileAssociations'][0]['AssociationId']
		print(instance_profile)
		res =ec2.replace_iam_instance_profile_association(
    		IamInstanceProfile={
        		'Arn': instance_profile['InstanceProfile']['Arn'],# place your arn instance_profile here 
        		'Name': ProfileName
    		},
    		AssociationId=AssociationId
		)
	except Exception as e:
        print("Error")
        raise e
if __name__=='__main__':
        main()
