#!/usr/bin/env python 3

"""
This file converts specific sportdata into json files.
"""
import sys
import datetime
import json

# -----------------
lines = []
# Using a default date to filter out the entries which have an date error
data_raw = {
    "date": datetime.datetime(2000, 1, 1),
    "exercise": "",
    "sets": []
}

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()


# -----------------
# Create date
date_data = lines[0].strip().split('.')
date_created = datetime.datetime(
    int(date_data[2]), int(date_data[1]), int(date_data[0]))
data_raw["date"] = date_created.strftime('%d.%m.%Y %H:%M:%S')


# -----------------
# Append exercise
data_raw["exercise"] = lines[1]


# -----------------
# append sets
sets = []
for x in range(2, len(lines)):
    set = lines[x].strip().split(' ')
    temp_set = [int(set[0]), float(set[1])]
    sets.append(temp_set)
data_raw["sets"] = sets


json_object = json.dumps(data_raw)


# -----------------
# Output
print(lines)
print(data_raw)
print(json_object)


# -----------------
# Create JSON file
sys_argument = sys.argv[1].strip().split('.')
filename = sys_argument[0] + '.json'
filepath = 'data/' + filename

with open(filepath, 'w') as file:
    file.write(json_object)
