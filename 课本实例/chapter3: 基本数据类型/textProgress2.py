#单行动态刷新
import time
for i in range(101):
    print("\r{:2}%".format(i), end="")
    time.sleep(0.05)
print("\r{}".format("加载完成!"), end="")