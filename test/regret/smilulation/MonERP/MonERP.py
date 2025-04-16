import numpy as np
import pandas as pd
import math
import os


'''
Implementation of the MonERP online learning algorithm.

Parameters:
-----------
data_file : str
    Path to the Excel file containing r, w, a values

'''
all_regret_list=[]

for i in range(10):
    para = pd.read_excel('b.xlsx')
    b=para.iloc[i:+1+i,1:3].values.tolist()[0]
    file_path =  f'days{i}.xlsx'

    # Run the algorithm
    df = pd.read_excel(file_path)

    # Extract r, w, a columns

    r_values = df['r'].values
    w_values = df['demand'].values
    a_values = df['a'].values

    # Get the number of samples
    n = len(r_values)

    # Initialize parameters
    epsilon = [x / n for x in b ]  # Step 1
    print(epsilon)
    p_t = [0,0]  #
    x_t_values = []  # To store decisions
    # for regret
    reward = 0
    x_opt = df['x']
    regret = 0
    regret_list = []

    # For each time step
    for t in range(n):
        r_t = r_values[t]
        w_t = w_values[t]
        a_t = a_values[t]

        # Learning rate (as specified in Parameter)
        gamma_t = 1 / math.sqrt(n)

        # Step 4: Set x_t
        if r_t > w_t * p_t[0] + a_t * p_t[1]:  # r_t > [w_t a_t]p_t
            x_t = 1
        else:
            x_t = 0

        # Append the decision
        x_t_values.append(x_t)

        # Step 5: Compute p_{t+1}
        # p_{t+1} = max{p_t + γ_t([w_t/a_t]x_t - ε), 0}
        p_t_plus_1 = [max(p_t[0] + gamma_t * (w_t  * x_t - epsilon[0]), 0),
                      max(p_t[1] + gamma_t * (a_t  * x_t - epsilon[1]), 0)]

        # Update p_t for next iteration
        p_t = p_t_plus_1

        regret += r_t * x_t- x_opt[i] * r_t
        regret_list.append(regret)

    print(regret_list)
    all_regret_list.append(regret_list)

result_df = pd.DataFrame(all_regret_list).transpose()
# Rename columns
result_df.columns = [f'day{i}' for i in range(len(all_regret_list))]
# Save to Excel
result_df.to_excel('MonERP_regret.xlsx', index=False)


