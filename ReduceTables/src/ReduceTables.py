#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

#input_filename = '../algorun_info/input_example/localModelTables.txt'
#output_filename = '../algorun_info/output_example/reducedTables.txt'

input_filename = sys.argv[1]
output_filename = 'reducedTables.txt'

def prod(vec):
    res = 1
    for el in vec:
        res *= el
    return res

def reduce_table(f,variable_names,numstates,degree):
    n_states = prod(numstates) #X.shape[0]
    i = 0
    while i<degree:
        prod_right = prod(numstates[i+1:])
        prod_current = prod_right * numstates[i]
        DEPENDS_ON_I = False
        for j in range(n_states):
            if j%prod_current//prod_right==0:
                if len(set([f[j+k*prod_right] for k in range(numstates[i])]))>1:
                    DEPENDS_ON_I = True
                    break
            else:
                continue
        if not DEPENDS_ON_I:
            f = [f[j] for j in range(n_states) if j%prod_current//prod_right==0]
            variable_names.pop(i)
            degree-=1
            n_states //= numstates.pop(i)
        else:
            i+=1
    return (f,variable_names,numstates,degree)

f = open(input_filename,'r')
json_data = f.read()
f.close()
json_data = json.loads(json_data)

n_variables = len(json_data['variableNames'])
dict_variable_to_index = dict(zip(json_data['variableNames'],range(n_variables)))

for i in range(n_variables):
    f = json_data['updateRules'][i]['table']
    variable_names = json_data['updateRules'][i]['inputs']
    numstates = [json_data['numberOfStates'][dict_variable_to_index[variable]] for variable in variable_names]
    degree = len(numstates)
    (reduced_f,new_inputs,_,new_degree) = reduce_table(f,variable_names,numstates,degree)
    if new_degree<degree:
        json_data['updateRules'][i]['table'] = reduced_f
        json_data['updateRules'][i]['inputs'] = new_inputs

with open(output_filename, 'w') as outfile:  
    json.dump(json_data, outfile, indent=2)