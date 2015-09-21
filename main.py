#!/usr/bin/env python
from services.ec2 import connection
print "service intializing...\ntype in any service of the following:"
aws_services=('ec2','s3', 'vpc')
for i in aws_services:
    print i
user_input()
def user_input():
    service_input=raw_input()
    if service_input is 'ec2':
        connection.connect_region()
    elif service_input is 's3':
        s3_fun()
    else:
        print "don't just fool around! Enter a valid service"
        user_input()
