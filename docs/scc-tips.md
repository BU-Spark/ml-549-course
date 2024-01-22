# SCC Tips and Tricks

A collection of tips and tricks for using the BU 
[Shared Computing Cluster (SCC)](https://www.bu.edu/tech/support/research/computing-resources/scc/).

> To get an account and/or be added to the Spark! SCC project, email
Michelle Voong at mailto:mvoong@bu.edu.

Once you have an account, there are a number of ways of 
[connecting to the SCC](https://www.bu.edu/tech/support/research/system-usage/connect-scc/). The recommended way is via [SCC OnDemand](https://www.bu.edu/tech/support/research/system-usage/connect-scc/scc-ondemand/),
which lets you check your storage quotas as well as start terminal sessions in 
your browser, or graphical interface based sessions.

To access OnDemand, navigate to https://scc-ondemand.bu.edu/ in recent versions of Chrome or Firefox.

## Storage Quotas and Project Memberships
Your home directory quota will most likely be 10GB which can easily be filled up
once you start doing machine learning projects and setting up python virtual 
environments. See the [Pyton Virtual Environments](#python-and-virtual-environments) below for tips on how to manage the associated storage.

Besides your Home folder, you will also be added to the `sparkgrp` project and
gain access to `/projectnb/sparkgrp` directory with a quota of 5 TBs.

## Python and Virtual Environments

The default `python3` version in SCC is probably older than you may want. At the
time of this writing it was `3.6.8`. It also doesn't seem to have any packages
installed.

```bash
$ python3 -m pip list
pip (9.0.3)
setuptools (39.2.0)
```

So the recommended way to use python is to use the `module` command. You can run

```sh
$ module avail python
```
to see the list of python versions available in the system. Then load the pythyon
version you want:
```sh
$ module load python3/3.10.5
```
for example to load version 3.10.5.

Note that it comes with many packages already installed, but not necessarily the 
version or packages you need for your project. To install additional packages, there
are two recommended approaches:

1. Installing packages to a shared location, and
2. Creating a virtual environment outside of your home folder

#1 is useful so that a project team can all use the same set of packages. #2 is
useful especially in the early stages when you are doing exploration. We'll
summarize each in the next two sections.

### Installing Packages to a Shared Location

In this process you will install python packages to a shared location which can 
then be shared among your team members.

> This is an adaptation of these [SCC Instructions](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/install-packages/#pip-shared).

First, load your python3 module version of choice:
```sh
$ module avail python3     # see which versions are available
$ module load python3/3.X.Y
```
Then install packages to a shared location. A good candidate would be on 
`/projectnb/sparkgrp` or a class project directory is one is setup by the
instructors.

For example
<pre>
$ pip install --no-cache-dir --prefix=/projectnb/sparkgrp/pythonlibs/<i style="color:red">projectname</i>  <i style="color:red">packagename</i>
</pre>

This will install packages in
<pre>
/projectnb/sparkgrp/pythonlibs/<i style="color:red">projectname</i>/lib/pythonX.Y/site-packages/<i style="color:red">packagename</i>
</pre>

But in order to use the packages, you have to update the `PYTHONPATH` environment
variable and also the `PATH` variable for any library executables or scripts.

<pre>
$ export PYTHONPATH=/projectnb/sparkgrp/pythonlibs/<i style="color:red">projectname</i>/lib/pythonX.Y/site-packages/:$PYTHONPATH
$ export PATH=/projectnb/sparkgrp/pythonlibs/<i style="color:red">projectname</i>/bin:$PATH
</pre>

Note that you have to update the environment variables as above each time you launch a new session. If you are submitting batch jobs, add them as commands in your
job file before your python script.

### Installing Packages into Virtual Environment

In this process, you will create a python virtual environment outside of your
home directory and invoke it.

> These instructions are adapted from these [SCC Instructions](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/virtualenv/).

The SCC instructions use `virtualenv`. Below we use `venv`. You may also consider
using the `pipenv` framework. The process is similar for each.

Load the python version you plan to use.
```sh
$ module load python3/3.X.Y
```

Now create the virtual environment in the `/projectnb/sparkgrp` space. Either in a location to share with team members:

<pre>
$ python3 -m venv /projectnb/sparkgrp/venvs/<i style="color:red">projectname</i>/<i style="color:red">mynewenv</i>
</pre>

Or in your own workspace there.
<pre>
$ python3 -m venv /projectnb/sparkgrp/workspaces/<i style="color:red">yourusername</i>/<i style="color:red">mynewenv</i>
</pre>

Then you can activate the virtual environment

<pre>
<span style="color:green"># Activate shared virtual environment</span>
$ source /projectnb/sparkgrp/venvs/<i style="color:red">projectname</i>/<i style="color:red">mynewenv</i>/bin/activate

<span style="color:green"># Or activate personal virtual environment</span>
$ source /projectnb/sparkgrp/workspaces/<i style="color:red">yourusername</i>/<i style="color:red">mynewenv</i>/bin/activate
</pre>

As opposed to the shared packages option of the previous section, to install 
additional packages you only need to run a simple `pip` command:

<pre>
$ pip install <i style="color:red">packagename</i>
</pre>

and finally to deactivate the virtual environment, just type
```sh
$ deactivate
```
as usual.

## Interactive Jupyter Notebook Session

### Academic ML Environment

List of modules to load (space separated): miniconda academic-ml

Pre-Launch Command (optional): conda activate spring-2024-pyt

Interface: lab

Working Directory: /projectnb/ds549/students/<your BU username>

Then select hours, cores, GPUs, etc.

### Custom Python Virtual Environment

List of modules to load (space separated): python3

Pre-Launch Command (optional): source /path/to/your/virtual/environemnt/bin/activate; ipython kernel install --user --name=<virtual env name>

Interface: lab

Working Directory: /projectnb/ds549/students/<your BU username>

Then select hours, cores, GPUs, etc.
