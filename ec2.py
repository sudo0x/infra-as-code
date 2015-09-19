#!/usr/bin/env python
def services():
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
    region_input = raw_input()
    print "connecting..."
    if region_input in regions:
        ec2 = boto.ec2.connect_to_region(region_input)
        print "you've successfully landed in" + region_input
    else:
        print "Invalid region. Try again."
        ec2_fun()
    print "What to do..type any one of the following"
    ec2_services = (
            'Launch Instance',
            'Stop Instance')
    for j in ec2_services:
        print j
    ec2_service_input = raw_input()
    while True:
        if ec2_service_input in ec2_services[0]:
            ec2_launch()
            break
        elif ec2_service_input in ec2_services[1]:
            ec2_stop()
            break
        else:
            print "wrong input, try again."
            ec2_service_input=raw_input()
