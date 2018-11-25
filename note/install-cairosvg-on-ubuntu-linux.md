# install pip3 on Ubuntu Linux

- 在控制台执行如下命令：
```shell
pip3 install --user cairosvg
```

- 控制台输出如下：
```log
~/code/python/Pylearn$ pip3 install --user cairosvg
Collecting cairosvg
  Using cached https://files.pythonhosted.org/packages/5c/57/dadc80948bcb83ea9c0968ccfd5a1a25ace6be0884484526f70dad3c10b9/CairoSVG-2.2.1-py3-none-any.whl
Collecting defusedxml (from cairosvg)
  Using cached https://files.pythonhosted.org/packages/87/1c/17f3e3935a913dfe2a5ca85fa5ccbef366bfd82eb318b1f75dadbf0affca/defusedxml-0.5.0-py2.py3-none-any.whl
Requirement already satisfied: pillow in /usr/lib/python3/dist-packages (from cairosvg) (3.1.2)
Collecting cairocffi (from cairosvg)
Collecting tinycss2 (from cairosvg)
  Using cached https://files.pythonhosted.org/packages/88/95/0ec73db7fc638ec000e662936ffe1a4e1eaa22f2861c8de18b1597c42584/tinycss2-0.6.1-py2.py3-none-any.whl
Collecting cssselect2 (from cairosvg)
  Using cached https://files.pythonhosted.org/packages/12/e2/91fcd4cd32545beec6e11628d64d3e20f11b5a95dd1ccf3216fd69f176b7/cssselect2-0.2.1-py2.py3-none-any.whl
Collecting cffi>=1.1.0 (from cairocffi->cairosvg)
  Using cached https://files.pythonhosted.org/packages/59/cc/0e1635b4951021ef35f5c92b32c865ae605fac2a19d724fb6ff99d745c81/cffi-1.11.5-cp35-cp35m-manylinux1_x86_64.whl
Collecting webencodings>=0.4 (from tinycss2->cairosvg)
  Using cached https://files.pythonhosted.org/packages/f4/24/2a3e3df732393fed8b3ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.whl
Collecting pycparser (from cffi>=1.1.0->cairocffi->cairosvg)
Installing collected packages: defusedxml, pycparser, cffi, cairocffi, webencodings, tinycss2, cssselect2, cairosvg
Successfully installed cairocffi-0.9.0 cairosvg-2.2.1 cffi-1.11.5 cssselect2-0.2.1 defusedxml-0.5.0 pycparser-2.19 tinycss2-0.6.1 webencodings-0.5.1

```

- 如果上面的命令不管用，去掉 `--user` 标志位试下
    - 这时可能需要用 `sudo` 去执行
- 测试是否安装成功：
```shell
~/code/python/Pylearn$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cairosvg
>>> # 没有报错提示则说明安装成功
```