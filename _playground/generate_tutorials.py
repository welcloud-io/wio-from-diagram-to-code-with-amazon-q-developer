#!/usr/bin/env python3

import yaml
import os

def generate_tutorials_md():
    # Read tutorials.yaml
    with open('TUTORIALS.yaml', 'r') as file:
        tutorials = yaml.safe_load(file)
    
    # Generate TUTORIALS.md content
    content = []
    
    # Generate index
    content.append("# Tutorial Index")
    content.append("")
    for i, (tutorial_key, tutorial_data) in enumerate(tutorials.items(), 1):
        title = tutorial_data.get('Title', '')
        anchor = title.lower().replace(' ', '-').replace('mermaid', 'mermaid')
        content.append(f"{i}. [{title}](#{anchor})")
    content.append("")
    
    for tutorial_key, tutorial_data in tutorials.items():
        title = tutorial_data.get('Title', '')
        tutorial = tutorial_data.get('Tutorial', {})
        
        # Add title
        content.append(f"## {title}")
        content.append("")

        # Add tutorial
        if 'Starting_Point' in tutorial:
            content.append("### Initialize Tutorial (In VS Code tutorial window terminal)")
            # content.append("---")
            content.append("```")
            for starting_point in tutorial['Starting_Point']:

                content.append(f"../init-playground.sh {starting_point}")
            content.append("```")
            # content.append("---")

        # Add tutorial
        if 'Prompts' in tutorial:
            for prompt in tutorial['Prompts']:
                content.append("### Write Prompt (In Q Desktop, Q CLI, Kiro, ...)")
                content.append("")
                # content.append("---")
                content.append("")
                content.append("```")
                content.append(prompt)
                content.append("```")
                content.append("")
                # content.append("---")
                content.append("")
        
        # Add result examples
        if 'Result_Example' in tutorial:
            content.append("### Result Example")
            content.append("")
            for example in tutorial['Result_Example']:
                # Extract filename from path for alt text
                filename = os.path.basename(example).replace('.png', '').replace('-', ' ')
                content.append(f"![{filename}]({example})")
            content.append("")
    
    # Write to TUTORIALS.md
    with open('TUTORIALS.md', 'w') as file:
        file.write('\n'.join(content))
    
    print("TUTORIALS.md generated successfully!")

if __name__ == "__main__":
    generate_tutorials_md()