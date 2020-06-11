import json
import re
import sys
_input_file=sys.argv[1]
_type=sys.argv[2]
_output_file=sys.argv[3]
with open(_input_file) as f:
    data=json.load(f)
print(len(data))
import os
def converter(_id,_type):
    di={}
    di={"index":{}}
    di["index"]["_type"]=_type
    di["index"]["_id"]=int(str(_id).strip())
    return(di,data[str(_id+1)])
for i in  range(len(data)):
    meta,record=converter(i,_type)
    #raw_record=meta  "+str(record)
    #meta_record=raw_record
    #meta_record+="\n"
    try:
        with open(_output_file,"a") as fp:    
            fp.write(json.dumps(meta))
            fp.write("\n")
            fp.write(json.dumps(record))
            fp.write("\n")

        
    except:
        with open(_output_file,"w") as fp:
            fp.write(json.dumps(meta))
            fp.write("\n")
            fp.write(json.dumps(record))
            fp.write("\n")
