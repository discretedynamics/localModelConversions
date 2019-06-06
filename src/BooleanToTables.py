#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import itertools

def find_all_indices(array,el):
    res=[]
    for i,a in enumerate(array):
        if a==el:
            res.append(i)
    if res==[]:
        raise ValueError('The element is not in the array at all')
    return res

#input_filename = '../algorun_info/input_example/localModelBoolean.txt'
#output_filename = '../algorun_info/output_example/localModelTables.txt'

input_filename = sys.argv[1]
output_filename = 'localModelTables.txt'

f = open(input_filename,'r')
json_data = f.read()
f.close()
json_data = json.loads(json_data)

original_not = 'NOT'
original_and = 'AND'
original_or = 'OR'
new_not = '~'
new_and = '&'
new_or = '|'

n_variables = len(json_data['variableNames'])

#dict_numStates_per_variable = dict(zip(json_data['variableNames'],json_data['numberOfStates']))
dict_variable_to_index = dict(zip(json_data['variableNames'],range(n_variables)))

dict_variables = dict({original_not:new_not,original_and:new_and,original_or:new_or})
dict_variables.update(dict(list(zip(json_data['variableNames'],["x[%i]" % i for i in range(n_variables)]))))

json_data['type'] = 'localModelTables'
for i in range(n_variables):
    rule = json_data['updateRules'][i].pop('booleanFunction')
    rule = rule.replace('(',' ( ').replace(')',' ) ')#.replace('  ',' ').strip(' ')
    dummy = rule.split(' ')
    for ii,el in enumerate(dummy):
        if el not in ['(',')', '',' ']:
            dummy[ii] = dict_variables[el]
    rule = ' '.join(dummy)
    
    indices_open = find_all_indices(rule,'[')
    indices_end = find_all_indices(rule,']')
    dummy = list(map(int,list(set([rule[(begin+1):end] for begin,end in zip(indices_open,indices_end)]))))
    dummy.sort()
    n_inputs = len(dummy)
    dict_dummy = dict(list(zip(dummy,list(range(n_inputs)))))
    for el in dummy:
        rule = rule.replace('[%i]' % el,'[%i]' % dict_dummy[el]) #needs to be done with an ascending order in dummy
    f = []
    for x in itertools.product([0, 1], repeat = n_inputs):
        f.append(eval(rule)) #x is used here "implicitly"
    json_data['updateRules'][i]['table'] = f

with open(output_filename, 'w') as outfile:  
    json.dump(json_data, outfile, indent=2)
