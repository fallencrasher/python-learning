# 1.安装包下载

这里推荐去官网当然。但是上不去官网就去腾讯软件中心下载就好(打钱！)。

# 2. 安装后的处理

## Package Control 的处理

sublime text 3 如今恶心了，初始安装的程序都没有 Package Control 的，恶心！

怎么办呢？

首先呢，去[sublime_package_control](https://github.com/wbond/package_control)下载项目的zip文件，解压，改名"Package Control"，注意大小写。然后把这个文件夹拖到sublime的packages文件夹里，这个文件夹在哪呢？

Preferences ——> Browse Packages

就行了，然后把文件夹拖进去。重启sublime，就有 package control 了。

然后点击package control, 找到 install packages 那一套，发现，不能成，说没有包可以装。

接着就是改这个包安装寻找的路径。

找到 Package Control 的 settings 文件。

加入下边这一行就行了

```
"channels":
	[
		"http://packagecontrol.cn/channel_v3.json"
	],
```

http://packagecontrol.cn/channel_v3.json



或者不写这个网址，我们打开这个网站：https://raw.githubusercontent.com/wilon/sublime/master/download/channel_v3.json，复制所有内容，然后保存在本地的文件，改名"channel_v3.json"，然后把这个改成

```
"channels":
	[
		"http://packagecontrol.cn/channel_v3.json"
	],
```

## 关于推荐的插件

最近在搞python，发现，这个 sublime 编辑器默认对python的支持已经很吊了。没啥可安装的。

就下边这几个：

```
anaconda
autopep8
sublimetmpl
sublimeREPL
sublimecodeintel
sidebar
autofilename
```

## 插件的设置

### sublimetREPL

```
#设置SublimeREPL运行的Python环境

在你的Sublime Text 3的路径下，我的是...\Sublime Text 3\Data\Packages\SublimeREPL\config\Python\ 找到Main.sublime-menu文件，然后用Sublime Text 3 打开，找到id 为 repl_python行，修改 "cmd": ["python", "-i", "-u","$file_basename"]，保存。

#快捷键设定。

在路径：Preferences->Key Bindings 
输入如下代码
[
    {
    "keys": ["f5"],
    "caption": "SublimeREPL: Python - RUN current file",
    "command": "run_existing_window_command",
    "args": {
        "id": "repl_python_run",
        "file": "config/Python/Main.sublime-menu"}
    },
    {
    "keys": ["f8"],
    "caption": "SublimeREPL: Python - PDB current file",
    "command": "run_existing_window_command",
    "args": {
        "id": "repl_python_pdb",
        "file": "config/Python/Main.sublime-menu"}
    },   
]
这样，就是在当前文件下，按F5运行，F8调试

```

## subliimecodeintel 设置

```python
#在 Perefences-->Browes Packages里，找到sublimecodeintel的文件夹，进去，用 cmd 新建文件夹（.codeintel）,然后在这个文件夹里新建一个没有后缀名的文件（config），打开，把下边的复制进去，或者不一样的，自己看看在哪，基本就是python的安装路径和包的位置

{
	"python":{
			"python":"C:/Program Files (x86)/Python3.8/python.exe",
			"pythonExtraPaths":
				[
					"C:/Program Files (x86)/Python3.8",
					"C:/Program Files (x86)/Python3.8/DLLs",
					"C:/Program Files (x86)/Python3.8/Lib",
					"C:/Program Files (x86)/Python3.8/Lib/site-packages"
				]
	},
}
```

