import csv
import sys
import ipaddress
from os import path


from values import defaultVlanSubnets, coreVlans, adminVlans, idfThirdOctet


# Calculate the number of usable IP Addresses in the Subnet
def calculateUsableAddresses(subnet):
    subnetMask = str(subnet).split('/')[1]
    return int(2**(32-int(subnetMask))) - 3 # High and Low Multicast and Gateway


# Globally Define the idfThirdOctet Variable
def incrementThirdOctet():
    global idfThirdOctet
    idfThirdOctet += 8
    return idfThirdOctet


# Generate the Subnet Calc
def genSubnet(rack, vlan, core=False, thirdOctet=None):
    if thirdOctet is not None:
        ipaddr = str(
            ipaddress.ip_network(
                f'10.{rack}.{thirdOctet}.0/{adminVlans[str(vlan)]["subnet"]}',
                False
            )
        )
        incrementThirdOctet()
        return ipaddr

    elif str(vlan) in list(adminVlans.keys()):
        ipaddr = str(
            ipaddress.ip_network(
                f'10.{rack}.{adminVlans[str(vlan)]["cidrBlock"]}.0/{adminVlans[str(vlan)]["subnet"]}',
                False
            )
        )
        adminVlans[str(vlan)].update({
            "cidrBlock": str(int(adminVlans[str(vlan)]['cidrBlock']) + 8)
        })
        return ipaddr

    elif vlan in list(defaultVlanSubnets.keys()):
        return str(
            ipaddress.ip_network(
                f'10.{vlan}.0.0/{defaultVlanSubnets[str(vlan)]}',
                False
            )
        )
    else:
        if vlan not in list(int(i) for i in defaultVlanSubnets.keys()):
            return ipaddress.ip_network(
                f'10.{vlan}.0.0/24',
                False
            )
        elif vlan in (list(int(i) for i in defaultVlanSubnets.keys())):
            return ipaddress.ip_network(
                f'10.{vlan}.0.0/{defaultVlanSubnets[str(vlan)]}',
                False
            )


# Generate and write the config file
def generateConfig(args, coreVlans, thirdOctet):
    f = open(f'rack-{args.rackId}.csv', 'w')
    writer = csv.writer(f)
    header = ['Rack ID', 'VLAN ID', 'CIDR', 'USABLE IPs']

    # Write the header
    writer.writerow(header)

    # Generate the Core
    if args.vlanCount == 0:
        vlans = sorted([*coreVlans, *list(
            int(i) for i in defaultVlanSubnets.keys()
        )])
        for vlan in vlans:
            subnet = genSubnet(args.rackId, vlan, True)
            row = ['core', vlan, subnet, calculateUsableAddresses(subnet)]
            writer.writerow(row)
    elif args.vlanCount >= 1:
        extraVlans = sorted([*range(121, args.vlanCount+121, 1)])
        vlans = sorted(
            [*coreVlans, *list(int(i) for i in defaultVlanSubnets.keys()), *extraVlans])
        for vlan in vlans:
            subnet = genSubnet(args.rackId, vlan, True)
            row = ['core', vlan, subnet, calculateUsableAddresses(subnet)]
            writer.writerow(row)

    # Loop through each IDF
    for idfIndex in range(1, args.idfCount+1, 1):
        # Create the management VLAN
        subnet = genSubnet(rack=args.rackId, vlan='101', core=True, thirdOctet=idfThirdOctet)
        row = [
            f'IDF-{idfIndex}',
            '101',
            subnet,
            calculateUsableAddresses(subnet)
        ]

        # Write the row
        writer.writerow(row)
        # Loop thorugh the rest of the VLANs
        if args.vlanCount == 0:
            for vlan in list(defaultVlanSubnets.keys()):
                subnet = genSubnet(idfIndex, vlan)
                row = [f'IDF-{idfIndex}', vlan, subnet, calculateUsableAddresses(subnet)]
                writer.writerow(row)
        elif args.vlanCount >= 1:
            extraVlans = sorted([*range(121, args.vlanCount+121, 1)])
            vlans = sorted([*list(int(i)
                                  for i in defaultVlanSubnets.keys()), *extraVlans])
            for vlan in vlans:
                subnet = genSubnet(idfIndex, vlan)
                row = [f'IDF-{idfIndex}', vlan, subnet, calculateUsableAddresses(subnet)]
                writer.writerow(row)
    f.close()


# Check if the file exists correctly
def checkFileStatus(args):
    # Open the new CSV file
    if path.exists(f'rack-{args.rackId}.csv') is True:
        confirm = input(
            f"The file 'rack-{args.rackId}.csv' already exists. Do you wish to overwrite it? ")
        if confirm.casefold() in ['y', 'yes']:
            generateConfig(args, coreVlans, thirdOctet=idfThirdOctet)
        else:
            print('Not continuing at this time.')
            sys.exit(0)
    else:
        generateConfig(args, coreVlans, thirdOctet=idfThirdOctet)
