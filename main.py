#!/usr/bin/env python
from services.ec2 import connection
print "service intializing...\ntype in any service of the following:"
aws_services={'ec2': connection.connect_region }

for i,j in enumerate(aws_services):
    print `i+1`+'.'+j
aws_service_input = int(raw_input())
for i,j in enumerate(aws_services):
    if i+1 == aws_service_input:
        aws_services[j]()
        break
    else:
        print "do nothing"
