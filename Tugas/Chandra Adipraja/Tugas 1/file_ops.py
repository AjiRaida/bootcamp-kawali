import json

def write_to_file(file,data):
    json_string = json.dumps(data)

    f = open(file,'w')
    f.write(json_string)
    f.close

def read_file(file, mode = 'r'):
    try:
        f = open(file, mode=mode)
        json_string = f.read()
        json_dict = json.loads(json_string)
        f.close()
        return json_dict
    except:
        return False
    
