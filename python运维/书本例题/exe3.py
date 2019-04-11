#进程的管理方法
import psutil
from subprocess import PIPE

print(psutil.pids()) #列出所有进程pid
p = psutil.Process(8096) #实例化一个Process对象，参数为一进程PID
print(p.name()) #进程名
# for i in psutil.pids():
#     print("进程号%d"%i,psutil.Process(i).name())
print(p.exe()) #进程bin路径
print(p.cwd()) #进程工作目录绝对路径
print(p.status()) #进程的状态
print(p.create_time()) #进程的创建时间，时间戳格式
print(p.cpu_times()) #进程cpu时间信息=用户时间+系统时间
print(p.cpu_affinity()) #进程的cpu亲和度
print(p.memory_percent()) #进程的内存利用率
print(p.memory_info) #进程内存rss，vms信息
print(p.io_counters()) #进程的io信息
print(p.connections()) #返回打开进程socket的namedutples列表，包括fs，fa'mily等信息
print(p.num_threads()) #进程开启的线程数

#popen类的使用
#通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息
# p = psutil.Popen([...])
