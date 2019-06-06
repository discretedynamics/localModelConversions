#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

#input_filename = '../algorun_info/input_example/localModelPolynomials.txt'
#output_filename = '../algorun_info/output_example/WiringDiagram.txt'

input_filename = sys.argv[1]
output_filename = 'WiringDiagram.txt'

f = open(input_filename,'r')
json_data = f.read()
f.close()
json_data = json.loads(json_data)

json_data['type'] = 'directedGraph'
json_data['edges'] = []
for el in json_data["updateRules"]:
    json_data['edges'].append({'node':el['node'], 'inputs':el['inputs']})

keys = list(json_data.keys())
for key in keys:
    if key not in ['type', 'name', 'description', 'edges']:
        json_data.pop(key)

with open(output_filename, 'w') as outfile:  
    json.dump(json_data, outfile, indent=2)
