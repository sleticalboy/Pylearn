# install pip3 on Ubuntu Linux

- 在控制台执行如下命令：
```shell
pip3 install --user matplotlib
```

- 控制台输出如下：
```log
sleticalboy@Lee:~/code/python/Pylearn$ pip3 install --user matplotlib
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/ad/4c/0415f15f96864c3a2242b1c74041a806c100c1b21741206c5d87684437c6/matplotlib-3.0.2-cp35-cp35m-manylinux1_x86_64.whl (12.9MB)
    100% |████████████████████████████████| 12.9MB 111kB/s 
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (59kB)
    100% |████████████████████████████████| 61kB 537kB/s 
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting numpy>=1.10.0 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/86/04/bd774106ae0ae1ada68c67efe89f1a16b2aa373cc2db15d974002a9f136d/numpy-1.15.4-cp35-cp35m-manylinux1_x86_64.whl (13.8MB)
    100% |████████████████████████████████| 13.8MB 117kB/s 
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/7e/31/d6fedd4fb2c94755cd101191e581af30e1650ccce7a35bddb7930fed6574/kiwisolver-1.0.1-cp35-cp35m-manylinux1_x86_64.whl (949kB)
    100% |████████████████████████████████| 952kB 345kB/s 
Collecting python-dateutil>=2.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl (225kB)
    100% |████████████████████████████████| 235kB 338kB/s 
Collecting six (from cycler>=0.10->matplotlib)
  Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Collecting setuptools (from kiwisolver>=1.0.1->matplotlib)
  Downloading https://files.pythonhosted.org/packages/e7/16/da8cb8046149d50940c6110310983abb359bbb8cbc3539e6bef95c29428a/setuptools-40.6.2-py2.py3-none-any.whl (573kB)
    100% |████████████████████████████████| 573kB 328kB/s 
Installing collected packages: pyparsing, six, cycler, numpy, setuptools, kiwisolver, python-dateutil, matplotlib
Successfully installed cycler kiwisolver matplotlib numpy pyparsing-2.0.3 python-dateutil setuptools-20.7.0 six-1.10.0
You are using pip version 8.1.1, however version 18.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

- 如果上面的命令不管用，去掉 `--user` 标志位试下
- 测试是否安装成功：
```shell
~/code/python/Pylearn$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib
>>> # 没有报错提示则说明安装成功
```