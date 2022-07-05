# Live (Event) Net Planner

Quick little piece of software that'll help you plan multi-router networks. 

## Setup

```bash
# Set up the python3 environment
python3 -m venv .env
source .env/bin/activate
```

## Software Execution

You can run this software like so:

```bash
# Help Documentation
$ python livenetplanner.py -h
usage: livenetplanner.py [-h] --rack-id RACKID [--idf-count IDFCOUNT] [--vlans VLANCOUNT] [--debug]

Sets up your homelab environment with Bolt

optional arguments:
  -h, --help            show this help message and exit
  --rack-id RACKID, -r RACKID
                        Defines the ID of your Rack.
  --idf-count IDFCOUNT, -i IDFCOUNT
                        Defines the number of IDF Cabinets.
  --vlans VLANCOUNT, -v VLANCOUNT
                        Defines the number of VLANs to generate per router.
  --debug               Enables Debug

# Execution (Example A)
python livenetplanner.py --rack-id 10 --idf-count 2 --vlans 10

# Execution (Example B)
python livenetplanner.py -r10 -i2 -v10
```

## CSV Output

Finally, you'll be able to open the CSV output in whatever tool you want to get the output of your described subnets.
