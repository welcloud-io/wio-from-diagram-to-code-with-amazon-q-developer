#!/usr/bin/env python3

import yaml
import os

# -----------------------------------------------------------------------------
# FILE MANAGEMENT
# -----------------------------------------------------------------------------
def empty_target_file(target_file):
    with open(target_file, 'w') as file:
        file.write("")

def write_target_file(target_file, content):
    with open(target_file, 'w') as file:
        file.write('\n'.join(content))

# -----------------------------------------------------------------------------
# BUILD TUTORIAL INDEX
# -----------------------------------------------------------------------------
class TutorialIndex:
    def __init__(self, tutorial_page_folder=''):
        self.content = []

        with open('tutorial-descriptions/main-index.yaml', 'r') as f:
            index_data = yaml.safe_load(f)
        
        self.content.append("# Tutorial Index")
        self.content.append("")
        
        section_counter = 1
        tutorial_counter = 1
        
        for section in index_data['tutorial_index']:
            section_info = section['index_section']
            section_name = section_info['index_section_name']
            section_anchor = f"{section_counter}-{section_name.lower().replace(' ', '-')}"
            
            self.content.append(f"{section_counter}. [{section_name}]({tutorial_page_folder}#{section_anchor})")
            self.content.append("")
            
            sub_counter = 1
            for tutorial_file in section_info['indexed_tutorials']:
                full_path = f"tutorial-descriptions/{tutorial_file}"
                title = self.get_tutorial_title(full_path)
                hierarchical_number = f"{section_counter}.{sub_counter}"
                indexed_title = f"{hierarchical_number}. {title}"
                anchor = indexed_title.lower().replace(' ', '-').replace('.', '')
                self.content.append(f"    - {hierarchical_number} [{title}]({tutorial_page_folder}#{anchor})")
                sub_counter += 1
            
            self.content.append("")
            section_counter += 1

    def get_tutorial_title(self, tutorial_file):
        title = ''
        with open(tutorial_file, 'r') as file:
            tutorial_data = yaml.safe_load(file)
            title = tutorial_data['tutorial']['title']
        return title
        
# -----------------------------------------------------------------------------
# BUILD TUTORIAL SECTIONS
# -----------------------------------------------------------------------------
class TutorialSection:
    def __init__(self, tutorial_file, index_number):
        full_path = f"tutorial-descriptions/{tutorial_file}"
        with open(full_path, 'r') as file:
            self.tutorial_data = yaml.safe_load(file)
        
        self.index_number = index_number

        self.content = []
            
        for tutorial_key, tutorial_properties in self.tutorial_data.items():
            self.content += self._title(tutorial_properties, self.index_number)
            self.content += self._prerequisites()
            self.content += self._starting_point(tutorial_properties)
            self.content += self._prompts(tutorial_properties)
            self.content += self._results(tutorial_properties)
            self.content.append("")
        
    def _title(self, tutorial_properties, index_number):
        content = []
        title = tutorial_properties.get('title', '')

        content.append(f"## {index_number}. {title}")
        content.append("")

        return content

    def _prerequisites(self):
        content = []

        content.append("### Install Prerequisites if not done yet")
        content.append("#### [=> Install Prerequisites](../../README.md#prerequisites)")
        content.append("")
        
        return content

    def _starting_point(self, tutorial_properties):
        content = []

        content.append("### Script to execute In VS Code terminal ('_playground/vscode-app-folder/')")

        content.append("#### [=> Start tutorial playground](../../README.md#1-start-tutorial-window)")

        content.append("```")

        command_to_execute = '../init-playground.sh'
        for starting_point in tutorial_properties['starting_point']:
            command_to_execute += f" {starting_point}"
        content.append(command_to_execute)
        content.append("```")
        content.append("")

        return content

    def _prompts(self, tutorial_properties):
        content = []

        content.append("### Prompts to execute In Q Desktop, Q CLI, Kiro, ...")
        for prompt in tutorial_properties['prompts']:
            
            content.append("```")
            content.append(prompt)
            content.append("```")
        content.append("")

        return content

    def _results(self, tutorial_properties):
        content = []    

        content.append("### Result Example")
        for example in tutorial_properties['result_example']:
            filename = os.path.basename(example).replace('.png', '').replace('-', ' ')
            content.append(f"![{filename}]({example})")
        content.append("")
        
        return content
        
