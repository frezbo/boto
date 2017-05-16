#!/usr/bin/env python
""" Get the list of instance types in ec2 """
__author__ = 'Noel Georgi'
__email__ = 'noelgeorgi@frezbo.com'
__license__ = 'Apache 2.0'
__verison__ = '0.1.0'
__maintainer__ = 'Noel Georgi'

# Used to parse json and get the URL
import requests
# GitHub API
URL = 'https://api.github.com/repos/boto/botocore/contents/botocore/data/ec2'
# Get the response from api
RESPONSE = requests.get(URL).json()
# Get the length of the returned string
LENGTH = len(RESPONSE) - 1
# Generate the URL containing the list of ec2 instance types in JSON
JSON_URL = 'https://raw.githubusercontent.com/boto/botocore/develop/botocore/data/ec2/' + \
           RESPONSE[LENGTH]['name'] + "/" + 'service-2.json'
# Get the response from the JSON file
RESPONSE = requests.get(JSON_URL).json()
# Print the list of instance types
print RESPONSE['shapes']['InstanceType']['enum']

