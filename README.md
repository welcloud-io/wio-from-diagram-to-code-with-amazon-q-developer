# **From Diagram to Code with Amazon Q Developer**

This repo is a list of tutorials based on this blog post:
https://github.com/welcloud-io/wio-from-diagram-to-code-with-amazon-q-developer

It demonstrates how you can generate diagrams from an application code, but also how to generate code from diagrams using Amazon Q Developer in the Visual Studio Code IDE.

---

# Prerequisites

I assume that you are running on Ubuntu 22-04 linux, but the instructions below can be adapted to you environment.

## Install & start VS Code

The official procedure:

https://code.visualstudio.com/docs/setup/linux#_debian-and-ubuntu-based-distributions

From the terminal, this also works for me:

```
$> sudo snap install --classic code
$> code
```

## Clone the repo & go to the tutorial folder

Open a terminal in VS Code and execute the following commands

```
$> git clone https://github.com/welcloud-io/wio-from-diagram-to-code-with-amazon-q-developer.git
$> cd wio-from-diagram-to-code-with-amazon-q-developer/
```

## Configure VS Code Manually (Option 1)

N.B. You can try to configure VS Code Automatically if you start from a blank VS Code environement (see Option 2)

### Install Amazon Q Developer extension & Enable @workspace

Q Developer plugin installation:
https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html#setup-vscode

Q Developer settings option to tick: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/workspace-context.html

Then connect to Amazon Q with your builder ID

### Install Mermaid extension

https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

### Install Draw.io Integration extension

https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio

Then:
- Go to 'File > Preferences > Settings' 
- Search for 'editorasso' setting 
- Add the following association item: *.drawio.xml => hediet.vscode-drawio-text)

## Configure VS Code Automatically (Option 2)

Be aware that this may not work if you environment has some settings already

```bash
$> ./setup-vscode.sh
```

Once done, connect to Amazon Q Developer using your Builder ID (folow the procedure in VS Code)

# Start tutorials

## Follow tutorial instructions in the tutorial readme

[TUTORIAL INSTRUCTIONS](_playground/README.md)