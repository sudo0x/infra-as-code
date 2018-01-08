#!/usr/bin/env python
import boto
import boto.ec2
import boto.vpc
import time
#ami selection
def run(*args):
    vpc_region = boto.vpc.connect_to_region(args[0])
    ami = {
       'Amazon Linux AMI 2015.03.1 (HVM), SSD Volume Type':'ami-d44b4286',# Amazon Linux AMI 2015.03.1 (HVM), SSD Volume Type
       'Red Hat Enterprise Linux 7.1 (HVM), SSD Volume Type':'ami-dc1c2b8e',      # Red Hat Enterprise Linux 7.1 (HVM), SSD Volume Type
       'Ubuntu Server 14.04 LTS (HVM), SSD Volume Type':'ami-96f1c1c4'      # Ubuntu Server 14.04 LTS (HVM), SSD Volume Type
       }
    for n,keys in enumerate(ami.keys()):
        print `n+1`+'.'+keys
    ami_input = int(raw_input("Choose an Amazon Machine Image (AMI)\n"))

    for n,name in enumerate(ami.keys()):
        if n+1 == ami_input:
            selected_ami = ami[name]

#instance selection
    instance_types = (
                      't2.micro',
                      't2.small' )
    for n,inst in enumerate(instance_types):
        print `n+1`+'.'+inst
    instance_input = int(raw_input("select any one instance type\n"))
    for i,j in enumerate(instance_types):
        if i+1 == instance_input:
            selected_instance = j


    vpcop_dic={}  #output dic for user to select vpc
    vpc_dic={}   #dic with vpc name as keys and id as values
    subop_dic={}  #output dic for user to select subnet
    sub_dic={}    #dic with subnet name as keys and id as values

#vpc selection

    vpcs = vpc_region.get_all_vpcs()
    for n,vpcid in enumerate(vpcs):
        print `n+1`+'.'+vpcid.tags['Name']
        vpcop_dic.update({n+1:str(vpcid.tags['Name'])})
        vpc_dic.update({str(vpcid.tags['Name']):str(vpcid.id)})

    vpc_input = int(raw_input("Which VPC would you like to launch instance in?\n"))

    for inp in vpcop_dic.keys():
        if inp == vpc_input:
            selected_vpc = vpcop_dic[inp]
            selected_vpc_id = vpc_dic[selected_vpc]

#subnet selection

    subnets = vpc_region.get_all_subnets(filters=[('vpc-id',[selected_vpc_id])])
    for n, subid in enumerate(subnets):
        print `n+1`+'.'+subid.tags['Name']
        subop_dic.update({n+1:str(subid.tags['Name'])})
        sub_dic.update({str(subid.tags['Name']):str(subid.id)})

    subnet_input = int(raw_input("select subnet of " + selected_vpc + "\n"))

    for inp in subop_dic.keys():
        if inp == subnet_input:
            selected_subnet = subop_dic[inp]
            selected_subnet_id = sub_dic[selected_subnet]

#keypair

    keypair_input = str(raw_input("Do you want to create a new key pair for this instance? [y/n]\n"))
    if 'y' == keypair_input:
        keypair_name=str(raw_input("Type name of the key pair\n"))
        vpc_region.create_key_pair(keypair_name)
    elif 'n' == keypair_input:
        keypair_list=vpc_region.get_all_key_pairs()
        for n,name in enumerate(keypair_list):
            print `n+1`+'.'+`name`
        keypair_list_input = int(raw_input("select which key pair of the above to use?\n"))
        for n,name in enumerate(keypair_list):
            if n+1 == keypair_list_input:
                keypair_name = str(name.name)

#security group

    sg_input=str(raw_input("creating security group..\n[Enter name for security group]:"))
    sg_dscp=str(raw_input("[Description for the security group]:"))
    sg_name=vpc_region.create_security_group(name=sg_input, description=sg_dscp, vpc_id=selected_vpc_id)
    sg_id=str(sg_name.id)
    print "add inbound rules to the "+ sg_input +"security group:"
    ip_protocol=str(raw_input("ip protocol[tcp|udp|icmp]:"))
    from_port=int(raw_input("from port:"))
    to_port=int(raw_input("to port:"))
    cidr_ip=str(raw_input("cidr ip:"))
    sg_name.authorize(ip_protocol,from_port,to_port,cidr_ip)

#create EBS Volume

    ebsvol = boto.ec2.blockdevicemapping.EBSBlockDeviceType()
    ebsvol.size = int(raw_input("[size for the ebs in GB]:"))
    ebsvol.volume_type = 'gp2'
    bdm = boto.ec2.blockdevicemapping.BlockDeviceMapping()
    bdm['/dev/sda1'] = ebsvol

    instance_tag = str(raw_input("[add tag]:"))

    reservation = vpc_region.run_instances(image_id=selected_ami,
                                    instance_type=selected_instance,
                                    security_group_ids= [sg_id],
                                    subnet_id=selected_subnet_id,
                                    block_device_map=bdm
                                    )
    instance = reservation.instances[0]

    status = str(instance.update())
    while status == 'pending':
        time.sleep(10)
        status = str(instance.update())
    if status == 'running':
        instance.add_tag('Name', value=instance_tag)
        print 'New instance "' + instance.id + '" accessible at ' + str(instance.ip_address)
    else:
        print 'Instance status: ' + status
