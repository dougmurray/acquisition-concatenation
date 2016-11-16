# acquisition-concatenation.py
#!usr/bin/env python27
import csv
"""Script to help Urna with tedious work.

   Author:  Douglass Murray
   Date:  2016-11-14
"""

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

# Simple finder helper function
def matched_entity_finder(data_list):
    """Looks at csv data and finds all entites that have the same company name.

        Args:
            data_list: list structured as [company, PICK, attribute1, ...]
        Returns:
            matched_items: list with the indexes of the same company attribute
    """
    matched_items = []
    check_element = data_list[0][1]
    for i, element in enumerate(data_list):
        for j, sub_element in enumerate(element):
            if sub_element == check_element:
                print("%s in %s" % (check_element, element))
                matched_items.append(i)
            else:
                # print("BOO: %s" % j)
                None
    print(matched_items)
    return matched_items

# to_be_picked = main_termina()
to_be_picked = "acquisition-concatenation-test"
usr_picked_csv = "%s.csv" % to_be_picked

csv_file_data = []
with open(usr_picked_csv, 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		csv_file_data.append(row)

# print(csv_file_data[1][1])
print(csv_file_data)

matching_entities = matched_entity_finder(csv_file_data)

# To run in terminal session
# if __name__ == '__main__':
    # from frontend.runner import *

