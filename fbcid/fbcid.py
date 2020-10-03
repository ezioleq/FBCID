#!/usr/bin/env python
"""Program entrypoint"""

import sys
from getpass import getpass
from fbchat import Client
from fbchat.models import FBchatException
from utils import print_logo

print_logo()

EMAIL = str(input("Email: "))
PASSWD = getpass("Password: ")

print("Logging in...")

try:
    CLIENT = Client(EMAIL, PASSWD, max_tries=3, logging_level=50)
except FBchatException as exception:
    print("An error occurred while logging to Facebook account:\n", exception)
    sys.exit(1)

if CLIENT is not None and CLIENT.isLoggedIn():
    USER = CLIENT.fetchUserInfo(CLIENT.uid)
    print("Welcome {}! Select thread to download from:".format(USER[CLIENT.uid].first_name))
    
    # List threads
    # Download all attachments

CLIENT.logout()
