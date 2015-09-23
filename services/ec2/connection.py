#!/usr/bin/env python
import boto
import boto.ec2
import boto.vpc
import launch
def connect_region():
    regions = (
        'ap-northeast-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'eu-central-1',
        'eu-west-1',
        'sa-east-1',
        'us-east-1',
        'us-west-1',
        'us-west-2' )
    for i,j in enumerate(regions):
        print `i+1`+'.'+j
    vpc_region_input = int(raw_input("[enter a region to connect to]:"))
    print "connecting..."
    for i,j in enumerate(regions):
        if i+1 == vpc_region_input:
            selected_vpc_region = j
            break
        #else:
        #    print "wrong input, try again"
        #    connect_region()

    vpc_region = boto.vpc.connect_to_region(selected_vpc_region)
    print "you have successfully landed in " + selected_vpc_region

    vpc_services = {
            'Launch Instance': launch.run
            #'Stop Instance': stop
            }
    for i,j in enumerate(vpc_services):
        print `i+1`+'.'+j
    vpc_service_input = int(raw_input("[type any one of the above services]:"))

    for i,j in enumerate(vpc_services):
        if i+1 == vpc_service_input:
            vpc_services[j](selected_vpc_region)
            break
        else:
            print "wrong input"
