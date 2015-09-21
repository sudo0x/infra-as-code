#!/usr/bin/env python
import boto
import boto.ec2
import boto.vpc
import launch
import stop
def connect_region():
    print "enter a region to connect to"
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
    for i in regions:
        print i
    vpc_region_input = raw_input()
    print "connecting..."
    if vpc_region_input in regions:
        vpc_region = boto.vpc.connect_to_region(vpc_region_input)
        print "you've successfully landed in" + vpc_region_input
    else:
        print "Invalid region. Try again."
        connect_region()
    print "What to do..type any one of the following"
    vpc_services = (
            'Launch Instance',
            'Stop Instance')
    for j in vpc_services:
        print j
    vpc_service_input = raw_input()
    while True:
        if vpc_service_input in vpc_services[0]:
            launch(vpc_region)
            break
        elif vpc_service_input in vpc_services[1]:
            stop()
            break
        else:
            print "wrong input, try again."
            vpc_service_input=raw_input()
