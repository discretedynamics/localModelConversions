#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

input_filename = sys.argv[1]
f = open(input_filename,'r')
json_data = f.read()
f.close()
json_data = json.loads(json_data)

try:
    name_of_graph = json_data["name"]
except KeyError:
    name_of_graph = 'no name provided'
    
n_variables = len(json_data['variableNames'])
    
output = '''MODEL NAME: %s
SIMULATION NAME: %s
NUMBER OF VARIABLES: %i
VARIABLE NAMES: %s
NUMBER OF STATES: %s
SPEED OF VARIABLES: %s

%s''' % (name_of_graph,'sim1',n_variables,' '.join(json_data['variableNames']),' '.join(map(str,json_data["numberOfStates"])),' '.join(['1' for _ in range(n_variables)]),'\n'.join(['f'+str(i+1)+' = '+json_data['updateRules'][i]['polynomial'] for i in range(n_variables)]))

with open('output.txt','w') as f: 
    f.write(output)
