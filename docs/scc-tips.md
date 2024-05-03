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

## Group Membership

Once you are given access, you are added to the 'sparkgrp' group. You can see the groups you are in by running the command `groups` from a
terminal prompt. It will likely show you more than one group, but one of them should be 'sparkgrp'.

Note that even though you may be a member of several groups, your current default group may differ than the one you want. This could 
lead to some confusing file ownership issues. It's a good idea to run `ls -al` to see what user and group a file is assigned to if you
are having issues.

To see what your current default group is, you can run

```bash
id -ng       # display current default group
```

To change your current default group to 'sparkgp', run

```bash
newgrp sparkgrp
```

Then run `id -ng` again and you should see the change.

Note that running `newgrp` creates a new login shell, so you may have to rerun your conda or venv activate command again to
activate the environment.

When you are done, simply type `exit` to end the log in session. You can type `exit` again to exit the terminal session.

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

### Package Caches

You find that even though you create and run virtual environments on your project folder, you get quote exceeded
error for your home directory. This could be because conda or pip are caching python installation packages in
your home directory.

#### Conda

For Conda, try running
```bash
conda info
```
And look for the section called `package cache :`. See [shared-pkg-cache](https://docs.anaconda.com/free/working-with-conda/packages/shared-pkg-cache/)
for a little more info.

#### PIP

For PIP, try running

```bash
pip cache dir
pip cache info
```

to find out more about where pip is caching. See [caching](https://pip.pypa.io/en/stable/topics/caching/) for more info.


## Interactive Jupyter Notebook or Session

Before you start an interactive Jupyter Notebook session in SCC OnDemand, you need to configure it
to start your intended conda or python virtual environment. Two examples are shown below.

### Academic ML Environment

List of modules to load (space separated): `miniconda academic-ml`

Pre-Launch Command (optional): `conda activate spring-2024-pyt`

Interface: `lab`

Working Directory: `/projectnb/ds549/students/<your BU username>`

Then select hours, cores, GPUs, etc.

### Custom Python Virtual Environment

List of modules to load (space separated): `python3`

Pre-Launch Command (optional): `source /path/to/your/virtual/environemnt/bin/activate; ipython kernel install --user --name=<virtual env name>`

Interface: `lab`

Working Directory: `/projectnb/ds549/students/<your BU username>`

Then select hours, cores, GPUs, etc.

## VS Code Remote Development on SCC Compute Node

Here's a way to run VS Code locally with the remote development extension and connect to an SCC compute node, rather than just the SCC log-in node. You're not supposed to be running compute loads on scc1 (or scc2). It's just a log-in node where you can do some minor file management, and also connect to compute nodes.

The first thing you need to do is to get a compute node assigned to you. There might be a more direct way to do this, but one way is to start an interactive VS Code session with the environment configuration as shown [above](#academic-ml-environment). Once the environment is allocated for you, look at your [My Interactive Sessions](https://scc-ondemand1.bu.edu/pun/sys/dashboard/batch_connect/sessions) on [SCC OnDemand](https://scc-ondemand1.bu.edu/pun/sys/dashboard/) to see which host was assigned to you. It should be in a blue box in the format of something like `>__scc-xyz`, where the exact name will be different for you. The `scc-xyz` part is the hostname.

Now you can't directly connect to that compute node from your local machine via, for example, ssh. But you can get there in two hops:
```sh
# ssh to the SCC login node from your local machine
ssh <username>@scc1.bu.edu

# once you're on the login node you can connect to the remote machine.
$ ssh scc-xyz
```

You can automate this by adding a configuration to your `.ssh/config` file:

```sh
Host scc-xyz    # change this to the actual compute node you want to connect to
  Hostname scc-xyz    # update this with the real compute node name
  User <username>     # replace with your username
  ProxyJump scc1.bu.edu   # this says that you need to first log-in here
```

Now you can try this from your local command line.
```sh
ssh scc-xyz
```
It might ask you to log in twice, but should work.

Then for VSCode remote development, you can now put  `scc-xyz` as your remote host.
