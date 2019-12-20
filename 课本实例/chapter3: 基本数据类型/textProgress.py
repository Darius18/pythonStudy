# p89 example4.1
import time

scale = 10
print("{0:=^30}".format("正在加载"))
for i in range(scale+1):
    a,b = '**'*i,'..'*(scale-i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}->{}]".format(c, a, b))
    time.sleep(0.5) #使当前程序挂起
print("{0:=^30}".format("加载完毕"))