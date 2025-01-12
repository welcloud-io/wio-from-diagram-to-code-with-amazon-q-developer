# Prerequisites

I assume that you are on an unbuntu 22-04 linux machine

## Install VSCODE

https://code.visualstudio.com/docs/setup/linux

From the terminal, this works for me:

```
$> sudo snap install --classic code # or code-insiders
```

## Install Amazon Q Developer extension & Enable @workspace

Q Developer plugin installation:
https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html#setup-vscode

Q Developer settings option to tick: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/workspace-context.html

Then connect to Amazon Q with your builder ID

## Install Mermaid extension

https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

## Install Draw.io Integration extension

https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio

Then:
- Go to 'File > Preferences > Settings' 
- Search for 'editorasso' setting 
- Add the following association item: *.drawio.xml => hediet.vscode-drawio-text)

# Clone repo

```
git clone https://github.com/welcloud-io/wio-from-diagram-to-code-with-amazon-q-developer.git
```

# Go to the _playground folder

```
cd wio-from-diagram-to-code-with-amazon-q-developer/_playground/
```

# Initiate the application folder

```
mkdir vscode-app-folder
```

# Open the application folder with vscode

Open vscode menu : File / Open Folder... 

Chose 'wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder' folder

# Choose a tutorial to initialize

```
../init-playground.sh 
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4):
```

# Follow tutorial instructions in the readme

[TUTORIAL INSTRUCTIONS](_playground/README.md)



