#!/usr/bin/env python3
import yaml

with open('../tutorials.yaml', 'r') as file:
    data = yaml.safe_load(file)

def print_green(text):
    """Print text in green color using ANSI escape codes"""
    print(f"\033[32m{text}\033[0m")

print_green("## TUTORIALS:")
print()

for tutorial_key, tutorial_data in data.items():
    title = tutorial_data.get('Title', '')
    prompts = tutorial_data.get('Prompts', {}).get('Prompts', [])
    
    print_green(f"## {title}")
    for prompt in prompts:
        print(f"> {prompt}")
    print()