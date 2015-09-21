#!/usr/bin/env python
print "Choose an Amazon Machin Image (AMI)"
ami = (
       'ami-d44b4286',      # Amazon Linux AMI 2015.03.1 (HVM), SSD Volume Type
       'ami-dc1c2b8e',      # Red Hat Enterprise Linux 7.1 (HVM), SSD Volume Type
       'ami-96f1c1c4' )     # Ubuntu Server 14.04 LTS (HVM), SSD Volume Type

instance_types = (
                't2.micro',
                't2.small' )
vpcop_dic={}  #output dic for user to select vpc
vpc_dic={}   #dic with vpc name as keys and id as values
subop_dic={}  #output dic for user to select subnet
sub_dic={}    #dic with subnet name as keys and id as values

#vpc selection

vpc_input = int(raw_input("Which VPC would you like to launch instance in?\n"))
vpcs = vpc_region.get_all_vpcs()
for n,vpcid in enumerate(vpcs):
    print `n+1`+'.'+vpcid.tags['Name']
    vpcop_dic.update({n+1:str(vpcid.tags['Name'])})
    vpc_dic.update({str(vpcid.tags['Name']):str(vpcid.id)})


for inp in vpcop_dic.keys():
    if inp == vpc_input:
        selected_vpc = vpcop_dic[inp]
        selected_vpc_id = vpc_dic[selected_vpc]

subnet_input = raw_input("select subnet of " + selected_vpc + "\n")

#subnet selection

subnets = vpc_region.get_all_subnets(filters=[('vpc-id',[selected_vpc_id])])

for n, subid in enumerate(subnets):
    print `n+1`+'.'+subid.tags['Name']
    subop_dic.update({n+1:str(subid.tags['Name'])})
    sub_dic.update({str(subid.tags['Name']):str(subid.id)})

for inp in subop_dic.keys():
    if inp == subnet_input:
        selected_subnet = subop_dic[inp]
        selected_subnet_id = sub_dic[selected_subnet]
