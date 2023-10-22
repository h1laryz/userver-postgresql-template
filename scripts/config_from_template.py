#!/usr/bin/env python3

import argparse
import ruamel.yaml
import os

def load_env_file(env_path):
    if env_path:
        with open(env_path, 'r') as env_file:
            env_data = ruamel.yaml.load(env_file, ruamel.yaml.RoundTripLoader)
        return env_data
    else:
        return {}

def process_yaml(data, env_data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = process_yaml(value, env_data)
        return data
    elif isinstance(data, str) and len(data) > 0 and data[0] == '$':
        return process_string(data, env_data)
    else:
        return data

def process_string(input_string, env_data):
    input_string = input_string[1:]

    if input_string not in env_data:
        env_value = os.getenv(input_string)
        if env_value is None:
            raise Exception(f"{input_string} is not defined.")
        return env_value

    return env_data[input_string]

def main():
    parser = argparse.ArgumentParser(description='Process YAML templates')
    parser.add_argument('-i', '--input', required=True, help='Path to the input template YAML file (file.py)')
    parser.add_argument('-o', '--output', required=True, help='Specify the output Python file and its location (e.g., -o /dir/output.py)')
    parser.add_argument('-e', '--env', help='Path to the environment YAML file (optional)')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    env_path = args.env

    if not input_path:
        parser.error('Parameter -i (--input) is required.')

    if not output_path:
        parser.error('Parameter -o (--output) is required.')

    try:
        with open(input_path, 'r') as input_file:
            template_data = ruamel.yaml.load(input_file, ruamel.yaml.RoundTripLoader)

        env_data = load_env_file(env_path)

        template_data = process_yaml(template_data, env_data)

        with open(output_path, 'w') as output_file:
            ruamel.yaml.dump(template_data, output_file, Dumper=ruamel.yaml.RoundTripDumper)

    except FileNotFoundError:
        print(f'Error: file is not found.')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
