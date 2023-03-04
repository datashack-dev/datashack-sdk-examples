import json
import boto3

kinesis_client = boto3.client('kinesis')
new_dict = {"c1": "123", "c2": "123", "c3": "123"}
for i in range(5):
    kinesis_client.put_record(StreamName="datashack-test-db_table_test_one", Data=json.dumps(new_dict), PartitionKey="c3")
