import argparse
import csv
import sys
from os import path
import ipaddress
from tokenize import Number
from wsgiref import validate

parser = argparse.ArgumentParser(
    description="Sets up your homelab environment with Bolt"
)

# Set the Rack ID
parser.add_argument(
    "--rack-id", "-r", dest="rackId",
    type=int, required=True,
    help="Defines the ID of your Rack.",
)

# Set the IDF Count for the rack
parser.add_argument(
    "--idf-count", "-i", dest="idfCount",
    type=int, default=1,
    help="Defines the number of IDF Cabinets."
)

# Define the number of default VLANs
parser.add_argument(
    "--vlans", "-v", dest="vlanCount", type=int, default=0,
    help="Defines the number of VLANs to generate per router."
)

# Parses all of your args.
args = parser.parse_args()

# Generate the list of Default VLANs
# 101, 103 to 108, and 110 to 120
defaultVlans = [101, *range(103, 109), *range(110, 120)]

# Run through the codebase


def generateConfig():
    f = open(f'rack-{args.rackId}.csv', 'w')
    writer = csv.writer(f)
    header = ['Rack ID', 'VLAN ID', 'CIDR']

    # Write the header
    writer.writerow(header)

    # Loop through each IDF
    for idfIndex in range(1, args.idfCount+1, 1):
        if args.vlanCount == 0:
            for vlan in defaultVlans:
                row = [idfIndex, vlan, ]
                writer.writerow(row)
        elif args.vlanCount >= 1:
            extraVlans = [*range(121, args.vlanCount+121, 1)]
            vlans = [*defaultVlans, *extraVlans]
            for vlan in vlans:
                row = [idfIndex, vlan]
                writer.writerow(row)
    f.close()


def checkFileStatus():
    try:
        # Open the new CSV file
        if path.exists(f'rack-{args.rackId}.csv') is True:
            confirm = input(
                f"The file 'rack-{args.rackId}.csv' already exists. Do you wish to overwrite it? ")
            if confirm.casefold() in ['y', 'n', 'yes', 'no']:
                generateConfig()
            else:
                print('Not continuing at this time.')
                sys.exit(0)

    except (KeyboardInterrupt, SystemExit):
        print("\nKeyboard Interrupt detected! Closing program.")
        sys.exit(1)


if __name__ == "__main__":
    checkFileStatus()
