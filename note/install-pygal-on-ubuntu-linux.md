# install pip3 on Ubuntu Linux

- 在控制台执行如下命令：
```shell
pip3 install --user pygal
```

- 控制台输出如下：
```log
~/code/python/Pylearn$ pip3 install --user pygal
Collecting pygal
  Downloading https://files.pythonhosted.org/packages/5f/b7/201c9254ac0d2b8ffa3bb2d528d23a4130876d9ba90bc28e99633f323f17/pygal-2.4.0-py2.py3-none-any.whl (127kB)
    100% |████████████████████████████████| 133kB 538kB/s 
Installing collected packages: pygal
Successfully installed pygal-2.4.0
```

- 如果上面的命令不管用，去掉 `--user` 标志位试下
    - 这时可能需要用 `sudo` 去执行
- 测试是否安装成功：
```shell
~/code/python/Pylearn$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pygal
>>> # 没有报错提示则说明安装成功
```