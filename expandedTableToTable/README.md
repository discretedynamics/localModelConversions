This takes in a JSON file of a local model where the functions f1,...,fn are described as an "expanded table". It removes the "expandedTable" key from the updateRules within the JSON file, and replaces them with a "table" key. 

For example, f1 = x1 * x2 would be encoded in the input as:

"updateRules: {
    	      "node": "x1",
    	      "inputs": ["x1","x2"],
	      "expandedTable":
		 [
                 [[0,0],0],
                 [[0,1],0],
                 [[1,0],0],
                 [[1,1],1],
            	 ]
	       }


In the output JSON file, the above would be replaced by:


"updateRules: {
    	      "node": "x1",
    	      "inputs": ["x1","x2"],
	      "table": [0, 0, 0, 1]
	       }