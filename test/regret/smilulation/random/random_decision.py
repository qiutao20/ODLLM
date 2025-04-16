import pandas as pd
import os
import random
# 创建一个字典来存储所有表格数据
all_data = {}

# 遍历10个Excel文件
all_regret_list=[]
for i in range(10):
    file_name = f'days{i}.xlsx'

    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        reward = 0
        x_opt=df['x']
        r=df['r']
        regret=0
        regret_list=[]
        regret_list.append(regret)
        for j in range(61):
            regret+=r[i]*random.randint(0, 1)-x_opt[i]*r[i]
            regret_list.append(regret)
        print(regret_list)
    else:
        print('no file')
    all_regret_list.append(regret_list)
result_df = pd.DataFrame(all_regret_list).transpose()
# Rename columns
result_df.columns = [f'day{i}' for i in range(len(all_regret_list))]
# Save to Excel
result_df.to_excel('random_regret.xlsx', index=False)
print("Results saved to 'random_regret.xlsx'")
