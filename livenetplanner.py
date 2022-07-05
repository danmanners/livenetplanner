import argparse
import sys
from functions.tools import checkFileStatus

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

# Determines if Debug is enabled or not
parser.add_argument(
    "--debug", default=False,
    action="store_true", help="Enables Debug"
)

# Parse all of the arguments.
args = parser.parse_args()


# If the main program
if __name__ == "__main__":
    try:
        checkFileStatus(args)
    except (KeyboardInterrupt):
        print("\nKeyboard Interrupt detected! Closing program.")
        sys.exit(1)
