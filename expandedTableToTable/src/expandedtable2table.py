#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

#import file to json_data 
input_filename = sys.argv[1] 
f = open(input_filename,'r')
json_data = f.read()
f.close()
json_data = json.loads(json_data)

# Go through each updateRule, create the (condensed) table, and remove the expanded table
for i,elt in enumerate(json_data['updateRules']):
    current_table = []
    for row in json_data['updateRules'][i]['expandedTable']:
        current_table.append(row[1])
    json_data['updateRules'][i]['table'] = current_table 
    json_data['updateRules'][i].pop('expandedTable', None)
    
#print(json_data)

# write to output file
output_filename = 'table_outputfile.json'
with open(output_filename, 'w') as outfile:  
    json.dump(json_data, outfile, indent=4)
