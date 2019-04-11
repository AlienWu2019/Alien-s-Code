import psutil
import datetime

#内存信息
mem = psutil.virtual_memory() #获取内存信息
print(mem.total,mem.used)  #第一个参数为内存得总大小，第二个参数是内存得使用量

#cpu信息
u_time = psutil.cpu_times() #获取cpu得完整信息
utime_user = u_time.user
print(u_time)
print(utime_user)

#物理CPU就是计算机上实际配置的CPU个数。操作系统可以使用逻辑CPU来模拟出真实CPU的效果。在之前没有多核处理器的时候，一个CPU只有一个核，而现在有了多核技术，其效果就好像把多个CPU集中在一个CPU上。当计算机没有开启超线程时，逻辑CPU的个数就是计算机的核数。而当超线程开启后，逻辑CPU的个数是核数的两倍。
cpu_count_l = psutil.cpu_count() #获取cpu的逻辑个数，默认logical为True
cpu_count_p = psutil.cpu_count(logical=False) #获取cpu的物理个数
print(cpu_count_l)
print(cpu_count_p)
if cpu_count_l==cpu_count_p:
    print("cpu没有开启超线程")

#磁盘信息
print(psutil.swap_memory())
print(psutil.disk_partitions()) #打印磁盘的总体信息
print(psutil.disk_usage("D:\\")) #打印磁盘的使用信息
print(psutil.disk_io_counters()) #使用psutil.disk_io_counters获取硬盘总的IO个数
print(psutil.disk_io_counters(perdisk=True)) #单个分区IO个数

#网络信息
print(psutil.net_io_counters())#使用psutil.net_io_counters获取网络总的IO信息，默认pernic=False

#其他系统信息
print(psutil.users())
print(psutil.boot_time())
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print(boot_time)