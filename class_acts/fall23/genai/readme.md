---
marp: false
footer: BU Spark! DS 549
---

# GenAI -- Using GitHub CoPilot to Kickstart Projects

## Introduction

This is an in-class activity to 
1. develop ML code examples for some common datasets then 
2. kickstart project development

all while using Generative AI.

We will start with GitHub CoPilot, and if we run into limitations, we will
try ChatGPT-4.

---

Depending on where you are in your project you can use this activity to:
* explore how to load your data
* experiment with pre-processing or feature engineering techniques
* understand your dataset better with some exploratory data analysis, data summarizations, or visualizations
* try to apply some task specific ML models

---

## The In-Class Assignment

All preferably on SCC.

1. Fork and clone the class repository
2. Create a virtual environment for this project
3. Setup VS Code and the Remote Development Extension Pack if you haven't done so already
4. _Individually_ follow along with the 2 in-class challenges
5. _As a team_, use GenAI to kickstart your project

---

## Developer Setup

We will be running VS Code with a remote connection to SCC, with CoPilot
installed on the remote machine.

We will also use OpenAI's ChatGPT-4 if and when we come across limitations
of CoPilot.

---

### OpenAI ChatGPT

Create an account at OpenAI. 

https://chat.openai.com/auth/login is probably a good starting point.

If you don't have a subscription to GPT4, you may be able to start a trial. If not, see the instructor during lab time to enter your query and get the response.

---

### Fork and Clone the Class Repository

If you haven't already, 
* navigate to https://github.com/BU-Spark/ml-549-course and fork the repository to your own GitHub account. 
* Then clone your fork to your folder on SCC. You probably want to clone it to 
`/projectnb/ds549/students/<your_bu_login>`.

---

### Virtual Environment Setup

Create a Conda or `venv` virtual environment for this project on SCC, preferable in your workspace on `/projectnb/ds549/students`. You can either do it after you get VS Code with Remote Development working and connected and do it in the integrated terminal, or you can connect to https://scc1-ondemand.bu.edu and connect to a login node.

Remember that the default python version on SCC is quite old, so we suggest you load a newer version before you create the virtual environment.

```bash
# show what python versions are available
module avail python3

# pick the latest version available. Might be different when you read this.
module load python3/3.10.12

# check python version
python --version
```

For example:

```bash
# Conda
conda create -n genai
conda activate genai
```
Alternatively...

```bash
# venv
python3 -m venv genai
source genai/bin/activate
```

When you start using a Jupyter notebook in VS Code, you will be prompted to
select a kernel. Select your virtual environment to use as the kernel.

---

### Visual Studio Code Setup

Download and install VS Code from https://code.visualstudio.com/download.

Install the Remote Development Extension Pack. See
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack.

---

### CoPilot Setup

See https://github.com/features/copilot for signup and installation instructions. I believe there is a site license for BU, but miminally you 
can sign up for the free trial.

Make sure you install the 
[GitHub CoPilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) for VS Code.

Also, be sure to install 
[GitHub CoPilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat).

---

### Remote Connection to SCC

From VS Code, open the Command Palette (Ctrl+Shift+P on Windows or Cmd+Shift+P
on Mac) and select Remote-SSH:
Connect to Host... and enter `scc1.bu.edu` as the host name. You will be
prompted for your SCC password. If you have two-factor authentication enabled,
you will be prompted for your 2FA code.

Once connected to SCC through the VS Code remote connection, you will likely
have to install the CoPilot extension on the remote machine. You can do this
by opening the Extensions tab in VS Code, searching for CoPilot, and clicking
Install or Enable on 'SSH: scc1.bu.edu'

---

### SCC GPU Access Ideas

When you SSH to scc1.bu.edu, you are on a login node where you cannot use 
GPU compute resources.

From a terminal prompt, including the one integrated into VS Code, you can
enumerate the GPUs available on SCC with the `qqpus` command.

```bash
# list GPUS and their status
$ qgpus
```

But you cannot execute Jupyter cells on the GPU.

See [GPU Computing](https://www.bu.edu/tech/support/research/software-and-programming/programming/multiprocessor/gpu-computing/) for more information.

---

A workaround is to also create an interactive Jupyter session on scc-ondemand
with a GPU, and starting in the same folder you are editing in VS Code.

In my case, I used the following configuration for the SCC interactive notebook.

---

```bash
# list of modules to load
python3/3.10.12

# Pre-Launch Command (optional)
source /projectnb/ds549/workspaces/tgardos/venv_ds549/bin/activate; ipython kernel install --user --name=venv_ds549

# Working Directory
/projectnb/ds549/workspaces/tgardos/ml-549-course

...
```
---

```bash

# Number of cores
1

# Number of gpus
1

# GPU compute capability
3.5 (K40m or P100 or V100)

# Project
ds549
```
---

## Jupyter Notebook Templates

The notebooks for this in-class activity are in  `class_acts/fall23/genai`.
