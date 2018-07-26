'''
5.CPython，在命令行下运行Python，就是启动CPython解释器
  IPython，IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPyhton是完全一样的
  PyPy，PyPy是另一个Python解释器，它的目标是执行速度，PyPy采用JIT技术，对Python代码进行动态编译，所以可以显著提高Python代码的执行速度。
  Jython，Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
  IronPython，IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
6.8位等于一字节
7.1 B = 8b （8个bit/ 位） 一个字节（byte）等于8位（bit）
  1 kB = 1024 B (kB - kilobajt)
  1 MB = 1024 kB (MB - megabajt)
  1 GB = 1024 MB (GB - gigabajt)
8.一 代码编排
  1 缩进。4个空格的缩进（编辑器都可以完成此功能），不使用Tap，更不能混合使用Tap和空格。
  2 每行最大长度79，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。
  3 类和top-level函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。
  二 文档编排
  1 模块内容的顺序：模块说明和docstring—import—globals&constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。
  2 不要在一句import中多个库，比如import os, sys不推荐。
  3 如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。
  三 空格的使用
  总体原则，避免不必要的空格。
  1 各种右括号前不要加空格。
  2 逗号、冒号、分号前不要加空格。
  3 函数的左括号前不要加空格。如Func(1)。
  4 序列的左括号前不要加空格。如list[2]。
  5 操作符左右各加一个空格，不要为了对齐增加空格。
  6 函数默认参数使用的赋值符左右省略空格。
  7 不要将多句语句写在同一行，尽管使用‘；’允许
9.
10.
11.999
    
    def f(n):
        n += 1
        f(n)
    if __name__ == '__main__':
        f(1)
12.
13.
14.机器码(machine code)，学名机器语言指令，有时也被称为原生码（Native Code），是电脑的CPU可直接解读的数据。
    字节码（Bytecode）是一种包含执行程序、由一序列 op 代码/数据对 组成的二进制文件。字节码是一种中间码，它比机器码更抽象，需要直译器转译后才
    能成为机器码的中间代码。
15.
'''