class TutorialSections:
    def __init__(self):
        self.content = []
        section_counter = 1

        with open('tutorial-descriptions/main-index.yaml', 'r') as f:
            index_data = yaml.safe_load(f)

        for section in index_data['tutorial_index']:
            section_info = section['index_section']
            section_name = section_info['index_section_name']
            
            self.content.append(f"# {section_counter}. {section_name}")
            self.content.append("")
            
            sub_counter = 1
            for tutorial_file in section_info['indexed_tutorials']:
                hierarchical_number = f"{section_counter}.{sub_counter}"
                self.content += TutorialSection(tutorial_file, hierarchical_number).content
                sub_counter += 1
            
            section_counter += 1
            
# -----------------------------------------------------------------------------
# BUILD TUTORIAL PAGE
# -----------------------------------------------------------------------------
class TutorialPageBuilder:
    
    def __init__(self, target_file='TUTORIALS.md'):
        self.target_file = target_file
        self.content = []
        
        with open('tutorial-descriptions/main-index.yaml', 'r') as f:
            self.index_data = yaml.safe_load(f)
        
        self.tutorial_index = TutorialIndex()
        self.tutorial_sections = TutorialSections()
            
    def build(self):
        empty_target_file(self.target_file)
        
        self.content += self.tutorial_index.content
        self.content += self.tutorial_sections.content
        
        write_target_file(self.target_file, self.content)

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------
class TutorialChecker:

    def __init__(self):
        with open('tutorial-descriptions/main-index.yaml', 'r') as f:
            index_data = yaml.safe_load(f)

        tutorial_files = []
        for section in index_data['tutorial_index']:
            for tutorial_file in section['index_section']['indexed_tutorials']:
                tutorial_files.append(f"tutorial-descriptions/{tutorial_file}")
        
        self.tutorial_files = tutorial_files

    def check_orphans(self):
        files = [f for f in os.listdir('tutorial-descriptions') if f != 'main-index.yaml']    # find all files that are not in the index
        orphan_files = []
        for file in files:
            if f"tutorial-descriptions/{file}" not in self.tutorial_files:
                orphan_files.append(file)

        if orphan_files != []: print ('orphans tutorials', orphan_files)

    def check_screenshot_dead_links(self):
        screenshot_dead_links = []
        for file in self.tutorial_files:
            with open(file, 'r') as f:
                data = yaml.safe_load(f)

            if 'result_example' in data['tutorial']:
                for example in data['tutorial']['result_example']:
                    if not os.path.exists(example):
                        screenshot_dead_links.append((example, file))

        if screenshot_dead_links != []: print ('screenshot dead links', screenshot_dead_links)

# -----------------------------------------------------------------------------
# UPDATE MAIN README INDEX
# -----------------------------------------------------------------------------
def update_readme_tutorial_index(tutorial_index_content):
    # Replace section between '# Tutorial Index' and '# Prerequisites' in ../README.md
    with open('../../README.md', 'r') as f:
        content = f.read()

    start_marker = '# Tutorial Index'; end_marker = '# Prerequisites'
    start_idx = content.find(start_marker); end_idx = content.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + '\n'.join(tutorial_index_content) + '\n\n' + content[end_idx:]

    with open('../../README.md', 'w') as f:
        f.write(content)

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    tutorial_page_builder = TutorialPageBuilder()
    tutorial_page_builder.build()

    checker = TutorialChecker()
    checker.check_orphans()
    checker.check_screenshot_dead_links()
    
    tutorial_index = TutorialIndex('_playground/tutorials/TUTORIALS.md')
    update_readme_tutorial_index(tutorial_index.content)