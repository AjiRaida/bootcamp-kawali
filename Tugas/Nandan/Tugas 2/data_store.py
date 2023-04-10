import json
def write_file(file, data):
    json_data = json.dumps(data)
    f = open(file, 'w')
    f.write(json_data)
    f.close()
    return True
    
def read_file(file, mode='r'):
    f = open(file, mode=mode)
    json_data = f.read()
    json_data = json.loads(json_data)
    f.close()
    return json_data