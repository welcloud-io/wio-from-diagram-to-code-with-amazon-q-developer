# **From Diagram to Code with Amazon Q Developer**

This repo is a list of tutorials based on this blog post:
https://github.com/welcloud-io/wio-from-diagram-to-code-with-amazon-q-developer

It demonstrates how you can generate diagrams from an application code, but also how to generate code from diagrams using Amazon Q Developer in the Visual Studio Code IDE.

![test](screenshots/vscode-bigpicture.png)

---

# Prerequisites

I assume that you are using a **Linux Ubuntu 22-04** distribution, but the instructions below can be adapted to your environment.

## 1) Install & start VS Code (If not done yet in your environment)

The official procedures to install & start VS Code is there:

https://code.visualstudio.com/docs/setup/linux#_debian-and-ubuntu-based-distributions

N.B.: These simple commands below work for me to intsall & start VS Code on Linux Ubuntu 22-04:

```
$> sudo snap install --classic code
$> code
```

## 2) Clone the repo & go to the tutorial folder

Open a terminal in VS Code and execute the following commands

```
$> git clone https://github.com/welcloud-io/wio-from-diagram-to-code-with-amazon-q-developer.git
$> cd wio-from-diagram-to-code-with-amazon-q-developer/
```

## 3) Configure VS Code

### 3.1) Configure VS Code Manually (Option 1)

N.B.
__You can atempt to configure VS Code automatically__
if it is a fresh installation (__see Option 2__)

### Install Amazon Q Developer extension & Enable @workspace

Q Developer plugin installation:
https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html#setup-vscode

Q Developer setting options to tick: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/workspace-context.html

Then connect to Amazon Q with your builder ID

### Install Mermaid extension

https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

### Install Draw.io Integration extension

https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio

Then:
- Go to 'File > Preferences > Settings' 
- Search for 'editorasso' setting 
- Add the following association item: *.drawio.xml => hediet.vscode-drawio-text)

### 3.2) Configure VS Code Automatically (Option 2)

**Be aware that this may not work** if you environment has some settings already

```bash
$> ./setup-vscode.sh
```

Once done, connect to Amazon Q Developer using your Builder ID (folow the procedure in VS Code)

## 4) Install Q CLI (Optional)

Amazon Q Developer CLI (Command Line Interface) is used for some tutorials, but not for all.

To install it, you either you follow this link:

https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html

OR you can attempt using this script in you terminal (n.b. it's only been tested on Linux Ubuntu 22-04):

```bash
$> ./install-q-cli.sh
```

# Start tutorials

## Follow tutorial instructions in the tutorial readme

[CLASSIC TUTORIALS INSTRUCTIONS](_playground/README.md)

[MORE TUTORIALS](_playground/README-More.md)