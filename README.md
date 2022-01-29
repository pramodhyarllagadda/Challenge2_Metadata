# Challenge2_Metadata


Below are the tests and outputs. Executed from a baston host on my personal AWS Account.


[root@ip-172-31-86-59 source]# python3 metadata.py
{
    "meta-data": {
        "ami-id": "ami-08e4e35cccc6189f4",
        "ami-launch-index": 0,
        "ami-manifest-path": "(unknown)",
        "block-device-mapping": {
            "ami": "/dev/xvda",
            "root": "/dev/xvda"
        },
        "events": {
            "maintenance": {
                "history": [],
                "scheduled": []
            }
        },
        "hibernation": {
            "configured": false
        },
        "hostname": "ip-172-31-86-59.ec2.internal",
        "identity-credentials": {
            "ec2": {
                "info": {
                    "AccountId": "192555343051",
                    "Code": "Success",
                    "LastUpdated": "2022-01-28T23:51:24Z"
                },
                "security-credentials": {
                    "ec2-instance": {
                        "AccessKeyId": "ASIASZVJRLTF5ZHI63MP",
                        "Code": "Success",
                        "Expiration": "2022-01-29T06:03:21Z",
                        "LastUpdated": "2022-01-28T23:52:34Z",
                        "SecretAccessKey": "/emURxrVLG0VQYQv5oIKpim/vQ1QB1BzIMioh1BD",
                        "Token": "IQoJb3JpZ2luX2VjELj//////////wEaCXVzLWVhc3QtMSJHMEUCIDWqTmRoSz1/d1PCMsg6AntVqJaNWh1SaMavB3xlLJQyAiEA8VQeslf1g9ffghmMy6NTIbozRgIzH+zFf9ryJdAKbuwq2QMI4f//////////ARAAGgwxOTI1NTUzNDMwNTEiDNHoyRDNxqBHpuJcqiqtA9a5+KMII1fBHet/6sNiI+igdbx81PriWMYCf1xwNNL+kIDbA7aig6cGqaz7SqAJZPVSRmvssemWyDkMlkDCX2Hcx2YqMpnxnwuc6tssjUjwaV+qgj7nLdFOWsl0m5BF87GRk1fL1iz3dMuJxDnXUmVwTApuiGOa1AWUqn4gszMZAE+xyTE5w2glJHX7lBy98N4nrVYqgnkQZgBbE0pxo0awaf34DQnDrGOA+dFvxN95U4ddk38GdV2s9dcJhaQJEvESrCejVJfqR2kmmgnpEKweotbK2hgrZcKtPDxVNXj3B13AIaVxqU233g5S1Mw9XGWW8RZX/oPR79G6CogYH+rmRYY2J6lKEqtFPuHNaiNBJgbeKD+a/69RTOfB/vopzGVPtqIQE0N75Ung78FNVFJyr2tBkLAwINvaifn49IcC7ZJXoTGemMpyCrbNTS/dPpGCGURRyMJGbXIUcD4Gx7bXVBn8jaf9lFbb3BaDA+OMgT6VOmWpqcjzTRwZeqwBV0TYK7FgPzBDzRXon6b2h8ak9CDPfGxVWZI3Py5E5CupIzn48LOFAzzHGfBiwzCqg9KPBjqLAqYjqScBRTy8v21KoiMg/vzQJRGH7OkLSARLJufTdKA70avWvebIW+iU2pl3Q1rVhUqWHpurMp8jdP9bxa+vmBzmBLiTinFRVCBgG7s4NY+M2sE2gjH4XT1EtbJmM4ydg7XOSGNhrWowZBiJzHopxM60wqB65Ffl7l/d/Dne9Fnuj+cVpTGwiVSrGzj2KEPOqHFI/5aMPtzNxXDb6l3btLlQdZGFokNGcbywdJOhhNyhAFQLEDL0wIZ7KxunXKZLiTzFMqf30Ce4NeSlYKpaUSpkmo3dlS5V4NQ9pp3PChMerakK3B46SnvzIV0lZLb9VVvyKAr+Awaf3ggCLYgKeWmwKSdieY1lbgv69Q==",
                        "Type": "AWS-HMAC"
                    }
                }
            }
        },
        "instance-action": "none",
        "instance-id": "i-068c89b58535ed6cb",
        "instance-life-cycle": "on-demand",
        "instance-type": "t2.micro",
        "local-hostname": "ip-172-31-86-59.ec2.internal",
        "local-ipv4": "172.31.86.59",
        "mac": "12:7d:19:c7:ca:db",
        "metrics": {
            "vhostmd": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        },
        "network": {
            "interfaces": {
                "macs": {
                    "12:7d:19:c7:ca:db": {
                        "device-number": 0,
                        "interface-id": "eni-01a2e494b69a0bec5",
                        "ipv4-associations": {
                            "3.95.13.252": "172.31.86.59"
                        },
                        "local-hostname": "ip-172-31-86-59.ec2.internal",
                        "local-ipv4s": "172.31.86.59",
                        "mac": "12:7d:19:c7:ca:db",
                        "owner-id": 192555343051,
                        "public-hostname": "ec2-3-95-13-252.compute-1.amazonaws.com",
                        "public-ipv4s": "3.95.13.252",
                        "security-group-ids": "sg-00721af2ffbfb8825",
                        "security-groups": "launch-wizard-1",
                        "subnet-id": "subnet-0862054c497ef1844",
                        "subnet-ipv4-cidr-block": "172.31.80.0/20",
                        "vpc-id": "vpc-031a71149569293dc",
                        "vpc-ipv4-cidr-block": "172.31.0.0/16",
                        "vpc-ipv4-cidr-blocks": "172.31.0.0/16"
                    }
                }
            }
        },
        "placement": {
            "availability-zone": "us-east-1d",
            "availability-zone-id": "use1-az2",
            "region": "us-east-1"
        },
        "profile": "default-hvm",
        "public-hostname": "ec2-3-95-13-252.compute-1.amazonaws.com",
        "public-ipv4": "3.95.13.252",
        "public-keys": {
            "0=Access_Server": "<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\"\n\t\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\n <head>\n  <title>404 - Not Found</title>\n </head>\n <body>\n  <h1>404 - Not Found</h1>\n </body>\n</html>\n"
        },
        "reservation-id": "r-078ef3b53ad4eca26",
        "security-groups": "launch-wizard-1",
        "services": {
            "domain": "amazonaws.com",
            "partition": "aws"
        }
    }
}
[root@ip-172-31-86-59 source]# python3 querymetadata.py
Enter the key name to get the value
ami-id
['ami-08e4e35cccc6189f4']
[root@ip-172-31-86-59 source]# python3 querymetadata.py
Enter the key name to get the value
vpc-id
['vpc-031a71149569293dc']
[root@ip-172-31-86-59 source]# python3 querymetadata.py
Enter the key name to get the value
instace-id
[]
[root@ip-172-31-86-59 source]# python3 querymetadata.py
Enter the key name to get the value
network
[{'interfaces': {'macs': {'12:7d:19:c7:ca:db': {'device-number': 0, 'interface-id': 'eni-01a2e494b69a0bec5', 'ipv4-associations': {'3.95.13.252': '172.31.86.59'}, 'local-hostname': 'ip-172-31-86-59.ec2.internal', 'local-ipv4s': '172.31.86.59', 'mac': '12:7d:19:c7:ca:db', 'owner-id': 192555343051, 'public-hostname': 'ec2-3-95-13-252.compute-1.amazonaws.com', 'public-ipv4s': '3.95.13.252', 'security-group-ids': 'sg-00721af2ffbfb8825', 'security-groups': 'launch-wizard-1', 'subnet-id': 'subnet-0862054c497ef1844', 'subnet-ipv4-cidr-block': '172.31.80.0/20', 'vpc-id': 'vpc-031a71149569293dc', 'vpc-ipv4-cidr-block': '172.31.0.0/16', 'vpc-ipv4-cidr-blocks': '172.31.0.0/16'}}}}]
[root@ip-172-31-86-59 source]# python3 querymetadata.py
Enter the key name to get the value
public-keys
[{'0=Access_Server': '<?xml version="1.0" encoding="iso-8859-1"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n\t"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n <head>\n  <title>404 - Not Found</title>\n </head>\n <body>\n  <h1>404 - Not Found</h1>\n </body>\n</html>\n'}]
[root@ip-172-31-86-59 source]#
