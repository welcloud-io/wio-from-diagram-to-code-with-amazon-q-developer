#!/usr/bin/env python3

import yaml
import os

def create_content(data):
    # Handle the current YAML structure where tutorial is the top-level key
    if 'tutorial' in data:
        tutorials = {'tutorial': data['tutorial']}
    elif 'Tutorial' in data:
        tutorials = {'Tutorial': data['Tutorial']}
    else:
        tutorials = data
    
    # Generate TUTORIALS.md content
    content = []
    
    # Generate index
    content.append("# Tutorial Index")
    content.append("")
    for i, (tutorial_key, tutorial_data) in enumerate(tutorials.items(), 1):
        title = tutorial_data.get('title', tutorial_data.get('Title', ''))
        anchor = title.lower().replace(' ', '-')
        content.append(f"{i}. [{title}](#{anchor})")
    content.append("")
    
    for tutorial_key, tutorial_data in tutorials.items():
        title = tutorial_data.get('title', tutorial_data.get('Title', ''))
        tutorial = tutorial_data
        
        # Add title
        content.append(f"## {title}")
        content.append("")

        # Add tutorial
        starting_point_key = 'starting_point'
        if starting_point_key in tutorial:
            content.append("### Initialize Tutorial (In VS Code tutorial window terminal)")
            content.append("```")
            for starting_point in tutorial[starting_point_key]:
                content.append(f"../init-playground.sh {starting_point}")
            content.append("```")

        content.append("")

        # Add tutorial
        prompts_key = 'prompts'
        if prompts_key in tutorial:
            for prompt in tutorial[prompts_key]:
                content.append("### Write Prompt (In Q Desktop, Q CLI, Kiro, ...)")
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

    return content  

def generate_tutorials_md():
    # Read tutorials.yaml
    with open('tutorials/tutorial-mermaid-generate-architecture-diagram-from-code.yaml', 'r') as file:
        data = yaml.safe_load(file)
    
    # Create content
    content = create_content(data)
    
    # Write to TUTORIALS.md
    with open('TUTORIALS.md', 'w') as file:
        file.write('\n'.join(content))
    
    print("TUTORIALS.md generated successfully!")

if __name__ == "__main__":
    generate_tutorials_md()