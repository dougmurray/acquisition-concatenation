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
            data_list: list structured as [blah, company, attribute1, ...]
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

# Simple concatenate helper function
def concatenate_matched_entities_attributes(matched_entities):
    """Concatenates the 5th column attributes from the matched entities.

        Args:
            matched_entities: list with the indexes of matched entities
        Returns:
            element_to_add: string with concenated 5th column attributes
    """
    matched_attributes_to_add = []
    for i, element in enumerate(matched_entities):
        attribute_to_add = csv_file_data[element][5]
        # print(csv_file_data[element][5])
        matched_attributes_to_add.append(attribute_to_add)
    else:
        None
    
    element_to_add = str()
    for i, element in enumerate(matched_attributes_to_add):
        element_to_add += element + ' '
    else:
        None
    return element_to_add

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

fifth_column_concat_strings = concatenate_matched_entities_attributes(matching_entities)
print(fifth_column_concat_strings)

# Deletes 5th column elements in matched indexes and replaces with concat string
# TODO: make into function
for i, element in enumerate(matching_entities):
    del csv_file_data[element][5]
    csv_file_data[element].insert(5, fifth_column_concat_strings)

print(csv_file_data)
print("==============================")

# TODO: Make into function
# Look at first column, if # then delete all same with no number in 1st column
# Check if # in first column, if not label to be removed
for i, element in enumerate(matching_entities):
    if csv_file_data[element][0].isdigit():
        break
    else:
        # del csv_file_data[element]
        csv_file_data[element] = "REMOVE ME!"

# Remove labled entities
for i, element in enumerate(csv_file_data):
    if csv_file_data[i] == "REMOVE ME!":
        del csv_file_data[i]


print(csv_file_data)
print(csv_file_data[2][0])
# To run in terminal session
# if __name__ == '__main__':
    # from frontend.runner import *

