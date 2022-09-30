export ISENGARD_PRODUCTION_ACCOUNT=false
export AWS_ACCESS_KEY_ID=ASIA4DLSJ2EKTTSASCUT
export AWS_SECRET_ACCESS_KEY=nl9lSvcPfBxCiKFQNsEsjBxFDPlhxIQE9a2wq4gb
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEFYaCXVzLWVhc3QtMSJGMEQCIE1u18S3TzacuCN7pLh4zh9/lY5hEoTnvr7wbSssxIJLAiAktUi6ZbKBpTsgKbQq2vCeAhJ/ia8FMX9I6oQy1ml+QCqnAgjP//////////8BEAIaDDgzMTg1Mjc2MTM2NSIMikllcS1UCz9fDqmGKvsBT72DWkdh+gt+bzqmka5mHN/bOZ8bUdGDXONxQmRHvtW583kdQRNRir0SFoObiO/d0oA8evu8kov27jn3Avw9rIuhLmYRWR1pKgKMx3ZiAwAD3J2gH9tlgGS8FHCd/QX7SizI4g2oh4QVhCIngkoHu1t1W19tavTMGad75lAPfM2JN5TMVzHg4fnHeqKkLIpKMiRBbyjGD58vkcKAFtxrGQRxeDB7v3lu7/UgBtnvbwVK3Zgk698cWIVrwOGM9cBPPiTYLfTzQ5iIoIhuAvjj5cc19B1MA//aOBzGQry0F0WYN5iM4VrCOF+LaqZVRfFRIGIwN+y5G7v4hB0w77WhmAY6ngEHgUCvPFFVOENBXmV3cM4IgT1c1HELgLFItcJDf3dGp9t1vk2ub6nop6PRFkok0OSuN3fRG231UISM6X6SM9TprdxDD1lfKh63aDR9f5tSV43PEy8N9abcbINlmSlE6jcghra8hH1Jvl47uE3Nebioj2k575kK1AyYXpqD2RM+/EOOg1hUYHHrtbvsYbSMGWtL6WmWsQqxaD4gMMQCzA==

#aws ec2 describe-instances --filters  "Name=tag:Name,Values=Dopamine_2" "Name=key-name,Values=mirror_cali" "Name=instance-state-name,Values=running" --region us-west-1  --query 'Reservations[].Instances[].PublicDnsName'
#aws ec2 describe-instances --filters  "Name=tag:Name,Values=Dopamine" "Name=key-name,Values=mirror_cali" "Name=instance-state-name,Values=running" --region us-west-1  --query 'Reservations[].Instances[].PublicDnsName'
aws ec2 describe-instances --filters  "Name=key-name,Values=mirror_cali" "Name=instance-state-name,Values=running" --region us-west-1  --query 'Reservations[].Instances[].PublicDnsName'
#aws ec2 describe-instances --filters  "Name=tag:Name,Values=Dopamine_3" "Name=key-name,Values=mirror_cali" "Name=instance-state-name,Values=running" --region us-west-1  --query 'Reservations[].Instances[].PublicDnsName'



