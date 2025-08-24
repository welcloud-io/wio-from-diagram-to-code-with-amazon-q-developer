#!/usr/bin/env python3
import yaml
import os

def read_tutorial_index():
    with open('tutorials/tutorial-index.yaml', 'r') as f:
        return yaml.safe_load(f)

def read_tutorial_file(tutorial_path):
    with open(tutorial_path, 'r') as f:
        return yaml.safe_load(f)
        
def write_index_file(content):
    with open('INDEX.md', 'w') as f:
        f.write(content)

def create_markdown_content(index_data):
    markdown_content = "# Tutorial Index\n\n"
    
    for i, tutorial_file in enumerate(index_data['tutorial_index'], 1):
        tutorial_path = f"tutorials/{tutorial_file}"
        
        if os.path.exists(tutorial_path):
            tutorial_data = read_tutorial_file(tutorial_path)
            title = tutorial_data['tutorial']['title']
            markdown_content += f"{i}. [{title}]({tutorial_file})\n"
        else:
            markdown_content += f"{i}. {tutorial_file} (file not found)\n"
    
    return markdown_content

def generate_markdown_index():
    # Read tutorial-index.yaml
    index_data = read_tutorial_index()
    
    # Create markdown content
    markdown_content = create_markdown_content(index_data)
    
    # Write to INDEX.md
    write_index_file(markdown_content)
    
if __name__ == "__main__":
    generate_markdown_index()