#!/usr/bin/env python3
import yaml
import os
import sys

def set_green(text):
    """Print text in green color using ANSI escape codes"""
    return f"\033[32m{text}\033[0m"

def get_tutorial_files(tutorials_folder, tutorial_configuration):
    list_of_files = [f for f in os.listdir(tutorials_folder) if f.startswith('tutorial')]
    filtered_list_of_files = []
    for yaml_file in list_of_files:
        with open(f"{tutorials_folder}/{yaml_file}", 'r') as file:
            data = yaml.safe_load(file)
        if tutorial_configuration in data['tutorial']["starting_point"]:
            filtered_list_of_files.append(f"{tutorials_folder}/{yaml_file}")
    return filtered_list_of_files

def get_prompts(file):
    """Load and display tutorial prompts from YAML file"""
    with open(file, 'r') as file:
        data = yaml.safe_load(file)

    tutorials = {'tutorial': data['tutorial']}
    
    content=[]

    for tutorial_key, tutorial_data in tutorials.items():
        title = tutorial_data.get('title', '')
        prompts = tutorial_data.get('prompts', tutorial_data.get('Prompts', []))
        starting_point = tutorial_data.get('starting_point', [])

        content.append(set_green(f"## {title}"))
        for prompt in prompts:
            content.append(f"> {prompt}")
        content.append("")
    
    return content

def build_tutorial_prompts(filtered_list_of_files):

    content = []

    content.append(set_green("## TUTORIALS:"))
    content.append("")

    for (file) in filtered_list_of_files:
        content += get_prompts(file)
    
    return content
        
def display_format(content):
    return '\n'.join(content)

def show_tutorial_prompts(tutorials_folder, tutorial_configuration):
    
    filtered_list_of_files = get_tutorial_files(tutorials_folder, tutorial_configuration)
    content = build_tutorial_prompts(filtered_list_of_files)
    print(display_format(content))

if __name__ == '__main__':
    tutorial_configuration = sys.argv[1]
    show_tutorial_prompts('../tutorials', tutorial_configuration)
