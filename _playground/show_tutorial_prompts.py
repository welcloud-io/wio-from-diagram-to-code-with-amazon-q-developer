#!/usr/bin/env python3
import yaml

def print_green(text):
    """Print text in green color using ANSI escape codes"""
    print(f"\033[32m{text}\033[0m")

def show_tutorial_prompts(tutorials_folder, tutorial_configuration):
    # list all tutorial files
    import os
    list_of_files = [f for f in os.listdir(tutorials_folder) if f.startswith('tutorial')]
    filtered_list_of_files = []
    for yaml_file in list_of_files:
        with open(f"{tutorials_folder}/{yaml_file}", 'r') as file:
            data = yaml.safe_load(file)
        if tutorial_configuration in data['tutorial']["starting_point"]:
            filtered_list_of_files.append(f"{tutorials_folder}/{yaml_file}")

    print_green("## TUTORIALS:")
    print()

    for (file) in filtered_list_of_files:
        """Load and display tutorial prompts from YAML file"""
        with open(file, 'r') as file:
            data = yaml.safe_load(file)

        # Handle the current YAML structure where tutorial is the top-level key
        tutorials = {'tutorial': data['tutorial']}
        
        for tutorial_key, tutorial_data in tutorials.items():
            title = tutorial_data.get('title', '')
            prompts = tutorial_data.get('prompts', tutorial_data.get('Prompts', []))
            starting_point = tutorial_data.get('starting_point', tutorial_data.get('starting_Point', tutorial_data.get('Starting_Point', [])))
            
            # Check if starting_point list is not empty and contains the expected value
            if starting_point[0] == '--with-starting-point-folder=feedback-app-code':
                print_green(f"## {title}")
                for prompt in prompts:
                    print(f"> {prompt}")
                print()

if __name__ == '__main__':
    import sys
    tutorial_configuration = sys.argv[1]
    show_tutorial_prompts('../tutorials', tutorial_configuration)
