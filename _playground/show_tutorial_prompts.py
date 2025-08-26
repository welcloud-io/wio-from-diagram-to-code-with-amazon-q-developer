#!/usr/bin/env python3
import yaml

def print_green(text):
    """Print text in green color using ANSI escape codes"""
    print(f"\033[32m{text}\033[0m")

def show_tutorial_prompts(yaml_file='../tutorials/tutorial-mermaid-generate-architecture-diagram-from-code.yaml'):
    """Load and display tutorial prompts from YAML file"""
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    print_green("## TUTORIALS:")
    print()
    
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
    show_tutorial_prompts()