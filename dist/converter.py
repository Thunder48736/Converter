import sys
import os
import xmltodict
import json
import yaml

def convert_data(input_file, output_file):
    _, input_extension = os.path.splitext(input_file)
    _, output_extension = os.path.splitext(output_file)

    with open(input_file, 'r') as file:
        data = file.read()

    if input_extension == '.xml':
        if output_extension == '.json':
            converted_data = json.dumps(xmltodict.parse(data), indent=4)
        elif output_extension == '.yaml':
            converted_data = yaml.dump(xmltodict.parse(data), indent=4)
    elif input_extension == '.json':
        if output_extension == '.xml':
            converted_data = xmltodict.unparse(json.loads(data), pretty=True)
        elif output_extension == '.yaml':
            converted_data = yaml.dump(json.loads(data), indent=4)
    elif input_extension == '.yaml' or input_extension == '.yml':
        if output_extension == '.xml':
            converted_data = xmltodict.unparse(yaml.safe_load(data), pretty=True)
        elif output_extension == '.json':
            converted_data = json.dumps(yaml.safe_load(data), indent=4)

    with open(output_file, 'w') as file:
        file.write(converted_data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: program.exe input_file output_file')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_data(input_file, output_file)
