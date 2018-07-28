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
15.c= a if a>1 else b
16.Python3中print为一个函数，必须用括号括起来；Python2中print为class
   Python3中input得到的为str；Python2的input的到的为int型，Python2的raw_input得到的为str类型
   Python3中/表示真除，%表示取余，//结果取整；Python2中带上小数点/表示真除，%表示取余，//结果取整
17.a,b = b,a
18
19.xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
20.xreadlines返回一个生成器，来循环操作文件的每一行。
21.‘’ False 0 [] () {}
22.str: split() strip() isalpha() join() count() upper() replace()
   list:append() index() pop() reverse() remove() count()
   dict:get() items() update() clear()
   https://www.cnblogs.com/nianlei/p/5642315.html
23.lambda x : x+x  配合map reduce filter使用
24.语义完整性
25.*args：可以理解为只有一列的表格，长度不固定。
   def sum(*args):
      count = 0
      for i in args:
          count += i
      print(count)
   sum(1,2,3)
   **kwargs：可以理解为字典，长度也不固定。
   def fun(**kwargs):
      for key in kwargs:
          print("person's info: %s %s"%(key,kwargs[key]))
   fun(chw='27',zch='23')
26.is对比的是数据地址，==比较的是value
27.
28.
29.可变类型： 字典、列表
   不可变类型： 字符串、元祖、数字
30. {'k2': [666], 'k1': [666]}
    False
    {'k2': [666], 'k1': 777}
31.[6,6,6,6]作用域   好好看下
32.
33.def f(x,y):
      return x+y
   print(reduce(f,[1,2,3,4]))
   from functools import reduce
   print(reduce(lambda x,y:x+y,[1,2,3,4]))
   print(list(map(lambda n:n*2,range(10))))
   print(list(filter(lambda x:x>2,range(10))))
34.print('\n'.join(['\t'.join(["%2s*%2s=%2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
35.
36.re.os.time.math.random.sys.Django.pip.pygame.pyMysql.numpy
37.print(re.match('super','superstition').span())
   # print(re.match('super','insuperable').span())
   print(re.search('super','superstition').span())
   print(re.search('super','insuperable').span())
   (0,5)
   报错
   (0,5)
   (2,7)
38.String str="abcaxc";
   Patter p="ab*c";
   贪婪匹配:正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配。如上面使用模式p匹配字符串str，结果就是匹配到：abcaxc(ab*c)。
   非贪婪匹配：就是匹配到结果就好，就少的匹配字符。如上面使用模式p匹配字符串str，结果就是匹配到：abc(ab*c)。
39.[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
   [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
40.
41.
42.split(',')
43.
44.
45.print(list(map(lambda x:x*x,range(1,11))))
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
46.先set在list
47.global
48.logging模块的作用？以及应用场景
49.class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self, item):
        return self.items.pop()
50.
51.
52.def search(list,target):
      high = len(list) - 1
      low = 0
      while low <= high:
          mid = (high + low) // 2
          if list[mid] == target:
              return mid
          elif list[mid] > target:
              high = mid - 1
          else:
              low = mid + 1
      return -1
   ret = search(list(range(1,1000)),0)
   print(ret)
53.
'''