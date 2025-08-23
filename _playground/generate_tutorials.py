#!/usr/bin/env python3

import yaml
import os

def generate_tutorials_md():
    # Read tutorials.yaml
    with open('tutorials.yaml', 'r') as file:
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
        prompts = tutorial_data.get('Prompts', {})
        
        # Add title
        content.append(f"## {title}")
        content.append("")
        
        # Add prompts
        if 'Prompts' in prompts:
            for prompt in prompts['Prompts']:
                content.append("### Q Prompt >")
                content.append("")
                content.append("---")
                content.append("")
                content.append("```")
                content.append(prompt)
                content.append("```")
                content.append("")
                content.append("---")
                content.append("")
        
        # Add result examples
        if 'Result_Example' in prompts:
            content.append("### Result Example")
            content.append("")
            for example in prompts['Result_Example']:
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