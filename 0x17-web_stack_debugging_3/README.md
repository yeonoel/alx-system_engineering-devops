# 0x17. Web stack debugging #3
i
This was the fourth in a series of web stack debugging projects. In these projects, I was given broken/bugged webstacks in isolated
containers, and tasked with fixing the web stack to a working state. For each task, I wrote a script automating the commands necessary to fix the web stack.

### Requirements
**General**
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension .pp
* Files will be checked with Puppet v3.4


**0. Strace is your friend**
* 0-strace_is_your_friend.pp: Puppet manifest that fixes a typo error causing a WordPress application being served by an Apache web server to fail.
Usage: puppet apply 0-strace_is_your_friend.pp


Hint:

* strace can attach to a current running process
* You can use tmux to run strace in one window and curl in another one

Requirements:

* Your 0-strace_is_your_friend.pp file must contain Puppet code
* You can use whatever Puppet resource type you want for you fix
