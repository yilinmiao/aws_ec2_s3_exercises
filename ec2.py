import boto.ec2
conn = boto.ec2.connect_to_region('us-west-1')
# conn.stop_instances(instance_ids=['i-0ed9988f770a58b93'])
conn.start_instances(instance_ids=['i-0ed9988f770a58b93'])