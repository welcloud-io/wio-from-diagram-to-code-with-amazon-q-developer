#!/usr/bin/env python3

import yaml
import os

# -----------------------------------------------------------------------------
# ONE TUTORIAL SECTION
# -----------------------------------------------------------------------------

def tutorial_title(tutorial_properties, index_number):
    content = []
    title = tutorial_properties.get('title', '')

    content.append(f"## {index_number}. {title}")
    content.append("")

    return content

def prerequisites():
    content = []

    content.append("### [=> PREREQUISITES](../README.md#prerequisites)")
    content.append("")
    
    return content

def tutorial_starting_point(tutorial_properties):
    content = []

    content.append("### Script to execute In VS Code terminal ('_playground/vscode-app-folder/')")
    content.append("```")

    command_to_execute = '../init-playground.sh'
    for starting_point in tutorial_properties['starting_point']:
        command_to_execute += f" {starting_point}"
    content.append(command_to_execute)
    content.append("```")
    content.append("")

    return content

def tutorial_prompts(tutorial_properties):
    content = []

    content.append("### Prompts to execute In Q Desktop, Q CLI, Kiro, ...")
    for prompt in tutorial_properties['prompts']:
        
        content.append("```")
        content.append(prompt)
        content.append("```")
    content.append("")

    return content

def tutorial_results(tutorial_properties):
    content = []    

    content.append("### Result Example")
    for example in tutorial_properties['result_example']:
        filename = os.path.basename(example).replace('.png', '').replace('-', ' ')
        content.append(f"![{filename}]({example})")
    content.append("")
    
    return content

def create_tutorial_section(tutorial_data, index_number):
    content = []
        
    for tutorial_key, tutorial_properties in tutorial_data.items():
        content += tutorial_title(tutorial_properties, index_number)
        content += prerequisites()
        content += tutorial_starting_point(tutorial_properties)
        content += tutorial_prompts(tutorial_properties)
        content += tutorial_results(tutorial_properties)
        content.append("")

    return content

# -----------------------------------------------------------------------------
# TUTORIALS PAGE WITH INDEX
# -----------------------------------------------------------------------------

def empty_target_file(target_file):
    with open(target_file, 'w') as file:
        file.write("")

def write_target_file(target_file, content):
    with open(target_file, 'w') as file:
        file.write('\n'.join(content))

def get_tutorial_title(tutorial_file):
    title = ''
    with open(tutorial_file, 'r') as file:
        tutorial_data = yaml.safe_load(file)
        title = tutorial_data['tutorial']['title']
    return title

def tutorial_index(index_data):
    content = []
    
    content.append("# Tutorial Index")
    content.append("")
    
    section_counter = 1
    tutorial_counter = 1
    
    for section in index_data['tutorial_index']:
        section_info = section['index_section']
        section_name = section_info['index_section_name']
        section_anchor = f"{section_counter}-{section_name.lower().replace(' ', '-')}"
        
        content.append(f"{section_counter}. [{section_name}](#{section_anchor})")
        content.append("")
        
        sub_counter = 1
        for tutorial_file in section_info['indexed_tutorials']:
            full_path = f"tutorials/{tutorial_file}"
            title = get_tutorial_title(full_path)
            hierarchical_number = f"{section_counter}.{sub_counter}"
            indexed_title = f"{hierarchical_number}. {title}"
            anchor = indexed_title.lower().replace(' ', '-').replace('.', '')
            content.append(f"    - {hierarchical_number} [{title}](#{anchor})")
            sub_counter += 1
        
        content.append("")
        section_counter += 1
    
    return content

def tutorials_section(index_data):
    content = []
    section_counter = 1
    
    for section in index_data['tutorial_index']:
        section_info = section['index_section']
        section_name = section_info['index_section_name']
        
        content.append(f"# {section_counter}. {section_name}")
        content.append("")
        
        sub_counter = 1
        for tutorial_file in section_info['indexed_tutorials']:
            full_path = f"tutorials/{tutorial_file}"
            with open(full_path, 'r') as file:
                tutorial_data = yaml.safe_load(file)
            
            hierarchical_number = f"{section_counter}.{sub_counter}"
            content += create_tutorial_section(tutorial_data, hierarchical_number)
            sub_counter += 1
        
        section_counter += 1
    
    return content

def build_tutorials_page(index_data, target_file='TUTORIALS.md'):
    empty_target_file(target_file)

    content = []
    content += tutorial_index(index_data)
    content += tutorials_section(index_data)
    
    write_target_file(target_file, content)

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------

def check_orphans(tutorial_files):
    files = [f for f in os.listdir('tutorials') if f != 'main-index.yaml']    # find all files that are not in the index
    orphaned_files = []
    for file in files:
        if f"tutorials/{file}" not in tutorial_files:
            orphaned_files.append(file)
    return orphaned_files

def check_screenshot_dead_links(tutorial_files):
    dead_links = []
    for file in tutorial_files:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

        if 'result_example' in data['tutorial']:
            for example in data['tutorial']['result_example']:
                if not os.path.exists(example):
                    dead_links.append((example, file))

    return dead_links

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
        
if __name__ == "__main__":

    with open('tutorials/main-index.yaml', 'r') as f:
        index_data = yaml.safe_load(f)
    
    # Extract all tutorial files for orphan and dead link checks
    tutorial_files = []
    for section in index_data['tutorial_index']:
        for tutorial_file in section['index_section']['indexed_tutorials']:
            tutorial_files.append(f"tutorials/{tutorial_file}")

    build_tutorials_page(index_data)

    orphan_files = check_orphans(tutorial_files)
    if orphan_files != []: print ('orphans tutorials', orphan_files)

    screenshot_dead_links = check_screenshot_dead_links(tutorial_files)
    if screenshot_dead_links != []: print ('screenshot dead links', screenshot_dead_links)
