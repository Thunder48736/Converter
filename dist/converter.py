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

    import os
    import xmltodict
    import json
    import yaml
    import sys

    def convert_data(input_file, output_file):
        _, input_extension = os.path.splitext(input_file)
        _, output_extension = os.path.splitext(output_file)

        if input_extension == '.xml':
            with open(input_file, 'r') as file:
                data = file.read()
            converted_data = convert_from_xml(data, output_extension)
        elif input_extension == '.json':
            with open(input_file, 'r') as file:
                data = json.load(file)
            converted_data = convert_from_json(data, output_extension)
        elif input_extension == '.yaml' or input_extension == '.yml':
            with open(input_file, 'r') as file:
                data = yaml.safe_load(file)
            converted_data = convert_from_yaml(data, output_extension)
        else:
            print("Unsupported input file format.")
            return

        if converted_data is not None:
            with open(output_file, 'w') as file:
                file.write(converted_data)
            print("Conversion successful!")
        else:
            print("Conversion failed.")

    def convert_from_xml(data, output_extension):
        try:
            if output_extension == '.json':
                return json.dumps(xmltodict.parse(data), indent=4)
            elif output_extension == '.yaml':
                return yaml.dump(xmltodict.parse(data), indent=4)
            else:
                print("Unsupported output file format.")
                return None
        except Exception as e:
            print("Error converting from XML:", str(e))
            return None

    def convert_from_json(data, output_extension):
        try:
            if output_extension == '.xml':
                return xmltodict.unparse(data, pretty=True)
            elif output_extension == '.yaml':
                return yaml.dump(data, indent=4)
            else:
                print("Unsupported output file format.")
                return None
        except Exception as e:
            print("Error converting from JSON:", str(e))
            return None

    def convert_from_yaml(data, output_extension):
        try:
            if output_extension == '.xml':
                return xmltodict.unparse(data, pretty=True)
            elif output_extension == '.json':
                return json.dumps(data, indent=4)
            else:
                print("Unsupported output file format.")
                return None
        except Exception as e:
            print("Error converting from YAML:", str(e))
            return None

    if __name__ == '__main__':
        if len(sys.argv) != 3:
            print('Usage: program.py input_file output_file')
        else:
            input_file = sys.argv[1]
            output_file = sys.argv[2]
            convert_data(input_file, output_file)
