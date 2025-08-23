#!/usr/bin/env python3
import yaml

def print_green(text):
    """Print text in green color using ANSI escape codes"""
    print(f"\033[32m{text}\033[0m")

def show_tutorial_prompts(yaml_file='../TUTORIALS.yaml'):
    """Load and display tutorial prompts from YAML file"""
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    print_green("## TUTORIALS:")
    print()
    
    for tutorial_key, tutorial_data in data.items():
        title = tutorial_data.get('Title', '')
        prompts = tutorial_data.get('Tutorial', {}).get('Prompts', [])
        starting_point = tutorial_data.get('Tutorial', {}).get('Starting_Point', [])
        
        if starting_point[0] == '--with-starting-point-folder=feedback-app-code':
            print_green(f"## {title}")
            for prompt in prompts:
                print(f"> {prompt}")
            print()

if __name__ == '__main__':
    show_tutorial_prompts()