'''
得到当前工作目录，即当前Python脚本工作的目录路径：os.getcwd()
返回指定目录下的所有文件和目录名：os.listdir()
函数用来删除一个文件：os.remove()
删除多个目录：os.removedirs(r"c:\python")
检查给出的路径是否是一个文件：os.path.isfile()
检查给出的路径是否是一个目录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检查给出的路径是否真的存在：os.path.exists()
返回一个路径的目录名和文件名：os.path.split()
分离扩展名：os.path.splitext()
获取路径名：os.path.dirname()
运行shell命令：os.system()
>>> os.system('df -h')
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   233Gi   46Gi  185Gi    21%  812377 9223372036853963430    0%   /
devfs          190Ki  190Ki    0Bi   100%     658                   0  100%   /dev
/dev/disk1s4   233Gi  2.0Gi  185Gi     2%       2 9223372036854775805    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
/dev/disk2s1    30Mi   15Mi   15Mi    51%     542          4294966737    0%   /Volumes/网易云音乐
0

读取操作系统环境变量HOME的值：os.getenv("HOME")
返回操作系统所有的环境变量：os.environ
设置系统环境变量，仅程序运行时有效：os.environ.setdefault('HOME','/home/alex')
给出当前平台使用的行终止符：os.linesep Windows使用'\r\n'，linux使用'\n',Mac'\r'
指示你正在使用的平台：os.name
重命名：os.rename(old,new)
创建多级目录：os.makedirs(r"c:\python\test")
创建单个目录：os.mkdir("test")
获取文件属性：os.stat(file)
修改文件权限与时间戳:os.chmod('file',777)
获取文件大小：os.path.join(dir,filename)
# 结合目录名与文件名：os.path.join(dir,filename)
# 改变工作目录到dirname:os.chdir(dirname)
获取当前终端的大小：os.get_terminal_size()
杀死进程：os.kill(10884,singal.SIGKILL)
'''