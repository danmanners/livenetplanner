import argparse
import csv
import sys
import ipaddress
from tokenize import Number

parser = argparse.ArgumentParser(
    description="Sets up your homelab environment with Bolt"
)

# Set the Rack ID
parser.add_argument(
    "--rack-id", "-r", dest="rackId", type=int,
    help="Defines the ID of your Rack.",
)

# Set the IDF Count for the rack
parser.add_argument(
    "--idf-count", "-i", dest="idfCount", type=int,
    help="Defines the number of IDF Cabinets."
)

# Define the number of default VLANs
parser.add_argument(
    "--vlans", "-v", dest="vlanCount", type=int,
    help="Defines the number of VLANs to generate per router."
)

# Parses all of your args.
args = parser.parse_args()

try:
    # Validate the Arguments


except (KeyboardInterrupt, SystemExit):
    print("\nKeyboard Interrupt detected! Closing program.")
    sys.exit(1)
