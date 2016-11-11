# urna.py
#!usr/bin/env python27
import csv
import scipy as sc

# Notes
 # First match rows with same 2nd column entites
    # take entities in 5th column of matched entities and add
        # if 5th cloumn entities are equal don't add 

# Function to run in terminal session
# def main_terminal():
    # """Runs general Terminal version of script.
    # """
    # print("Welcome to Urna's Program")
    # picked_file = str(raw_input("Pick file: "))
    # print("you entered", picked_file)
    # return picked_file

# to_be_picked = main_termina()
to_be_picked = "urna_test"
usr_picked_csv = "%s.csv" % to_be_picked

data_list = []
with open(usr_picked_csv, 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		data_list.append(row)

# print data_list[1][1]
print data_list

# match_me = []
# for i, element in enumerate(data_list):
    # match_me.append([i,element[1]])

# print match_me
# first_sub_match = match_me[0][1]
# print first_sub_match
total_checks = []
for i, element in enumerate(data_list):
    checker_value = data_list[i][1]
    print "checker_value: %s" % checker_value
    for j, sub_element in enumerate(data_list):
        if sub_element[1] == checker_value:
            print "FOUND, %s" % sub_element[5]
            total_checks.append([j, sub_element[1], sub_element[5]])
        else:
            print "NOT FOUND"
    else:
        print "FAILED"

print total_checks
# To run in terminal session
# if __name__ == '__main__':
    # from frontend.runner import *

"""
L = [a,b,c]
a = [1,2,3,4]
b = [5,2,6,7]
c = [12,14,17,18]

for i, element in L:
    tester = element[1]
    for j, element[1] == tester:
"""