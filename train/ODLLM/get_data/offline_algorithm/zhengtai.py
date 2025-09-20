import random
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
# 生成数据
data = np.random.normal(10, 10, 222)
data=data.astype(int) # 转换为整数类型
# 绘制密度图
#.hist(data, bins=10, density=True)
#plt.show()
demand=[]

for i in range(222):
    demand_day = np.zeros(810,dtype=float)
    if data[i]<=0:data[i]=1
    #while sum(demand_day)<data[i]:
        #demand_day[random.randint(0,809)]=1
    demand_day[random.randint(0, 809)]=data[i]
    demand.append(demand_day)
demand=(np.array(demand)).T
print(demand)
scipy.io.savemat('Demand.mat',{'Demand':demand})