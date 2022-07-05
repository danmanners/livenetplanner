# Core Network VLANs
# 1 to 3
coreVlans = [*range(1, 4)]

# Administrative VLANs
adminVlans = {
    "1": {
        "cidrBlock": "0",
        "subnet": "20"
    },
    "2": {
        "cidrBlock": "8",
        "subnet": "21",
    },
    "3": {
        "cidrBlock": "12",
        "subnet": "21"
    },
    "101": {
        "cidrBlock": "0",
        "subnet": "20"
    }
}


# IDF Starting Point for the Third Octet
idfThirdOctet = 16


# Default VLAN Subnets
defaultVlanSubnets = {
    "103": "24",
    "104": "24",
    "105": "24",
    "110": "22",
    "111": "22",
    "112": "22",
    "113": "21",
    "114": "24",
    "115": "24",
    "116": "22",
    "117": "22",
    "150": "24",
    "151": "23",
    "152": "23",
    "153": "23",
    "154": "23",
    "155": "23",
}
