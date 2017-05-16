#!/usr/bin/env python
""" Code to get the list of EBS optimized instances and its IOPS """
__author__ = 'Noel Georgi'
__email__ = 'noelgeorgi@frezbo.com'
__license__ = 'Apache 2.0'
__verison__ = '0.1.0'
__maintainer__ = 'Noel Georgi'

# importing python regex
import re
# importing requests for opening URL's
import requests
# importing third party library for parsing HTML
from bs4 import BeautifulSoup as soup
# dict to store the instance-type/IOPS key/value
DATA = {}
# URL which contains the list of EBS optimized instances
URL = 'http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html'
# Get the HTML response and pass to soup
RESPONSE = soup(requests.get(URL).text, 'html.parser')
# finding the second table in the HTML
TABLE_PARSED = RESPONSE.find_all('table')[1].find_all('tr')
# regex for getting instance type
REGEX_INSTANCE = re.compile(r'[a-z]{1}[0-9]{1}\.[0-9]{0,2}[a-z]{0,9}')
# regex for getting numbers above 2000
# kind of a dirty workaround, please feel free to fix this
REGEX_IOPS = re.compile(r'[2-9]{1,9}[0-9]{0,9}')
# iterating over the table that's parsed
for i in TABLE_PARSED:
    # iterating over the <td> tags
    for j in i.find_all('td'):
        # checking whether the ouput contains the instance-type regex and not none
        if REGEX_INSTANCE.search(str(j.find_all('code'))) is not None:
            # assigning the instance type to instance_type variable after regex
            instance_type = REGEX_INSTANCE.search(str(j.find_all('code'))).group(0)
        # checking whether the ouput contains the IOPS value regex and not none
        if REGEX_IOPS.search(str(j).replace(',', '')) is not None:
            # assigning the IOPS value to iops variable after regex
            iops = REGEX_IOPS.search(str(j).replace(',', '')).group(0)
            # adding the instance-type/IOPS key/value to the DATA dict
            DATA.update({instance_type:iops})
# Printing the DATA dict
print DATA

