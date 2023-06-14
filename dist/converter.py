import os
import xmltodict
import json
import yaml
from sys import argv

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError:
        raise IOError(f"Unable to read file: {file_path}")

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError:
        raise IOError(f"Unable to write file: {file_path}")

def convert_data(input_file, output_file):
    _, input_extension = os.path.splitext(input_file)
    _, output_extension = os.path.splitext(output_file)

    data = read_file(input_file)

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
    else:
        raise ValueError(f"Unsupported file format: {input_extension}")

    write_file(output_file, converted_data)

if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: program.exe input_file output_file')
    else:
        input_file = argv[1]
        output_file = argv[2]
        try:
            convert_data(input_file, output_file)
            print("Conversion successful!")
        except (IOError, ValueError) as e:
            print(f"Error: {str(e)}")
