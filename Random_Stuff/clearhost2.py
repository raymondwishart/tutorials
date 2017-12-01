#! /usr/local/bin/python
import getpass

# Created by Harley Hopkings
# Modified by Ray Wishart 12/1/2017, no more blanks lines

# Asks user for line number then converts the string to an integer

linedel = input("Enter Offending Line Number:")

linedel = int(linedel)


# Gets the username to apply to the filename

user = getpass.getuser()

# Creates filename variable containing the path to known_hosts with username inserted in between


# # filename = "/usr/home/" + user + "/.ssh/known_hosts"
filename = "/home/" + user + "/.ssh/known_hosts"

with open(filename, 'r') as textobj:
    list = list(textobj)
del list[linedel - 1]  # to compisate for list starting at 0

with open(filename, 'w') as textobj:
    for n in list:
        textobj.write(n)
