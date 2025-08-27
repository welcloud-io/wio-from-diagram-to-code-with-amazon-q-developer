#!/usr/bin/env python3

import yaml
import os

def create_page(tutorial_data, index_number):
    # Handle the current YAML structure where tutorial is the top-level key
    tutorial = {'tutorial': tutorial_data['tutorial']}

    # Generate TUTORIALS.md content
    content = []
        
    for tutorial_key, tutorial_properties in tutorial.items():
        title = tutorial_properties.get('title', tutorial_properties.get('Title', ''))
        tutorial = tutorial_properties
        
        # Add title
        content.append(f"## {index_number}. {title}")
        content.append("")

        # Add tutorial
        starting_point_key = 'starting_point'
        if starting_point_key in tutorial:
            content.append("### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)")
            content.append("```")
            for starting_point in tutorial[starting_point_key]:
                content.append(f"../init-playground.sh {starting_point}")
            content.append("```")

        content.append("")

        # Add tutorial
        prompts_key = 'prompts'
        if prompts_key in tutorial:
            for prompt in tutorial[prompts_key]:
                content.append("### Prompts to execute In Q Desktop, Q CLI, Kiro, ...")
                content.append("```")
                content.append(prompt)
                content.append("```")
                
        content.append("")
        
        # Add result examples
        result_key = 'result_example'
        if result_key in tutorial:
            content.append("### Result Example")
            for example in tutorial[result_key]:
                # Extract filename from path for alt text
                filename = os.path.basename(example).replace('.png', '').replace('-', ' ')
                content.append(f"![{filename}]({example})")
        
        content.append("")
        content.append("")

    return content

def get_tutorial_title(tutorial_file):
    title = ''
    with open(tutorial_file, 'r') as file:
        tutorial_data = yaml.safe_load(file)
        title = tutorial_data['tutorial']['title']
    return title

def build_tutorials_page(tutorial_files, target_file='TUTORIALS.md'):

    # Clear existing content in TUTORIALS.md
    with open(target_file, 'w') as file:
        file.write("")

    # Generate index
    content = []
    content.append("# Tutorial Index")
    for i, filename in enumerate(tutorial_files, 1):
        title = get_tutorial_title(filename)
        indexed_title = f"{i}. {title}"
        anchor = indexed_title.lower().replace(' ', '-').replace('.', '')               
        content.append(f"{i}. [{title}](#{anchor})")
    content.append("")
    content.append("")

    # Write to TUTORIALS.md
    with open(target_file, 'a') as file:
        file.write('\n'.join(content))

    for i, filename in enumerate(tutorial_files, 1):
        # Read tutorials.yaml
        with open(filename, 'r') as file:
            tutorial_data = yaml.safe_load(file)
        
        # Create content
        content = create_page(tutorial_data, i)
        
        # Write to TUTORIALS.md
        with open(target_file, 'a') as file:
            file.write('\n'.join(content))
        
if __name__ == "__main__":

    with open('tutorials/main-index.yaml', 'r') as f:
        index_data = yaml.safe_load(f)
    
    tutorial_files = index_data['tutorial_index']
    tutorial_files = [f"tutorials/{file}" for file in tutorial_files]

    build_tutorials_page(tutorial_files)