#!/usr/bin/env python3
import yaml
import os
import sys

def set_green(text):
    """Print text in green color using ANSI escape codes"""
    return f"\033[32m{text}\033[0m"

def files_related_to_tutorial_configuration(tutorials_folder, tutorial_configuration):
    list_of_tutorials = [f for f in os.listdir(tutorials_folder) if f.startswith('tutorial')]

    filtered_list_of_tutorials = []
    for tutorial_file in list_of_tutorials:
        with open(f"{tutorials_folder}/{tutorial_file}", 'r') as file:
            data = yaml.safe_load(file)
        if tutorial_configuration in data['tutorial']["starting_point"]:
            filtered_list_of_tutorials.append(f"{tutorials_folder}/{tutorial_file}")

    return filtered_list_of_tutorials

def tutorial_prompts(tutorial_file):
    with open(tutorial_file, 'r') as file:
        tutorial = yaml.safe_load(file)
    
    content=[]

    for tutorial_key, tutorial_data in tutorial.items():
        title = tutorial_data.get('title', '')
        prompts = tutorial_data.get('prompts', tutorial_data.get('Prompts', []))
        starting_point = tutorial_data.get('starting_point', [])

        content.append(set_green(f"## {title}"))
        for prompt in prompts:
            content.append(f"> {prompt}")
        content.append("")
    
    return content
        
def terminal_formated_prompts_related_to_tutorial_configuration(tutorials_folder, tutorial_configuration):
    content = []

    content.append("┌" + "─" * 50 + "┐")
    content.append(set_green("## TUTORIALS:"))
    content.append("")

    filtered_list_of_tutorials = files_related_to_tutorial_configuration(tutorials_folder, tutorial_configuration)
    for (tutorial_file) in filtered_list_of_tutorials:
        content += tutorial_prompts(tutorial_file)

    content.append("└" + "─" * 50 + "┘")

    return content

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    tutorial_configuration = sys.argv[1]
    content = terminal_formated_prompts_related_to_tutorial_configuration('../tutorial-descriptions', tutorial_configuration)
    print('\n'.join(content))
