# install pip3 on Ubuntu Linux

- 在控制台执行如下命令:
```shell
sudo apt install python3-pip
```

- 控制台输出如下：
```log
~/code/python/Pylearn$ sudo apt install python3-pip 
[sudo] password for your_name: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  fonts-lato javascript-common libjs-jquery libruby2.3 rake ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby2.3 rubygems-integration
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  python-pip-whl python3-setuptools python3-wheel
Suggested packages:
  python-setuptools-doc
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python-pip-whl python3-pip python3-setuptools python3-wheel
0 upgraded, 4 newly installed, 0 to remove and 3 not upgraded.
Need to get 1,319 kB of archives.
After this operation, 2,398 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu xenial/universe amd64 python-pip-whl all 8.1.1-2 [1,074 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial/universe amd64 python3-pip all 8.1.1-2 [109 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-setuptools all 20.7.0-1 [88.0 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial/universe amd64 python3-wheel all 0.29.0-1 [48.1 kB]
Fetched 1,319 kB in 4s (323 kB/s)        
Selecting previously unselected package python-pip-whl.
(Reading database ... 230172 files and directories currently installed.)
Preparing to unpack .../python-pip-whl_8.1.1-2_all.deb ...

Progress: [  0%] [..............................................................................................................................................................................................................] 
Unpacking python-pip-whl (8.1.1-2) .............................................................................................................................................................................................] 

Progress: [  9%] [####################..........................................................................................................................................................................................] 
Selecting previously unselected package python3-pip.............................................................................................................................................................................] 
Preparing to unpack .../python3-pip_8.1.1-2_all.deb ...

Unpacking python3-pip (8.1.1-2) ...#######################......................................................................................................................................................................] 

Progress: [ 23%] [##################################################............................................................................................................................................................] 
Selecting previously unselected package python3-setuptools.##################...................................................................................................................................................] 
Preparing to unpack .../python3-setuptools_20.7.0-1_all.deb ...

Unpacking python3-setuptools (20.7.0-1) ...############################################.........................................................................................................................................] 

Progress: [ 38%] [###############################################################################...............................................................................................................................] 
Selecting previously unselected package python3-wheel.#####################################################.....................................................................................................................] 
Preparing to unpack .../python3-wheel_0.29.0-1_all.deb ...

Unpacking python3-wheel (0.29.0-1) ...###############################################################################...........................................................................................................] 

Progress: [ 52%] [############################################################################################################..................................................................................................] 
Processing triggers for man-db (2.7.5-1) ...############################################################################################........................................................................................] 
Setting up python-pip-whl (8.1.1-2) ...

Progress: [ 61%] [################################################################################################################################..............................................................................] 
Setting up python3-pip (8.1.1-2) ...########################################################################################################################....................................................................] 

Progress: [ 71%] [####################################################################################################################################################..........................................................] 
Setting up python3-setuptools (20.7.0-1) ...###################################################################################################################################.................................................] 

Progress: [ 80%] [#######################################################################################################################################################################.......................................] 
Setting up python3-wheel (0.29.0-1) ...############################################################################################################################################################.............................] 

Progress: [ 90%] [###########################################################################################################################################################################################...................] 
```

- 测试是否安装成功
```shell
~/code/python/Pylearn$ pip3 --version
pip 18.1 from ~/.local/lib/python3.5/site-packages/pip (python 3.5)
或者
~/code/python/Pylearn$ which pip3
~/.local/bin/pip3
```